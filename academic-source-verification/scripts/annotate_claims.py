#!/usr/bin/env python3
"""
annotate_claims.py — highlight claim-supporting passages in a source PDF (tjek #3).

Part of academic-source-verification's claim-support (T3) workflow: once you have located,
for each in-text claim, the exact supporting phrase in the source article, this marks those
phrases in the PDF -> a *_ANNOTATED.pdf. That file is an auditable record that the source
genuinely says what the manuscript attributes to it.

Requires PyMuPDF:  pip install pymupdf

Two modes:
  1) Manifest:  python annotate_claims.py --manifest jobs.json
       jobs.json = [{"in": "x.pdf", "out": "x_ANNOTATED.pdf", "phrases": ["...","..."]}, ...]
  2) One PDF:   python annotate_claims.py --in x.pdf --out x_ANNOTATED.pdf --phrase "..." --phrase "..."

Phrases should be SHORT, distinctive, single-line fragments — search_for matches the text
layer, so long sentences that wrap across lines may not be found. READ-ONLY on the source
(writes a separate _ANNOTATED copy). Reports any phrase it could NOT locate (verify manually:
a missing phrase may mean the source does not actually contain that claim).
"""
import argparse, json, os, sys
try:
    import fitz
except ImportError:
    sys.exit("PyMuPDF not installed. Run: pip install pymupdf")

def annotate(inp, outp, phrases):
    doc = fitz.open(inp); total = 0; hit = set()
    for page in doc:
        for ph in phrases:
            rects = page.search_for(ph)
            for r in rects:
                page.add_highlight_annot(r).update(); total += 1
            if rects:
                hit.add(ph)
    doc.set_metadata({**doc.metadata, "keywords": "ANNOTATED claim-support (academic-source-verification)"})
    doc.save(outp, garbage=4, deflate=True); doc.close()
    missing = [p for p in phrases if p not in hit]
    print(f"{os.path.basename(outp)}: {total} highlights, {len(hit)}/{len(phrases)} phrases"
          + (f"  ⚠ NOT FOUND (verify!): {missing}" if missing else ""))

ap = argparse.ArgumentParser()
ap.add_argument("--manifest")
ap.add_argument("--in", dest="inp"); ap.add_argument("--out")
ap.add_argument("--phrase", action="append", default=[])
a = ap.parse_args()
if a.manifest:
    for job in json.load(open(a.manifest)):
        annotate(job["in"], job["out"], job["phrases"])
elif a.inp and a.out and a.phrase:
    annotate(a.inp, a.out, a.phrase)
else:
    ap.error("give --manifest, or --in/--out/--phrase")
print("DONE")
