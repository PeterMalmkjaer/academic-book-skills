#!/usr/bin/env python3
"""
engagement_score.py — READ-ONLY reading-engagement audit for English academic prose.

MEASURES, never rewrites. Reports the validated Flesch Human-Interest score plus
evidence-informed proxies (concreteness, reader-engagement, narrativity). Engagement is a
distinct axis from readability. Raising the score is NOT a goal in itself: interesting but
irrelevant detail (seductive details) HARMS learning (Harp & Mayer, 1998). Body prose
only; citations/quotes/boxes/cases/figures excluded.

Usage:
  python engagement_score.py --input <folder-or-glob> [--out report.md] [--log RUN_LOG.md]
                             [--ext .tex,.md,.txt]
"""
from __future__ import annotations
import argparse, glob, hashlib, os, re, sys
from datetime import datetime

WORD = re.compile(r"[A-Za-z][A-Za-z'-]*")
SENT_SPLIT = re.compile(r"(?<=[.!?])\s+")

PRONOUNS = {"i","me","my","mine","myself","we","us","our","ours","ourselves","you","your",
 "yours","yourself","yourselves","he","him","his","himself","she","her","hers","herself",
 "they","them","their","theirs","themselves"}
PERSON_NOUNS = {"people","folks","man","woman","men","women","boy","girl","child","children",
 "mother","father","mom","dad","sister","brother","son","daughter","friend","teacher",
 "student","doctor","patient","manager","employee","worker","author","reader","colleague",
 "person","everyone","someone","nobody","he's","she's"}
CONCRETE = ["for example","for instance","e.g.","such as","consider","imagine","picture",
 "take the case","example","case","story","scenario","suppose","think of"]
ENGAGE_ADDR = {"you","your","yours","we","us","our","reader","readers"}
NARR = {"then","when","after","before","during","suddenly","first","next","finally","later",
 "once","meanwhile","eventually","soon"}

PROT_ENV=re.compile(r"\\begin\{[^}]*(definition|theorem|theory|perspective|case|summary|box|quote|quotation|tcolorbox|mdframed|figure|table|verbatim|lstlisting|equation)[^}]*\}", re.I)
PROT_END=re.compile(r"\\end\{[^}]*(definition|theorem|theory|perspective|case|summary|box|quote|quotation|tcolorbox|mdframed|figure|table|verbatim|lstlisting|equation)[^}]*\}", re.I)
PROT_LINE=re.compile(r"^\s*(Definition|Theory|Theorem|Perspective|Case|Summary|Figure|Table|Source|References|Further Reading)\b", re.I)
CITEPAR=re.compile(r"\([^)]*\b(19|20)\d\d[a-z]?\b[^)]*\)")
QUOTED=re.compile(r"[\"“”]")

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
    body_lines=[]; excluded=0; depth=0
    with open(path,encoding="utf-8",errors="replace") as f:
        for raw in f:
            line=raw.rstrip("\n")
            if PROT_ENV.search(line): depth+=1
            protected=depth>0 or bool(PROT_LINE.match(line))
            if PROT_END.search(line) and depth>0: depth-=1
            if protected: excluded+=1; continue
            body_lines.append(CITEPAR.sub(" ",line))
    text=" ".join(body_lines)
    words=WORD.findall(text); nw=len(words)
    sents=[s for s in SENT_SPLIT.split(text) if s.strip()]; ns=len(sents) or 1
    # personal words
    pw=0
    for w in words:
        if w.lower() in PRONOUNS or w.lower() in PERSON_NOUNS: pw+=1
    # personal sentences
    ps=0
    for s in sents:
        sl=s.lower()
        if ("?" in s) or ("!" in s) or QUOTED.search(s) or (" you" in " "+sl) or sl.startswith("you"):
            ps+=1
    pw100=100.0*pw/nw if nw else 0.0
    ps100=100.0*ps/ns if ns else 0.0
    HI=round(3.635*pw100+0.314*ps100,1)
    # proxies per 1000 words
    low=text.lower()
    conc=sum(low.count(m) for m in CONCRETE)
    quest=text.count("?")
    addr=sum(1 for w in words if w.lower() in ENGAGE_ADDR)
    narr=sum(1 for w in words if w.lower() in NARR)
    per=lambda n: round(1000.0*n/nw,1) if nw else 0.0
    return {"words":nw,"sentences":ns,"excluded":excluded,"HI":HI,
            "pw_per100":round(pw100,1),"ps_per100":round(ps100,1),
            "concreteness_per1k":per(conc),"engagement_per1k":per(quest+addr),
            "questions":quest,"narrativity_per1k":per(narr)}

