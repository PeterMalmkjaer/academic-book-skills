---
name: academic-translation-da-en
description: >-
  Craft-level support for translating Danish academic books (textbooks and
  monographs) into English. OPT-IN ONLY — invoke only when the user explicitly
  asks for it (e.g. "use academic-translation-da-en", "brug oversættelses-skill").
  Use when translating a Danish social-science / management / economics textbook
  or monograph into English: register calibration, concept/termbase handling,
  per-section workflow, LaTeX integration (tcolorbox boxes, citations, TikZ),
  and reference fidelity. Also covers journal-article manuscripts derived from such
  projects (v0.2). NOT a general-purpose or literary translation tool;
  NOT for short texts, marketing copy, or non-academic prose.
metadata:
  version: "0.2"---

# Academic translation: Danish → English (DA▸EN)

This skill packages the craft of translating a Danish academic book into English so
that each new chapter starts from a calibrated register and a fixed, reliable
workflow — instead of re-deriving conventions every session. It encodes
intellectual property accumulated on a live project (a Danish *Performance
Management* textbook, pilot chapter kap03), generalised for reuse.

It is a **companion** to any project-specific files (skopos brief, decision log,
termbase) and to any book-specific build skill — it does not replace them. Where a
project decision log and this skill disagree, **the project decision log wins**.

## When to use

Invoke (opt-in) when the user is translating a **Danish academic textbook or
monograph** into English and wants help with:

- register and voice calibration (textbook genre, formal academic English);
- concept/terminology consistency across chapters (a termbase);
- the per-section translation workflow (anchors first, prose, scaffolding);
- LaTeX integration (pedagogical boxes, citations, figures, build-testing);
- reference fidelity (every citation preserved, Harvard parenthetical).

## When NOT to use

- General-purpose, literary, or creative translation.
- Short texts, slides, emails, marketing/web copy.
- Non-academic or non-Danish source material.
- Any case where the user has not explicitly opted in.

## The four hard rules (carry into every project)

1. **The source master is read-only.** Translate in a working copy. Never edit,
   delete, or propose fixes to the author's source edition. Source observations go
   into a single sanctioned log file (e.g. `TODO_DA_from_EN_translation.md`), using
   the convention: file, line, verbatim text, what is wrong, proposed fix,
   rationale, confidence.
2. **Reference fidelity is non-negotiable.** Every inline citation, every box
   source attribution, every further-reading entry crosses to English unchanged.
   No claim is "smoothed" to drop a citation. See `07_reference_fidelity.md`.
3. **Default-trust the source.** A current, proofread edition is usually right.
   When something looks like an inconsistency, read the actual chapter first and
   assume pedagogical intent until you have strong evidence. Frame any flag as an
   *observation worth verifying*, not a *bug*. (Observed false-positive rate on a
   live project: ~1 in 3.)
4. **Analyse and ask before big steps.** Translate anchors first and get author
   sign-off before the prose pass. Surface judgement calls; offer alternatives;
   prefer the more universal English form when in doubt and let the author elevate.

## How a project runs with this skill

1. Confirm or write a one-page **skopos brief** (target reader, function, register,
   cases policy, citation style, quality bar). Project-specific; keep it with the
   project, not in this skill.
2. Build a **termbase** from the book's concept register (not a glossary): one row
   per concept with proposed EN form, confidence (H/M/L), and tier (T1 core 10–15 /
   T2 standard 30–40 / T3 periphery). Author signs off; Tier-1 forms become
   canonical.
3. Translate chapter by chapter using `04_per_section_workflow.md`.
4. Apply `02_style_register.md` to every sentence, `06_latex_integration.md` to
   every box/figure/build, and `07_reference_fidelity.md` to every citation.
5. **Build-test** each chapter as a standalone (xelatex, 2 passes) before declaring
   it done. Reading does not catch what the compiler catches.
6. Pilot one chapter end-to-end; gate scaling on a **native-EN copyedit** and an
   **audit against 2–3 benchmark textbooks** in the field. Self-rated quality is
   uncalibrated until an external native-EN reader passes a chapter.

## Invariants, abbreviations and mechanical tests (v0.2)

Added from a journal-article translation prepared with this skill's method (August 2026).
These apply to books AND articles; for articles they are mandatory.

1. **Invariant list — register before translating, never translate.** Project-internal
   codes and labels (analysis codes, decision-log numbers, verification levels, version
   numbers, audit-finding IDs) bind the text to its logs, appendices and open data.
   Spelling them out or translating them breaks traceability. Build the list FIRST;
   enforce with a count test (each invariant: same count in source and target).
2. **Abbreviation mapping — one binding table.** Danish micro-abbreviations (jf., fx,
   bl.a., dvs., kap., inkl., evt., ca., s.) get ONE fixed English equivalent each,
   decided before translation; ambiguous ones (bl.a., evt.) are marked for per-instance
   decision and logged. Final test: zero Danish abbreviations in the target text.
   Do NOT rewrite the source to remove abbreviations first — that adds an edit surface;
   the mapping plus the mechanical test is safer.
3. **Mechanical tests per main section, not only at the end:** invariant count; Danish-
   abbreviation grep; number fidelity (decimal comma → decimal point is the ONLY permitted
   change to any number); per-year citation count (source/target diff must be empty);
   acronym first-use (each international acronym spelled out exactly once).
4. **AI prose rhythm on the way across:** when the source is AI-assisted, translation is
   the cheapest place to normalise LLM style markers — reduce em-dash density, normalise
   quotation marks, and flag slogan-register sentences for the author (do not silently
   rewrite). Coordinate with the ai-tell-audit skills rather than duplicating them.
5. **Articles differ from books in scope control:** target text gets its OWN version
   series; journal-format conversion (reference style, anonymisation for review) is
   explicitly OUT of the translation pass — one transformation at a time, each with its
   own verification.

## Files in this skill

- `02_style_register.md` — register direction, hedging, voice, false-friends
  starter list, spelling, quotes, numbers/dates.
- `04_per_section_workflow.md` — the order of operations per chapter, with the
  per-section cross-check.
- `06_latex_integration.md` — tcolorbox boxes, box-title comma trap, preamble for
  English, TikZ labels, build discipline.
- `07_reference_fidelity.md` — the citation-preservation rules and the
  cross-check method, plus RAG-verification of attributed theory.

*Lean core, v0.2 (2026-08-07: invariants/abbreviations/mechanical-tests section added from the article-translation gate work; article manuscripts now in scope). Originally v0.1, drafted 2026-06-08 from the PM-textbook project. Grow with
`03_termbase_methodology`, `05_false_friends_register`, `08_rag_verification`,
`09_success_rating`, `10_source_observations`, `11_quality_bar`,
`12_lessons_learned` as later chapters surface the need.*
