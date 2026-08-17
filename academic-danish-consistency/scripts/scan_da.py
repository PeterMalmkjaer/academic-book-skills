#!/usr/bin/env python3
"""
scan_da.py — deterministisk, LÆS-KUN konsistens-scanner for academic-danish-consistency.

Redigerer ALDRIG kildefiler og BESLUTTER intet. Producerer objektive tal og
linjeplacerede hits, der frø-sætter stilark-beslutninger (Fase 1) og kandidat-
afvigelser (Fase 3). LLM-laget bekræfter beskyttet-status og dømmekald.

Brug:
    python scan_da.py --input <mappe-eller-glob> [--out rapport.md] [--log KOERSELSLOG.md]
                      [--ext .tex,.md,.txt]
"""
from __future__ import annotations
import argparse, glob, hashlib, os, re, sys
from collections import Counter
from datetime import datetime

# --- danglish labels (engelsk i dansk strukturramme) ---
DANGLISH_LABEL = {
    "Figure (→ Figur)":  re.compile(r"\bFigure\s*\d"),
    "Table (→ Tabel)":   re.compile(r"\bTable\s*\d"),
    "Box (→ Boks)":      re.compile(r"\bBox\b"),
}

# engelske ord midt i dansk brødtekst (kurateret; ikke bevidste fagtermer)
ENGELSK_I_DANSK = [
    "measures", "performance", "output", "feedback", "targets", "benchmark",
    "framework", "tool", "substitut", "tradeoff", "trade-off", "screening",
    "gaming", "commitment", "discretion", "outside option", "back office",
]
ENG_RE = re.compile(r"\b(" + "|".join(re.escape(w) for w in ENGELSK_I_DANSK) + r")\b")

# kalke-/term-konsistens: dansk oversættelseslån ↔ engelsk fagterm. Flag den danske kalke-
# form som review-kandidat (LLM/forfatter vælger ÉN konsistent form: engelsk term ELLER en
# ren dansk term). Generel, disciplin-agnostisk seed-liste — udvid pr. projekt-stilark.
# Matcher også bøjninger ("rammeværker", "rammeværkets"). Fanger IKKE selve den engelske
# term (den tælles separat via totaler, så et split bliver synligt).
KALKE = {
    "rammeværk": "framework",
    "vokabular":  "vocabulary (evt. begrebsapparat/ordforråd)",
}
KALKE_RE = re.compile(r"\b(" + "|".join(KALKE) + r")[a-zæøå]*\b", re.I)

# overskrifts-Title-Case (flere indholdsord med stort, ud over første) — proxy
TITLE_CASE = re.compile(r"^\s*(\d+(\.\d+)*\s+)?([A-ZÆØÅ][a-zæøå]+\s+){1,}[A-ZÆØÅ][a-zæøå]+")

REFS = {
    "(afsnit x.y)":      re.compile(r"\(afsnit\s+\d"),
    "(Afsnit x.y)":      re.compile(r"\(Afsnit\s+\d"),
    "(§ x.y)":           re.compile(r"\(?§\s*\d"),
    "(jf. afsnit ...)":  re.compile(r"\(jf\.\s+afsnit"),
    "(se afsnit ...)":   re.compile(r"\(se\s+afsnit"),
}
# genitiv-apostrof (RO § 21): egennavn tager -s UDEN apostrof; -s/-x/-z: apostrof uden s;
# punktumløse forkortelser tager 's (korrekt). GEN_NAME kræver lille bogstav som 2. tegn,
# så all-caps-forkortelser (EU's, USA's, IBM's) IKKE fanges som anglicisme.
GEN_NAME = re.compile(r"\b([A-ZÆØÅ][a-zæøå][A-Za-zÆØÅæøå]*)['’]s\b")
GEN_ABBR = re.compile(r"\b[A-ZÆØÅ]{2,}['’]s\b")
GEN_BRAND = {"McDonald"}  # varemærke: apostrof er en del af navnet
TYPO = {
    "punktum-decimal (→ komma?)": re.compile(r"\d+\.\d+"),
    "komma-decimal":              re.compile(r"\d+,\d+"),
    "danske anførselstegn »«":    re.compile(r"[»«„]"),
    "engelske krøllede ‟”":       re.compile(r"[“”]"),
    "lige anførselstegn":         re.compile(r"\""),
    "dobbeltmellemrum":           re.compile(r"\S  +\S"),
}
PROTECTED_LINE = re.compile(
    r"^\s*(Definition|Teoretisk|Teoriboks|Perspektiv|Perspektivbox|Case|Sammenfatning|"
    r"Figur|Figure|Tabel|Table|Kilde)\b", re.I)
