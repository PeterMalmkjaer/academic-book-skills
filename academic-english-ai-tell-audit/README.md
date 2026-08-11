# academic-english-ai-tell-audit

A standalone, **opt-in** skill that **measures** the density of "AI tells" — LLM-overused
style markers and formulaic structures — in **English** academic prose, and recommends
reductions that respect the material's own register. It **measures and flags; it never
rewrites**, and it is **not** an AI-authorship detector or a tool for evading AI-use
disclosure.

The metric is a **style-density index** (markers per 1,000 body-prose words), *not* an
"% AI-written" verdict. Citations, sources, cases, quotations, boxes, figures and defined
terms are excluded from the count — only running body prose is measured.

## Research basis

The skill is grounded in peer-reviewed evidence that LLM use leaves measurable
vocabulary traces in academic writing:

- **Kobak, D., González-Márquez, R., Horvát, E.-Á., & Lause, J. (2025).** *Delving into
  LLM-assisted writing in biomedical publications through excess vocabulary.* **Science
  Advances.** https://doi.org/10.1126/sciadv.adt3813 · preprint: arXiv:2406.07016,
  https://arxiv.org/abs/2406.07016
  — Analysed ~14–15M PubMed abstracts (2010–2024); an abrupt post-ChatGPT surge in
  specific *style words* (e.g. *delve, underscore, showcasing, potential, crucial*);
  ≥13.5% of 2024 abstracts LLM-processed. Method: *excess vocabulary* — the signal is
  **excess frequency, not presence.**
- **Liang, W., et al. (2024).** *Monitoring AI-Modified Content at Scale: A Case Study on
  the Impact of ChatGPT on AI Conference Peer Reviews.* **ICML 2024 (PMLR 235).**
  arXiv:2403.07183, https://arxiv.org/abs/2403.07183
  — 6.5–16.9% of ML peer-review sentences substantially LLM-modified; characteristic
  adjectives (*commendable, meticulous, intricate, innovative, comprehensive*).

Design consequences (see `references/research_basis.md` for the full, confidence-rated
account): measure over-use not presence; no document-level authorship claim; a
**versioned** marker lexicon (moving target); register-aware, advisory recommendations;
research-integrity guardrails.

## Installation

- **As a skill (Cowork / Claude):** import the packaged `.skill` archive
  ("Save skill"), or place the `academic-english-ai-tell-audit/` folder in your skills
  directory. It is **opt-in only** — it never starts automatically; invoke it by name or
  an unambiguous request.
- **Script only:** requires **Python 3.8+**, standard library only (no third-party
  dependencies).

## Usage

Invoke the skill explicitly, e.g. *"run academic-english-ai-tell-audit on chapter 17"*.
Or run the read-only script directly:

```bash
python scripts/ai_tell_density.py --input <folder-or-glob> --out report.md --log RUN_LOG.md
```

Output: AI-tell density per 1,000 body-prose words (bands: low < 3 · medium 3–6 · high >
6), top markers with counts, structural tells, and an advisory recommendation. For the
actual rewriting, hand the report to **academic-english-narrative** — this skill never
edits source files.

## What it is NOT
Not an AI-authorship detector; not a way to evade AI-use disclosure; not a rewriter.

## License
MIT — see the repository `LICENSE`.
