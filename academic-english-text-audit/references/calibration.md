# Calibration: genre profile + level baseline

Two independent parameters are fixed BEFORE scoring. Scores are only comparable under
identical calibration (same profile AND same baseline). For book-wide use: lock the
baseline across chapters.

## Parameter 1: Genre profile

The profile sets dimension weights v, active dimensions and tolerance adjustments.
Criterion weights w within a dimension are equal unless the profile says otherwise.
Evidence for task-specific rubrics: Jonsson & Svingby (2007).

| Dimension | Textbook chapter | Methods chapter | Afterword/preface | Monograph chapter | Journal article |
|---|---|---|---|---|---|
| S Semantic | 0.25 | 0.35 | 0.20 | 0.25 | 0.30 |
| H Hermeneutic | 0.20 | 0.10 | 0.35 | 0.30 | 0.25 |
| T Technical | 0.20 | 0.25 | 0.20 | 0.20 | 0.25 |
| M Metaphor | 0.15 | 0.10 | 0.25 | 0.10 | 0.05 |
| F Tables/figures | 0.20 | 0.20 | — | 0.15 | 0.15 |

**The F rule (both directions):**
- If the text has no tables/figures, F drops out and its weight is distributed
  proportionally over the remaining dimensions (renormalise so Σv = 1).
- If the text HAS tables/figures but the profile excludes F (e.g. afterword/preface),
  ACTIVATE F with weight 0.10 and renormalise the other weights proportionally.
  An afterword with a table must have the table assessed — genre does not exempt apparatus.

Always report the weights actually used, and note any F activation/deactivation in the
method box.

**Tolerance adjustments per profile:**
- *Afterword/preface:* A personal voice and "we"-address are genre-correct — do not
  penalise them under S4/T3. Metaphor density may be high; the M criteria assess quality,
  not count. The H1 expectation is sharpened: an afterword that merely summarises is a
  0–1 on H1.
- *Methods chapter:* S1/S2 are sharpened — one undefined key term is already a 2 on S1.
  Few metaphors are expected; a single imprecise mapping weighs more (M2).
- *Textbook chapter:* Pedagogical repetition is not a T4 violation when functional
  (summary boxes and the like are apparatus, not body prose).
- *Journal article:* IMRaD conventions override generic T1 expectations; score T1
  against the genre's template.
- *Journal article (empirical) — methods block (v1.4):* Five checkpoints, scored as part
  of dimension S (S1/S4 evidence) and always reported as standalone flags:
  (1) **Search documentation:** if the text carries a literature-coverage claim ("nothing
  exists"), search strings, dates and inclusion criteria must be stated (supplement allowed).
  (2) **Operationalisation:** estimates and weights (e.g. effort shares) must state their
  indicators and combination rule — or be reported as intervals rather than point estimates.
  (3) **Design explication:** the case's units (overall case + embedded units of analysis)
  must be named if the design is in fact embedded.
  (4) **Self-validation delimitation:** where validation was performed by the same system/
  model family, the text itself must delimit what would require an external (human) eye.
  (5) **Residual-error coverage:** wordings of the type "all known errors" must be
  accompanied by a coverage device (spot-check, blind re-audit, or an estimated residual
  error rate) or an explicit statement of what the wording cannot claim.
  **S4 sharpenings for the genre:** beyond claim strength against evidence strength, check
  (a) generalisation scope — claims sliding from the case to the general without a marked
  delimitation — and (b) institutional precision — claims about products/results must
  reflect their actual institutional status (e.g. manuscript versus published,
  peer-reviewed work).
- *Monograph chapter:* The chapter must both stand alone and carry the work's through-line —
  T3 also assesses cross-references to other chapters.

## Parameter 2: Level baseline

The baseline defines what step 2 ("the normal expectation") means. Criterion-referenced
measurement requires an explicit standard (Glaser 1963); standards are best communicated
through exemplars (Sadler 1989). Ask the user; never guess.

**(a) Draft for internal review.** Step 2 = an honest working draft: the argument stands,
but definitions may be missing and transitions rough. Exemplar anchor for "2 on S1":
key concepts are named and partly delineated, but 1–2 definitions are outstanding.
Use for formative feedback early in the writing process.

**(b) Publication-ready textbook.** Step 2 = the level of an average published
social-science textbook in the relevant market. Exemplar anchor for "2 on S1": all key
concepts are defined, but some only well into the chapter, and delimitations ("what falls
outside") are missing in places. Default baseline for book manuscripts late in the process.

**(c) International journal standard.** Step 2 = what survives review at a solid
international journal in the field. Exemplar anchor for "2 on S1": definitions in place at
first use; what is missing for a 3–4 is explicit scope conditions and relations to
neighbouring constructs (the Suddaby standard). The hardest baseline — the same text
typically scores 10–20 pp lower than against (b), and that is correct, not an error.

**Communication rule:** The report must remind the reader that a score holds only against
the chosen standard: "82 % against baseline (b)" and "68 % against baseline (c)" can
describe the same text, and neither number is "the true one" in any absolute sense.

## Interpretation scale: what the numbers mean

These percentages do NOT follow the school scale. The school intuition "80 % = adequate,
90–100 % = the goal" comes from the mastery learning tradition, where 80–90 % correct on a
formative test is the mastery threshold (Bloom via Guskey 2007; Kulik et al. 1990) — there,
100 % means "knowing everything". On this scale 100 % means something else: ALL criteria at
exemplar level (4/4), and step 2 — the middle — is by definition the chosen baseline's
standard. The zero point sits elsewhere, and cut scores are in any case declared
conventions, not natural boundaries (the standard-setting tradition: Cizek 2013).

| Score (dimension/total) | Mean criterion level | Meaning against the chosen baseline |
|---|---|---|
| 100 % | 4.0 | Theoretical maximum: every criterion could serve as an exemplar. Not a working target. |
| 90–99 % | ≥ 3.6 | Exemplar zone: the text can serve as a model for other chapters. Rare by design — frequent 90+ scores signal score inflation (check the halo alarm). |
| 75–89 % | 3.0–3.5 | Strong text, well above the baseline standard. Realistic target zone for a flagship chapter or afterword. |
| 50–74 % | 2.0–2.9 | At or above the baseline standard — i.e. "sufficient" against the chosen standard. Publishable ONCE the binding constraints are empty. |
| 25–49 % | 1.0–1.9 | Below the standard: substantial rework on the flagged points. |
| 0–24 % | < 1.0 | Structural problems across dimensions. |

**The gate rule (the number alone never triggers "ready for print"):** Whatever the score,
the text is ready only when (1) the production findings are cleared, (2) no load-bearing
claim remains miscalibrated in the claim table, and (3) the list of binding constraints is
empty. A leftover production note cannot be outweighed by 90 %.

**The only road to higher numbers runs through the anchors.** Every criterion assessment
must explain "why x and not x+1" — that is the recipe. The binding constraints are thus
the roadmap: resolve the top flag, and the report tells you what comes next. Chasing 90+
on every dimension is miscalibrated ambition; the goal is an empty list of binding
constraints at the baseline the publication requires.
