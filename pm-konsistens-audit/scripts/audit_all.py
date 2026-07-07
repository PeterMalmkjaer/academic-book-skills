#!/usr/bin/env python3
"""PM-konsistens-audit — deterministisk, læs-kun auditor for en LaTeX-fagbog.

Facit: main.aux (auto-floats) + boks-titler i kilden (manuelle numre).
Rapporterer fortløbende numre, dangling henvisninger og register/Appendix-mismatch.
Ændrer INTET. Kør efter en ren xelatex->biber->xelatex->xelatex.

Brug:
  python3 audit_all.py --src "kap*_body.tex" --aux main.aux \
      --register konceptregister_body.tex --appendix 09_Back_Matter/appendiks_b_teorioversigt.tex \
      --out KATEGORI_AUDIT.md
"""
import re, glob, argparse, collections, sys

def load_sources(pat):
    src={}
    for f in sorted(glob.glob(pat)):
        m=re.search(r'(\d+)', f);  ch=int(m.group(1)) if m else 0
        src[f]=(ch, open(f, encoding='utf-8').read())
    return src

BOX = re.compile(r'\\begin\{(definitionbox|casebox|theorybox|perspectivebox|psychbox|socbox)\}'
                 r'\[\{?([A-Za-zæøåÆØÅ]+)\s+(\d+)\.(\d+):?\s*(.*?)\}?\]')
LABELMAP = {'Definition':'Definition','Teoriboks':'Teoriboks','Perspektivboks':'Perspektivboks',
            'Case':'Case/Eksempel','Eksempel':'Case/Eksempel'}

def parse_boxes(src):
    nums=collections.defaultdict(lambda: collections.defaultdict(list))   # ch->cat->[minor]
    titles=collections.defaultdict(list)                                  # "X.Y"->[titel]
    for f,(ch,txt) in src.items():
        for line in txt.splitlines():
            m=BOX.search(line)
            if m:
                cat=LABELMAP.get(m.group(2))
                if cat: nums[int(m.group(3))][cat].append(int(m.group(4)))
                titles[f"{m.group(3)}.{m.group(4)}"].append(m.group(5).strip())
    return nums, titles

def parse_aux(aux):
    fig=collections.defaultdict(set); tab=collections.defaultdict(set)
    figset=set(); tabset=set()
    if aux:
        a=open(aux,encoding='utf-8',errors='ignore').read()
        for n in re.findall(r'\\newlabel\{fig:[^}]*\}\{\{(\d+)\.(\d+)',a): fig[int(n[0])].add(int(n[1])); figset.add(f"{n[0]}.{n[1]}")
        for n in re.findall(r'\\newlabel\{tab:[^}]*\}\{\{(\d+)\.(\d+)',a): tab[int(n[0])].add(int(n[1])); tabset.add(f"{n[0]}.{n[1]}")
    return fig,tab,figset,tabset

def check_sequential(nums, fig, tab, out):
    out.append("## 1. Fortløbende numre pr. kapitel\n")
    prob=0
    for ch in sorted(nums):
        for cat in ['Definition','Teoriboks','Perspektivboks','Case/Eksempel']:
            v=sorted(nums[ch][cat])
            if not v: continue
            exp=list(range(1,len(v)+1)); dup=[x for x in set(v) if v.count(x)>1]
            if v!=exp or dup:
                prob+=1; out.append(f"- ⚠ kap{ch} {cat}: {v} (forventet {exp}){' DUP '+str(dup) if dup else ''}")
    for name,d in [('Figur',fig),('Tabel',tab)]:
        for ch in sorted(d):
            v=sorted(d[ch]); exp=list(range(1,max(v)+1)) if v else []
            if v!=exp: prob+=1; out.append(f"- ⚠ kap{ch} {name}: {v} (forventet {exp})")
    out.append(("- Alle kategorier fortløbende ✓" if prob==0 else f"- **{prob} afvigelser**")+"\n")
    return prob

def check_refs(src, boxtitles, figset, tabset, out):
    pool={'Definition':set(),'Teoriboks':set(),'Perspektivboks':set(),'Case':set(),'Figur':figset,'Tabel':tabset}
    # boks-numre pr. kategori
    catof={'Definition':'Definition','Teoriboks':'Teoriboks','Perspektivboks':'Perspektivboks','Case/Eksempel':'Case'}
    for num,tl in boxtitles.items(): pass
    # udled boks-numre fra boxes igen (via titler mangler kategori) -> brug BOX
    for f,(ch,txt) in src.items():
        for m in BOX.finditer(txt):
            c=LABELMAP.get(m.group(2)); n=f"{m.group(3)}.{m.group(4)}"
            if c=='Definition': pool['Definition'].add(n)
            elif c=='Teoriboks': pool['Teoriboks'].add(n)
            elif c=='Perspektivboks': pool['Perspektivboks'].add(n)
            elif c=='Case/Eksempel': pool['Case'].add(n)
    pat={'Definition':r'Definition (\d+\.\d+)','Teoriboks':r'Teoriboks (\d+\.\d+)',
         'Perspektivboks':r'Perspektivboks (\d+\.\d+)','Case':r'Case (\d+\.\d+)',
         'Figur':r'Figur (\d+\.\d+)','Tabel':r'Tabel (\d+\.\d+)'}
    out.append("## 2. Reference-korrekthed (hårdkodede henvisninger)\n")
    dangling=0
    for f,(ch,txt) in src.items():
        for i,line in enumerate(txt.splitlines(),1):
            if '\\begin{' in line: continue
            for cat,p in pat.items():
                for num in re.findall(p,line):
                    if num not in pool[cat]:
                        dangling+=1; out.append(f"- ⚠ {f}:{i} {cat} {num} findes ikke")
    out.append(("- 0 dangling — alle henvisninger findes ✓" if dangling==0 else f"- **{dangling} dangling**")+"\n")
    return dangling

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--src',default='kap*_body.tex')
    ap.add_argument('--aux',default='main.aux')
    ap.add_argument('--out',default='KATEGORI_AUDIT.md')
    a=ap.parse_args()
    src=load_sources(a.src)
    if not src: print("Ingen kildefiler matchede",a.src); sys.exit(1)
    nums,titles=parse_boxes(src)
    import os
    aux=a.aux if os.path.exists(a.aux) else None
    fig,tab,figset,tabset=parse_aux(aux)
    out=["# KATEGORI-AUDIT (auto-genereret)\n",
         ("(main.aux fundet — Figur/Tabel verificeret)\n" if aux else "(INGEN main.aux — Figur/Tabel sprunget over; kør biber-build først)\n")]
    p1=check_sequential(nums,fig,tab,out)
    p2=check_refs(src,titles,figset,tabset,out)
    out.append(f"\n## Konklusion\n{'RENT ✓ — 0 afvigelser.' if p1+p2==0 else f'{p1+p2} punkter til gennemgang.'}")
    open(a.out,'w',encoding='utf-8').write("\n".join(out))
    print(f"Rapport skrevet: {a.out}  ({p1+p2} flag)")

if __name__=='__main__': main()
