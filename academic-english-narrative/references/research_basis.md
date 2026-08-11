# Research basis — academic-english-narrative

Why this skill exists and why its dials are what they are. The skill treats
"narrative academic English" as a measurable, register-selectable construct grounded
in published linguistics, science-communication, and management-writing research —
not as personal taste. Each entry carries a **confidence** tag:

- **[verified]** — checked against a primary source / publisher record during build.
- **[classic]** — well-established canonical work, cited from disciplinary knowledge,
  not re-verified line-by-line here; verify the exact edition/page before quoting.

Intellectual-honesty note: do not attach claims to these sources beyond what is
stated here without checking the source. Never fabricate page numbers or DOIs.

---

## 1. The foundational distinction: narrative vs. paradigmatic

- **Bruner, J. (1986). *Actual Minds, Possible Worlds*. Harvard UP. [classic]**
  Two irreducible modes of thought — *narrative* and *paradigmatic/logico-scientific*.
  Scientific prose is traditionally paradigmatic; "narrative academic English" is the
  question of how much narrative texture to admit *without* losing paradigmatic rigour.
  → Frames the whole skill: we tune the balance, we do not abandon rigour.

## 2. Narrativity is measurable — and correlates with uptake (with a caveat)

- **Hillier, A., Kelly, R. P., & Klinger, T. (2016). Narrative Style Influences
  Citation Frequency in Climate Change Science. *PLOS ONE*, 11(12), e0167983. [verified]**
  732 climate-science abstracts; more-narrative abstracts cited more often. **Caveat
  the authors themselves stress:** the effect is confounded with journal identity
  (higher-impact venues carry both more narrative prose and more citations).
  → Dial design lesson: aim for *appropriate*, venue-calibrated narrativity, not
  maximal narrativity. Encoded as the `trade-crossover` caution and the
  "respect disciplinary norm" hard rule.

- **Boyd, Blackburn & Pennebaker (2020) narrative-arc work, operationalised via LIWC
  (Staging, Plot Progression, Cognitive Tension); applied diachronically in *The
  Evolution of Narrativity in Abstracts of the Biomedical Literature 1989–2022*
  (2023, *Publications*, MDPI). [verified]**
  Demonstrates narrativity can be quantified as text features.
  → Justifies a metrics-based approach (`measure.py`) instead of vibes.

- **Dahlstrom, M. F. (2014). Using narratives and storytelling to communicate science
  with nonexpert audiences. *PNAS*, 111(Suppl. 4), 13614–13620. [classic]**
  Narrative improves comprehension/engagement, but raises an accuracy/persuasion
  tension. → Hard rule: **precision always wins over story.**

## 3. The semantic lever: grammatical metaphor & nominalisation

- **Halliday, M. A. K., & Martin, J. R. (1993). *Writing Science*. [classic]**
  *Grammatical metaphor*: processes (verbs) and properties (adjectives) re-encoded as
  *things* (nouns) = nominalisation. Builds abstraction and authority but backgrounds
  agents and motion. → The primary thing a narrative lift adjusts: selectively
  un-pack nominalisations into agent + active verb. Dial: **nominalisation density**.

- **Biber, D., & Gray, B. (2016). *Grammatical Complexity in Academic English*. [classic]**
  Documents noun-phrase compression / nominal density in science prose.
  → Supports nominalisation density and noun-compression as measurable targets.

- **Sword, H. (2012). *Stylish Academic Writing*. Harvard UP. [verified]**
  Empirical analysis of 1,000+ articles across sciences/social sciences/humanities.
  "Zombie nouns" (nominalisations) deaden prose; stylish writers use concrete nouns,
  active verbs, human agency, examples, vivid titles, occasional metaphor.
  → Dials: **agent visibility / active-verb ratio**, **concreteness**, **metaphor
  tolerance**.

- **COUNTERPOINT — Jiang, F. (Kevin), & Hyland, K. (e.g. 2021, *Written Communication*
  / *Applied Linguistics*): "metadiscursive nouns" / academic naming. [verified]**
  Nominalisations are not merely dead weight; they are *interactive*, organise
  argument, and carry authority and cohesion. Explicit pushback on Sword's "zombie
  nouns". → Critical design lesson: **nominalisation is a trade-off, never stripped
  blindly.** The default preset lowers it moderately, not to zero.

