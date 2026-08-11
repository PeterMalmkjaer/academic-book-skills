#!/usr/bin/env python3
"""
maal.py — LÆS-KUN danske register-/læsbarhedsmål for academic-danish-klarsprog.

Gør stilprofilerne målbare i stedet for subjektive. Beregner proxy-mål for dialerne i
references/stilprofiler.md og (valgfrit) flagger, hvor en fil ligger ift. en profils
vejledende bånd. Skriver ALDRIG til kildefiler og BESLUTTER intet — den informerer den
menneskelige diagnose (Fase 1) og før/efter-tjekket (Fase 4).

VIGTIGT: LIX er rådgivende (Björnsson 1971) — et symptom, ikke et mål. Scriptet
rapporterer LIX; det foreslår aldrig at "optimere" tallet.

Mål (alle proxyer; fortolk med dømmekraft):
  - ord, sætninger
  - gennemsnitlig sætningslængde + SD (rytme)
  - LIX = ord/sætninger + (lange ord >6 bogstaver * 100 / ord)
  - lange-ord-procent
  - nominal-suffiks-tæthed /1000 (verbalsubstantiver: -ing/-ning/-else/-hed/
    -tion/-sion/-ering/-isering/-ans/-ens/-ITet)
  - anglicisme-proxy (kurateret ordliste over klodsede hybrider)
  - passiv-proxy /1000 (s-passiv + blive-passiv, tilnærmet)
  - læser-tiltale /1000 (du/I/vi/man/dig/jer)

Brug:
  python maal.py --input <mappe-eller-glob> [--profil laerebog-klarsprog]
                 [--out maal.md] [--log KOERSELSLOG.md] [--ext .tex,.md,.txt]
"""
from __future__ import annotations
import argparse, glob, hashlib, os, re, statistics, sys
from datetime import datetime

ORD = re.compile(r"[A-Za-zÆØÅæøåéüäöÉ]+")
SAETN = re.compile(r"(?<=[.!?:])\s+")
NOMINAL = re.compile(
    r"\b\w{4,}(ing|ning|else|hed|tion|sion|ering|isering|ans|ens|itet)\b", re.I)
PASSIV = re.compile(
    r"\b\w+(es|edes)\b|\b(blev|bliver|blevet|være|er)\s+\w+(et|t)\b", re.I)
TILTALE = re.compile(r"\b(du|dig|din|dit|dine|I|jer|jeres|vi|os|vores|man)\b")

# kuraterede klodsede anglicisme-hybrider (verbede/danglish); NB: ikke etablerede
# fagtermer, som beholdes bevidst (moral hazard, ratchet effect osv.)
ANGLICISMER = [
    "applicere", "applicerer", "applicerbar", "applicerbart", "applicerbare",
    "processere", "processerer", "processeret",
    "redesigne", "redesigner", "redesignet",
    "crowde", "crowder", "crowdet",
    "screene", "screener", "screenet",
    "flagge", "flagger", "flagget",
    "booste", "booster", "boostet",
    "performe", "performer", "performet",
    "mismatched", "mismatch",
    "outsource", "outsourcer", "outsourcet",
    "deploye", "deployer", "deployet",
]
ANG_RE = re.compile(r"\b(" + "|".join(ANGLICISMER) + r")\b", re.I)

# vejledende bånd pr. profil (LIX rådgivende; nominal/1k proxy)
PROFILER = {
    "laerebog-klarsprog":      {"lix": (45, 52), "nominal/1k": (0, 70), "sd_min": 5.0},
    "formidlende-engagerende": {"lix": (40, 48), "nominal/1k": (0, 55), "sd_min": 5.5},
    "stram-faglig":            {"lix": (50, 56), "nominal/1k": (0, 95), "sd_min": 3.5},
}


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


def per_k(n, w):
    return round(1000.0 * n / w, 1) if w else 0.0


