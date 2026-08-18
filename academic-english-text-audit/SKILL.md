---
name: academic-english-text-audit
description: >-
  Evidence-based quality audit of ENGLISH academic prose (chapters, afterwords/prefaces,
  monographs, article drafts) on five dimensions — semantic content, hermeneutic content,
  technical composition, metaphor use, and tables/figures — using an anchored 0–4 rubric,
  two-parameter calibration (genre profile + level baseline), weighted aggregation,
  confidence bands, and verbatim textual evidence per score. It MEASURES and FLAGS — it
  never rewrites (rewriting is handed off to academic-english-narrative). OPT-IN ONLY:
  run only on explicit request. Cues (only on direct request): "text audit",
  "quality audit", "five-dimension analysis", "score this chapter/text",
  "audit the afterword", "semantic/hermeneutic analysis with scores". Scores BODY PROSE
  plus the text's own tables/figures; quotations, boxes and the reference list are not
  scored as prose. Sister skill of akademisk-tekstaudit (Danish).
---

# Academic text audit (English)

## What this skill is — and is not

The skill produces a **structured second opinion** on the quality of an academic text:
an analytic rubric assessment with 19 criteria in 5 dimensions, where every score is tied
to verbatim textual evidence. It is NOT a psychometrically validated measurement
instrument, and the report's method box must say so. It NEVER rewrites text — it flags
and prioritises, and rewriting is handed off to the narrative/consistency skills.
The reason for this division of labour: a judge who may also rewrite loses independence
and starts scoring its own preferences instead of the text.

The evidence base (full reference list in `references/references.md`), briefly: anchored,
task-specific rubrics score more reliably than free holistic judgments (Jonsson & Svingby
2007); "analyse before you score" improves LLM judges' agreement with humans (Liu et al.
2023, G-Eval); and LLM judges show documented score inflation, halo tendencies and
instability, which the workflow below is designed to counteract (Zheng et al. 2023;
Lai et al. 2014).

## Workflow

### Step 0 — Calibration (mandatory, BEFORE reading the text)

Ask two questions, and do not accept skipping them — without them the score is tied to an
implicit, unstable norm and cannot be compared with any other run:

1. **Genre profile** (which criteria and weights apply): textbook chapter, methods chapter,
   afterword/preface, monograph chapter, or journal article.
2. **Level baseline** (what step 2, "the normal expectation", means): draft for internal
   review, publication-ready textbook, or international journal standard.

A third, OPTIONAL parameter: **Dimension D (discourse and power reflexivity)** — ask only
if the user has raised discourse/power themselves; otherwise do NOT run it. Default: OFF.
If activated, flag mode (unscored) is the default — see `references/rubric-D-discourse.md`.

Details, weight sets and exemplar anchors: read `references/calibration.md` now.
If the user stated both parameters in the request, confirm them briefly instead of asking.
When auditing several chapters of the same work, the baseline must be identical across
chapters — otherwise chapter scores are not comparable.

### Step 1 — Delimit the scoring material

Body prose plus the text's own tables/figures is the material. Direct quotations, boxes
with third-party wording, the reference list and apparatus are not scored as prose (but a
faulty reference TO a box/figure is a T or F finding). Note the scope (words/sections)
for the method box.

### Step 1b — Argument reconstruction (before any scoring)

Reconstruct the text's argument BEFORE opening the rubric — a judge who has not understood
the argument scores surface instead of substance:

1. **Central thesis:** state the text's core claim in one sentence.
2. **Claim structure:** list the 3–8 load-bearing sub-claims and their dependencies.
3. **Levels of meaning:** note which levels the text works on (e.g. empirical, theoretical,
   normative, ontological), and whether the text itself marks the transitions.

The reconstruction goes into the report and feeds S3 (concept relations), S4 (the claim
table), H1–H2 and T1. Disagreement between your reconstruction and the text's own
self-description (e.g. "four criticisms" announced, six claims delivered) is a finding
in its own right.

### Step 2 — Analyse and score per criterion

Read `references/rubrics.md` (all 19 criteria with 0/2/4 anchors). For EACH active
criterion, in this order — the analysis must precede the score, because the reverse order
demonstrably produces worse-calibrated numbers:

1. **Evidence:** quote 1–3 verbatim passages with location (section/page).
2. **Analysis:** what does the evidence show against the criterion's anchors?
3. **Score:** 0–4 (integer; 1 and 3 are intermediate steps).
4. **Confidence:** high/medium/low. Without at least one verbatim quote: mark the score
   "estimate" and set confidence to low automatically. H1 and H2 require at least two
   quotes and can never exceed medium confidence (interpretive depth is disciplined
   judgment, not measurement).

Two criteria score at sub-level, because the aggregate otherwise hides the profile:

- **S4 scores per central claim** (the claim table from step 1b): for each load-bearing
  claim, assess formulation strength (hedged/calibrated/absolute) against evidential
  strength (weak/moderate/strong). "Absolute formulation + moderate evidence" is a flag;
  the S4 score follows from how many claims are miscalibrated.
