# Excluded from the score — body prose only

The audit scores **running body prose only**. Excluded from both the word/sentence totals
and the feature counts:
- Citations, author names, years, DOIs, reference lists, "Further Reading"
- Direct quotations and epigraphs (they would inflate Human Interest artificially)
- Boxes: definitions, theory/perspective/case/summary boxes and framed elements
- Figure/table captions, labels, table cells
- Cross-references and section/chapter numbers
- Defined-term names, equations, code/verbatim

## Detection heuristics
- LaTeX: box/quote/figure/table/verbatim/equation environments; \cite*, \ref*, \caption,
  \label; $…$, \[ … \].
- Plain text / PDF: lines starting Definition/Theory/Case/Figure/Table/Source/References/
  Further Reading; quotation-mark spans; parenthetical (Author, 19xx/20xx).
- When uncertain, treat as protected and exclude.
