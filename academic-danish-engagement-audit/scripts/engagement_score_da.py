#!/usr/bin/env python3
"""
engagement_score_da.py — READ-ONLY reading-engagement audit for DANISH academic prose.

MEASURES, never rewrites. Reports an ADAPTED Human-Interest-style number (Flesch logic;
coefficients are English-calibrated, so treat as RELATIVE) plus Danish proxies
(concreteness, reader-engagement, narrativity). NOT a readability grade (that is LIX).
Raising the score with irrelevant detail HARMS learning (seductive details; Harp & Mayer
1998). Body prose only; citations/quotes/boxes/cases/figures excluded.

Usage:
  python engagement_score_da.py --input <folder-or-glob> [--out report.md] [--log RUN_LOG.md]
                                [--ext .tex,.md,.txt]
"""
from __future__ import annotations
import argparse, glob, hashlib, os, re, sys
from datetime import datetime

WORD = re.compile(r"[A-Za-zÆØÅæøåéüäö][A-Za-zÆØÅæøåéüäö'-]*")
SENT_SPLIT = re.compile(r"(?<=[.!?])\s+")

PRONOUNS={"jeg","mig","min","mit","mine","vi","os","vores","du","dig","din","dit","dine",
 "i","jer","jeres","han","ham","hans","hun","hende","hendes","de","dem","deres","man","sig",
 "selv","vor","vort"}
PERSON_NOUNS={"folk","mennesker","menneske","mand","kvinde","mænd","kvinder","dreng","pige",
 "barn","børn","mor","far","søster","bror","ven","venner","lærer","elev","studerende","læge",
 "patient","leder","medarbejder","læser","kollega","person","chef","forfatter"}
CONCRETE=["for eksempel","f.eks.","fx","såsom","forestil dig","tænk på","eksempel","case",
 "tilfælde","historie","scenarie","antag","betragt","for eksempels skyld"]
ENGAGE_ADDR={"du","dig","din","dit","dine","vi","os","vores","læser","læseren"}
NARR={"så","da","når","efter","før","pludselig","først","dernæst","sidst","senere","imens",
 "efterhånden","siden","derefter"}

PROT_ENV=re.compile(r"\\begin\{[^}]*(definition|teorem|teoretisk|perspektiv|case|sammenfatning|boks|box|quote|quotation|tcolorbox|mdframed|figure|table|verbatim|lstlisting|equation)[^}]*\}", re.I)
PROT_END=re.compile(r"\\end\{[^}]*(definition|teorem|teoretisk|perspektiv|case|sammenfatning|boks|box|quote|quotation|tcolorbox|mdframed|figure|table|verbatim|lstlisting|equation)[^}]*\}", re.I)
PROT_LINE=re.compile(r"^\s*(Definition|Teoretisk|Teoriboks|Perspektiv|Case|Sammenfatning|Figur|Figure|Tabel|Table|Kilde|Videre Læsning|Referencer)\b", re.I)
CITEPAR=re.compile(r"\([^)]*\b(19|20)\d\d[a-z]?\b[^)]*\)")
QUOTED=re.compile(r"[\"“”„»«]")

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
    body=[]; excluded=0; depth=0
    with open(path,encoding="utf-8",errors="replace") as f:
        for raw in f:
            line=raw.rstrip("\n")
            if PROT_ENV.search(line): depth+=1
            protected=depth>0 or bool(PROT_LINE.match(line))
            if PROT_END.search(line) and depth>0: depth-=1
            if protected: excluded+=1; continue
            body.append(CITEPAR.sub(" ",line))
    text=" ".join(body); words=WORD.findall(text); nw=len(words)
    sents=[s for s in SENT_SPLIT.split(text) if s.strip()]; ns=len(sents) or 1
    pw=sum(1 for w in words if w.lower() in PRONOUNS or w.lower() in PERSON_NOUNS)
    ps=0
    for s in sents:
        sl=s.lower()
        if ("?" in s) or ("!" in s) or QUOTED.search(s) or (" du" in " "+sl) or sl.startswith("du"):
            ps+=1
    pw100=100.0*pw/nw if nw else 0.0; ps100=100.0*ps/ns if ns else 0.0
    HI=round(3.635*pw100+0.314*ps100,1)
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

