# academic-english-engagement-audit

A standalone, **opt-in** skill that produces a **reportable reading-engagement score** for
**English** academic prose — an estimate of how well the text triggers and sustains a
reader's interest and motivation to keep reading — with a clear explanation and
**register-aware** recommendations.

It **measures only. It does not change the text** unless the user gives an explicit,
specific order — and even then it does not rewrite here: it states the consequences and
hands the rewriting to `academic-english-narrative`. It is **not** a readability grade and
**not** a licence to add decorative interest (see *seductive details* below).

## The score
- **Human Interest (HI)** — the validated **Flesch** formula: `HI = 3.635·(personal words
  /100 words) + 0.314·(personal sentences /100 sentences)`; Flesch bands: ~30 interesting,
  50 very interesting, 80 dramatic. This is the headline, validated number.
- **Concreteness**, **reader-engagement** and **narrativity** proxies (per 1,000 words),
  reported separately and labelled as directional, not validated instruments.
- An advisory overall band, read in the light of genre (dense theory prose legitimately
  scores low HI).

## Research basis
- **Flesch, R. (1948/1949).** *A new readability yardstick / The Art of Readable Writing.*
  Human-Interest formula (personal words + personal sentences).
- **Sadoski, M., Goetz, E. T., & Rodriguez, M. (2000).** Engaging texts: effects of
  concreteness on comprehensibility, interest, and recall. *J. Educ. Psychol., 92*(1),
  85–95. https://doi.org/10.1037/0022-0663.92.1.85 — concreteness is the strongest
  text-based predictor of interest and recall (dual-coding theory).
- **Schraw, G., & Lehman, S. (2001).** Situational interest: a review. *Educ. Psychol.
  Rev., 13*(1), 23–52 — coherence, vividness, character identification, suspense, novelty.
- **Hidi, S., & Renninger, K. A. (2006).** Four-phase model of interest development.
  *Educ. Psychologist.* · **Guthrie et al. (2006),** *RRQ*, doi:10.1002/rrq.81.
- **Harp, S. F., & Mayer, R. E. (1998).** How seductive details do their damage. *J. Educ.
  Psychol., 90*(3), 414–434. https://doi.org/10.1037/0022-0663.90.3.414 — interesting but
  **irrelevant** detail *reduces* learning. Meta-analysis: Sundararajan & Adesope (2020),
  *Educ. Psychol. Rev., 32.*

Full, confidence-rated account: `references/research_basis.md`.

## The seductive-details guardrail
Raising an engagement score is **not** a goal in itself. Adding vivid but irrelevant
material harms comprehension and recall (Harp & Mayer, 1998). This skill rewards
**relevant** concreteness and coherence; a recommendation to "raise engagement" never
means "add trivia," and a low score in a dense theory passage is often genre-appropriate.

## Installation
- **As a skill (Cowork / Claude):** import the `.skill` archive ("Save skill"), or place
  the `academic-english-engagement-audit/` folder in your skills directory. **Opt-in only**
  — it never starts automatically.
- **Script only:** **Python 3.8+**, standard library only.

## Usage
Invoke explicitly, e.g. *"run academic-english-engagement-audit on chapter 17"*. Or run the
read-only script:

```bash
python scripts/engagement_score.py --input <folder-or-glob> --out report.md --log RUN_LOG.md
```

Output: Human Interest (with Flesch band), concreteness/engagement/narrativity proxies,
overall band, a plain-language reading, and register-aware recommendations. Body prose
only; citations, quotations, boxes, cases, figures and defined terms are excluded. It never
edits source files; to act on the recommendations, use `academic-english-narrative`.

## What it is NOT
Not a readability grade (use LIX / Flesch Reading Ease); not an AI detector; not a
rewriter; not a licence for seductive details.

## License
MIT — see the repository `LICENSE`.
