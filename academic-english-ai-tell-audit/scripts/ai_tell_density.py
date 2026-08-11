#!/usr/bin/env python3
"""
ai_tell_density.py — READ-ONLY AI-tell density audit for English academic prose.

MEASURES, never rewrites. Reports an AI-tell DENSITY (markers per 1,000 body-prose
words) plus structural tells, with locations. It is a STYLE-DENSITY INDEX, NOT an
"% AI-written" verdict and NOT an authorship detector.

Scope: body prose only. Citations, quotations, boxes/cases, figures, defined terms and
reference lists are excluded from both the word total and the marker count.

Usage:
  python ai_tell_density.py --input <folder-or-glob> [--out report.md] [--log RUN_LOG.md]
                            [--ext .tex,.md,.txt]
"""
from __future__ import annotations
import argparse, glob, hashlib, os, re, sys
from datetime import datetime

WORD = re.compile(r"[A-Za-z][A-Za-z'-]*")

# --- marker lexicon (mirror of references/markers.md, v0.1.0) ---
SINGLE = [
    "delve","delves","delving","delved","underscore","underscores","underscored",
    "underscoring","showcase","showcases","showcased","showcasing","leverage",
    "leverages","leveraged","harness","harnesses","harnessed","foster","fosters",
    "fostered","align","aligns","aligned","boast","boasts","boasted","encompass",
    "encompasses","encompassed","surpass","surpasses","surpassed","unlock","unlocks",
    "unlocked","illuminate","illuminates","garner","garners","garnered","spearhead",
    "spearheads","crucial","pivotal","intricate","meticulous","commendable",
    "comprehensive","notable","notably","robust","seamless","seamlessly","nuanced",
    "multifaceted","invaluable","paramount","versatile","innovative","holistic",
    "additionally","moreover","furthermore","potential","insights","realm","tapestry",
    "testament","paradigm","synergy","cornerstone","interplay",
]
SINGLE_SET = set(SINGLE)
PHRASES = [
    "a wide range of","plays a pivotal role","plays a crucial role","it is worth noting",
    "it is important to note","in the realm of","a testament to","sheds light on",
    "paves the way","the ever-evolving","at the forefront of","cutting-edge","ever-evolving",
]
STRUCT = {
    "negative parallelism (not only...but also)": re.compile(r"\bnot only\b.*?\bbut\b", re.I),
    "not just...but": re.compile(r"\bnot just\b.*?\bbut\b", re.I),
    "boilerplate emphasis": re.compile(r"\b(it is worth noting|it is important to note)\b", re.I),
    "sentence-initial Notably/Importantly": re.compile(r"(^|\.\s+)(Notably|Importantly),", ),
    "connective opener": re.compile(r"(^|\.\s+)(Moreover|Furthermore|Additionally|In particular)\b"),
    "formulaic closer": re.compile(r"\b(In conclusion|In summary),", re.I),
    "rule-of-three (x, y, and z)": re.compile(r"\b\w+,\s+\w+,\s+and\s+\w+\b"),
}
PROT_ENV = re.compile(r"\\begin\{[^}]*(definition|theorem|theory|perspective|case|summary|box|quote|quotation|tcolorbox|mdframed|figure|table|verbatim|lstlisting|equation)[^}]*\}", re.I)
PROT_END = re.compile(r"\\end\{[^}]*(definition|theorem|theory|perspective|case|summary|box|quote|quotation|tcolorbox|mdframed|figure|table|verbatim|lstlisting|equation)[^}]*\}", re.I)
PROT_LINE = re.compile(r"^\s*(Definition|Theory|Theorem|Perspective|Case|Summary|Figure|Table|Source|References|Further Reading)\b", re.I)
CITE = re.compile(r"\([^)]*\b(19|20)\d\d[a-z]?\b[^)]*\)")
QUOTE = re.compile(r"[\"“”].*?[\"“”]")
DASH = re.compile(r"—")

def sha(p):
    h=hashlib.sha256()
    with open(p,"rb") as f:
        for c in iter(lambda:f.read(8192),b""): h.update(c)
    return h.hexdigest()[:12]

def gather(inp,exts):
    if os.path.isdir(inp):
        out=[]
        for e in exts: out+=glob.glob(os.path.join(inp,"**","*"+e),recursive=True)
        return sorted(set(out))
    return sorted(set(glob.glob(inp,recursive=True)))

