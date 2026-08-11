#!/usr/bin/env python3
"""
ai_tell_density_da.py — READ-ONLY AI-tell density audit for DANISH academic prose.

MEASURES, never rewrites. Reports AI-tell DENSITY (markers per 1,000 body-prose words)
plus structural tells. STYLE-DENSITY INDEX, NOT an "% AI-written" verdict.
NOTE: the Danish marker list is an informed adaptation (calibrate against a Danish
baseline). Body prose only; citations/quotes/boxes/cases/figures excluded.

Usage:
  python ai_tell_density_da.py --input <folder-or-glob> [--out report.md] [--log RUN_LOG.md]
                               [--ext .tex,.md,.txt]
"""
from __future__ import annotations
import argparse, glob, hashlib, os, re, sys
from datetime import datetime

WORD = re.compile(r"[A-Za-zÆØÅæøåéüäö][A-Za-zÆØÅæøåéüäö'-]*")

SINGLE = [
    "afgørende","central","centralt","centrale","nuanceret","robust","banebrydende",
    "sømløs","alsidig","mangefacetteret","uvurderlig","essentiel","markant","betydelig",
    "dybdegående","omfattende","innovativ","holistisk","ydermere","endvidere","desuden",
    "derudover","udnytte","muliggøre","understøtte","fremhæve","belyse","forankre",
    "sammenvæve","potentiale","indsigt","indsigter","synergi","hjørnesten","samspil",
]
SINGLE_SET=set(SINGLE)
PHRASES=[
    "en bred vifte af","spiller en central rolle","spiller en afgørende rolle",
    "det er værd at bemærke","det er vigtigt at bemærke","kaster lys over","baner vejen for",
    "i takt med","i en verden hvor","i sidste ende","i stigende grad",
]
STRUCT={
    "negativ parallelisme (ikke kun...men også)": re.compile(r"\bikke kun\b.*?\bmen\b", re.I),
    "ikke blot...men": re.compile(r"\bikke blot\b.*?\bmen\b", re.I),
    "boilerplate-fremhævelse": re.compile(r"\b(det er værd at bemærke|det er vigtigt at bemærke)\b", re.I),
    "forbinder-opener": re.compile(r"(^|\.\s+)(Derudover|Desuden|Endvidere|Ydermere|Ikke desto mindre)\b"),
    "formeludtryk-closer": re.compile(r"(^|\.\s+)(Afslutningsvis|Sammenfattende)\b"),
    "rule-of-three (x, y og z)": re.compile(r"\b\w+,\s+\w+\s+og\s+\w+\b"),
}
PROT_ENV=re.compile(r"\\begin\{[^}]*(definition|teorem|teoretisk|perspektiv|case|sammenfatning|boks|box|quote|quotation|tcolorbox|mdframed|figure|table|verbatim|lstlisting|equation)[^}]*\}", re.I)
PROT_END=re.compile(r"\\end\{[^}]*(definition|teorem|teoretisk|perspektiv|case|sammenfatning|boks|box|quote|quotation|tcolorbox|mdframed|figure|table|verbatim|lstlisting|equation)[^}]*\}", re.I)
PROT_LINE=re.compile(r"^\s*(Definition|Teoretisk|Teoriboks|Perspektiv|Case|Sammenfatning|Figur|Figure|Tabel|Table|Kilde|Videre Læsning|Referencer)\b", re.I)
CITE=re.compile(r"\([^)]*\b(19|20)\d\d[a-z]?\b[^)]*\)")
QUOTE=re.compile(r"[\"“”„».*?[\"“”«]")
DASH=re.compile(r"—")

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
    body_words=0; excluded=0; dash=0; markers={}; struct={}; depth=0
    with open(path,encoding="utf-8",errors="replace") as f:
        for i,raw in enumerate(f,1):
            line=raw.rstrip("\n"); dash+=len(DASH.findall(line))
            if PROT_ENV.search(line): depth+=1
            protected=depth>0 or bool(PROT_LINE.match(line))
            if PROT_END.search(line) and depth>0: depth-=1
            if protected: excluded+=1; continue
            clean=CITE.sub(" ",line)
            toks=WORD.findall(clean); body_words+=len(toks); low=clean.lower()
            for t in toks:
                tl=t.lower()
                if tl in SINGLE_SET: markers[tl]=markers.get(tl,0)+1
            for ph in PHRASES:
                n=low.count(ph)
                if n: markers[ph]=markers.get(ph,0)+n
            for name,pat in STRUCT.items():
                n=len(pat.findall(line))
                if n: struct[name]=struct.get(name,0)+n
    total=sum(markers.values())
    density=round(1000.0*total/body_words,1) if body_words else 0.0
    return {"body_words":body_words,"excluded_lines":excluded,"em_dashes":dash,
            "markers":markers,"struct":struct,"density":density}

