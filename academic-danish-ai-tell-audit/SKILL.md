---
name: academic-danish-ai-tell-audit
description: >-
  Measure the density of "AI tells" (LLM-overused style markers and formulaic
  structures) in DANISH academic prose, and recommend reductions that respect the
  material's own voice. Use when a Danish manuscript is AI-assisted and the author wants
  a quantified read of stylistic LLM markers. It MEASURES and FLAGS — it never rewrites,
  and it is NOT an AI-authorship detector or a tool for evading AI-use disclosure.
  Explicit-invocation cues (only on direct request): "AI-tells", "AI-tell-tæthed", "lyder det som ChatGPT", "mål LLM-stilmarkører",
  "af-AI-tjek". OPT-IN ONLY — this skill never auto-starts on topic detection; it runs only when the user explicitly asks for this audit (by name or an unambiguous request). Excludes citations, sources, cases, quotations, boxes, figures and
  defined terms — it scores BODY PROSE only. General purpose (any Danish academic
  manuscript). For the actual rewriting, hand results to academic-danish-klarsprog.
license: MIT
metadata:
  family: academic-danish
  siblings: academic-danish-consistency, academic-danish-klarsprog
  english-counterpart: academic-english-ai-tell-audit
  version: 0.1.2
  evidence_base: references/research_basis.md
---

# Academic Danish — AI-tell audit (measure, don't change)

A standalone, general-purpose **measurement** skill for DANISH academic prose. It
computes an **AI-tell density** — how often LLM-overused Danish style markers and
formulaic structures appear — and recommends reductions **in the material's own
register**. It does not rewrite (that is `academic-danish-klarsprog`'s job) and it does
not judge authorship.

## What it is — and is NOT
- **It IS** a *style-density index*: markers per 1,000 body-prose words, plus formulaic
  structures, with locations and counts.
- **It is NOT** an "% AI-written" verdict (marker lists cannot attribute authorship at
  the document level). Reporting "X% AI" would be false precision and an integrity hazard.
- **It is NOT** for evading AI-use disclosure.

## Important calibration note (honesty)
The strongest empirical evidence for AI tells is **English** (Kobak 2025; Liang 2024).
The Danish marker list here is an **informed adaptation, not yet corpus-validated for
Danish** — Danish LLM markers (calques, connectives) differ from English. Treat the
list as a **starting point to calibrate against a Danish baseline**, and bump the
versioned list as evidence accrues.

## Scope — body prose only
Citations, sources, "Videre Læsning", case boxes, definitions, quotations, figure/table
captions and defined-term names are **excluded from the count** (see
`references/protected_content.md`). Only running body prose is measured.

## The metric
- **AI-tell density** = flagged markers ÷ body-prose words × 1,000.
- Indicative bands (advisory): **low < 3/1,000 · medium 3–6 · high > 6.**
- Signal is **over-use / density**, never presence. Respect the material's register: a
  warm textbook legitimately uses some of these words, so recommendations are advisory.

## Workflow
1. Intake & log; run `scripts/ai_tell_density_da.py`.
2. Measure (body prose only; protected content excluded).
3. Recommend (never rewrite); hand rewriting to `academic-danish-klarsprog`.
4. Report density + breakdown + the disclaimer: *"style-density index, not an
   AI-authorship verdict."*

## Deterministic helper: `scripts/ai_tell_density_da.py`
Read-only. Danish marker lexicon (`references/markers.md`) + structural tells. Never edits
source files.

```bash
python scripts/ai_tell_density_da.py --input <folder-or-glob> --out report.md --log RUN_LOG.md
```

## Do not auto-start
This skill is **opt-in only**. Do not launch it because the topic of AI writing, ChatGPT, or style comes up; start it only when the user directly asks for the audit.

## When NOT to use
- To rewrite/remove tells → `academic-danish-klarsprog`.
- To detect or accuse AI authorship, or to evade disclosure → not supported.
- English text → `academic-english-ai-tell-audit`.

## Files
- `README.md` — overview, research references, installation, usage.
- `references/research_basis.md` — cited evidence + the Danish-calibration caveat.
- `references/markers.md` — the versioned Danish marker lexicon + structural tells.
- `references/protected_content.md` — what is excluded from the count.
- `references/run_log_template.md` — audit trail.
- `scripts/ai_tell_density_da.py` — read-only density measurement.
