# Research basis — academic-english-ai-tell-audit

The "AI-tell density" idea is empirically grounded. Confidence-tagged:
**[verified]** checked against a primary source; **[classic/known]** established but not
re-verified line-by-line here.

## Evidence that AI tells are real and measurable
- **Kobak, González-Márquez, Horvát & Lause (2025), Science Advances — "Delving into
  LLM-assisted writing in biomedical publications through excess vocabulary" (arXiv
  2406.07016). [verified]** Analysed ~14–15M PubMed abstracts (2010–2024). After
  ChatGPT, an abrupt frequency surge in specific *style words* (unrelated to content),
  e.g. *delve, underscore, showcasing, potential, crucial, findings*. Lower-bound
  estimate: ≥13.5% of 2024 abstracts LLM-processed (up to ~40% in sub-corpora) — larger
  than the COVID effect. Method: *excess vocabulary* (surge over a pre-2022
  counterfactual), i.e. the signal is **excess frequency, not presence**.
- **Liang et al. (2024), ICML — "Monitoring AI-Modified Content at Scale" (arXiv
  2403.07183). [verified]** Estimated 6.5–16.9% of sentences in ML-conference peer
  reviews were substantially LLM-modified, with characteristic adjectives
  (*commendable, meticulous, intricate, innovative, comprehensive*).

## Design consequences (why this skill is a *density index*, not a detector)
1. **Measure excess/over-use, not presence** (Kobak): the markers are legitimate words;
   only their density carries signal. → density per 1,000; prefer excess-over-baseline.
2. **No document-level authorship claim** (Kobak measures corpus prevalence): never
   output "% AI-written". → style-density index only.
3. **Marker lists are a moving target** (models and authors adapt): → versioned lexicon.
4. **Domain/register matters** (Kobak is biomedical): a warm textbook legitimately uses
   some markers. → recommendations are advisory and register-aware; the actual rewrite
   is deferred to the register skill.
5. **Integrity** (both papers stress research-integrity context): not for evading
   disclosure; fidelity preserved; flag, never rewrite.

## Source links (verify before quoting)
- Kobak et al. (2025), Science Advances — https://www.science.org/doi/10.1126/sciadv.adt3813 ; arXiv — https://arxiv.org/abs/2406.07016
- Liang et al. (2024), ICML — https://arxiv.org/abs/2403.07183 ; PMLR — https://proceedings.mlr.press/v235/liang24b.html
