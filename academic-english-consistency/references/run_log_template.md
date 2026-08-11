# RUN_LOG — academic-english-consistency

Append-only audit trail. One block per run. Never overwrite a previous run's block.
Purpose: any later error must be traceable to the exact run, rule, and confidence
that produced it. **No source change is ever proposed without a corresponding line
here.**

---

## RUN <n> — <YYYY-MM-DD HH:MM:SS TZ>

### 1. Header
- Skill version: 0.1.0
- Operator request (verbatim): "<paste user's exact instruction>"
- Phase(s) executed this run: <0 / 1 / 2 / 3 / 4>
- Files in scope (path — sha256 — word count):
  - <chapterXX.tex — a1b2c3… — 9088>
- Project decision log / skopos brief used: <path or "none">

### 2. Inputs
- scan.py command: `<exact command>`
- scan.py output: `<path>`
- Notable raw counts: <e.g. -ise: 41 / -ize: 0 ; -ization: 12 ; (Section x.y): 88>

### 3. Phase 1 — canonical decisions
| Item | Canonical chosen | Split counts | Confidence | Rationale |
|---|---|---|---|---|
| | | | | |
- Author sign-off: <name> @ <timestamp>  (REQUIRED before Phase 3)

### 4. Phase 2 — termbase deviations logged
| Concept | Canonical | Variant found | Location | Action |
|---|---|---|---|---|
| | | | | flag / verify |

### 5. Phase 3 — flags (per chapter)
| file | location | current | proposed | rule | conf. | in_protected? | status |
|---|---|---|---|---|---|---|---|
| | | | | | | N | proposed |
| | | | | | | Y | verify (protected) |

### 6. Phase 4 — fidelity self-check
- Proposals evaluated: <N>
- Dropped (failed fidelity), with reason:
  - <location — reason: e.g. would alter year inside citation>
- Result line: `Fidelity check passed: <N> proposals, 0 protected tokens altered.`

### 7. Skips & non-actions
- <item — why not checked: protected / low confidence / already consistent>

### 8. Outputs written this run
- MASTER_STYLE_SHEET.md (<draft|signed>)
- TERMBASE.md
- report_chapterXX.md
- this log block

---
<!-- next run appends below; do not edit blocks above -->
