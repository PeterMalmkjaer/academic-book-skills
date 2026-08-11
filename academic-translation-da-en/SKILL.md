---
name: academic-translation-da-en
description: >-
  Craft-level support for translating Danish academic books (textbooks and
  monographs) into English. OPT-IN ONLY — invoke only when the user explicitly
  asks for it (e.g. "use academic-translation-da-en", "brug oversættelses-skill").
  Use when translating a Danish social-science / management / economics textbook
  or monograph into English: register calibration, concept/termbase handling,
  per-section workflow, LaTeX integration (tcolorbox boxes, citations, TikZ),
  and reference fidelity. NOT a general-purpose or literary translation tool;
  NOT for short texts, marketing copy, or non-academic prose.
---

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

## Files in this skill

- `02_style_register.md` — register direction, hedging, voice, false-friends
  starter list, spelling, quotes, numbers/dates.
- `04_per_section_workflow.md` — the order of operations per chapter, with the
  per-section cross-check.
- `06_latex_integration.md` — tcolorbox boxes, box-title comma trap, preamble for
  English, TikZ labels, build discipline.
- `07_reference_fidelity.md` — the citation-preservation rules and the
  cross-check method, plus RAG-verification of attributed theory.

*Lean core, v0.1, drafted 2026-06-08 from the PM-textbook project. Grow with
`03_termbase_methodology`, `05_false_friends_register`, `08_rag_verification`,
`09_success_rating`, `10_source_observations`, `11_quality_bar`,
`12_lessons_learned` as later chapters surface the need.*
