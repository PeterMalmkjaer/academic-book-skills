# Excluded from the count — body prose only

The audit measures **running body prose only**. The following are EXCLUDED from both the
word total and the marker count, so the density is not distorted (e.g. "significant"
inside a statistical result, or "crucial" inside a quoted source, is not an AI tell):

- Citations, author names, years, DOIs, reference lists, "Further Reading"
- Direct quotations and epigraphs
- Boxes: definitions, theory/perspective/case/summary boxes and any framed element
- Figure/table captions, in-figure labels, table cells
- Cross-references and section/chapter numbers
- Defined-term names, equations, code/verbatim

## Detection heuristics
- LaTeX: `\begin{...}`…`\end{...}` for box/quote/figure/table/verbatim/equation
  environments; `\cite*`, `\ref*`, `\caption`, `\label`; `$…$`, `\[ … \]`.
- Plain text / PDF: lines starting Definition/Theory/Case/Figure/Table/Source; text in
  quotation marks; parenthetical `(Author, 19xx/20xx)`; "Further Reading"/"References".
- When uncertain, treat as protected and exclude.

The script reports body-prose word count and excluded-region count separately, so the
denominator is transparent.
