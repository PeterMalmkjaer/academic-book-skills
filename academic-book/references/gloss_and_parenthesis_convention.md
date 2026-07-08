# Term glosses & parenthetical terms — house-style convention

A decision rule for the very common situation where a term is followed by another term in
parentheses — e.g. `agency theory (principal-agent theory)`. Especially frequent in **translated**
academic books: the source-language draft glossed a term with its foreign equivalent, and after
translation the gloss is left stranded (often redundant, sometimes misleading). This reference
tells you how to classify and fix each case.

Distilled from a live DA→EN textbook pass (PM-book, CBS, 2026). Language-general in principle;
examples are English.

---

## The style basis (why these rules)

- **Italicise a term at first use / when referred to *as a term*** — APA (Publication Manual,
  "introduction of a new, technical, or key term"; not italic thereafter), Chicago/Turabian
  ("italicise key terms on first use; thereafter roman"). Quotation marks are for scare-quotes,
  not term introduction.
- **"also known as / also called"** is the explicit-synonym form — use it when the alternative
  name genuinely helps and might otherwise be misread as a citation.
- **Expand an abbreviation at first use**: `key performance indicators (KPIs)`, then `KPI`.
- **A term glossed by itself is nonfunctional** — Farkas (1983), *The Use of Quotation Marks and
  Italics to Introduce Unfamiliar Terms*: the signalling convention "is nonfunctional when the
  explanation … repeats the term."

---

## Decision tree — five categories

For each `term (parenthetical)`:

1. **Redundant self-gloss** — the parenthetical repeats the term, or is near-identical
   (only adds/drops a word). → **DELETE the parenthetical.** If the parenthetical is the more
   precise term, promote it to the headword instead.
   - `Discretionary awards (discretionary awards)` → `Discretionary awards`
   - `discretionary bonuses (discretionary awards)` → `discretionary awards` (standardise on the
     canonical term; also fixes an internal inconsistency)
   - `Subjective evaluation (subjective performance evaluation)` → `Subjective performance evaluation`

2. **Genuine established synonym / alternative name** (a reader benefits; verified real). →
   **KEEP, but mark it as a term:** italicise the alternative, optionally add "also called".
   Gloss **once**, at first use; **drop it on later mentions**.
   - `Agency theory (principal-agent theory)` → `Agency theory (also called *principal-agent theory*)`
   - second mention, already cross-referenced → drop the parenthetical entirely
   - `Input control (behaviour control)` → `Input control (*behaviour control*)` (Ouchi/Merchant)

3. **False synonym / calque** — looks like an alternative name but only made sense next to the
   source-language word; **not** an established term in the target language. → **DELETE the false
   gloss.** If the etymology teaches something, keep it as a plain sentence, not as an "alternative
   name" in headings/definition titles.
   - `The Ratchet Effect (the Pawl Effect)` → `The Ratchet Effect` ("pawl effect" is a calque of
     Danish *pal-effekten*; the established English term is *the ratchet effect / ratchet
     principle*, Weitzman 1980). Keep the mechanical-ratchet image in the body if useful.

4. **Missing gloss (ADD)** — a warranted alternative name or abbreviation expansion is *absent*
   where the reader needs it. → **ADD it** — but only after verifying the term is real (see below).
   Two sub-cases: (a) the audience's expected synonym is missing; (b) an abbreviation is used but
   never expanded.
   - add `performance-related pay (PRP)` next to `performance-based pay` (dominant British/European
     HR term; CIPD/Acas/Eurofound; synonymous per UK-gov evidence review)
   - `KPIs` → `key performance indicators (KPIs)` at first use
   - `motivation crowding theory` named at first substantive use, not only in further-reading

5. **Not a gloss — leave alone.** Explanatory parentheticals (components, examples, clarifications)
   and genuine first-use technical-term introductions in italics are correct and stay.
   - `organisational justice (distributive, procedural, interactional)` — lists sub-dimensions
   - `motivation (*crowding-out*)`, `alternative (*outside option*)` — real term introductions
   - possessives and ordinary asides (`the manager's (…)`) — false positives of any overlap scan

---

## Two rules that prevent errors

**A. Never invent a synonym — verify every proposed alternative name.**
Before adding or keeping an alternative name (categories 2 and 4), confirm it exists and is used
that way in the literature (Elicit / Scite / Exa / CrossRef). Fabricated synonyms are as bad as
fabricated citations.

**B. Precision over label — distinguish related-but-distinct terms.**
A parenthetical is only a true synonym if it denotes the *same* thing. Watch for terms that name a
*related* concept, not the same one:
- *target ratcheting* = the target-setting **practice**; *the ratchet effect* = the **behavioural
  consequence**. Present the relationship, don't equate them.
- a **rational** phenomenon (ratchet effect) is not a **cognitive bias** (anchoring). Do not merge
  them; if you introduce the bias, cite it separately (e.g. Tversky & Kahneman 1974) and frame the
  distinction.

---

## Detection (how to find the cases)

- **Present glosses** (categories 1–3): grep for a word immediately followed by `(...)`; exclude
  citations (year / `\cite`), cross-references (`\ref`, "see", "Section"), and all-caps
  abbreviations. An overlap heuristic (parenthetical shares a content word with the preceding
  term) surfaces the redundant/calque class — but expect false positives (possessive `'s`,
  ordinary explanatory asides), so triage by hand.
- **Missing glosses** (category 4): a **first-use + termbase** pass — for each canonical term, find
  its first occurrence, check whether it is marked/glossed/expanded, and check whether its
  established alternative name appears anywhere. A regex cannot find an *absence*; drive this from
  the termbase.

---

## Workflow (flag, don't silently rewrite)

1. Scan and classify every case into the five categories above.
2. Verify all category-2/4 synonyms in the literature.
3. **Present** before/after + recommendation + justification for each; get explicit sign-off (GATE).
4. Apply transactionally: backup → assertion per edit (old string count == expected; new string
   present) → byte-diff per file → build → log the run. Only the approved items.

This mirrors the companion consistency/verification skills: flag and propose; the human decides;
every applied edit is asserted, diffed, built and logged.
