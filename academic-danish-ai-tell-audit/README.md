# academic-danish-ai-tell-audit

A standalone, **opt-in** skill that **measures** the density of "AI tells" — LLM-overused
style markers and formulaic structures — in **Danish** academic prose, and recommends
reductions that respect the material's own register. It **measures and flags; it never
rewrites**, and it is **not** an AI-authorship detector or a tool for evading AI-use
disclosure.

The metric is a **style-density index** (markers per 1,000 body-prose words), *not* an
"% AI-written" verdict. Citations, sources, cases, quotations, boxes, figures and defined
terms are excluded — only running body prose is measured.

## Research basis

The *method* is grounded in peer-reviewed English evidence; the **Danish marker list is
an informed adaptation, not yet corpus-validated** (calibrate against a Danish baseline).

- **Kobak, D., González-Márquez, R., Horvát, E.-Á., & Lause, J. (2025).** *Delving into
  LLM-assisted writing in biomedical publications through excess vocabulary.* **Science
  Advances.** https://doi.org/10.1126/sciadv.adt3813 · arXiv:2406.07016
- **Liang, W., et al. (2024).** *Monitoring AI-Modified Content at Scale…* **ICML 2024.**
  arXiv:2403.07183, https://arxiv.org/abs/2403.07183

See `references/research_basis.md` for the full, confidence-rated account and the honest
Danish-calibration caveat. Design principles: measure over-use not presence; no
document-level authorship claim; **versioned** lexicon; register-aware recommendations;
research-integrity guardrails.

## Installation

- **As a skill (Cowork / Claude):** import the packaged `.skill` archive ("Save skill"),
  or place the `academic-danish-ai-tell-audit/` folder in your skills directory. It is
  **opt-in only** — it never starts automatically.
- **Script only:** requires **Python 3.8+**, standard library only.

## Usage

Invoke the skill explicitly, e.g. *"kør academic-danish-ai-tell-audit på kapitel 17"*.
Or run the read-only script directly:

```bash
python scripts/ai_tell_density_da.py --input <folder-or-glob> --out report.md --log RUN_LOG.md
```

Output: AI-tell density per 1,000 body-prose words, top Danish markers, structural tells,
and an advisory recommendation. For the actual rewriting, hand the report to
**academic-danish-klarsprog** — this skill never edits source files.

## What it is NOT
Not an AI-authorship detector; not a way to evade AI-use disclosure; not a rewriter.

## License
MIT — see the repository `LICENSE`.