PROTECTED_ENV = re.compile(
    r"\\begin\{[^}]*(definition|teorem|teoretisk|perspektiv|case|sammenfatning|boks|box|"
    r"quote|quotation|tcolorbox|mdframed|figure|table|verbatim|lstlisting|equation)[^}]*\}", re.I)
PROTECTED_END = re.compile(
    r"\\end\{[^}]*(definition|teorem|teoretisk|perspektiv|case|sammenfatning|boks|box|"
    r"quote|quotation|tcolorbox|mdframed|figure|table|verbatim|lstlisting|equation)[^}]*\}", re.I)

# boks-miljø-konsistens: en NUMMERERET pædagogisk boks (Teoriboks/Perspektivboks/Case/
# Definition N.N) bør ikke bruge et miljø, der ellers er reserveret til UNUMMEREREDE
# strukturbokse (fx kapitlets intro-boks "Hvad dette kapitel handler om"). Fanger præcis
# fejlen "Perspektivboks 17.1" sat med \begin{perspectivebox} (intro-miljøet).
# VIGTIGT: samme overskrift kan LEGITIMT bruge flere miljøer (disciplin-farvning, fx
# Teoriboks som theorybox/psychbox/socbox), så vi tjekker IKKE label→miljø, men om et
# enkelt miljø BLANDER nummererede og unummererede bokse. Kun *box-miljøer; sprog-neutral.
BOX_ANY = re.compile(r"\\begin\{(\w*box\w*)\}\s*\[([^\]]*)\]")


def collect_boxes(path):
    out = []
    with open(path, encoding="utf-8", errors="replace") as f:
        for i, raw in enumerate(f, 1):
            m = BOX_ANY.search(raw)
            if m:
                env, title = m.group(1), m.group(2)
                out.append((env, bool(re.search(r"\d", title)), i, title.strip()[:50]))
    return out


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(8192), b""):
            h.update(c)
    return h.hexdigest()[:12]


def gather(inp, exts):
    if os.path.isdir(inp):
        out = []
        for e in exts:
            out += glob.glob(os.path.join(inp, "**", f"*{e}"), recursive=True)
        return sorted(set(out))
    return sorted(set(glob.glob(inp, recursive=True)))


def scan(path):
    counts = Counter()
    hits = []
    depth = 0
    looks_heading = re.compile(r"^\s*(\d+(\.\d+)*\s+)?\S")
    with open(path, encoding="utf-8", errors="replace") as f:
        for i, raw in enumerate(f, 1):
            line = raw.rstrip("\n")
            if PROTECTED_ENV.search(line):
                depth += 1
            protected = depth > 0 or bool(PROTECTED_LINE.match(line))
            if PROTECTED_END.search(line) and depth > 0:
                depth -= 1
            tag = "[beskyttet]" if protected else "[brødtekst]"

            for name, pat in DANGLISH_LABEL.items():
                n = len(pat.findall(line))
                if n:
                    counts[f"{name} {tag}"] += n
                    hits.append((i, name, line.strip()[:60]))
            if not protected:
                for w in set(m.group(0) for m in ENG_RE.finditer(line)):
                    counts[f"engelsk-i-dansk: {w} [brødtekst]"] += 1
                    hits.append((i, f"engelsk-i-dansk: {w}", line.strip()[:60]))
                # Title-Case-overskrift: kort linje (<= 9 ord) med flere store indholdsord
                words = line.split()
                if 1 < len(words) <= 9 and TITLE_CASE.match(line):
                    caps = sum(1 for w in words if w[:1].isupper())
                    if caps >= 3:
                        counts["overskrift Title Case (→ sætningscase) [brødtekst]"] += 1
                        hits.append((i, "overskrift Title Case", line.strip()[:60]))
            for name, pat in {**REFS, **TYPO}.items():
                n = len(pat.findall(line))
                if n:
                    counts[f"{name} {tag}"] += n
            # genitiv-apostrof: flag egennavns-kandidater; forkortelses-'s tælles som korrekt.
            # LLM-laget bekræfter undtagelser (eponym "X's Law", referencetitler, "Cohen's d").
            for m in GEN_NAME.finditer(line):
                if m.group(1) in GEN_BRAND:
                    continue
                cat = f"genitiv-apostrof egennavn (→ uden apostrof) {tag}"
                counts[cat] += 1
                hits.append((i, cat, line.strip()[:60]))
            na = len(GEN_ABBR.findall(line))
            if na:
                counts[f"genitiv 's på forkortelse (korrekt) {tag}"] += na
            # kalke-/term-konsistens: flag dansk kalke-form (review-kandidat)
            for m in KALKE_RE.finditer(line):
                base = m.group(1).lower()
                eng = KALKE.get(base, "?")
                cat = f"kalke-kandidat: {base} (← {eng}) {tag}"
                counts[cat] += 1
                hits.append((i, cat, line.strip()[:60]))
    return counts, hits


