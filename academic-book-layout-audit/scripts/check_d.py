#!/usr/bin/env python3
"""
Check D — folio-paritet og folio-placering i en sat bog.

To ting kontrolleres:

  1. ARABERTAL-1-PARITET. Den første arabisk nummererede side (folio "1") skal
     ligge på en ULIGE PDF-side, fordi PDF-side 1 = recto. Ligger den på en lige
     side, står hele brødteksten på den forkerte side af hvert opslag, og hele
     bogens ombrydning er spejlvendt i forhold til hensigten. Fejlen opstår, når
     frontmatteret vokser eller skrumper med et ULIGE antal sider.

  2. FOLIO-PLACERING. På sider med marginfolio skal folioen stå ude ved
     forkanten: venstre på verso (lige PDF-side), højre på recto (ulige).
     Sider med `plain` pagestyle (kapitelåbninger) har centreret folio og
     tælles for sig — de er ikke fejl.

Kørsel:
    python3 scripts/check_d.py main.pdf [main_EN.pdf ...]

Exitkode:
    0  alt OK
    1  paritetsfejl ELLER forkert placerede folioer
    2  inkonklusiv — arabertal-1 blev ikke fundet

VIGTIGT: kør mod den PDF, der er bygget på den maskine, der ejer trykfilen.
Samme kilde under en anden TeX Live-version pagineres anderledes, og
frontmatterets længde er netop det, pariteten afhænger af.

---------------------------------------------------------------------------
FEJLEN, DER GAV ANLEDNING TIL AT SKRIVE DEN HER ORDENTLIGT (2026-08-21)

Den oprindelige ad hoc-udgave meldte "arabertal-1 ikke fundet → paritetsfejl"
på en bog med FULDSTÆNDIG KORREKT paritet, hver eneste gang den blev kørt.
Årsagen er værd at kende, fordi den vil ramme enhver ny implementering:

    Arabertal 1 falder ALTID på en kapitelåbningsside, og kapitelåbninger
    bruger `plain` pagestyle med CENTRERET folio.

Koden sprang centrerede folioer over med `continue` — før den registrerede
tallet — så tælleren nåede aldrig frem til den ene side, den skulle måle:

    if abs(x - W/2) < CENTRE_TOL:
        centred += 1; continue          # ← her døde arabertal-1
    ...
    if t.isdigit() and int(t) == 1 and arabic1 is None:
        arabic1 = p + 1                 # ← nås aldrig for en kapitelåbning

Målt i PM-bogen: DA s. 31, sidebredde 439,4 pt, folioens midte 225,4 pt →
5,7 pt fra sidemidten. EN s. 27: 595,3 pt bred, midte 304,7 → 7,1 pt.
Begge langt inden for centrerings-toleransen.

To lærdomme er bygget ind nedenfor:
  * MÅL FØRST, KLASSIFICÉR BAGEFTER. Registrér observationen, før du beslutter,
    om siden hører til den kategori, du er ved at måle.
  * "IKKE MÅLT" ER IKKE "MÅLT OG FEJLET". De to udfald skal have hver sin
    tilstand og hver sin exitkode, ellers råber værktøjet ulv.
---------------------------------------------------------------------------
"""
import sys
import re

try:
    import pymupdf
except ImportError:
    sys.exit(
        "check_d.py kræver PyMuPDF:  pip3 install pymupdf\n"
        "  (eller: pip3 install pymupdf --break-system-packages)\n"
        "  Uden netadgang: pip3 install --no-index /sti/til/pymupdf-*.whl"
    )

ROMAN = re.compile(r"^[ivxlcdm]+$", re.I)
BAND = 65          # bundbåndets højde i pt, hvor folioen søges
CENTRE_TOL = 40    # afstand fra sidemidten i pt, hvorunder folioen regnes centreret


def _candidates(page):
    """Alle folio-lignende spans i sidens bundbånd, som (y, x_midte, tekst)."""
    H = page.rect.height
    out = []
    for block in page.get_text("dict")["blocks"]:
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                y = span["bbox"][3]
                if y <= H - BAND:
                    continue
                t = span["text"].strip()
                if t.isdigit() or ROMAN.match(t):
                    out.append((y, (span["bbox"][0] + span["bbox"][2]) / 2, t))
    return out


def _pick(cands, W):
    """Vælg folioen: den nederste span; ved uafgjort den yderst placerede.

    Den oprindelige kode tog den SIDSTE matchende span i læserækkefølge, hvilket
    er vilkårligt, hvis bundbåndet indeholder andet end folioen (kolumnetitel
    med årstal, sidefodsnote).
    """
    if not cands:
        return None
    ymax = max(c[0] for c in cands)
    lowest = [c for c in cands if abs(c[0] - ymax) < 1.0]
    return max(lowest, key=lambda c: abs(c[1] - W / 2))


def folio_scan(path):
    doc = pymupdf.open(path)
    arabic1 = None
    arabic1_style = None
    ok = 0
    bad = []
    centred = 0
    nofolio = 0

    for p in range(doc.page_count):
        page = doc[p]
        W = page.rect.width
        cand = _pick(_candidates(page), W)
        if cand is None:
            nofolio += 1
            continue
        _, x, t = cand
        is_centred = abs(x - W / 2) < CENTRE_TOL

        # MÅL FØRST: registrér arabertal-1, uanset folioens stil.
        if arabic1 is None and t.isdigit() and int(t) == 1:
            arabic1 = p + 1
            arabic1_style = "plain/centreret" if is_centred else "marginfolio"

        # KLASSIFICÉR BAGEFTER: centrerede folioer har ingen forkant at fejle på.
        if is_centred:
            centred += 1
            continue
        pos = "L" if x < W / 2 else "R"
        phys = "R" if (p + 1) % 2 == 1 else "L"   # PDF-side 1 = recto
        if pos == phys:
            ok += 1
        else:
            bad.append((p + 1, t, pos, phys))

    return dict(pages=doc.page_count, arabic1=arabic1, arabic1_style=arabic1_style,
                ok=ok, bad=bad, centred=centred, nofolio=nofolio)


def main(paths):
    rc = 0
    for path in paths:
        r = folio_scan(path)
        a = r["arabic1"]
        if a is None:
            verdict = "INKONKLUSIV ⚠ — arabertal-1 blev ikke fundet"
            rc = max(rc, 2)
        elif a % 2 == 1:
            verdict = f"ULIGE ✓ ({r['arabic1_style']})"
        else:
            verdict = f"LIGE ✗ — PARITETSFEJL ({r['arabic1_style']})"
            rc = 1
        print(path)
        print(f"  sider={r['pages']}  arabertal-1 på PDF-side {a}  {verdict}")
        print(f"  korrekt placerede folioer: {r['ok']}   FORKERTE: {len(r['bad'])}"
              f"   centrerede(plain): {r['centred']}   uden folio: {r['nofolio']}")
        if r["bad"]:
            rc = 1
            print("  første 10 forkerte (side, folio, fundet, forventet):", r["bad"][:10])
    return rc


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1:]))