def hi_band(hi):
    if hi>=50: return "very interesting / dramatic"
    if hi>=30: return "interesting"
    if hi>=10: return "modest human interest"
    return "low human interest (typical of dense expository prose)"

def overall(hi,conc):
    if hi>=30 or conc>=8: return "engaging"
    if hi>=10 or conc>=4: return "moderately engaging"
    return "low engagement (may be genre-appropriate for dense theory)"

def main():
    ap=argparse.ArgumentParser(description="Read-only reading-engagement audit (English).")
    ap.add_argument("--input",required=True); ap.add_argument("--out",default="engagement_report.md")
    ap.add_argument("--log",default=None); ap.add_argument("--ext",default=".tex,.md,.txt")
    a=ap.parse_args()
    exts=[e if e.startswith(".") else "."+e for e in a.ext.split(",")]
    files=gather(a.input,exts)
    if not files: print("No files matched: "+a.input,file=sys.stderr); return 1
    ts=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    out=["# Reading-engagement report (English) — "+ts,"",
         "_Engagement index (Human Interest is validated; concreteness/engagement/narrativity "
         "are directional proxies). NOT a readability grade. Body prose only. Measures only — "
         "never rewrites; raising the score with irrelevant detail harms learning (seductive details)._",""]
    for p in files:
        r=audit(p)
        out.append("## "+os.path.basename(p)+"  (`"+sha(p)+"`)")
        out.append("- body prose: %d words, %d sentences (excluded lines: %d)"%(r["words"],r["sentences"],r["excluded"]))
        out.append("- **Human Interest (Flesch): %.1f — %s**"%(r["HI"],hi_band(r["HI"])))
        out.append("  (personal words %.1f/100, personal sentences %.1f/100)"%(r["pw_per100"],r["ps_per100"]))
        out.append("- concreteness proxy: %.1f/1000 · reader-engagement: %.1f/1000 (questions: %d) · narrativity: %.1f/1000"%(r["concreteness_per1k"],r["engagement_per1k"],r["questions"],r["narrativity_per1k"]))
        out.append("- **overall band (advisory): %s**"%overall(r["HI"],r["concreteness_per1k"]))
        ob=overall(r["HI"],r["concreteness_per1k"])
        if ob.startswith("low"):
            rec=("If this is an introduction, case, or student-facing section, consider RELEVANT "
                 "concreteness (worked examples, a running case, a well-placed question) — Sadoski's "
                 "lever. If it is dense theory, a low score is usually appropriate. Never add "
                 "irrelevant vividness (seductive details). Rewriting: academic-english-narrative.")
        elif ob.startswith("moderately"):
            rec="Reasonable for academic prose. Optional: a concrete example or reader-question where it aids the argument. No rewrite here."
        else:
            rec="Engaging. Guard only against decorative/irrelevant interest. No action needed."
        out.append("- recommendation (advisory, register-aware): "+rec)
        out.append("- to change the text: this skill will not rewrite; on an explicit order it states these consequences and hands rewriting to academic-english-narrative.")
        out.append("")
    out.append("_Consequence note: engagement is a distinct axis from readability and correctness; "
               "optimise it only where the genre calls for it, and only through relevant concreteness "
               "and coherence — never seductive details._")
    open(a.out,"w",encoding="utf-8").write("\n".join(out)+"\n")
    print("Wrote "+a.out+" ("+str(len(files))+" files)")
    if a.log:
        with open(a.log,"a",encoding="utf-8") as f:
            f.write("\n- engagement_score.py @ "+ts+": "+str(len(files))+" files; report="+a.out+"\n")
            for p in files:
                r=audit(p); f.write("  - "+os.path.basename(p)+" ("+sha(p)+"): HI="+str(r["HI"])+" conc="+str(r["concreteness_per1k"])+"/1k overall="+overall(r["HI"],r["concreteness_per1k"])+"\n")
        print("Appended to "+a.log)
    return 0

if __name__=="__main__": sys.exit(main())
