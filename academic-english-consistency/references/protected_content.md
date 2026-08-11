# Protected content — never altered, format-checked only

The cardinal safety rule of this skill. The wording of everything below is **never
changed and never proposed for change**, including spelling-system swaps. Only the
*format of the wrapper* (label, numbering, title-line punctuation) may be flagged.

If a style rule would touch any token inside protected content, **skip the edit** and
log it as `verify (protected)` with no proposed change.

## What is protected (wording untouchable)

1. **Boxes** — Definitions, Theory Boxes, Perspective Boxes, Case boxes, Summary
   boxes, and any framed pedagogical element. Check only: label format
   (`Definition 17.1: …`), numbering continuity, title-line punctuation.
2. **Quotations & epigraphs** — anything in quotation marks or a quote environment,
   including chapter-opening epigraphs.
3. **Citations & references** — in-text `(Author, Year)`, author names, years, DOIs,
   page numbers, "Further Reading" entries, box source attributions.
4. **Cross-references** — `(Section x.y)`, `Chapter n`, `Figure/Table n`, `§`, and
   the numbers themselves.
5. **Figures & tables** — captions, in-figure text, axis/box labels, table cells.
6. **Defined-term names** — the term itself (e.g. *plausible deniability*,
   *the six R's*). Only its bold-on-first-use *format* is in scope, never its wording.
7. **Numbers, data, and results** — statistics, currency amounts, percentages,
   dates, sample sizes. Format (e.g. en-dash range) may be flagged; the value never.
8. **Proper nouns & named frameworks** — laws (EU AI Act, Annex references),
   theories, model names, organisation names.

## Detection heuristics (.tex)

These help the script and the LLM locate protected regions. They are conservative:
when uncertain, treat as protected.

- **Box environments:** `\begin{...}` … `\end{...}` where the environment name
  matches `(?i)(definition|theorem|theory|perspective|case|summary|box|quote|tcolorbox|mdframed)`.
- **Citation commands:** `\cite`, `\citep`, `\citet`, `\parencite`, `\textcite`,
  `\footcite`, `\autocite`, and their arguments.
- **Cross-reference commands:** `\ref`, `\cref`, `\Cref`, `\autoref`, `\pageref`,
  `\nameref`, and literal `(Section …)`, `§…`.
- **Quotes:** `\begin{quote}`/`\begin{quotation}`/`\epigraph{…}`, `\enquote{…}`, and
  text between matched curly/straight quotation marks.
- **Floats:** `\begin{figure}`…`\end{figure}`, `\begin{table}`…`\end{table}`,
  `\caption{…}`, `\label{…}`, TikZ node text.
- **Defined terms:** first **bold** instance of a known termbase entry.
- **Verbatim/code/math:** `verbatim`, `lstlisting`, `$…$`, `\[ … \]`, `equation`.

## Detection heuristics (plain text / PDF-extracted)

- Lines beginning with a box label pattern: `^(Definition|Theory Box|Perspective Box|
  Case|Summary|Figure|Table)\s*\d`.
- Parenthetical `(... 19xx)` / `(... 20xx)` and `(Section \d`, `§\d`.
- Quotation-mark spans (curly or straight).
- "Further Reading" and "Discussion Questions" blocks (format only).

## The rule, restated

> A proposed change is valid only if its `current` and `proposed` strings differ in
> nothing but a body-prose spelling/format token, AND the change lies outside every
> protected region above. Phase 4 asserts this for every proposal before delivery.