def overall(hi,conc):
    if hi>=30 or conc>=8: return "engagerende"
    if hi>=10 or conc>=4: return "moderat engagerende"
    return "lav engagement (kan være genre-passende for tæt teori)"

def main():
    ap=argparse.ArgumentParser(description="Read-only reading-engagement audit (Danish).")
    ap.add_argument("--input",required=True); ap.add_argument("--out",default="engagement_report_da.md")
    ap.add_argument("--log",default=None); ap.add_argument("--ext",default=".tex,.md,.txt")
    a=ap.parse_args()
    exts=[e if e.startswith(".") else "."+e for e in a.ext.split(",")]
    files=gather(a.input,exts)
    if not files: print("Ingen filer matchede: "+a.input,file=sys.stderr); return 1
    ts=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    out=["# Læse-engagement-rapport (Dansk) — "+ts,"",
         "_Adapteret engagement-indeks (Human-Interest-logikken er valideret på engelsk; tallet "
         "er RELATIVT for dansk). IKKE et læsbarhedstal (det er LIX). Kun brødtekst. Måler kun — "
         "omskriver aldrig; at hæve tallet med irrelevant stof skader læring (seductive details)._",""]
    for p in files:
        r=audit(p)
        out.append("## "+os.path.basename(p)+"  (`"+sha(p)+"`)")
        out.append("- brødtekst: %d ord, %d sætninger (ekskluderede linjer: %d)"%(r["words"],r["sentences"],r["excluded"]))
        out.append("- **Human-Interest-style (adapteret, relativ): %.1f**  (personlige ord %.1f/100, personlige sætninger %.1f/100)"%(r["HI"],r["pw_per100"],r["ps_per100"]))
        out.append("- konkretisering: %.1f/1000 · læser-engagement: %.1f/1000 (spørgsmål: %d) · narrativitet: %.1f/1000"%(r["concreteness_per1k"],r["engagement_per1k"],r["questions"],r["narrativity_per1k"]))
        out.append("- **samlet band (vejledende): %s**"%overall(r["HI"],r["concreteness_per1k"]))
        ob=overall(r["HI"],r["concreteness_per1k"])
        if ob.startswith("lav"):
            rec=("Er dette intro, case eller studentervendt afsnit, så overvej RELEVANT "
                 "konkretisering (gennemregnede eksempler, en gennemgående case, et velplaceret "
                 "spørgsmål) — Sadoskis løftestang. Er det tæt teori, er en lav score oftest "
                 "passende. Tilføj aldrig irrelevant liv (seductive details). Omskrivning: academic-danish-klarsprog.")
        elif ob.startswith("moderat"):
            rec="Rimeligt for fagprosa. Evt. et konkret eksempel eller læser-spørgsmål hvor det gavner argumentet. Ingen omskrivning her."
        else:
            rec="Engagerende. Vogt kun mod dekorativ/irrelevant interesse. Ingen handling nødvendig."
        out.append("- anbefaling (vejledende, register-bevidst): "+rec)
        out.append("- at ændre teksten: denne skill omskriver ikke; ved en eksplicit ordre oplyser den disse konsekvenser og overlader omskrivningen til academic-danish-klarsprog.")
        out.append("")
    out.append("_Konsekvens-note: engagement er en anden akse end læsbarhed og korrekthed; optimér den "
               "kun hvor genren kalder på det, og kun gennem relevant konkretisering og kohæsion — aldrig seductive details._")
    open(a.out,"w",encoding="utf-8").write("\n".join(out)+"\n")
    print("Skrev "+a.out+" ("+str(len(files))+" filer)")
    if a.log:
        with open(a.log,"a",encoding="utf-8") as f:
            f.write("\n- engagement_score_da.py @ "+ts+": "+str(len(files))+" filer; rapport="+a.out+"\n")
            for p in files:
                r=audit(p); f.write("  - "+os.path.basename(p)+" ("+sha(p)+"): HI="+str(r["HI"])+" konk="+str(r["concreteness_per1k"])+"/1k band="+overall(r["HI"],r["concreteness_per1k"])+"\n")
        print("Tilføjede til "+a.log)
    return 0

if __name__=="__main__": sys.exit(main())