def band(d): return "low" if d<3 else ("medium" if d<=6 else "high")

def main():
    ap=argparse.ArgumentParser(description="Read-only AI-tell density audit (Danish).")
    ap.add_argument("--input",required=True); ap.add_argument("--out",default="ai_tell_report_da.md")
    ap.add_argument("--log",default=None); ap.add_argument("--ext",default=".tex,.md,.txt")
    a=ap.parse_args()
    exts=[e if e.startswith(".") else "."+e for e in a.ext.split(",")]
    files=gather(a.input,exts)
    if not files: print("Ingen filer matchede: "+a.input,file=sys.stderr); return 1
    ts=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    out=["# AI-tell density report (Dansk) — "+ts,"",
         "_Stiltæthedsindeks, IKKE en AI-forfatterskabs-dom. Kun brødtekst; "
         "citater/kilder/bokse/cases/figurer ekskluderet. Dansk liste = kalibrér mod baseline._",""]
    for p in files:
        r=audit(p)
        out.append("## "+os.path.basename(p)+"  (`"+sha(p)+"`)")
        out.append("- brødtekst-ord: %d (ekskluderede linjer: %d)"%(r["body_words"],r["excluded_lines"]))
        out.append("- **AI-tell density: %.1f / 1000  (band: %s)**"%(r["density"],band(r["density"])))
        out.append("- em-dash-antal: %d"%r["em_dashes"])
        if r["markers"]:
            top=sorted(r["markers"].items(),key=lambda x:-x[1])[:15]
            out.append("- top-markører: "+", ".join("%s x%d"%(w,n) for w,n in top))
        else: out.append("- top-markører: ingen")
        if r["struct"]:
            out.append("- strukturelle tells: "+", ".join("%s x%d"%(k,v) for k,v in sorted(r["struct"].items(),key=lambda x:-x[1])))
        b=band(r["density"])
        rec=("Tæthed høj. Overvej at udtynde top-markørerne mod ~3/1000 — men behold ord, materialets register legitimt kræver. Send til academic-danish-klarsprog for selve omskrivningen." if b=="high"
             else "Tæthed moderat. Evt. udtynd de mest gentagne markører; register-bevidst, ingen omskrivning her." if b=="medium"
             else "Tæthed lav. Ingen handling nødvendig på stilmarkører.")
        out.append("- anbefaling (vejledende): "+rec); out.append("")
    out.append("_Markører er legitime i moderation; signalet er overforbrug, ikke tilstedeværelse. Denne audit måler og flagger — den omskriver aldrig._")
    open(a.out,"w",encoding="utf-8").write("\n".join(out)+"\n")
    print("Skrev "+a.out+" ("+str(len(files))+" filer)")
    if a.log:
        with open(a.log,"a",encoding="utf-8") as f:
            f.write("\n- ai_tell_density_da.py @ "+ts+": "+str(len(files))+" filer; rapport="+a.out+"\n")
            for p in files:
                r=audit(p); f.write("  - "+os.path.basename(p)+" ("+sha(p)+"): density="+str(r["density"])+"/1000 band="+band(r["density"])+"\n")
        print("Tilføjede til "+a.log)
    return 0

if __name__=="__main__": sys.exit(main())
