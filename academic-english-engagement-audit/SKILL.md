---
name: academic-english-engagement-audit
description: >-
  Produce a reportable READING-ENGAGEMENT score for ENGLISH academic prose — how likely
  the text is to hold a reader's interest and motivation to keep reading — with a clear
  explanation and register-aware recommendations. It MEASURES only; it does NOT change the
  text unless the user gives an explicit, specific order, and even then it states the
  consequences and hands the rewriting to academic-english-narrative. It is NOT a
  readability grade and NOT a licence to add decorative "interest" (seductive details harm
  learning). OPT-IN ONLY — never auto-starts on topic detection; run only on explicit
  request. Explicit-invocation cues (only on direct request): "engagement score", "reading
  engagement", "how engaging is this", "reader-motivation score". Scores BODY PROSE only
  (citations, sources, cases, quotations, boxes, figures, defined terms excluded). General
  purpose (any English academic manuscript).
license: MIT
metadata:
  family: academic-english
  siblings: academic-english-consistency, academic-english-narrative, academic-english-ai-tell-audit
  danish-counterpart: academic-danish-engagement-audit
  version: 0.1.0
  evidence_base: references/research_basis.md
---

# Academic English — reading-engagement audit (measure, don't change)

A standalone, **opt-in**, **measurement** skill. It reports a **reading-engagement score**
for English academic prose — an estimate of how well the text triggers and sustains a
reader's interest and motivation — explains the score, and gives **register-aware**
recommendations. It **does not rewrite**.

## What it is — and is NOT
- **It IS** a reportable, feature-based engagement index built around the validated
  **Flesch Human-Interest** formula plus evidence-based text-interest proxies
  (concreteness, reader engagement, narrativity). See `references/features.md`.
- **It is NOT** a readability grade (that is LIX / Flesch Reading Ease) and NOT an AI
  detector. Engagement and readability are distinct axes.
- **It is NOT** a licence to inject decorative interest. **Seductive details** —
  interesting but irrelevant material — *reduce* learning (Harp & Mayer, 1998). The
  score rewards *relevant* concreteness and coherence, never trivia.

## Measure only — and the consequence of changing
By default this skill **only measures and recommends; it changes nothing.** If — and only
if — the user gives an **explicit, specific order to change the text**, the skill still
does **not** rewrite here; it states the **consequences** and hands the actual rewriting to
`academic-english-narrative`:
- raising engagement by adding *irrelevant* vividness harms comprehension and recall
  (seductive-details effect);
- a low engagement score in a dense theory passage is often *appropriate* for the genre,
  not a defect;
- rewriting is a fidelity-bound act (no claim, citation, or number may change) and belongs
  in the register skill, not here.

## Scope — body prose only
Citations, sources, "Further Reading", case boxes, definitions, quotations, figure/table
captions and defined-term names are **excluded** (`references/protected_content.md`).

## The score
- **Human Interest (HI)** — Flesch (1949): HI = 3.635·(personal words/100 words) +
  0.314·(personal sentences/100 sentences). Flesch bands: ~30 interesting, 50 very
  interesting, 80 dramatic. *Validated formula — the headline number.*
- **Concreteness proxy** — example/imagery markers per 1,000 words (Sadoski et al.:
  concreteness is the strongest text-based predictor of interest and recall).
- **Reader-engagement proxy** — questions and direct address per 1,000 words
  (situational-interest triggers; Schraw & Lehman, 2001).
- **Narrativity proxy** — temporal/event and agent markers (Dahlstrom, 2014).
- An overall **band** (advisory) is derived mainly from HI + concreteness, read in the
  light of genre.

## Workflow
1. Intake & log; run `scripts/engagement_score.py`.
2. Report HI + proxy sub-scores + band, body prose only, with a plain-language reading.
3. Recommend (register-aware, seductive-details-safe) — never rewrite.
4. State the standing disclaimer + the consequence note (above).

## Deterministic helper: `scripts/engagement_score.py`
Read-only. Computes Flesch HI + proxies, excludes protected regions, never edits source.

```bash
python scripts/engagement_score.py --input <folder-or-glob> --out report.md --log RUN_LOG.md
```

## When NOT to use
- To rewrite / raise engagement → `academic-english-narrative` (on explicit request).
- Readability grade → LIX / Flesch Reading Ease. AI-style markers → academic-english-ai-tell-audit.
- Danish text → `academic-danish-engagement-audit`.

## Files
- `README.md` — overview, research references, installation, usage.
- `references/research_basis.md` — cited evidence + confidence.
- `references/features.md` — the scored features + the Flesch HI definition.
- `references/protected_content.md` — what is excluded.
- `references/run_log_template.md` — audit trail.
- `scripts/engagement_score.py` — read-only measurement.