- **The M criteria score per bearing metaphor** (the metaphor inventory): each bearing
  metaphor gets function, mapping check, consistency and framing risk assessed separately;
  the M criterion scores aggregate from the inventory (the weakest BEARING metaphor weighs
  most — one defective master metaphor does more damage than three weak minor ones).

Scale discipline, because LLM judges demonstrably cluster at the top: 2 is the normal
expectation for a solid draft against the chosen baseline; 3 is a strong text; 4 is
reserved for passages that could serve as exemplars. Never give a whole dimension the
same score out of convenience — the criteria are designed to be able to diverge.

### Step 2b — Internal fact consistency (deterministic sweep)

BEFORE computing, run a mechanical consistency sweep across the whole material. Findings are
reported under production findings and/or as evidence for conceptual consistency (S2); the
sweep carries no score of its own:

1. **Number against number:** the same artefact or quantity described with different numbers
   (e.g. "245 entries" in one place, "277 terms" in another). List every number pair about
   the same referent and reconcile them.
2. **Word against fact:** qualitative time and quantity words ("multi-year", "decades",
   "most", "all") held against the text's own documented dates, durations and counts — a
   "multi-year collaboration" in a case the text itself dates to eight months is a finding
   no rubric line will catch.
3. **Promise against delivery in numbers:** counts in headings and roadmaps ("five
   episodes", "nine phases") against what the text actually delivers.

The rationale is in the design history (v1.2): rubric anchoring directs attention and is
therefore systematically blind to finding classes outside the rubric. The sweep is the
rubric's deterministic safety net — it requires no judgment, only systematicity, and must
never be skipped to save time.

### Step 2c — Terminological anchoring (missing established terms)

Alongside Step 2b, run an anchoring check on the text's conceptual apparatus. Findings are
reported as flags under semantic content (S2/S3 evidence) and in "Prioritised flags"; the
check carries no score of its own:

1. **Homemade terms against established ones:** List the text's load-bearing coined terms
   and metaphors. For each, ask: does the literature have an ESTABLISHED term for (part of)
   the same phenomenon? If so, that is a flag — either the established term should be used,
   or the coinage should be explicitly anchored to it ("what the literature calls X is here
   called Y because …"). A text that coins words for known phenomena without marking it
   loses precision AND signals unfamiliarity with the literature.
2. **Obvious but absent anchor terms:** Ask the reverse: which technical terms would a peer
   reviewer EXPECT to meet in a text on this topic (e.g. *stage-gate* and
   *human-in-the-loop* in a text about gate-governed human–AI processes)? The absence of an
   obvious anchor term is a flag — even when the text's own wording is perfectly clear.
3. **Calibrating the volume:** The check measures anchoring, not jargon density. Never
   recommend replacing a well-functioning, defined coinage with a worse-fitting technical
   term — the flag is an observation plus a question to the author, never a command.

The rationale is in the design history (v1.3): both finding classes (unanchored coinages
and absent anchor terms) were found in practice by a free-form read-through AFTER two full
rubric runs had missed them.

### Step 3 — Compute

- Criterion score s ∈ {0,1,2,3,4}; criterion weights w (default equal) from the genre profile.
- Dimension score: `D_j = (Σ w·s) / (4·Σ w) · 100 %`.
- Total: `Total = Σ v_j · D_j` with the profile's dimension weights v (always report the weights).
- Confidence band per dimension: all criteria high → ±3 pp; at least one medium → ±6 pp;
  at least one low → ±10 pp. The bands are conventions, not statistics — say so in the
  method box.

### Step 4 — Stability and halo check

- **Halo alarm:** if all D_j fall within a 10 pp band, add a warning to the report about a
  possible halo effect, and revisit the two criteria with the thinnest evidence.
- **Stability check (on request, or for book-wide use):** rerun steps 2–3 in a fresh
  context (subagent without access to the first pass's scores) and report |ΔD_j|.
  Divergence > 8 pp on a dimension → mark it "unstable — needs a human eye".

### Step 5 — Report

Follow the template in `references/report-template.md` EXACTLY — the fixed format is what
makes runs comparable over time. The report always opens with the calibration block and
always closes with the method box. Improvement suggestions are prioritised FLAGS
("S2, section 4: 'performance' is used in three senses — consider a terminological key"),
never finished rewrites.

Four elements beyond the criterion assessments:

- **Production findings (unscored):** production remnants (internal notes, version
  markers), hyphenation/parsing artefacts, empty pages, table/figure formatting, dangling
  numbers. They do NOT enter the score (they are manuscript mechanics, not text quality)
  but are always reported — a leftover production note is often the single most important
  pre-publication finding.
- **Binding constraints:** per dimension, identify the flag(s) currently holding the score
  down ("S will not rise above 60 % until the S2 drift is resolved"). This conveys the
  same information as a "readiness before/after" percentage without inventing a number
  that cannot be justified.
- **"What the text does not claim" (optional flag):** if the text is polemically exposed,
  suggest that the author add an explicit delimitation of what the argument does NOT
  assert — but do not write it.
- **Handoff package:** close with precise rewrite briefs for the relevant skills
  (academic-english-narrative / academic-english-consistency etc.): which passages, which
  problem, which direction — but no finished wording.

### Communication rules (apply to the whole report)

- **The report ALWAYS opens with the "How to read this report" block** from the template —
  the interpretation scale and the language model's limitations must sit where the reader
  meets the numbers, not only in a skill file the reader never sees.
- **Few abbreviations.** Use full criterion names with the code in parentheses —
  "conceptual consistency (S2)", not "S2". Explain every abbreviation at first use.
  The reader of the report does not know the skill's internal codes.
- **The audit is a dialogue tool.** Phrase findings as contributions to a conversation
  ("this suggests …; judge for yourself whether …"), not as verdicts. A language model can
  misread — the report must invite verification, stated both in the opening block and in
  the method box.

## Boundaries

- Never deliver a score without evidence without marking it as an estimate.
- Never change the text; never propose concrete new wording (that is the narrative
  skill's job).
- Never compare scores across different calibrations.
- If in doubt whether a criterion applies to the genre: note the doubt in the method box
  rather than scoring low "to be safe".
- Dimension D assesses reflexivity about position and framing — NEVER the position itself.
  D findings are phrased as observation plus a question to the author, never as a
  prescription of stance. D is opt-in, unscored by default, confidence-capped at medium,
  and weighted ≤ 0.05 in scored mode.


- **Case facts about real companies/events:** NEVER flag as "error" merely because one
  secondary work gives different numbers — secondary literature often varies. Check
  contemporaneous primary/press sources, and phrase the finding as "sources vary — verify",
  citing the specific counter-source and its year. "Differs from one source" is not "wrong".

## Design history (dimension choices MUST be justified here)

- **v1.0 (July 2026):** Five dimensions (S/H/T/M/F), formalised from a cross-model review
  experiment; English sister of the Danish `akademisk-tekstaudit`. The discourse/power
  dimension from the original whole-book review was NOT included, and the omission was
  undocumented — a lapse of design discipline.
- **v1.1 (August 2026):** Dimension D (discourse and power reflexivity) adopted as an
  optional flag dimension with four safety valves (opt-in; unscored default; confidence cap
  medium; position neutrality), ported from the Danish sister skill. Rationale:
  discourse/power was the most productive finding class in the review the skill family was
  formalised from — the instrument must not be blind to its own most value-creating finding
  class. Counter-concerns (hence the valves): the risk that an LLM judge scores stances
  rather than quality, and pseudo-quantification of what is hardest to measure. The rubric
  is translated, not mirrored: established English terminology (positionality, definitional
  authority, voice, framing) replaces the Danish coinages.
- **v1.2 (August 2026):** Deterministic fact-consistency sweep (Step 2b) added after two
  independent blind runs of the Danish sister missed a word-against-fact error ("multi-year
  collaboration" for a case the text itself dated to eight months) that a free-form
  cross-model review caught spontaneously. Lesson: anchored rubrics buy reliability by
  directing attention — and are therefore systematically blind outside the rubric.
  Everything that can be checked deterministically should be; the rubric covers only what
  requires judgment.
- **v1.3 (August 2026):** Terminological anchoring check (Step 2c) added after a free-form
  read-through of the article case found two finding classes that two full rubric runs had
  missed: (a) 18 coined terms, several covering phenomena with established names (the gate
  concept ↔ *stage-gate*/Cooper 1990; the feeling of cheating ↔ *impostor phenomenon*/
  Clance & Imes 1978 — with an explicit distinction), and (b) six obvious but absent anchor
  terms (*human-in-the-loop*, *quality by design*, *poka-yoke* and others) whose insertion
  markedly strengthened the text's scholarly grounding. Same lesson as v1.2: the rubric only
  sees what it asks about — the absence of something expected requires an explicit step that
  asks about absence.
- Future inclusion or exclusion of dimensions must be justified in this section.
- **v1.5 (August 2026, mirrored from Danish sister):** Source-variation rule for case facts
  added (Boundaries), after the PM-book quality gate produced a false positive: an auditor
  flagged Enron's 20/70/10 split as a GE transplant, but contemporaneous press (TIME, 2001)
  documents exactly that split for Enron — secondary accounts vary (PRC 1-5 with ~15% bottom
  also circulates). Lesson: for real-world cases, "differs from one source" must be
  distinguished from "wrong"; the flag phrasing is "sources vary — verify". The same gate
  confirmed the value of the F1/F4 criteria (14 unreferenced floats found) — that check is now
  also deterministic in pm-konsistens-audit (§8).
