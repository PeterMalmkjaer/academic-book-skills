# Pre-press / PDF-format checklist (print + archive)

A LaTeX book that compiles cleanly is not yet a print-ready file. Before sending a PDF to a
publisher or print house, check the items below. **Confirm the actual requirements with the
publisher first** — the values here are the common defaults, not universal law, and the spec
determines which apply.

Ordering matters: **trim size and any geometry change reflow the whole book**, so they must be
settled *before* the final typography/overfull pass — never after (see the pipeline-ordering
rule in SKILL.md). Fixing format after typography invalidates the typography pass.

## The checklist

1. **Trim size (page size).** `a4paper` is a manuscript default, not a book trim. Printed
   academic books are usually B5 (176×250 mm) or 170×240 mm. If the publisher wants a specific
   trim, change `\documentclass`/`geometry` and re-run typography. Verify with `pdfinfo` →
   `Page size`.
2. **Image resolution ≥ 300 dpi.** Cover and any full-page/photographic image must be ≥300 dpi
   *at final print size*. A 1024-px image placed full-page on A4 is ~124 dpi — too low. Check:
   `python3 -c "from PIL import Image; print(Image.open('cover.png').size)"` vs the print
   dimensions in inches.
3. **Fonts embedded + subsetted.** Every font must be embedded (and ideally subsetted). XeLaTeX/
   xdvipdfmx does this by default. Verify: `pdffonts file.pdf` → every row `emb=yes sub=yes`.
4. **PDF standard.** Plain PDF (1.5–1.7) is often *not* accepted for offset print. Print houses
   commonly require **PDF/X-1a** or **PDF/X-4** (ISO 15930); archival/deposit copies may require
   **PDF/A** (ISO 19005); accessible e-books may require tagging (**PDF/UA**, ISO 14289). Verify
   intent with the publisher; a plain XeLaTeX PDF is none of these.
5. **Colour space.** Screen PDFs are RGB; offset print usually wants **CMYK** (plus any spot
   colours). Brand colours (e.g. a house red) defined in RGB must be converted. Decide with the
   publisher; conversion is a controlled step, not automatic.
6. **Bleed + crop marks.** Any element that runs to the page edge (full-bleed cover/figures)
   needs ~3 mm bleed and crop marks. Interior text pages usually need neither.
7. **Tagging / accessibility.** `pdfinfo` → `Tagged: no` means the PDF is not tagged; matters for
   e-book/PDF/UA and accessibility mandates, not for basic offset print.
8. **Document metadata.** Title/author set (hyperref `pdftitle`/`pdfauthor`); some workflows also
   want an XMP metadata stream.

## How to inspect (read-only)

```bash
pdfinfo  file.pdf     # pages, Page size (trim), PDF version, Tagged, Encrypted
pdffonts file.pdf     # font embedding/subsetting (want emb=yes sub=yes on every row)
```

## Standards referenced
- **PDF/X** — ISO 15930 (graphic-arts / print exchange).
- **PDF/A** — ISO 19005 (long-term archiving).
- **PDF/UA** — ISO 14289 (universal accessibility / tagging).
- 300 dpi and CMYK/offset conventions are standard commercial-print practice; confirm the exact
  numbers (trim, dpi, colour, bleed) against the specific publisher's submission guidelines.