def maal(path):
    t = open(path, encoding="utf-8", errors="replace").read()
    ord_ = ORD.findall(t)
    nw = len(ord_)
    sents = [s for s in SAETN.split(t) if s.strip()] or [t]
    ns = len(sents)
    lens = [len(ORD.findall(s)) for s in sents] or [0]
    lange = [w for w in ord_ if len(w) > 6]
    lix = round(nw / ns + len(lange) * 100.0 / nw, 1) if nw else 0.0
    return {
        "ord": nw, "saetninger": ns,
        "saetn_laengde": round(statistics.mean(lens), 1),
        "saetn_sd": round(statistics.pstdev(lens), 1) if len(lens) > 1 else 0.0,
        "lange_ord_pct": round(len(lange) * 100.0 / nw, 1) if nw else 0.0,
        "LIX": lix,
        "nominal/1k": per_k(len(NOMINAL.findall(t)), nw),
        "anglicismer": len(ANG_RE.findall(t)),
        "passiv/1k": per_k(len(PASSIV.findall(t)), nw),
        "tiltale/1k": per_k(len(TILTALE.findall(t)), nw),
    }


def flag(m, profil):
    b = PROFILER.get(profil)
    if not b:
        return []
    out = []
    lo, hi = b["lix"]
    if m["LIX"] > hi:
        out.append(f"LIX={m['LIX']} over sigtebånd {lo}-{hi} (rådgivende — handl ikke mekanisk)")
    elif m["LIX"] < lo:
        out.append(f"LIX={m['LIX']} under sigtebånd {lo}-{hi} (evt. for afsnubbet)")
    nlo, nhi = b["nominal/1k"]
    if m["nominal/1k"] > nhi:
        out.append(f"nominal/1k={m['nominal/1k']} over {nhi} (substantivsyge — verbalisér hvor muligt)")
    if m["saetn_sd"] < b["sd_min"]:
        out.append(f"saetn_sd={m['saetn_sd']} < {b['sd_min']} (flad rytme)")
    if m["anglicismer"] > 0:
        out.append(f"anglicisme-hybrider: {m['anglicismer']} (fordansk; behold bevidste fagtermer)")
    return out


def main():
    ap = argparse.ArgumentParser(description="Læs-kun danske register-/læsbarhedsmål.")
    ap.add_argument("--input", required=True)
    ap.add_argument("--profil", default=None, help=f"en af: {', '.join(PROFILER)}")
    ap.add_argument("--out", default="maal.md")
    ap.add_argument("--log", default=None)
    ap.add_argument("--ext", default=".tex,.md,.txt")
    a = ap.parse_args()

    exts = [e if e.startswith(".") else "." + e for e in a.ext.split(",")]
    files = gather(a.input, exts)
    if not files:
        print(f"Ingen filer matchede: {a.input} ({exts})", file=sys.stderr)
        return 1

    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cols = ["ord", "saetninger", "saetn_laengde", "saetn_sd", "lange_ord_pct",
            "LIX", "nominal/1k", "anglicismer", "passiv/1k", "tiltale/1k"]
    rows = [(p, maal(p)) for p in files]

    out = [f"# maal.py — danske register-/læsbarhedsmål — {ts}", "",
           f"Profil: **{a.profil or 'ingen (rå mål)'}**", f"Filer: {len(files)}",
           "", "_LIX er rådgivende (Björnsson 1971) — et symptom, ikke et mål._", "",
           "| fil | " + " | ".join(cols) + " |", "|---|" + "---|" * len(cols)]
    for p, m in rows:
        out.append("| " + os.path.basename(p) + " | " +
                   " | ".join(str(m[c]) for c in cols) + " |")
    if a.profil:
        out += ["", f"## Flag ift. `{a.profil}` (proxy-vejledning — bekræft ved læsning)"]
        for p, m in rows:
            fl = flag(m, a.profil) or ["inden for vejledende bånd"]
            out.append(f"- **{os.path.basename(p)}**: " + "; ".join(fl))
    out += ["", "_Mål er proxyer; de informerer — erstatter ikke — menneskelig dømmekraft._"]

    open(a.out, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print(f"Skrev {a.out} ({len(files)} filer)")

    if a.log:
        with open(a.log, "a", encoding="utf-8") as f:
            f.write(f"\n- maal.py @ {ts}: profil={a.profil}; filer={len(files)}; rapport={a.out}\n")
            for p, m in rows:
                f.write(f"  - {os.path.basename(p)} ({sha(p)}): LIX={m['LIX']} "
                        f"nominal/1k={m['nominal/1k']} sd={m['saetn_sd']} "
                        f"anglicismer={m['anglicismer']}\n")
        print(f"Tilføjede resumé til {a.log}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
