---
name: academic-danish-engagement-audit
description: >-
  Produce a reportable READING-ENGAGEMENT score for DANISH academic prose — how likely the
  text is to hold a reader's interest and motivation to keep reading — with a clear
  explanation and register-aware recommendations. It MEASURES only; it does NOT change the
  text unless the user gives an explicit, specific order, and even then it states the
  consequences and hands rewriting to academic-danish-klarsprog. It is NOT a readability
  grade (that is LIX) and NOT a licence to add decorative interest (seductive details harm
  learning). OPT-IN ONLY — never auto-starts; run only on explicit request. Cues (only on
  direct request): "engagement-score", "læse-engagement", "hvor engagerende er det",
  "læsemotivations-score". Scores BODY PROSE only. General purpose (any Danish academic
  manuscript).
license: MIT
metadata:
  family: academic-danish
  siblings: academic-danish-consistency, academic-danish-klarsprog, academic-danish-ai-tell-audit
  english-counterpart: academic-english-engagement-audit
  version: 0.1.0
  evidence_base: references/research_basis.md
---

# Academic Danish — reading-engagement audit (measure, don't change)

A standalone, **opt-in**, **measurement** skill for DANISH academic prose. It reports a
**reading-engagement score**, explains it, and gives **register-aware** recommendations.
It **does not rewrite**.

## Calibration note (honesty)
The validated **Flesch Human-Interest** formula is English-calibrated (coefficients 3.635 /
0.314). This skill applies the **same feature logic** to Danish (personal words / personal
sentences) but the resulting number is an **adapted, relative index — not a validated
Danish instrument.** The interest-theory (Sadoski; Schraw & Lehman; Hidi & Renninger) is
language-general; the concrete marker lists are a Danish adaptation to calibrate.

## What it is — and is NOT
- **It IS** a reportable engagement index: an adapted Human-Interest-style number plus
  Danish concreteness / reader-engagement / narrativity proxies.
- **It is NOT** a readability grade (that is LIX) and NOT an AI detector.
- **It is NOT** a licence for decorative interest. **Seductive details** — interesting but
  irrelevant material — *reduce* learning (Harp & Mayer, 1998).

## Measure only — and the consequence of changing
By default it **only measures and recommends; it changes nothing.** Only on an **explicit,
specific order** does it act — and even then it does **not** rewrite here: it states the
consequences (irrelevant vividness harms learning; a low score in dense theory is often
genre-appropriate; rewriting is fidelity-bound) and hands rewriting to
`academic-danish-klarsprog`.

## Scope — body prose only
Citations, sources, "Videre Læsning", case boxes, definitions, quotations, figure/table
captions and defined-term names are **excluded** (`references/protected_content.md`).

## Workflow
1. Intake & log; run `scripts/engagement_score_da.py`.
2. Report the adapted HI-style number + Danish proxies + band, with a plain-language reading.
3. Recommend (register-aware, seductive-details-safe) — never rewrite.
4. State the disclaimer + consequence note.

## Deterministic helper: `scripts/engagement_score_da.py`
Read-only. Danish feature lists. Never edits source files.

```bash
python scripts/engagement_score_da.py --input <folder-or-glob> --out report.md --log RUN_LOG.md
```

## When NOT to use
- To rewrite / raise engagement → `academic-danish-klarsprog` (on explicit request).
- Readability → LIX. AI-style markers → academic-danish-ai-tell-audit. English → english counterpart.

## Files
- `README.md` — overview, research references, installation, usage.
- `references/research_basis.md` — cited evidence + the Danish-calibration caveat.
- `references/features.md` — the scored features (Danish).
- `references/protected_content.md` — what is excluded.
- `references/run_log_template.md` — audit trail.
- `scripts/engagement_score_da.py` — read-only measurement.
