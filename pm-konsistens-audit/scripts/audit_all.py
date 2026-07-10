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

def _deacc(x):
    import unicodedata
    return unicodedata.normalize('NFKD', x).encode('ascii','ignore').decode()

def _norm_sur(x):
    return re.sub(r'[^a-zA-Z]','', _deacc(x)).lower()

# Kendte ikke-efternavne (virksomheder/magasiner/ord) der giver A-støj
_NOISE = {'og','al','et','se','jf','kap','boks','case','figur','tabel','del','the','of',
          'ceo','general','electric','today','accounting','forordning','microsoft',
          'netflix','gallup','workhuman','textio','ge'}

def parse_bib(bib_path):
    raw=open(bib_path, encoding='utf-8').read()
    entries=re.findall(r'@(\w+)\s*\{\s*([^,]+),(.*?)\n\}', raw, re.S)
    keys={}
    for etype,key,body in entries:
        key=key.strip()
        m=re.search(r'\b(author|editor)\s*=\s*[{"](.+?)[}"]\s*,?\s*\n', body, re.S|re.I)
        authors=m.group(2) if m else ''
        surs=[]
        for a in re.split(r'\s+and\s+', authors):
            a=a.strip()
            if not a: continue
            sur=a.split(',')[0] if ',' in a else (a.split()[-1] if a.split() else a)
            surs.append(_norm_sur(sur))
        ym=re.search(r'\byear\s*=\s*[{"]?(\d{4})', body, re.I)
        tm=re.search(r'\btitle\s*=\s*[{"](.+?)[}"]\s*,?\s*\n', body, re.S|re.I)
        dm=re.search(r'\bdoi\s*=\s*[{"](.+?)[}"]', body, re.I)
        keys[key]=dict(type=etype, surs=surs, year=(ym.group(1) if ym else None),
                       title=(tm.group(1).strip() if tm else ''),
                       doi=(dm.group(1).strip().lower() if dm else ''))
    return keys

def _prose_citations(text):
    text=re.sub(r'(?<!\\)%.*','',text)          # fjern kommentarer
    text=_deacc(text)                             # ö->o, é->e (undgå trunkering)
    text=re.sub(r"'s\b","",text)                 # fjern genitiv-'s (Milgrom's->Milgrom)
    pairs=set()
    NAME=r"[A-Z][A-Za-z'\-]+"
    for m in re.finditer(r'('+NAME+r'(?:\s+(?:og|and|&|et\s+al\.?|,)\s*[A-Z]?[A-Za-z'+r"'"+r'\-]*)*)\s*\((\d{4})[a-z]?\)', text):
        yr=m.group(2)
        for n in re.findall(NAME, m.group(1)):
            ns=_norm_sur(n)
            if ns and ns not in _NOISE and len(ns)>1: pairs.add((ns,yr))
    for m in re.finditer(r'\(([^()]*?\b\d{4}[a-z]?)\)', text):
        inner=m.group(1); yrs=re.findall(r'(\d{4})',inner)
        for n in re.findall(NAME, inner):
            ns=_norm_sur(n)
            if ns in _NOISE or not ns or len(ns)<3: continue
            for yr in yrs: pairs.add((ns,yr))
    return pairs