## 4. The pragmatic lever: reader-orientation, metadiscourse, stance

- **Hyland, K. (2005). *Metadiscourse*; and Hyland (2005) stance & engagement work.
  [verified]**
  Prose is steered pragmatically: *interactive* metadiscourse (organising text for the
  reader) and *interactional* metadiscourse (author stance, reader engagement). Recent
  work (Hyland & Jiang) shows academic writing becoming more reader-oriented over 50
  years. → Dials: **metadiscourse/engagement density**, **hedging/stance calibration**.

- **Gopen, G. D., & Swan, J. A. (1990). The Science of Scientific Writing.
  *American Scientist*, 78(6), 550–558. [classic]**
  Reader-expectation theory: meaning is produced by *structure* — topic position,
  stress position, subject–verb proximity — not word choice alone.
  → Dial: **information structure (theme/rheme, topic/stress)**. A core, low-risk lever
  because it improves flow without touching propositional content.

- **Swales, J. (1990). *Genre Analysis* (CARS model). [classic]**
  Rhetorical "moves" structure research-article sections.
  → Informs section-level diagnosis (macro narrativity), used cautiously in textbooks.

- **Martin, J. R., & White, P. R. R. (2005). *The Language of Evaluation: Appraisal*.
  [classic]** Semantics of evaluation/stance. → Supports hedging/stance calibration.

- **Atkinson, D. (1999). *Scientific Discourse in Sociohistorical Context*. [verified
  via secondary corpus literature]** Science prose became *less* narrative and more
  abstract as it professionalised (18th–19thC). → Register is historically contingent
  ⇒ presets, not one "correct" style, are the right architecture.

## 5. Field-specific: management & organisation studies

- **Pollock, T. G., & Bono, J. E. (2013). From the Editors — Being Scheherazade: The
  Importance of Storytelling in Academic Writing. *Academy of Management Journal*,
  56(3), 629–634. [verified]**
  Scholars have "two jobs: answering interesting questions and telling the story."
  Three tools: the *human face*, *motion and pacing*, *titles*.
  → Directly motivates `textbook-pedagogical` and the concreteness/"human face" dial
  for a management textbook audience.

- **Czarniawska, B. (e.g. *Narrating the Organization*, 1997; *Narratives in Social
  Science Research*, 2004). [classic]** Narrative as a legitimate mode in organisation
  studies. → The user's own field sanctions narrative scholarship.

- **Academy of Management Discoveries — "Discoveries through Prose". [verified]**
  A management journal that formally values narrative prose over dry IMRAD.
  → Evidence that target venues in the field reward narrative register.

---

## 6. Reader impact & deployment (who benefits from the narrative lift)

