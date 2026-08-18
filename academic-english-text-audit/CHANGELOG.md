# Changelog — academic-english-text-audit

## 1.5 (2026-08-17)
- **Source-variation rule for case facts** (Boundaries) — never flag a real-world case fact
  as an "error" merely because one secondary work gives different numbers; check
  contemporaneous primary/press sources and phrase the finding as "sources vary — verify".
  Added after the PM-book quality gate produced a false positive on Enron's 20/70/10 split.
  (Mirrored from the Danish sister; merged here from academic-book-skills@5687513.)

## 1.4 (2026-08-07)
- New **Step 2d: AI-insertion check** — targeted spot-check of freshly AI-inserted/rewritten
  passages for adjacent-paragraph echo, metaphor residue from the AI register, and missing
  idiomatic warrant. Flag-mode. Derived from the language pass in the article case (7 findings
  in one fresh passage).
- **Genre profile "journal article (empirical)": methods block** (calibration.md) — five
  checkpoints (search documentation, operationalisation, design explication, self-validation
  delimitation, residual-error coverage) + S4 sharpenings (generalisation scope, institutional
  precision). Derived from a gap analysis of 30 external review findings: 6 genuine gaps
  clustered in methodological verifiability.
- **Battery recommendation** (new section): ai-tell-audit + engagement-audit + free-form
  cross-model review as a documented complementary battery; the handoff may recommend
  publishing the claims table in the text itself. Basis: 5 of 30 external findings were
  covered by sister skills that had not been run.

## 1.3 (2026-08-05)
- New **Step 2c: Terminological anchoring** — checks (a) coined terms covering phenomena
  with established names (use the term or anchor the coinage explicitly) and (b) obvious but
  absent anchor terms a peer reviewer would expect. Flag mode, no score of its own;
  calibration rule against jargon inflation.
- Design history extended with the v1.3 rationale: both finding classes were found by a
  free-form read-through AFTER two full rubric runs had missed them — the absence of
  something expected requires a step that explicitly asks about absence.

## 1.2 (2026-08-05)
- New **Step 2b: Internal fact consistency** — deterministic sweep BEFORE computing: number
  against number (same referent, different numbers), word against fact (qualitative
  time/quantity words against the text's own dates and counts), promise against delivery in
  numbers (heading/roadmap counts against what is delivered). Findings → production
  findings / S2 evidence; no score of its own.
- Design history extended with the v1.2 rationale: two blind runs of the Danish sister
  missed a word-against-fact error that a free-form cross-model review caught — rubric
  attention is systematically blind outside the rubric; deterministic checks must cover
  the rest.

## 1.1 (2026-08-05)
- Optional **Dimension D: discourse and power reflexivity** (D1 declared positionality,
  D2 definitional authority, D3 voice and absence, D4 framing) —
  `references/rubric-D-discourse.md`, ported from the Danish sister skill (v1.1) and
  translated to established English terminology rather than mirrored verbatim.
- Four safety valves: opt-in per run (default OFF); flag mode without score as default
  (scored mode on explicit request only, weight ≤ 0.05); confidence cap medium; position
  neutrality (findings = observation + question, never a prescription of stance).
- New "Design history" section in SKILL.md: dimension choices must be justified there.
- Method box extended with the D caveat (weaker evidential grounding than S/T).

## 1.0 (2026-07-22)
- First version: five-dimension audit (S semantic, H hermeneutic, T technical composition,
  M metaphor, F tables/figures), 19 BARS-anchored criteria, two-parameter calibration
  (genre profile + level baseline), analyse-before-score workflow, confidence bands,
  halo/stability checks, fixed report template. English sister of `akademisk-tekstaudit`;
  shares its evidence base (`references/references.md`).
