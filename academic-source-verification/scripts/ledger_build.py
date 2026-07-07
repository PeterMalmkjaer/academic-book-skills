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
        entries[key] = {"author": field("author"), "year": field("year"),
                        "journal": field("journal") or field("journaltitle") or field("title")}
    return entries

def surname(author):
    if not author: return ""
    first = re.split(r"\s+and\s+", author)[0]
    return (first.split(",")[0] if "," in first else first.split()[-1]).strip()

def scan_intext(globs):
    cites = []  # (surname_token, year, file)
    pat = re.compile(r"\(([A-Z][A-Za-zÀ-ÿ'`\-]+)(?:\s+(?:et al\.?|and|&)\s+[A-Z][A-Za-zÀ-ÿ'`\-]+)*,?\s+(\d{4})[a-z]?\)")
    for g in globs:
        for fp in glob.glob(g, recursive=True):
            try: t = Path(fp).read_text(encoding="utf-8", errors="replace")
            except Exception: continue
            for m in pat.finditer(t):
                cites.append((m.group(1), m.group(2), fp))
    return cites

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bib", required=True)
    ap.add_argument("--tex", nargs="+", required=True, help="glob(s) for manuscript .tex")
    ap.add_argument("--out", default="ledger_skeleton")
    a = ap.parse_args()

    bib = parse_bib(a.bib)
    cites = scan_intext(a.tex)

    bib_surnames = {k: surname(v["author"]).lower() for k, v in bib.items()}
    bib_years = {k: v["year"] for k, v in bib.items()}

    def matches(sname, yr):
        return [k for k in bib if bib_surnames.get(k) == sname.lower() and bib_years.get(k) == yr]

    phantoms = sorted({(s, y) for (s, y, _) in cites if not matches(s, y)})
    cited_keys = {k for (s, y, _) in cites for k in matches(s, y)}
    orphans = sorted(set(bib) - cited_keys)

    rows = []
    for k, v in sorted(bib.items()):
        row = {"Bib-nøgle": k, "Reference (forkortet)": f"{surname(v['author'])} ({v['year']})",
               "journal_title": v["journal"], "cited_in_text": "ja" if k in cited_keys else "NEJ (forældreløs?)"}
        row.update({c: PROV_DEFAULT.get(c, "") for c in PROV_COLS})
        rows.append(row)

    out = Path(a.out)
    with open(out.with_suffix(".json"), "w", encoding="utf-8") as f:
        json.dump({"rows": rows, "phantoms": [f"{s} {y}" for s, y in phantoms],
                   "orphans": orphans}, f, ensure_ascii=False, indent=2)
    with open(out.with_suffix(".csv"), "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

    print(f"bib entries      : {len(bib)}")
    print(f"in-text cites    : {len(cites)}")
    print(f"PHANTOM cites    : {len(phantoms)}  (in text, no bib entry)  -> {phantoms[:8]}")
    print(f"ORPHAN entries   : {len(orphans)}  (bib, never cited)       -> {orphans[:8]}")
    print(f"ledger skeleton  : {out.with_suffix('.json')} / {out.with_suffix('.csv')}")
    print("NOTE: external verification (existence/metadata/retraction/claim) is the human+backends step.")

if __name__ == "__main__":
    main()
