#!/usr/bin/env python3
"""layout_audit.py — deterministisk, LÆS-KUN pre-press-/layoutaudit af en LaTeX-fagbog.

Måler geometri i den SATTE PDF (og i .log, hvis den gives) og flager afvigelser med
sidenummer og sværhedsgrad. Ændrer INTET.

Brug:
    python3 layout_audit.py --pdf main.pdf [--log main.log] [--out LAYOUT_SCAN.md]
                            [--lang da|en] [--tail-cm 2.5] [--compare andet.pdf]

Sektioner: A (overfull), CheckA (brudt boks + tomrum), CheckB (småhaler),
CheckC (float-afstand), E (blanke sider), G (billede-DPI).

Kræver PyMuPDF. Farve→bokstype-kortet udledes af --preamble (main.tex), ellers bruges
generiske labels.
"""
from __future__ import annotations
import argparse, collections, os, re, sys

try:
    import pymupdf
except ImportError:
    sys.exit("layout_audit.py kræver PyMuPDF:  pip install pymupdf")

L = {  # minimal sprogtabel
 'da': dict(fig='Figur', tab='Tabel', see=r'se'),
 'en': dict(fig='Figure', tab='Table', see=r'see'),
}

# ---------------------------------------------------------------- hjælpere
def parse_boxcolors(preamble_path):
    """Udled farve→miljønavn fra \\definecolor + \\newtcolorbox{...}{... colback=NAVN ...}."""
    if not preamble_path or not os.path.exists(preamble_path):
        return {}
    src = open(preamble_path, encoding='utf-8', errors='replace').read()
    cols = {m.group(1): tuple(int(x) for x in m.group(2).split(','))
            for m in re.finditer(r'\\definecolor\{(\w+)\}\{RGB\}\{([\d,\s]+)\}', src)}
    out = {}
    for m in re.finditer(r'\\newtcolorbox\{(\w+)\}(?:\[[^\]]*\])*\s*\{(.*?)\n\}', src, re.S):
        env, body = m.group(1), m.group(2)
        cm = re.search(r'colback=(\w+)', body)
        if cm and cm.group(1) in cols:
            rgb = cols[cm.group(1)]
            out.setdefault(rgb, []).append(env)
    return {k: ' / '.join(v) for k, v in out.items()}


def near(fill, table, tol=3):
    if fill is None: return None
    r, g, b = [int(round(v * 255)) for v in fill[:3]]
    for k in table:
        if abs(k[0]-r) <= tol and abs(k[1]-g) <= tol and abs(k[2]-b) <= tol:
            return k
    return None


def collect_boxes(doc, table, min_width=250):
    rects = collections.defaultdict(list)
    for i, page in enumerate(doc, 1):
        for d in page.get_drawings():
            k = near(d.get('fill'), table)
            if k is None: continue
            r = d['rect']
            if r.width < min_width: continue
            rects[i].append((k, r.y0, r.y1, r.width))
    return rects


# ---------------------------------------------------------------- sektioner
def sec_overfull(logpath, out):
    out.append("## A. Overfull \\hbox")
    if not logpath or not os.path.exists(logpath):
        out.append("\n- (ingen --log givet; sprunget over)\n"); return 0
    log = open(logpath, encoding='utf-8', errors='replace').read()
    ov = [float(m.group(1)) for m in
          re.finditer(r"Overfull \\hbox \((\d+\.?\d*)pt too wide\)", log)]
    k = [x for x in ov if x >= 50]; t = [x for x in ov if 20 <= x < 50]; c = [x for x in ov if x < 20]
    out += ["", "| Klasse | Antal | Betydning |", "|---|---:|---|",
            "| ≥50pt KRITISK | %d | klippes i tryk |" % len(k),
            "| 20–50pt tydelig | %d | synligt i margen |" % len(t),
            "| <20pt kosmetisk | %d | acceptabelt |" % len(c), ""]
    if k: out.append("**Kritiske:** " + ", ".join("%.1fpt" % x for x in sorted(k, reverse=True)[:12]))
    else: out.append("**0 kritiske overskridelser ✓**")
    if t: out.append("\nTydelige: " + ", ".join("%.1fpt" % x for x in sorted(t, reverse=True)))
    out.append("")
    return len(k)


