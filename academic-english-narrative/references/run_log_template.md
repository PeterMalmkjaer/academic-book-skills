# RUN_LOG — academic-english-narrative

Append-only audit trail. One block per run. Never overwrite earlier blocks. Purpose:
every prose change must be traceable to the exact rewrite, preset, and run that made
it. **No rewrite ships without a corresponding line here.**

---

## RUN <n> — <YYYY-MM-DD HH:MM:SS TZ>

### 1. Header
- Skill version: 0.1.0
- Operator request (verbatim): "<paste exact instruction>"
- Target preset: <narrative-academic-european | textbook-pedagogical | journal-formal | trade-crossover>
- Element-type overrides (if any): <e.g. cases→textbook-pedagogical; declared>
- Files in scope (path — sha256 — word count):
  - <chapterXX.tex — a1b2c3… — 9088>
- Decision log / skopos brief used: <path or "none">

### 2. Baseline metrics (measure.py)
- Command: `<exact command>`  → output: `<path>`
| file | sent.len mean | sent.len SD | nominalisation/1k | hedges/1k | em-dash | first-person |
|---|---:|---:|---:|---:|---:|---:|
| | | | | | | |

### 3. Phase 1 — diagnosis vs preset
- <chapter/section — which dials are off target and how>

### 4. Phase 2 — rewrites
| location | before | after | dial(s) | conf. | note |
|---|---|---|---|---|---|
| | | | | | |

### 5. Phase 3 — meaning-fidelity self-check
- Rewrites evaluated: <N>
- Dropped (failed fidelity), with reason:
  - <location — reason: e.g. paraphrase weakened a hedged claim>
- Result line: `Fidelity check passed: <N> rewrites, 0 claims altered, 0 protected tokens changed.`

### 6. Phase 4 — post metrics & hand-off
- Post measure.py: <summary of movement toward preset>
- Consistency hand-off recommended? <Y/N — run academic-english-consistency next>

### 7. Skips & non-actions
- <span/sentence not rewritten and why: protected / precision-over-flow / low confidence>

### 8. Outputs written this run
- diagnosis_chapterXX.md
- rewrites_chapterXX.md (before/after)
- metrics_before.md / metrics_after.md
- this log block

---
<!-- next run appends below; do not edit blocks above -->
