#!/usr/bin/env python3
"""
ledger_build.py — READ-ONLY helper for academic-source-verification.

Seeds / refreshes the reference-audit ledger deterministically. It NEVER writes to
manuscript source files; it only emits a ledger CSV/JSON skeleton with the provenance
columns ready to be filled (by human + backends).

What it does (deterministic, offline):
  1. Parse references.bib  -> one row per bib key (key, author, year, journal/title).
  2. Scan .tex manuscript  -> extract literal in-text citations "(Author, YYYY)".
  3. Cross-check both directions:
       - ORPHAN  : bib entry never cited in text  (candidate to drop / \nocite noise)
       - PHANTOM : in-text citation with no matching bib key (e.g. a fabricated cite)
  4. Emit ledger skeleton (CSV + JSON) with the 10 provenance columns blank/defaulted.

External truth (existence, metadata correctness, retraction, claim-support) is NOT done
here — that is the human + backends step (CrossRef, Retraction Watch, scite, Elicit,
cbs-libsearch). This script only prepares the ledger and flags internal mismatches.

Usage:
  python ledger_build.py --bib references.bib --tex "chapters/*.tex" --out ledger_skeleton
"""
import argparse, glob, json, re, csv, sys
from pathlib import Path
import unicodedata

def _deacc(x):
    return unicodedata.normalize('NFKD', x).encode('ascii','ignore').decode()

def _norm_sur(x):
    return re.sub(r'[^a-zA-Z]','', _deacc(x)).lower()

_NOISE = {'og','al','et','se','jf','kap','the','of','ceo','general','electric','today',
          'accounting','forordning','microsoft','netflix','gallup','workhuman','textio','ge','and'}

PROV_COLS = ["verifikationsmetoder", "antal_kilder", "kilde_evidens", "annotation_ref",
             "retraktionsstatus", "claim_støttet", "in_text_match",
             "verificeret_af", "verifikationsdato", "værktøj_version"]
PROV_DEFAULT = {"retraktionsstatus": "ikke tjekket", "claim_støttet": "ikke tjekket",
                "in_text_match": "ikke tjekket"}

def parse_bib(path):
    text = Path(path).read_text(encoding="utf-8", errors="replace")
    entries = {}
    for m in re.finditer(r"@\w+\s*\{\s*([^,]+),", text):
        key = m.group(1).strip()
        # crude field grab within the entry braces
        start = m.end()
        depth, i = 1, start
        while i < len(text) and depth:
            if text[i] == "{": depth += 1
            elif text[i] == "}": depth -= 1
            i += 1
        body = text[start:i]
        def field(name):
            fm = re.search(name + r"\s*=\s*[{\"]([^}\"]*)", body, re.I)
            return fm.group(1).strip() if fm else ""
        au = field("author") or field("editor")
        surs = []
        for a in re.split(r"\s+and\s+", au):
            a=a.strip()
            if not a: continue
            sur = a.split(",")[0] if "," in a else (a.split()[-1] if a.split() else a)
            ns=_norm_sur(sur)
            if ns: surs.append(ns)
        entries[key] = {"author": au, "year": field("year"),
                        "journal": field("journal") or field("journaltitle") or field("title"),
                        "surs": surs}
    return entries

def surname(author):
    if not author: return ""
    first = re.split(r"\s+and\s+", author)[0]
    return (first.split(",")[0] if "," in first else first.split()[-1]).strip()

