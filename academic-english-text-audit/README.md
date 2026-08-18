# academic-english-text-audit

> **BETA — published without warranty of any kind.** © 2026 Peter Malmkjær. Free
> academic and non-commercial use with attribution; commercial use requires prior
> written agreement. LLM-produced assessments can be wrong; the user bears sole
> responsibility. See `LICENSE.md`.

Evidence-based quality audit of **English** academic prose (chapters, afterwords, monographs,
article drafts) on five dimensions — semantic content, hermeneutic content, technical
composition, metaphor use, tables/figures — plus an optional flag-mode Dimension D
(discourse and power reflexivity). Anchored 0–4 rubrics, two-parameter calibration,
weighted aggregation, confidence bands, verbatim evidence per score, and three targeted
sweeps/checks: deterministic fact consistency (v1.2), terminological anchoring (v1.3), and
an AI-insertion check on freshly inserted text (v1.4) — plus a methods block for empirical
journal articles and an explicit battery recommendation (v1.4). It **measures and flags — it never rewrites** (rewriting is handed
off to `academic-english-narrative`).

Sister skill of [`akademisk-tekstaudit`](https://github.com/PeterMalmkjaer/akademisk-tekstaudit)
(Danish); the two share one evidence base (`references/references.md`) and parallel version
numbering. Rubric terminology is translated, not mirrored: *positionality*, *definitional
authority*, *voice and absence*, *framing*.

## Files

- `SKILL.md` — the full workflow (calibration → argument reconstruction → analyse-before-score
  → fact-consistency sweep → computation → halo/stability checks → fixed report template),
  boundaries, and the design history in which all dimension choices must be justified.
- `references/calibration.md` — genre profiles, level baselines, interpretation scale.
- `references/rubrics.md` — 19 criteria with BARS anchors (0/2/4).
- `references/rubric-D-discourse.md` — optional Dimension D with four safety valves.
- `references/report-template.md` — the mandatory report format.
- `references/references.md` — shared evidence base (Danish/English), verification-marked.

## Version

1.4 — see `CHANGELOG.md`. Developed and used in the Performance Management book project
(CBS); design decisions are documented in the design history section of `SKILL.md`.
