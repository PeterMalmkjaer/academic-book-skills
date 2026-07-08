# Pre-press / PDF-format-tjekliste (tryk + arkiv)

En LaTeX-bog der kompilerer rent, er ikke dermed tryk-klar. Før en PDF sendes til forlag eller
trykkeri, tjek punkterne nedenfor. **Bekræft de faktiske krav med forlaget først** — værdierne her
er de almindelige standarder, ikke universel lov, og specen afgør hvad der gælder.

Rækkefølge betyder noget: **trim-størrelse og enhver geometri-ændring reflower hele bogen**, så de
skal afklares *før* den endelige typografi/overfull-runde — aldrig efter (se rækkefølge-reglen i
SKILL.md). At rette format efter typografien ugyldiggør typografi-passet.

## Tjeklisten

1. **Trim-størrelse (sidestørrelse).** `a4paper` er en manuskript-standard, ikke et bog-trim.
   Faglige bøger trykkes typisk i B5 (176×250 mm) eller 170×240 mm. Vil forlaget have et bestemt
   trim, så ret `\documentclass`/`geometry` og kør typografien igen. Tjek med `pdfinfo` →
   `Page size`.
2. **Billedopløsning ≥ 300 dpi.** Cover og alle helsides-/fotografiske billeder skal være ≥300 dpi
   *ved endelig trykstørrelse*. Et 1024-px billede placeret helsides på A4 er ~124 dpi — for lavt.
   Tjek: `python3 -c "from PIL import Image; print(Image.open('cover.png').size)"` mod trykmålene
   i tommer.
3. **Fonte indlejret + subsat.** Hver font skal være indlejret (og helst subsat). XeLaTeX/
   xdvipdfmx gør det som standard. Tjek: `pdffonts fil.pdf` → hver række `emb=yes sub=yes`.
4. **PDF-standard.** Almindelig PDF (1.5–1.7) accepteres ofte *ikke* til offset-tryk. Trykkerier
   kræver typisk **PDF/X-1a** eller **PDF/X-4** (ISO 15930); arkiv-/pligtafleverings-kopier kan
   kræve **PDF/A** (ISO 19005); tilgængelige e-bøger kan kræve tagging (**PDF/UA**, ISO 14289).
   Bekræft med forlaget; en almindelig XeLaTeX-PDF er ingen af delene.
5. **Farverum.** Skærm-PDF'er er RGB; offset-tryk vil oftest have **CMYK** (plus evt. spot-farver).
   Brand-farver (fx en husrød) defineret i RGB skal konverteres. Beslut med forlaget; konvertering
   er et kontrolleret trin, ikke automatisk.
6. **Bleed + skæremærker.** Ethvert element der går ud til kanten (helsides-cover/figurer) kræver
   ~3 mm bleed og skæremærker. Indvendige tekstsider kræver normalt ingen af delene.
7. **Tagging / tilgængelighed.** `pdfinfo` → `Tagged: no` betyder at PDF'en ikke er tagget; det
   betyder noget for e-bog/PDF/UA og tilgængelighedskrav, ikke for basalt offset-tryk.
8. **Dokument-metadata.** Titel/forfatter sat (hyperref `pdftitle`/`pdfauthor`); nogle workflows
   vil også have en XMP-metadata-stream.

## Sådan inspiceres (read-only)

```bash
pdfinfo  fil.pdf     # sider, Page size (trim), PDF-version, Tagged, Encrypted
pdffonts fil.pdf     # font-indlejring/subsetting (vil have emb=yes sub=yes på hver række)
```

## Refererede standarder
- **PDF/X** — ISO 15930 (grafisk/trykudveksling).
- **PDF/A** — ISO 19005 (langtidsarkivering).
- **PDF/UA** — ISO 14289 (universel tilgængelighed / tagging).
- 300 dpi og CMYK/offset-konventioner er standard kommerciel trykpraksis; bekræft de præcise tal
  (trim, dpi, farve, bleed) mod det konkrete forlags indleveringsvejledning.