def scan_intext(globs):
    """Robust: fanger BÅDE narrativ form 'Forfatter (år)' OG parentetisk '(Forfatter, år)'.
    Deaccenter (ö->o, é->e) + fjerner genitiv-'s. Returnerer (norm_surname, year)-par."""
    pairs = set()   # (norm_surname, year)
    NAME = r"[A-Z][A-Za-z'\-]+"
    for g in globs:
        for fp in glob.glob(g, recursive=True):
            try: t = Path(fp).read_text(encoding="utf-8", errors="replace")
            except Exception: continue
            t = re.sub(r"(?<!\\)%.*", "", t)      # fjern LaTeX-kommentarer
            t = _deacc(t)
            t = re.sub(r"'s\b", "", t)             # genitiv
            for m in re.finditer(r"("+NAME+r"(?:\s+(?:og|and|&|et\s+al\.?|,)\s*[A-Z]?[A-Za-z'\-]*)*)\s*\((\d{4})[a-z]?\)", t):
                yr=m.group(2)
                for n in re.findall(NAME, m.group(1)):
                    ns=_norm_sur(n)
                    if ns and ns not in _NOISE and len(ns)>1: pairs.add((ns,yr))
            for m in re.finditer(r"\(([^()]*?\b\d{4}[a-z]?)\)", t):
                inner=m.group(1); yrs=re.findall(r"(\d{4})", inner)
                for n in re.findall(NAME, inner):
                    ns=_norm_sur(n)
                    if ns in _NOISE or not ns or len(ns)<3: continue
                    for yr in yrs: pairs.add((ns,yr))
    return pairs

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bib", required=True)
    ap.add_argument("--tex", nargs="+", required=True, help="glob(s) for manuscript .tex")
    ap.add_argument("--out", default="ledger_skeleton")
    a = ap.parse_args()

    bib = parse_bib(a.bib)
    prose = scan_intext(a.tex)        # sæt af (norm_surname, year)

    # opslag (surname,year) -> nøgler (via ALLE forfatter-efternavne)
    sy = {}
    for k, v in bib.items():
        for ns in v.get("surs", []):
            if v["year"]: sy.setdefault((ns, v["year"]), []).append(k)

    def matches(ns, yr):
        return sy.get((ns, yr)) or sy.get((ns.rstrip("s"), yr)) or []

    all_surs = {ns for v in bib.values() for ns in v.get("surs", [])}
    cited_keys = {k for (ns, yr) in prose for k in matches(ns, yr)}
    # split phantoms: efternavn HELT fraværende (høj signal) vs år-mismatch (ofte co-forf.-støj)
    phantom_absent = sorted({(ns, yr) for (ns, yr) in prose
                             if not matches(ns, yr) and ns not in all_surs and ns.rstrip("s") not in all_surs})
    phantom_yrmis  = sorted({(ns, yr) for (ns, yr) in prose
                             if not matches(ns, yr) and (ns in all_surs or ns.rstrip("s") in all_surs)})
    phantoms = phantom_absent  # "ægte" phantom = uslåbar
    orphans = sorted(set(bib) - cited_keys)
    cites = prose  # for tælle-udskrift

    rows = []
    for k, v in sorted(bib.items()):
        row = {"Bib-nøgle": k, "Reference (forkortet)": f"{surname(v['author'])} ({v['year']})",
               "journal_title": v["journal"], "cited_in_text": "ja" if k in cited_keys else "NEJ (forældreløs?)"}
        row.update({c: PROV_DEFAULT.get(c, "") for c in PROV_COLS})
        rows.append(row)

    out = Path(a.out)
    with open(out.with_suffix(".json"), "w", encoding="utf-8") as f:
        json.dump({"rows": rows,
                   "phantoms_absent": [f"{s} {y}" for s, y in phantom_absent],
                   "phantoms_yearmismatch": [f"{s} {y}" for s, y in phantom_yrmis],
                   "orphans": orphans}, f, ensure_ascii=False, indent=2)
    with open(out.with_suffix(".csv"), "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

    print(f"bib entries      : {len(bib)}")
    print(f"in-text cites    : {len(cites)}")
    print(f"PHANTOM (absent) : {len(phantom_absent)}  (efternavn slet ikke i bib — HØJ signal)  -> {phantom_absent[:8]}")
    print(f"PHANTOM (år-mism): {len(phantom_yrmis)}  (efternavn findes, andet år — ofte co-forf.-støj)")
    print(f"ORPHAN entries   : {len(orphans)}  (bib, never cited)       -> {orphans[:8]}")
    print(f"ledger skeleton  : {out.with_suffix('.json')} / {out.with_suffix('.csv')}")
    print("NOTE: external verification (existence/metadata/retraction/claim) is the human+backends step.")

if __name__ == "__main__":
    main()