def check_bib_integrity(src, bib_path, out):
    """Sektion 3: prosa<->bib reference-integritet. HARDE flag = C (dublet) + D (nøgle/år).
    A (prosa uden nøgle) + B (orphan) listes som review-kandidater (tæller IKKE som flag: A er
    iboende støjende — co-forfattere/virksomheder/genitiver/diakritik)."""
    import collections
    out.append("## 3. Reference-integritet (prosa ↔ references.bib)\n")
    keys=parse_bib(bib_path)
    sy=collections.defaultdict(set); su=collections.defaultdict(set)
    for k,d in keys.items():
        for s in d['surs']:
            su[s].add(k)
            if d['year']: sy[(s,d['year'])].add(k)
    text="".join(t for _,(_,t) in src.items())
    prose=_prose_citations(text)
    dt=_deacc(text).lower()

    # C) dubletter (samme DOI, eller samme titel + samme år)
    bydoi=collections.defaultdict(list); bytitle=collections.defaultdict(list)
    for k,d in keys.items():
        if d['doi']: bydoi[d['doi']].append(k)
        t=re.sub(r'[^a-z0-9]','',_deacc(d['title']).lower())
        if t: bytitle[t].append(k)
    C=[]
    for doi,ks in bydoi.items():
        if len(ks)>1: C.append(f"  - DOI {doi} -> {', '.join(ks)}")
    for t,ks in bytitle.items():
        if len(ks)>1 and not any(set(ks)<=set(v) for v in bydoi.values() if len(v)>1):
            yrs={keys[k]['year'] for k in ks if keys[k]['year']}
            if len(yrs)>1: continue   # forskellige udgaver = ikke dublet
            C.append(f"  - titel-match -> {', '.join(ks)} (samme værk?)")
    # D) nøglenavn-år vs year-felt
    D=[]
    for k,d in keys.items():
        km=re.search(r'(\d{4})$',k)
        if km and d['year'] and km.group(1)!=d['year']:
            D.append(f"  - {k}: nøgle={km.group(1)} year={d['year']} ({d['title'][:40]})")
    # A) prosa uden nøgle (opdelt: høj signal vs støj)
    A_missing=[]; A_yrmis=[]
    for (s,y) in sorted(prose):
        if (s,y) in sy or (s.rstrip('s'),y) in sy: continue
        if s in su or s.rstrip('s') in su:
            yrs=sorted({keys[k]['year'] for k in su[s] if keys[k]['year']})
            A_yrmis.append(f"  - {s.capitalize()} ({y}) — efternavn findes, år: {','.join(yrs)}")
        else:
            A_missing.append(f"  - {s.capitalize()} ({y}) — efternavn IKKE i bib")
    # B) orphan-nøgler
    B=[]
    for k,d in keys.items():
        surs=d['surs'] or [_norm_sur(k)]; y=d['year']; hit=False
        for s in surs:
            if len(s)<3: continue
            for m in re.finditer(re.escape(s),dt):
                if y and y in dt[m.start():m.start()+70]: hit=True; break
            if hit: break
        if not hit: B.append(f"  - {k} (1.forf {surs[0] if surs else '-'}, {y or '-'})")

    hard=len(C)+len(D)
    out.append(f"### C) Dubletter [HARDT FLAG]: {len(C)}")
    out.append("\n".join(C) if C else "  - (ingen)")
    out.append(f"### D) Nøglenavn≠year-felt [HARDT FLAG]: {len(D)}")
    out.append("\n".join(D) if D else "  - (ingen)")
    out.append(f"### A) Prosa-citation uden nøgle [REVIEW, tæller ikke]:")
    out.append(f"  Høj signal — efternavn slet ikke i bib ({len(A_missing)}):")
    out.append("\n".join(A_missing) if A_missing else "  - (ingen)")
    out.append(f"  Lav signal — år-mismatch/co-forf.-støj ({len(A_yrmis)}): se fuld liste ved behov")
    out.append(f"### B) Orphan-nøgler [LAV PRIO, tæller ikke]: {len(B)}")
    out.append(("  (%d — uciterede; \\nocite{*} trykker dem alligevel)"%len(B)) if B else "  - (ingen)")
    out.append(f"\n- Reference-integritet: **{hard} hardt flag** (C+D); {len(A_missing)} A-højsignal + {len(B)} orphans til review.\n")
    return hard