def audit(path):
    body_words=0; excluded=0; dash=0
    markers={}; struct={}; depth=0
    with open(path,encoding="utf-8",errors="replace") as f:
        for i,raw in enumerate(f,1):
            line=raw.rstrip("\n")
            dash+=len(DASH.findall(line))
            if PROT_ENV.search(line): depth+=1
            protected = depth>0 or bool(PROT_LINE.match(line))
            if PROT_END.search(line) and depth>0: depth-=1
            if protected:
                excluded+=1
                continue
            # strip citations and quotations from body line before counting
            clean=QUOTE.sub(" ", CITE.sub(" ", line))
            toks=WORD.findall(clean)
            body_words+=len(toks)
            low=clean.lower()
            for t in toks:
                tl=t.lower()
                if tl in SINGLE_SET:
                    markers[tl]=markers.get(tl,0)+1
            for ph in PHRASES:
                n=low.count(ph)
                if n: markers[ph]=markers.get(ph,0)+n
            for name,pat in STRUCT.items():
                n=len(pat.findall(line))
                if n: struct[name]=struct.get(name,0)+n
    total_marks=sum(markers.values())
    density=round(1000.0*total_marks/body_words,1) if body_words else 0.0
    return {"body_words":body_words,"excluded_lines":excluded,"em_dashes":dash,
            "markers":markers,"struct":struct,"total_marks":total_marks,"density":density}

def band(d):
    return "low" if d<3 else ("medium" if d<=6 else "high")

def main():
    ap=argparse.ArgumentParser(description="Read-only AI-tell density audit (English).")
    ap.add_argument("--input",required=True)
    ap.add_argument("--out",default="ai_tell_report.md")
    ap.add_argument("--log",default=None)
    ap.add_argument("--ext",default=".tex,.md,.txt")
    a=ap.parse_args()
    exts=[e if e.startswith(".") else "."+e for e in a.ext.split(",")]
    files=gather(a.input,exts)
    if not files:
        print("No files matched: "+a.input,file=sys.stderr); return 1
    ts=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    out=["# AI-tell density report (English) — "+ts,"",
         "_Style-density index, NOT an AI-authorship verdict. Body prose only; "
         "citations/quotes/boxes/cases/figures excluded._",""]
    for p in files:
        r=audit(p)
        out.append("## "+os.path.basename(p)+"  (`"+sha(p)+"`)")
        out.append("- body-prose words: %d (excluded regions/lines: %d)"%(r["body_words"],r["excluded_lines"]))
        out.append("- **AI-tell density: %.1f / 1000  (band: %s)**"%(r["density"],band(r["density"])))
        out.append("- em-dash count: %d"%r["em_dashes"])
        if r["markers"]:
            top=sorted(r["markers"].items(),key=lambda x:-x[1])[:15]
            out.append("- top markers: "+", ".join("%s x%d"%(w,n) for w,n in top))
        else:
            out.append("- top markers: none")
        if r["struct"]:
            out.append("- structural tells: "+", ".join("%s x%d"%(k,v) for k,v in sorted(r["struct"].items(),key=lambda x:-x[1])))
        b=band(r["density"])
        if b=="high":
            rec="Density is high. Consider thinning the top markers toward ~3/1000 — but keep words the material's register legitimately needs. Send to academic-english-narrative for any rewriting."
        elif b=="medium":
            rec="Density is moderate. Optionally thin the most repeated markers; register-aware, no rewrite here."
        else:
            rec="Density is low. No action needed on style markers."
        out.append("- recommendation (advisory): "+rec)
        out.append("")
    out.append("_Reminder: markers are legitimate in moderation; the signal is over-use, not presence. This audit measures and flags — it never rewrites._")
    open(a.out,"w",encoding="utf-8").write("\n".join(out)+"\n")
    print("Wrote "+a.out+" ("+str(len(files))+" files)")
    if a.log:
        with open(a.log,"a",encoding="utf-8") as f:
            f.write("\n- ai_tell_density.py @ "+ts+": "+str(len(files))+" files; report="+a.out+"\n")
            for p in files:
                r=audit(p)
                f.write("  - "+os.path.basename(p)+" ("+sha(p)+"): density="+str(r["density"])+"/1000 band="+band(r["density"])+" body_words="+str(r["body_words"])+"\n")
        print("Appended to "+a.log)
    return 0

if __name__=="__main__":
    sys.exit(main())