Who a narrative lift helps depends on the reader's prior knowledge and reading skill —
which is why preset choice is an audience decision (see `style_presets.md`, "Preset
choice and reader expertise").

- **Kalyuga, S. (2007). Expertise Reversal Effect and Its Implications for
  Learner-Tailored Instruction. *Educational Psychology Review*, 19, 509–539; with
  Kalyuga, Ayres, Chandler & Sweller (2003), *Educational Psychologist*, 38(1). [verified]**
  Instructional support essential for novices becomes redundant or detrimental for
  experts. → Lighter presets for expert-only venues.
- **McNamara & Kintsch (1996); O'Reilly & McNamara (2007), *Discourse Processes*; and
  prior-knowledge × cohesion work on science texts. [verified]** High-cohesion text
  helps low-knowledge readers; high-knowledge readers can learn more from lower-cohesion
  text via generative inference — the *reverse cohesion effect* — moderated by reading
  skill. → Default to cohesion for textbook/mixed/L2 audiences; do not over-narrativise
  for experts.
- **Nominalisation & L2/EAP reading (Fang, Schleppegrell & Cox, 2006; Hyland & Tse,
  2007; complex-noun-phrase parsing studies). [verified]** Lexical density raises
  reading difficulty most for novices and second-language readers. → The nominalisation
  dial has its largest payoff for L2/novice audiences.

## 7. Reading motivation & engagement (wanting to read — and enjoy — the book)

Comprehension is not the only goal; whether the reader *wants* to read — and warms to
the book — is a distinct, empirically separable axis. (This mirrors the companion
`academic-danish-klarsprog` skill, so both languages share one reading-motivation axis
and one evidence base.)

- **Hidi & Renninger (2006), four-phase model of interest development.** [verified]
  Interest grows from *triggered situational interest* (via novel, concrete, surprising,
  relevant material) -> *maintained situational* -> *emerging individual* ->
  *well-developed individual* interest. -> Dial **reading motivation**: relevant
  concreteness, a human face and well-placed surprise trigger interest without lowering
  rigour.
- **Guthrie, Hoa, Wigfield, Tonks & Perencevich (2006), *Reading Research Quarterly*
  (doi:10.1002/rrq.81).** [verified] Situational reading interest feeds engagement and
  longer-term reading motivation and comprehension.
- **Hidi & Baird (1988).** [verified] Text-based interest increases recall of expository
  text.
- **Caution -- seductive details (Mayer coherence principle).** [classic] Eye-catching
  but irrelevant detail can *harm* learning; motivation devices must be relevant and
  content-bearing.

## How the evidence maps to the dials (summary)

| Dial | Primary source(s) | Direction for "more narrative" |
|---|---|---|
| Nominalisation density | Halliday & Martin; Biber & Gray; Sword ↔ Hyland (trade-off) | lower (moderately) |
| Agent visibility / active verbs | Sword | higher |
| Sentence-rhythm variance | Sword; general style research | higher variance |
| Information structure (topic/stress) | Gopen & Swan | tightened |
| Metadiscourse / engagement | Hyland | higher (esp. pedagogical) |
| Hedging / stance | Hyland; Martin & White | calibrated to venue |
| Concreteness / human face | Sword; Pollock & Bono | higher |
| Reading motivation / situational interest | Hidi & Renninger; Guthrie et al.; Hidi & Baird | higher via *relevant* concreteness/narrative -- never seductive details |
| Narrativity arc (macro) | Boyd/Pennebaker; MDPI 2023 | mild for textbooks |
| Metaphor tolerance | Sword | low default; higher only in trade-crossover |

## Built-in cautions (from the evidence)

1. **Venue/genre confound (Hillier):** more narrative ≠ universally better — respect
   disciplinary norm.
2. **Nominalisation defended (Hyland):** do not strip nominalisation reflexively.
3. **Accuracy over story (Dahlstrom):** never trade precision for narrativity.
4. **Historical contingency (Atkinson; Hyland & Jiang):** register is a moving target;
   the author's chosen preset, not a fixed ideal, governs.
5. **Reading motivation is relevance-bound (Hidi & Baird; Mayer):** raise interest via
   *relevant* concreteness and narrative; avoid seductive details that harm learning.

## Source links (as gathered at build time; verify before quoting)

- Hillier, Kelly & Klinger (2016), PLOS ONE — https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0167983
- Pollock & Bono (2013), AMJ — https://journals.aom.org/doi/10.5465/amj.2013.4003
- Narrativity in biomedical abstracts (2023), Publications/MDPI — https://www.mdpi.com/2304-6775/11/2/26
- Sword, Stylish Academic Writing (HUP) — https://www.hup.harvard.edu/file/feeds/PDF/9780674064485_sample.pdf
- Hidi & Renninger (2006), four-phase model of interest — https://www.academia.edu/27911093/The_Four_Phase_Model_of_Interest_Development
- Guthrie et al. (2006), situational interest & engagement, RRQ — doi:10.1002/rrq.81
- Hidi & Baird (1988), text-based interest & recall of expository text
- Jiang & Hyland, Academic Naming — https://journals.sagepub.com/doi/10.1177/00754242211019080
- Metadiscourse systematic review — https://www.sciencedirect.com/science/article/pii/S0024384123000852
- AMD "Discoveries through Prose" — https://www.aom.org/publications/journals/publishing-with-aom/author-and-reviewer-resources/author-resources/submitting-to-discoveries/amd-discoveries-through-prose/
