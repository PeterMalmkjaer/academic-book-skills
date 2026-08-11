# Style presets — voice profiles and their dial settings

A preset is a named bundle of settings on measurable **dials**. The dials are grounded
in `research_basis.md`. Levels are indicative bands, not hard thresholds; `measure.py`
reports where a text currently sits so the diagnosis is evidence-based, not subjective.

## The dials

1. **Nominalisation density** — proportion of nominalised processes (Halliday &
   Martin; measured via suffix proxy in `measure.py`). Lower = more verbal/agentive.
   *Never reduce to zero* (Hyland counterpoint).
2. **Agent visibility / active-verb ratio** — how often a human/agent subject performs
   an active verb vs. passive/abstract subjects (Sword).
3. **Sentence-rhythm variance** — spread of sentence lengths; narrative prose varies,
   avoiding staccato fragment chains and uniform long sentences.
4. **Information structure** — topic/stress positioning, subject–verb proximity
   (Gopen & Swan). Tightening this improves flow with zero content change.
5. **Metadiscourse / engagement** — signposting, reader address, glosses (Hyland).
6. **Hedging / stance** — density and calibration of epistemic markers (Hyland;
   Martin & White), tuned to venue.
7. **Concreteness / human face** — examples, named agents, vignettes (Sword;
   Pollock & Bono).
8. **Narrativity arc (macro)** — section-level staging/progression (Boyd/Pennebaker).
9. **Punctuation texture** — em-dash discipline, comma/parenthesis/subordination mix.
10. **Metaphor / figurative tolerance** — carefully chosen metaphor (Sword).
11. **Reading motivation / situational interest** — relevant concreteness, a human
    face, relevance and well-placed surprise that make the reader *want* to read
    (Hidi & Renninger; Guthrie et al.; Hidi & Baird). Realised jointly through dials
    5, 7 and 8; must be *relevant* — never seductive details (Mayer).

Scale shorthand: **VL / L / M / H / VH** (very low … very high).

---

## Preset: `narrative-academic-european`  *(default)*
Target: flowing OUP/CUP textbook register (the ~90% benchmark; Milgrom & Roberts,
Lazear & Gibbs in feel). The safe default for body prose.

| Dial | Setting |
|---|---|
| Nominalisation density | L–M (reduce, don't strip) |
| Agent visibility | M–H |
| Sentence-rhythm variance | H |
| Information structure | tightened (topic/stress disciplined) |
| Metadiscourse / engagement | M |
| Hedging / stance | M, calibrated |
| Concreteness / human face | M |
| Narrativity arc | L–M (mild) |
| Punctuation texture | tight dash discipline; varied connectives |
| Metaphor tolerance | L |

## Preset: `textbook-pedagogical`
Target: intro chapters, student-facing sections. Warmer, more guided.

| Dial | Setting |
|---|---|
| Nominalisation density | L |
| Agent visibility | H |
| Sentence-rhythm variance | H |
| Information structure | tightened |
| Metadiscourse / engagement | H (more signposting, reader address) |
| Hedging / stance | M |
| Concreteness / human face | H (examples, "human face") |
| Narrativity arc | M |
| Punctuation texture | tight |
| Metaphor tolerance | L–M |

## Preset: `journal-formal`
Target: article extracts, abstracts. Compact, conventional, venue-conservative.

| Dial | Setting |
|---|---|
| Nominalisation density | M–H (tolerated) |
| Agent visibility | L–M |
| Sentence-rhythm variance | M |
| Information structure | tightened |
| Metadiscourse / engagement | L |
| Hedging / stance | M–H, precise |
| Concreteness / human face | L |
| Narrativity arc | L |
| Punctuation texture | tight |
| Metaphor tolerance | VL |

## Preset: `trade-crossover`
Target: prefaces, epilogues, popular summaries. Vivid and story-led.
**Caution (research_basis §2, §3):** can cost disciplinary precision; the
narrativity↔accuracy tension (Dahlstrom) and venue confound (Hillier) apply. Use
sparingly and never for core theoretical exposition.

| Dial | Setting |
|---|---|
| Nominalisation density | VL–L |
| Agent visibility | VH |
| Sentence-rhythm variance | VH |
| Information structure | tightened |
| Metadiscourse / engagement | M–H |
| Hedging / stance | L–M |
| Concreteness / human face | VH |
| Narrativity arc | H |
| Punctuation texture | expressive (dashes allowed for rhetoric) |
| Metaphor tolerance | M–H |

---

## Preset choice and reader expertise (deployment guidance)

Choosing a preset is not only an aesthetic decision — it is an **audience** decision,
and the reading-science literature gives it a clear direction. The benefit of a
narrative lift is **largest for low-prior-knowledge and second-language (L2) readers
and smallest — occasionally slightly negative on deep learning — for domain experts**.
Two findings govern this:

- **Expertise reversal effect** (Kalyuga, 2007; Kalyuga, Ayres, Chandler & Sweller,
  2003): support that helps novices becomes redundant, even detrimental, for experts
  (added working-memory load from redundant guidance).
- **Reverse cohesion effect** (McNamara & Kintsch, 1996; O'Reilly & McNamara, 2007):
  high-cohesion, lower-density prose reduces load for novices, but high-knowledge
  readers can learn *more* from less cohesive text because gaps prompt generative
  inference. Moderated by reading skill — skilled high-knowledge readers still benefit
  from good cohesion.

Practical mapping (full citations in `research_basis.md`):

| Primary audience | Recommended preset | Rationale |
|---|---|---|
| Textbook / mixed / L2 (novice-leaning) | `narrative-academic-european` (default); `textbook-pedagogical` for intros & cases | cohesion + lower density help most; L2 nominalisation is the bottleneck |
| Advanced students / early PhD | `narrative-academic-european` | still benefit from cohesion; schema not yet automatic |
| Expert-only venue (specialist monograph, journal) | lean lighter / `journal-formal`; do **not** over-narrativise | reverse-cohesion: over-cohesion can dampen generative deep learning |

In all cases, **keep boxes, definitions and theory dense and protected** — their
precise nominal terminology serves expert readers regardless of the body preset. This
is deployment guidance, not a functional dial: it informs *which* preset you choose,
not how the skill rewrites.

---

## Application rules

- **One default preset per book.** Element-type overrides (e.g. cases → `textbook-
  pedagogical`, theory boxes left untouched, preface → `trade-crossover`) are allowed
  but must be **declared and logged**, so the book reads as one work.
- **Boxes, definitions, quotations, figures are never rewritten** regardless of preset
  (`protected_content.md`) — only the surrounding narrative prose is in scope.
- **Precision overrides the preset.** If hitting a dial would blur a claim, stop and
  keep the precise original; log it.
- **Sequence with the sibling.** Run narrative first, then `academic-english-
  consistency` to clean any spelling/format drift a rewrite introduced.
