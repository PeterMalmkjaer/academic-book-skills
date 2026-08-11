---
name: academic-english-ai-tell-audit
description: >-
  Measure the density of "AI tells" (LLM-overused style markers and formulaic
  structures) in ENGLISH academic prose, and recommend reductions that respect the
  material's own voice. Use when a manuscript is AI-assisted and the author wants an
  evidence-based, quantified read of stylistic LLM markers. It MEASURES and FLAGS —
  it never rewrites, and it is NOT an AI-authorship detector or a tool for evading
  AI-use disclosure. Explicit-invocation cues (only on direct request): "AI tells", "AI-tell density", "does this read like
  ChatGPT", "measure LLM style markers", "de-AI check". OPT-IN ONLY — this skill never auto-starts on topic detection; it runs only when the user explicitly asks for this audit (by name or an unambiguous request). Excludes citations,
  sources, cases, quotations, boxes, figures and defined terms — it scores BODY PROSE
  only. General purpose (any English academic manuscript). For the actual rewriting,
  hand results to academic-english-narrative.
license: MIT
metadata:
  family: academic-english
  siblings: academic-english-consistency, academic-english-narrative
  danish-counterpart: academic-danish-ai-tell-audit
  version: 0.1.2
  evidence_base: references/research_basis.md
---

# Academic English — AI-tell audit (measure, don't change)

A standalone, general-purpose **measurement** skill. It computes an **AI-tell density**
for English academic prose — how often LLM-overused style markers and formulaic
structures appear — and recommends reductions **in the material's own register**. It
does not rewrite (that is `academic-english-narrative`'s job) and it does not judge
authorship.

## What it is — and is NOT

- **It IS** a *style-density index*: markers per 1,000 body-prose words (and, where a
  pre-2022 baseline is available, *excess* over that baseline), plus a catalogue of
  formulaic structures, with locations and counts.
- **It is NOT** an "% AI-written" verdict. Marker lists cannot attribute authorship at
  the document level (Kobak et al. measure *corpus prevalence*, not per-text
  authorship). Reporting "X% AI" would be false precision and an integrity hazard.
- **It is NOT** for evading AI-use disclosure. It helps polish *style*; it does not
  hide AI assistance, and disclosure obligations remain the author's.

## Scope — body prose only

Citations, sources, "Further Reading", case boxes, definitions, quotations, figure/table
captions and defined-term names are **excluded from the count** (see
`references/protected_content.md`). Only running body prose is measured. This keeps the
signal clean (a term like *significant* inside a stats result is not an AI tell).

## The metric

- **AI-tell density** = flagged markers ÷ body-prose words × 1,000.
- Indicative bands (advisory, not law): **low < 3/1,000 · medium 3–6 · high > 6.**
- Because these markers are legitimate English in moderation, the signal is
  **over-use / density**, never presence. One "delve" is not a defect.
- **Respect the material's voice:** where the author supplies pre-2022 or personal
  baseline text, prefer *excess-over-baseline*; a warm textbook register legitimately
  uses some of these words, so recommendations are advisory and register-aware.

## Workflow
1. **Intake & log.** Confirm files/scope; open `RUN_LOG.md`; run `scripts/ai_tell_density.py`.
2. **Measure.** Density, top markers (with counts + locations), structural tells,
   band — body prose only, protected content excluded.
3. **Recommend (never rewrite).** Suggest a target density and *which* markers to
   thin, honouring the material's register. Hand the actual rewriting to
   `academic-english-narrative`.
4. **Report.** Density, breakdown, recommendations, and the standing disclaimer:
   *"This is a style-density index, not an AI-authorship verdict."*

## Deterministic helper: `scripts/ai_tell_density.py`
Read-only. Excludes protected regions, counts an evidence-based, **versioned** marker
lexicon (`references/markers.md`) + structural tells, reports density/‰ and locations.
Never edits source files.

```bash
python scripts/ai_tell_density.py --input <folder-or-glob> --out report.md --log RUN_LOG.md
```

## Do not auto-start
This skill is **opt-in only**. Do not launch it because the topic of AI writing, ChatGPT, or style comes up; start it only when the user directly asks for the audit.

## When NOT to use
- To rewrite/remove tells → `academic-english-narrative`.
- To detect or accuse AI authorship, or to evade disclosure → not supported.
- Danish text → `academic-danish-ai-tell-audit`.

## Files
- `README.md` — overview, research references, installation, usage.
- `references/research_basis.md` — cited evidence (Kobak; Liang) + caveats.
- `references/markers.md` — the versioned English marker lexicon + structural tells.
- `references/protected_content.md` — what is excluded from the count.
- `references/run_log_template.md` — audit trail.
- `scripts/ai_tell_density.py` — read-only density measurement.
