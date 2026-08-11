#!/usr/bin/env python3
"""
measure.py — READ-ONLY register/narrativity metrics for academic-english-narrative.

Makes the style presets measurable instead of subjective. It computes proxy metrics
for the dials described in references/style_presets.md and (optionally) flags where a
file sits relative to a preset's indicative bands. It NEVER edits source files and
NEVER decides — it informs the human diagnosis (Phase 1) and the before/after check
(Phase 4).

Metrics (all proxies; interpret with judgement):
  - sentences, words
  - sentence-length mean and SD  (rhythm variance)
  - nominalisation density /1000 (suffix proxy: -tion/-sion/-ment/-ness/-ity/-ance/-ence)
  - hedging density /1000        (may, might, could, perhaps, possibly, suggest, seem...)
  - metadiscourse/connective /1000 (however, therefore, thus, moreover, hence...)
  - passive proxy /1000          (be-form + past participle approximation)
  - first-person markers /1000   (I, we, our, us)
  - em-dash and en-dash counts

Usage:
  python measure.py --input <folder-or-glob> [--preset narrative-academic-european]
                    [--out metrics.md] [--log RUN_LOG.md] [--ext .tex,.md,.txt]
"""
from __future__ import annotations
import argparse, glob, hashlib, os, re, statistics, sys
from datetime import datetime

NOMINAL = re.compile(r"\b\w{4,}(tion|sion|ment|ness|ity|ance|ence)s?\b", re.I)
HEDGES = re.compile(
    r"\b(may|might|could|would|perhaps|possibly|probably|seem(s|ed)?|appear(s|ed)?|"
    r"suggest(s|ed)?|indicate(s|d)?|likely|arguably|relatively|somewhat|tend(s|ed)?)\b",
    re.I,
)
META = re.compile(
    r"\b(however|therefore|thus|hence|moreover|furthermore|nevertheless|nonetheless|"
    r"consequently|in addition|on the other hand|that is|for example|for instance|"
    r"in other words|by contrast|in particular|importantly)\b",
    re.I,
)
PASSIVE = re.compile(r"\b(is|are|was|were|be|been|being)\s+\w+(ed|en)\b", re.I)
FIRST = re.compile(r"\b(I|we|our|us|my|ours)\b")
EMDASH = re.compile(r"—")
ENDASH = re.compile(r"–")
SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z“\"(])")
WORD = re.compile(r"[A-Za-z][A-Za-z'-]*")

# indicative bands per preset (proxy /1000 unless noted). None = not constrained.
PRESETS = {
    "narrative-academic-european": {
        "nominalisation/1k": (40, 95), "hedges/1k": (8, 30),
        "sent_len_sd_min": 5.0, "first_person/1k": (0, 12),
    },
    "textbook-pedagogical": {
        "nominalisation/1k": (30, 80), "hedges/1k": (8, 30),
        "sent_len_sd_min": 5.0, "first_person/1k": (2, 20),
    },
    "journal-formal": {
        "nominalisation/1k": (70, 140), "hedges/1k": (12, 40),
        "sent_len_sd_min": 3.5, "first_person/1k": (0, 8),
    },
    "trade-crossover": {
        "nominalisation/1k": (10, 55), "hedges/1k": (4, 20),
        "sent_len_sd_min": 7.0, "first_person/1k": (2, 25),
    },
}


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
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


def per_k(n, words):
    return round(1000.0 * n / words, 1) if words else 0.0


def measure(path):
    text = open(path, encoding="utf-8", errors="replace").read()
    words = WORD.findall(text)
    nw = len(words)
    sents = [s for s in SENT_SPLIT.split(text) if s.strip()]
    lens = [len(WORD.findall(s)) for s in sents] or [0]
    return {
        "words": nw,
        "sentences": len(sents),
        "sent_len_mean": round(statistics.mean(lens), 1),
        "sent_len_sd": round(statistics.pstdev(lens), 1) if len(lens) > 1 else 0.0,
        "nominalisation/1k": per_k(len(NOMINAL.findall(text)), nw),
        "hedges/1k": per_k(len(HEDGES.findall(text)), nw),
        "metadiscourse/1k": per_k(len(META.findall(text)), nw),
        "passive/1k": per_k(len(PASSIVE.findall(text)), nw),
        "first_person/1k": per_k(len(FIRST.findall(text)), nw),
        "em_dash": len(EMDASH.findall(text)),
        "en_dash": len(ENDASH.findall(text)),
    }


def flags(m, preset):
    band = PRESETS.get(preset)
    if not band:
        return []
    out = []
    for key in ("nominalisation/1k", "hedges/1k", "first_person/1k"):
        if key in band and isinstance(band[key], tuple):
            lo, hi = band[key]
            v = m[key]
            if v < lo:
                out.append(f"{key}={v} below band {lo}-{hi}")
            elif v > hi:
                out.append(f"{key}={v} above band {lo}-{hi}")
    if "sent_len_sd_min" in band and m["sent_len_sd"] < band["sent_len_sd_min"]:
        out.append(f"sent_len_sd={m['sent_len_sd']} < {band['sent_len_sd_min']} (flat rhythm)")
    return out


def main():
    ap = argparse.ArgumentParser(description="Read-only register/narrativity metrics.")
    ap.add_argument("--input", required=True)
    ap.add_argument("--preset", default=None, help=f"one of: {', '.join(PRESETS)}")
    ap.add_argument("--out", default="metrics.md")
    ap.add_argument("--log", default=None)
    ap.add_argument("--ext", default=".tex,.md,.txt")
    a = ap.parse_args()

    exts = [e if e.startswith(".") else "." + e for e in a.ext.split(",")]
    files = gather(a.input, exts)
    if not files:
        print(f"No files matched: {a.input} ({exts})", file=sys.stderr)
        return 1

    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    rows, all_flags = [], {}
    cols = ["words", "sentences", "sent_len_mean", "sent_len_sd",
            "nominalisation/1k", "hedges/1k", "metadiscourse/1k", "passive/1k",
            "first_person/1k", "em_dash", "en_dash"]
    for p in files:
        m = measure(p)
        rows.append((p, m))
        if a.preset:
            all_flags[p] = flags(m, a.preset)

    lines = [f"# measure.py metrics — {ts}", "",
             f"Preset: **{a.preset or 'none (raw metrics only)'}**",
             f"Files: {len(files)}", "", "| file | " + " | ".join(cols) + " |",
             "|---|" + "---|" * len(cols)]
    for p, m in rows:
        lines.append("| " + os.path.basename(p) + " | " +
                     " | ".join(str(m[c]) for c in cols) + " |")
    if a.preset:
        lines += ["", f"## Flags vs `{a.preset}` (proxy guidance — verify by reading)"]
        for p, _ in rows:
            fl = all_flags.get(p) or ["within indicative bands"]
            lines.append(f"- **{os.path.basename(p)}**: " + "; ".join(fl))
    lines += ["", "_Metrics are proxies; they inform—not replace—human judgement._"]

    open(a.out, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print(f"Wrote {a.out} ({len(files)} files)")

    if a.log:
        with open(a.log, "a", encoding="utf-8") as f:
            f.write(f"\n- measure.py @ {ts}: preset={a.preset}; files={len(files)}; "
                    f"report={a.out}\n")
            for p, m in rows:
                f.write(f"  - {os.path.basename(p)} ({sha(p)}): "
                        f"nom/1k={m['nominalisation/1k']} sd={m['sent_len_sd']} "
                        f"hedge/1k={m['hedges/1k']} em-dash={m['em_dash']}\n")
        print(f"Appended summary to {a.log}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
