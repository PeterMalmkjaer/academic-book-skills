# academic-danish-engagement-audit

A standalone, **opt-in** skill that produces a **reportable reading-engagement score** for
**Danish** academic prose — how well the text triggers and sustains a reader's interest and
motivation — with a clear explanation and **register-aware** recommendations.

It **measures only. It does not change the text** unless the user gives an explicit,
specific order — and even then it does not rewrite here: it states the consequences and
hands rewriting to `academic-danish-klarsprog`. It is **not** a readability grade (that is
LIX) and **not** a licence to add decorative interest (see *seductive details*).

## Calibration note (honest)
The validated Human-Interest formula is English-calibrated (Flesch). This skill applies the
same feature logic to Danish, so its number is an **adapted, relative index — not a
validated Danish instrument.** Calibrate against Danish material before treating it as
absolute.

## Research basis
- **Flesch, R. (1948/1949).** Human-Interest formula (personal words + personal sentences).
- **Sadoski, Goetz & Rodriguez (2000),** *J. Educ. Psychol., 92*(1), 85–95,
  https://doi.org/10.1037/0022-0663.92.1.85 — concreteness is the strongest text-based
  predictor of interest and recall.
- **Schraw & Lehman (2001),** *Educ. Psychol. Rev., 13*(1) — situational interest.
- **Hidi & Renninger (2006);** **Guthrie et al. (2006),** *RRQ*, doi:10.1002/rrq.81.
- **Harp & Mayer (1998),** *J. Educ. Psychol., 90*(3), 414–434,
  https://doi.org/10.1037/0022-0663.90.3.414 — seductive details harm learning; meta-analysis
  Sundararajan & Adesope (2020), *EPR, 32.*

Full account: `references/research_basis.md`.

## The seductive-details guardrail
Raising the score is not a goal in itself. Vivid but irrelevant material harms comprehension
and recall. This skill rewards **relevant** concreteness and coherence; a low score in a
dense theory passage is often genre-appropriate.

## Installation
- **As a skill (Cowork / Claude):** import the `.skill` archive, or place the
  `academic-danish-engagement-audit/` folder in your skills directory. **Opt-in only.**
- **Script only:** **Python 3.8+**, standard library only.

## Usage
Invoke explicitly, e.g. *"kør academic-danish-engagement-audit på kapitel 17"*. Or:

```bash
python scripts/engagement_score_da.py --input <folder-or-glob> --out report.md --log RUN_LOG.md
```

Output: adapted Human-Interest-style number, Danish concreteness/engagement/narrativity
proxies, overall band, plain-language reading, register-aware recommendations. Body prose
only. Never edits source; to act, use `academic-danish-klarsprog`.

## What it is NOT
Not a readability grade (use LIX); not an AI detector; not a rewriter; not a licence for
seductive details.

## License
MIT — see the repository `LICENSE`.
