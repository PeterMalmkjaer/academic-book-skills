# Checkable items — the rule catalogue

What Phase 1 must decide a single canonical value for, and Phase 3 then enforces in
**body prose only**. For each item: detect dominant usage, report splits with counts,
recommend one canonical form. Never apply a rule inside protected content (see
`protected_content.md`); there, only the *format* of the wrapper is checked.

## 1. Spelling system
- `-ise` vs `-ize` verbs (organise/organize, systematise/systematize)
- `-isation` vs `-ization` nouns (organisation/organization)
- `-our` vs `-or` (behaviour/behavior, favour/favor)
- `-yse` vs `-yze` (analyse/analyze)
- `-re` vs `-er` (centre/center)
- single vs double `l` (modelling/modeling, labelled/labeled)
- **Common real-book trap:** mixing `-ise` verbs with `-ization` nouns. Decide the
  whole system at once (recommend full British `-ise/-isation`, or Oxford `-ize/
  -ization` — but be consistent across verbs AND nouns).

## 2. Numbers, units, ranges
- spelled-out vs numerals threshold (e.g. spell zero–nine, numerals from 10)
- number ranges: en-dash `12–17`, no spaces
- percentages: `35%` vs `35 per cent` vs `35 percent`
- currency format and placement (`€160`, `EUR 160`)
- thousands separator (comma, thin space, none)
- dates: format and order

## 3. Punctuation & dashes
- em-dash style: spaced `a — b` vs unspaced `a—b`; em `—` vs en `–` for parentheticals
- hyphen vs en-dash vs em-dash usage boundaries
- serial (Oxford) comma: on/off
- quotation marks: curly `“ ”` vs straight `" "`; single vs double for primary quotes
- quote/punctuation order: British (logical) vs American (inside)
- ellipsis: `…` vs `...`; spacing
- space before `:` `;` `?` (should be none in EN — flag leftover Danish spacing)

## 4. Cross-references (FORMAT only — never the number)
- `(Section 13.4)` vs `(section 13.4)` vs `(Sec. 13.4)` vs `(§13.4)`
- `(cf. Section x.y)` vs `(see Section x.y)` vs `(Section x.y)` — decide when each
- `Chapter` vs `Ch.`; `Figure` vs `Fig.`; `Table` vs `Tab.`
- range style in refs (`Sections 15.2–15.3`)

## 5. Citations (FORMAT only — never the reference itself)
- Harvard parenthetical shape: `(Smith, 2023)` vs `(Smith 2023)`
- `&` vs `and` between authors in parentheticals vs running text
- `et al.` style (italic? full stop? author count threshold)
- multiple cites: separator (`;`) and ordering (alphabetical vs chronological)
- "Further Reading" entry format: punctuation, italics for journal/book, em-dash gloss

## 6. Terminology & defined terms (→ feeds the termbase)
- canonical surface form per concept (one spelling/casing everywhere)
- acronym handling: define-on-first-use; `AI` vs `A.I.`; spell-out policy
- defined-term emphasis: **bold** on first use, roman thereafter — consistency of the
  *format*, not the wording
- author-name spellings consistent across chapters and "Further Reading"

## 7. Headings & box formatting
- heading capitalisation: title case vs sentence case, per level
- numbered vs unnumbered sections; numbering depth
- box title format: `Definition 17.1: Title` punctuation and casing, consistent
  across all boxes of a type
- **box ENVIRONMENT consistency (LaTeX):** a *numbered* pedagogical box must not use an
  environment otherwise reserved for *unnumbered* structural boxes (e.g. the chapter-opening
  "What this chapter is about" box). Classic bug: "Perspective Box 17.1" set with
  `\begin{perspectivebox}` (the intro environment) instead of the numbered perspective-box
  environment — invisible in the text (the title is correct), only the environment is wrong.
  `scan.py` flags any environment that MIXES numbered and unnumbered boxes. NB: one label may
  legitimately use several environments (discipline colouring, e.g. Theory Box as
  theorybox/psychbox/socbox) — that is NOT an error.
- "Learning objectives", "Summary", "Discussion Questions" header wording consistent

## 8. Mechanical hygiene (high-confidence, body prose)
- double spaces; space before punctuation; stray tabs
- straight vs curly apostrophes in contractions/possessives
- inconsistent capitalisation of recurring nouns
- `e.g.`/`i.e.` punctuation and following comma

> For each item, the Phase-1 output is exactly one canonical value + the split counts
> that justified it. Items the book never varies on need no decision — record them as
> "already consistent" so the log is complete.