def main():
    ap = argparse.ArgumentParser(description="Læs-kun dansk konsistens-scanner.")
    ap.add_argument("--input", required=True)
    ap.add_argument("--out", default="scan_da_rapport.md")
    ap.add_argument("--log", default=None)
    ap.add_argument("--ext", default=".tex,.md,.txt")
    a = ap.parse_args()
    exts = [e if e.startswith(".") else "." + e for e in a.ext.split(",")]
    files = gather(a.input, exts)
    if not files:
        print(f"Ingen filer matchede: {a.input} ({exts})", file=sys.stderr)
        return 1

    total = Counter()
    per = {}
    for p in files:
        c, h = scan(p)
        per[p] = (c, h)
        total.update(c)

    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    out = [f"# scan_da.py rapport — {ts}", "", f"Filer scannet: {len(files)}", "",
           "## Bogdækkende totaler (brødtekst vs. beskyttet adskilt)", "",
           "| Kategori | Antal |", "|---|---:|"]
    for k in sorted(total):
        out.append(f"| {k} | {total[k]} |")

    # boks-miljø-konsistens: flag et miljø der BLANDER nummererede og unummererede bokse
    env_roles = {}
    for p in files:
        for env, numbered, ln, title in collect_boxes(p):
            d = env_roles.setdefault(env, {"num": [], "unnum": []})
            d["num" if numbered else "unnum"].append((os.path.basename(p), ln, title))
    out += ["", "## Boks-miljø-konsistens (nummereret vs. unummereret miljø-brug)"]
    anomalies = False
    for env in sorted(env_roles):
        num, unnum = env_roles[env]["num"], env_roles[env]["unnum"]
        if num and unnum:
            anomalies = True
            minority = num if len(num) <= len(unnum) else unnum
            role = "nummereret" if minority is num else "unummereret"
            out.append(f"- `{env}` bruges BÅDE nummereret ({len(num)}×) og unummereret "
                       f"({len(unnum)}×) --- tjek minoriteten ({role}):")
            for fn, ln, title in minority:
                out.append(f"    - {fn}:{ln}  [{title}]")
    if not anomalies:
        out.append("- ingen afvigelser (intet box-miljø blander nummererede og unummererede bokse)")

    out += ["", "## Pr. fil — brødtekst-hits (kandidater — bekræft før brug)"]
    for p in files:
        c, h = per[p]
        out += ["", f"### {os.path.basename(p)}  (`{sha(p)}`)"]
        bod = [x for x in h if "beskyttet" not in x[1]][:120]
        if not bod:
            out.append("- ingen brødtekst-hits")
            continue
        out += ["", "| linje | kategori | tekst |", "|---:|---|---|"]
        for ln, cat, txt in bod:
            safe = txt.replace("|", "\\|")
            out.append(f"| {ln} | {cat} | {safe} |")

    open(a.out, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print(f"Skrev {a.out} ({len(files)} filer)")
    if a.log:
        with open(a.log, "a", encoding="utf-8") as f:
            f.write(f"\n- scan_da.py @ {ts}: {len(files)} filer; rapport={a.out}; "
                    f"Figure={total.get('Figure (→ Figur) [brødtekst]', 0)} "
                    f"Box={total.get('Box (→ Boks) [brødtekst]', 0)}\n")
        print(f"Tilføjede resumé til {a.log}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