def sec_boxes(doc, rects, names, tail_cm, out):
    H = doc[0].rect.height
    brud = []
    for i in sorted(rects):
        for (k, y0, y1, w) in rects[i]:
            if y1 <= H - 70: continue                    # rører ikke tekstbund
            for (kk, yy0, yy1, ww) in rects.get(i + 1, []):
                if kk != k or yy0 >= 75: continue         # ikke samme boks i top
                under = [b for b in doc[i].get_text("blocks") if b[1] > yy1 + 5 and b[4].strip()]
                brud.append((i, i + 1, names.get(k, str(k)), yy1 - yy0, len(under)))
    tom = [b for b in brud if b[4] == 0]
    out.append("## Check A. Brudt boks, hvor fortsættelsen efterfølges af tomrum [KRITISK]")
    out += ["", "Brudte bokse i alt: **%d**. Heraf med TOMRUM efter halen: **%d**." % (len(brud), len(tom)), ""]
    if tom:
        out += ["| Fra | Til | Bokstype | Halehøjde | Tekst under |", "|---:|---:|---|---:|---:|"]
        for a, b, t, h, u in tom:
            out.append("| %d | %d | %s | %.1f cm | %d |" % (a, b, t, h * 2.54 / 72, u))
    else:
        out.append("**Ingen ✓**")
    out.append("")
    lim = tail_cm * 72 / 2.54
    smaa = [b for b in brud if b[3] < lim and b[4] > 0]
    out.append("## Check B. Småhaler i midt-flow-bokse [KOSMETISK — udskyd til sidste paginering]")
    out += ["", "Haler under %.1f cm efterfulgt af tekst: **%d**" % (tail_cm, len(smaa)), ""]
    if smaa:
        out += ["| Side | Bokstype | Halehøjde |", "|---:|---|---:|"]
        for a, b, t, h, u in sorted(smaa, key=lambda x: x[3]):
            out.append("| %d | %s | %.1f cm |" % (b, t, h * 2.54 / 72))
    out.append("")
    return len(tom)


def sec_floats(doc, lang, out):
    w = L[lang]
    capt, refs = {}, collections.defaultdict(list)
    pat_c = re.compile(r"\b(%s|%s)\s+(\d+\.\d+):" % (w['fig'], w['tab']))
    pat_r = re.compile(r"\b(%s|%s)~?\s*(\d+\.\d+)\b" % (w['fig'], w['tab']))
    for i, page in enumerate(doc, 1):
        t = page.get_text()
        for m in pat_c.finditer(t): capt.setdefault((m.group(1), m.group(2)), i)
        for m in pat_r.finditer(t): refs[(m.group(1), m.group(2))].append(i)
    frem = [(k, rp, capt[k], capt[k] - rp) for k, ps in refs.items() if k in capt
            for rp in ps if capt[k] - rp > 1]
    out.append("## Check C. Float-afstand (kun fremad >1 side flages)")
    out += ["", "Captions: %d · referencer matchet: %d" % (len(capt), sum(len(v) for v in refs.values())),
            "Fremad-henvisninger >1 side: **%d**" % len(frem), ""]
    if frem:
        out += ["| Reference | Ref. side | Caption side | Afstand |", "|---|---:|---:|---:|"]
        for (t, n), rp, cp, d in sorted(frem, key=lambda x: -x[3]):
            out.append("| %s %s | %d | %d | %d sider |" % (t, n, rp, cp, d))
    out.append("")
    return len(frem)


def sec_blank(doc, out):
    blanke = [i for i, p in enumerate(doc, 1)
              if len(p.get_text().strip()) < 40 and not p.get_drawings()]
    out.append("## E. Blanke / næsten-blanke sider")
    out += ["", "Blanke sider: **%d**" % len(blanke), ""]
    if blanke: out.append("Sidenumre: " + ", ".join(map(str, blanke)))
    out.append("")
    return len(blanke)


