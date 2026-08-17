#!/usr/bin/env python3
"""
scan.py — deterministic, READ-ONLY consistency scanner for
academic-english-consistency (Phase 0/1/3 aid).

It does NOT edit source files and it does NOT decide anything. It produces
objective counts and line-located hits that seed the style-sheet decisions and
flag candidate deviations. The LLM still confirms protected-content status and all
judgement calls.

Usage:
    python scan.py --input <folder-or-glob> [--out report.md] [--log RUN_LOG.md]
                   [--ext .tex,.md,.txt]

Exit code is always 0 unless arguments are invalid; this is a reporter, not a gate.
"""
from __future__ import annotations
import argparse
import glob
import hashlib
import os
import re
import sys
from collections import Counter
from datetime import datetime

# --- Patterns -------------------------------------------------------------

SPELLING = {
    "-ise verbs":      re.compile(r"\b\w+is(e|es|ed|ing)\b"),
    "-ize verbs":      re.compile(r"\b\w+iz(e|es|ed|ing)\b"),
    "-isation nouns":  re.compile(r"\b\w+isation(s)?\b"),
    "-ization nouns":  re.compile(r"\b\w+ization(s)?\b"),
    "-our spelling":   re.compile(r"\b\w*(behaviour|favour|colour|labour|honour)\w*\b", re.I),
    "-or spelling":    re.compile(r"\b\w*(behavior|favor|color|labor|honor)\w*\b", re.I),
    "-yse spelling":   re.compile(r"\b\w*(analyse|paralyse)\w*\b", re.I),
    "-yze spelling":   re.compile(r"\b\w*(analyze|paralyze)\w*\b", re.I),
}

# crude false-positive guards for the generic -ise/-ize matchers
ISE_STOP = {"wise", "otherwise", "likewise", "rise", "arise", "raise", "praise",
            "noise", "promise", "premise", "expertise", "precise", "concise",
            "advertise", "exercise", "surprise", "comprise", "franchise", "anise"}
IZE_STOP = {"size", "prize", "seize", "maize", "capsize"}

REFS = {
    "(Section x.y)":     re.compile(r"\(Section\s+\d+(\.\d+)?"),
    "(section x.y) lc":  re.compile(r"\(section\s+\d+"),
    "(Sec. x.y)":        re.compile(r"\(Sec\.\s*\d+"),
    "(§ x.y)":           re.compile(r"\(?§\s*\d+"),
    "(cf. Section ...)": re.compile(r"\(cf\.\s+Section"),
    "(see Section ...)": re.compile(r"\(see\s+Section"),
}

CITES = {
    "& in parens":   re.compile(r"\([^)]*&[^)]*\d{4}"),
    "and in parens": re.compile(r"\([A-Z][^)]*\band\b[^)]*\d{4}"),
    "et al.":        re.compile(r"\bet\s+al\.?"),
    "\\cite cmd":    re.compile(r"\\cite[tp]?\b|\\parencite|\\textcite"),
}

PUNCT = {
    "curly double quotes": re.compile(r"[“”]"),
    "straight double quotes": re.compile(r'"'),
    "curly apostrophe":    re.compile(r"’"),
    "straight apostrophe": re.compile(r"'"),
    "em-dash (—)":         re.compile(r"—"),
    "en-dash (–)":         re.compile(r"–"),
    "ellipsis char (…)":   re.compile(r"…"),
    "ellipsis dots (...)": re.compile(r"\.\.\."),
    "double space":        re.compile(r"\S  +\S"),
    "space before punct":  re.compile(r"\s+[;:?!]"),
}

PROTECTED_ENV = re.compile(
    r"\\begin\{[^}]*(definition|theorem|theory|perspective|case|summary|box|quote|"
    r"quotation|tcolorbox|mdframed|figure|table|verbatim|lstlisting|equation)[^}]*\}",
    re.I,
)
PROTECTED_END = re.compile(
    r"\\end\{[^}]*(definition|theorem|theory|perspective|case|summary|box|quote|"
    r"quotation|tcolorbox|mdframed|figure|table|verbatim|lstlisting|equation)[^}]*\}",
    re.I,
)
PROTECTED_LINE = re.compile(
    r"^\s*(Definition|Theory Box|Perspective Box|Case|Summary|Figure|Table|Source)\b",
    re.I,
)

# box-environment consistency: a NUMBERED pedagogical box (Theory Box / Perspective Box /
# Case / Definition N.N) must not use an environment otherwise reserved for UNNUMBERED
# structural boxes (e.g. the chapter-opening "What this chapter is about" box). Catches the
# exact bug of a numbered box set with the intro-box environment. NOTE: one box label may
# LEGITIMATELY use several environments (discipline colouring, e.g. Theory Box as
# theorybox/psychbox/socbox), so we do NOT check label->environment; instead we flag any
# single environment that MIXES numbered and unnumbered boxes. Only *box environments.
BOX_ANY = re.compile(r"\\begin\{(\w*box\w*)\}\s*\[([^\]]*)\]")


def collect_boxes(path: str):
    out = []
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for i, raw in enumerate(f, 1):
            m = BOX_ANY.search(raw)
            if m:
                env, title = m.group(1), m.group(2)
                out.append((env, bool(re.search(r"\d", title)), i, title.strip()[:50]))
    return out


def sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()[:12]


def gather(inp: str, exts: list[str]) -> list[str]:
    if os.path.isdir(inp):
        files = []
        for e in exts:
            files += glob.glob(os.path.join(inp, "**", f"*{e}"), recursive=True)
        return sorted(set(files))
    return sorted(set(glob.glob(inp, recursive=True)))


def is_protected_line(line: str, depth: int) -> bool:
    return depth > 0 or bool(PROTECTED_LINE.match(line))


def scan_file(path: str) -> dict:
    counts: Counter = Counter()
    hits: list[tuple[int, str, str]] = []  # (lineno, category, snippet)
    depth = 0
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for i, raw in enumerate(f, 1):
            line = raw.rstrip("\n")
            if PROTECTED_ENV.search(line):
                depth += 1
            protected = is_protected_line(line, depth)
            if PROTECTED_END.search(line) and depth > 0:
                depth -= 1

            tag = "[protected]" if protected else "[body]"

            for name, pat in SPELLING.items():
                for m in pat.finditer(line):
                    word = m.group(0).lower()
                    if name == "-ise verbs" and word in ISE_STOP:
                        continue
                    if name == "-ize verbs" and word in IZE_STOP:
                        continue
                    counts[f"{name} {tag}"] += 1
                    if not protected:
                        hits.append((i, name, m.group(0)))
            for name, pat in {**REFS, **CITES, **PUNCT}.items():
                n = len(pat.findall(line))
                if n:
                    counts[f"{name} {tag}"] += n
    return {"counts": counts, "hits": hits}


def main() -> int:
    ap = argparse.ArgumentParser(description="Read-only consistency scanner.")
    ap.add_argument("--input", required=True, help="folder or glob of source files")
    ap.add_argument("--out", default="scan_report.md")
    ap.add_argument("--log", default=None, help="RUN_LOG.md to append a summary line")
    ap.add_argument("--ext", default=".tex,.md,.txt")
    args = ap.parse_args()

    exts = [e if e.startswith(".") else "." + e for e in args.ext.split(",")]
    files = gather(args.input, exts)
    if not files:
        print(f"No files matched: {args.input} ({exts})", file=sys.stderr)
        return 1

    total: Counter = Counter()
    per_file = {}
    for path in files:
        res = scan_file(path)
        per_file[path] = res
        total.update(res["counts"])

    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = [f"# scan.py report — {ts}", "", f"Files scanned: {len(files)}", ""]
    lines.append("## Book-wide totals (body vs protected separated)")
    lines.append("")
    lines.append("| Category | Count |")
    lines.append("|---|---:|")
    for k in sorted(total):
        lines.append(f"| {k} | {total[k]} |")
    lines.append("")

    # box-environment consistency: flag an environment that MIXES numbered + unnumbered boxes
    env_roles: dict = {}
    for path in files:
        for env, numbered, ln, title in collect_boxes(path):
            d = env_roles.setdefault(env, {"num": [], "unnum": []})
            d["num" if numbered else "unnum"].append((os.path.basename(path), ln, title))
    lines.append("## Box-environment consistency (numbered vs. unnumbered usage)")
    anomalies = False
    for env in sorted(env_roles):
        num, unnum = env_roles[env]["num"], env_roles[env]["unnum"]
        if num and unnum:
            anomalies = True
            minority = num if len(num) <= len(unnum) else unnum
            role = "numbered" if minority is num else "unnumbered"
            lines.append(f"- `{env}` is used BOTH numbered ({len(num)}x) and unnumbered "
                         f"({len(unnum)}x) --- check the minority ({role}):")
            for fn, ln, title in minority:
                lines.append(f"    - {fn}:{ln}  [{title}]")
    if not anomalies:
        lines.append("- no anomalies (no box environment mixes numbered and unnumbered boxes)")
    lines.append("")

    lines.append("## Per-file body-prose hits (candidates only — verify before use)")
    for path in files:
        res = per_file[path]
        lines.append("")
        lines.append(f"### {os.path.basename(path)}  (`{sha256(path)}`)")
        if not res["hits"]:
            lines.append("- no body-prose spelling-variant hits")
            continue
        shown = res["hits"][:200]
        lines.append("")
        lines.append("| line | category | text |")
        lines.append("|---:|---|---|")
        for ln, cat, txt in shown:
            safe = txt.replace("|", "\\|")
            lines.append(f"| {ln} | {cat} | {safe} |")
        if len(res["hits"]) > len(shown):
            lines.append(f"\n_(+{len(res['hits']) - len(shown)} more)_")

    with open(args.out, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Wrote {args.out}  ({len(files)} files)")

    if args.log:
        with open(args.log, "a", encoding="utf-8") as f:
            f.write(
                f"\n- scan.py @ {ts}: {len(files)} files; "
                f"report={args.out}; "
                f"-ise(body)={total.get('-ise verbs [body]', 0)} "
                f"-ize(body)={total.get('-ize verbs [body]', 0)} "
                f"-isation(body)={total.get('-isation nouns [body]', 0)} "
                f"-ization(body)={total.get('-ization nouns [body]', 0)}\n"
            )
        print(f"Appended summary to {args.log}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