def check_chapter_skeleton(src, out):
    """Sektion 4: kapitel-skabelon-konsistens. Udleder den MODALE aabningsstruktur fra
    flertallet af kapitler og flager afvigere. Fanger fx 'laeringsmaal foer handler-om-boks'
    og manglende paakraevede landemaerker. HARDE flag = raekkefoelge-afvigelser + manglende
    paakraevede landemaerker (H/L). Frase-afvigelser (laeringsmaal-indledning) = review.
    Laes kun .tex (ingen build noedvendig)."""
    import collections
    out.append("## 4. Kapitel-skabelon-konsistens (aabningsstruktur)\n")
    ch_data={}
    for fpath,(ch,txt) in src.items():
        msec=re.search(r'\\section\*?\{', txt)
        opening = txt[:msec.start()] if msec else txt
        def pos(pat, hay=opening):
            m=re.search(pat, hay); return m.start() if m else None
        intro=None
        ml=re.search(r'\\begin\{learninggoals\}\s*\n\s*(.+)', txt)
        if ml: intro=ml.group(1).strip()
        ch_data[ch]=dict(f=fpath,
                         H=pos(r'Hvad dette kapitel handler om'),
                         L=pos(r'\\begin\{learninggoals\}'),
                         R=pos(r'\\chaprule'),
                         intro=intro, has_sec=bool(msec))
    # relativ raekkefoelge H vs L
    order={ch:('H<L' if d['H']<d['L'] else 'L<H')
           for ch,d in ch_data.items() if d['H'] is not None and d['L'] is not None}
    modal_order = collections.Counter(order.values()).most_common(1)[0][0] if order else None
    bad_order = sorted(ch for ch,o in order.items() if o!=modal_order)
    # tilstedevaerelse: H/L paakraevet hvis >=50% af kapitler har dem
    n=len(ch_data) or 1
    req_H = sum(1 for d in ch_data.values() if d['H'] is not None) >= n/2
    req_L = sum(1 for d in ch_data.values() if d['L'] is not None) >= n/2
    miss=[]
    for ch,d in sorted(ch_data.items()):
        if req_H and d['H'] is None: miss.append(f"  - kap{ch}: mangler 'Hvad dette kapitel handler om'-boks ({d['f']})")
        if req_L and d['L'] is None: miss.append(f"  - kap{ch}: mangler laeringsmaal-boks ({d['f']})")
    # frase-konsistens (laeringsmaal-indledning)
    intros=collections.Counter(d['intro'] for d in ch_data.values() if d['intro'])
    modal_intro = intros.most_common(1)[0][0] if intros else None
    phrase=[f"  - kap{ch}: {d['intro']!r}" for ch,d in sorted(ch_data.items())
            if d['intro'] and d['intro']!=modal_intro]

    hard=len(bad_order)+len(miss)
    out.append(f"### Modal aabningsraekkefoelge: {modal_order or '?'}  (H='Hvad dette kapitel handler om', L=laeringsmaal)")
    out.append(f"### Afvigende raekkefoelge [HARDT FLAG]: {len(bad_order)}")
    if bad_order:
        for ch in bad_order:
            out.append(f"  - kap{ch}: {order[ch]} (afviger fra modal {modal_order}) — {ch_data[ch]['f']}")
    else: out.append("  - (ingen)")
    out.append(f"### Manglende paakraevede landemaerker [HARDT FLAG]: {len(miss)}")
    out.append("\n".join(miss) if miss else "  - (ingen)")
    out.append("### Laeringsmaal-indledning — afvigende frase [REVIEW]:")
    out.append(f"  modal: {modal_intro!r}")
    out.append("\n".join(phrase) if phrase else "  - (ingen afvigelser)")
    out.append(f"\n- Kapitel-skabelon: **{hard} hardt flag** (raekkefoelge+manglende); {len(phrase)} frase-afvigelser til review.\n")
    return hard


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--src',default='kap*_body.tex')
    ap.add_argument('--aux',default='main.aux')
    ap.add_argument('--out',default='KATEGORI_AUDIT.md')
    ap.add_argument('--bib',default='references.bib',help='references.bib til reference-integritet (sektion 3)')
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
    p3=check_bib_integrity(src,a.bib,out) if os.path.exists(a.bib) else 0
    if not os.path.exists(a.bib): out.append("## 3. Reference-integritet\n- (--bib ikke fundet; sprunget over)\n")
    p4=check_chapter_skeleton(src,out)
    total=p1+p2+p3+p4
    out.append(f"\n## Konklusion\n{'RENT ✓ — 0 afvigelser.' if total==0 else f'{total} punkter til gennemgang (numre/henvisninger: '+str(p1+p2)+', reference-integritet: '+str(p3)+', kapitel-skabelon: '+str(p4)+').'}")
    open(a.out,'w',encoding='utf-8').write("\n".join(out))
    print(f"Rapport skrevet: {a.out}  ({total} flag)")

if __name__=='__main__': main()