def sec_dpi(doc, threshold, out):
    lav = []
    for i, page in enumerate(doc, 1):
        for img in page.get_images(full=True):
            xref = img[0]
            try: info = doc.extract_image(xref)
            except Exception: continue
            px = info.get('width', 0)
            for r in page.get_image_rects(xref):
                if r.width <= 0: continue
                dpi = px / (r.width / 72)
                if dpi < threshold: lav.append((i, px, round(dpi)))
    out.append("## G. Rasterbilleder under %d dpi" % threshold)
    out += ["", "Under tærskel: **%d**" % len(lav), ""]
    if lav:
        out += ["| Side | Pixelbredde | Effektiv dpi |", "|---:|---:|---:|"]
        for i, px, d in lav: out.append("| %d | %d | %d |" % (i, px, d))
    out.append("")
    return len(lav)


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description="Læs-kun layout-/pre-press-audit.")
    ap.add_argument('--pdf', required=True)
    ap.add_argument('--log', default=None, help='LaTeX .log til overfull-analyse')
    ap.add_argument('--preamble', default=None, help='main.tex til farve→bokstype-kort')
    ap.add_argument('--out', default='LAYOUT_SCAN.md')
    ap.add_argument('--lang', default='da', choices=['da', 'en'])
    ap.add_argument('--tail-cm', type=float, default=2.5)
    ap.add_argument('--dpi', type=int, default=250)
    ap.add_argument('--compare', default=None,
                    help='tidligere PDF: rapportér om fundene er NYE eller præeksisterende')
    a = ap.parse_args()

    doc = pymupdf.open(a.pdf)
    table = parse_boxcolors(a.preamble)
    out = ["# LAYOUT-SCAN — %s" % os.path.basename(a.pdf), "",
           "Sider: %d · sidestørrelse: %.2f × %.2f pt (%.1f × %.1f mm)" %
           (doc.page_count, doc[0].rect.width, doc[0].rect.height,
            doc[0].rect.width * 25.4 / 72, doc[0].rect.height * 25.4 / 72), ""]
    if not table:
        out.append("> `--preamble` ikke givet eller uden `\\newtcolorbox` — bokstyper vises som RGB.\n")

    rects = collect_boxes(doc, table)
    krit = sec_overfull(a.log, out)
    tom = sec_boxes(doc, rects, table, a.tail_cm, out)
    frem = sec_floats(doc, a.lang, out)
    blank = sec_blank(doc, out)
    dpi = sec_dpi(doc, a.dpi, out)

    if a.compare and os.path.exists(a.compare):
        d2 = pymupdf.open(a.compare)
        r2 = collect_boxes(d2, table)
        o2 = []
        t2 = sec_boxes(d2, r2, table, a.tail_cm, o2)
        f2 = sec_floats(d2, a.lang, o2)
        b2 = sec_blank(d2, o2)
        out += ["## Regressionskontrol mod %s" % os.path.basename(a.compare), "",
                "| Fund | Denne PDF | Tidligere | Nyt? |", "|---|---:|---:|---|",
                "| Brudt boks + tomrum | %d | %d | %s |" % (tom, t2, "JA" if tom > t2 else "nej"),
                "| Fremad-float >1 side | %d | %d | %s |" % (frem, f2, "JA" if frem > f2 else "nej"),
                "| Blanke sider | %d | %d | %s |" % (blank, b2, "JA" if blank > b2 else "nej"), "",
                "Et fund, der findes i BEGGE, er præeksisterende --- ikke indført af den seneste runde.", ""]

    blokerende = krit + tom
    out += ["## Konklusion", "",
            ("**%d BLOKERENDE fund** (kritiske overfull + boks-tomrum) --- ret før tryk."
             % blokerende) if blokerende else
            "**0 blokerende fund.** Kritiske overfull: 0 · boks-tomrum: 0.",
            "", "Kosmetisk/til vurdering: %d fremad-floats, %d blanke sider, %d lav-dpi-billeder."
            % (frem, blank, dpi), ""]

    open(a.out, 'w', encoding='utf-8').write("\n".join(out) + "\n")
    print("Skrev %s — %d blokerende fund" % (a.out, blokerende))
    return 0

if __name__ == '__main__':
    sys.exit(main())
