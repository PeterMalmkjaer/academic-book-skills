---
name: academic-english-narrative
description: >-
  Register and narrative-voice editing for English-language academic manuscripts
  (textbooks, monographs, chapters). Use when the user wants to LIFT the prose toward
  a chosen target register — "narrative academic English", "make it flow", "more
  readable / less stilted", "European textbook voice", "less staccato", "vary the
  rhythm", "reduce nominalisation / zombie nouns". Works through selectable STYLE
  PRESETS (voice profiles) calibrated against measurable features (nominalisation
  density, agent visibility, sentence-rhythm variance, information structure,
  metadiscourse and hedging, narrativity). OPT-IN / explicit. It rewrites BODY PROSE
  only and NEVER alters meaning, theory, concepts, citations, cross-references,
  numbers, or any box/quotation/figure wording. NOT for spelling/terminology/format
  consistency (that is the companion academic-english-consistency skill); NOT for
  translation.
license: MIT
metadata:
  family: academic-english
  siblings: academic-english-consistency
  version: 0.1.1
  evidence_base: references/research_basis.md
---

# Academic English — Narrative (register & voice lift)

The *elevation* half of the `academic-english` family. Where
`academic-english-consistency` enforces ONE mechanical house-style (flag, don't
change), this skill **rewrites body prose** to reach a chosen **target register** —
the "narrative academic English" lift, the 82%→~90% prose work.

Two design facts make this skill safe and serious:

1. **It is register-selectable, not opinion-driven.** Register is a *choice*, so the
   skill exposes named **style presets**, each defined as settings on measurable
   linguistic dials drawn from the research literature (see "Evidence base" below and
   `references/research_basis.md`). The author picks the target; the skill aims at it.
2. **It rewrites prose but never content.** The same protected-content discipline as
   the sibling applies in full: theory, concepts, citations, cross-references,
   numbers, defined-term names, and all box/quote/figure wording are preserved
   exactly (`references/protected_content.md`).

---

## Design considerations & evidence base (read me)

This skill is grounded in published research rather than personal taste. The full,
cited account with confidence ratings is in `references/research_basis.md`; the
headline considerations it builds on are:

- **Narrativity is measurable and it correlates with uptake — with a caveat.**
  Hillier, Kelly & Klinger (2016, *PLOS ONE*) found more-narrative abstracts are
  cited more, but the effect is confounded with journal identity. Lesson: aim for
  *appropriate* narrativity for the venue, not maximum narrativity.
- **The semantic lever is grammatical metaphor / nominalisation** (Halliday & Martin;
  Biber & Gray). Un-packing some nominalisations into agents + active verbs is what
  makes prose more narrative. **But nominalisation is not simply bad** (Hyland & Jiang
  defend "metadiscursive nouns" as interactive and authority-building). Lesson: treat
  nominalisation as a *tunable trade-off*, never strip it blindly.
- **The pragmatic lever is reader-orientation** — metadiscourse, stance and
  engagement (Hyland), and reader-expectation structure such as topic/stress position
  (Gopen & Swan, 1990). Narrative voice largely lives here.
- **Register is historically contingent**, not a fixed law (Atkinson; Hyland & Jiang),
  which is exactly why presets — not a single "correct" style — are the right design.
- **In management/organisation studies the field invites narrative** (Pollock & Bono,
  2013, *AMJ*, "Being Scheherazade"; Czarniawska; AMD "Discoveries through Prose").
- **Narrativity must never cost accuracy** (Dahlstrom, 2014, *PNAS*). Precision wins
  over story, always.
- **Reading motivation is its own lever.** Situational/text-based interest (Hidi &
  Renninger 2006; Guthrie et al. 2006) makes readers *want* to read and warm to the
  book; realised through *relevant* concreteness and narrative — never seductive
  details (Mayer). Mirrors the Danish klarsprog sibling so both languages share one
  reading-motivation axis.

These considerations are deliberately visible in the skill so that any reader — or
reviewer, if the skill is published — can see *why* it does what it does.

---

## The hard rules (inherited, non-negotiable)

1. **Source is read-only.** Propose rewrites; never silently overwrite the author's
   files. Deliver before/after so changes are reviewable and reversible.
2. **Content & reference fidelity is absolute.** A rewrite preserves the propositional
   content exactly: no claim added, dropped, strengthened, or weakened. Every
   citation, author, year, DOI, `(Section x.y)`, number, and defined-term name is
   byte-identical. Box, quotation, and figure wording is never rewritten
   (`references/protected_content.md`).
3. **Respect disciplinary norm and the chosen preset.** Do not over-narrativise past
   the target. When a sentence's precision and its "flow" conflict, precision wins.
4. **Flag judgement calls.** Where a rewrite risks shifting nuance, present it as an
   option with the original, and explain the trade-off. Confidence H/M/L on each.

If a project decision log / skopos brief exists, it wins over preset defaults.

---

## Style presets (voice profiles)

Full definitions and dial settings in `references/style_presets.md`. Summary:

| Preset | Use for | Character |
|---|---|---|
| `narrative-academic-european` *(default)* | textbook/monograph body prose | flowing, varied rhythm, low-moderate nominalisation, restrained dashes; OUP/CUP register (~90% target) |
| `textbook-pedagogical` | intro chapters, student-facing sections | warmer, more signposting and reader address, more concrete examples / "human face" |
| `journal-formal` | article extracts, abstracts | tighter, higher nominalisation tolerance, low reader-address, calibrated hedging |
| `trade-crossover` | prefaces, epilogues, popular summaries | vivid, high narrativity and concreteness, metaphor allowed — **caution: can cost disciplinary precision; use sparingly** |

**One default preset per book.** Element-type variation (e.g. cases more concrete,
theory sections more formal) is allowed but must be declared and logged, so the book
does not feel disjointed.

---

## Workflow

### Phase 0 — Intake, preset selection, log open
- Confirm the manuscript folder/files and the **target preset** (default
  `narrative-academic-european`). Confirm scope (which chapters/sections).
- Open `RUN_LOG.md` from `references/run_log_template.md`: timestamp, files + hashes,
  preset chosen, skill version, any decision log used.
- Optionally run `scripts/measure.py` to record baseline metrics (nominalisation
  density, sentence-length variance, hedging density, dash counts, etc.). Log the
  command and output.

### Phase 1 — Diagnose against the preset
For each section, identify where the prose departs from the target preset's dial
settings (e.g. fragment chains, dash pile-ups, high nominalisation, flat rhythm).
Produce a short per-chapter diagnosis tied to the dials — not vibes.

### Phase 2 — Propose rewrites (before/after)
Rewrite body prose toward the preset. Deliver every change as:

`location | before | after | dial(s) addressed | confidence | note`

Never touch protected content. Keep each rewrite minimal — change texture, not
meaning.

### Phase 3 — Meaning-fidelity self-check  *(before delivering)*
For every rewrite assert:
- propositional content is unchanged (no claim added/removed/re-weighted);
- all citations, refs, numbers, defined-term names are byte-identical;
- nothing inside protected content was rewritten.
Drop any rewrite that fails (return the original) and log the reason. State:
`Fidelity check passed: N rewrites, 0 claims altered, 0 protected tokens changed.`

### Phase 4 — Optional re-measure & consistency hand-off
Re-run `measure.py` to show movement toward the preset. Because rewriting can
reintroduce spelling/format drift, recommend running `academic-english-consistency`
afterwards (or note that the two should be sequenced: narrative lift → consistency
clean-up).

---

## The run log (error traceability)

`RUN_LOG.md` (template in `references/`) is the audit trail. Per run it records the
header + file hashes, the chosen preset, baseline and post metrics, every rewrite
with dials + confidence, the meaning-fidelity result, and every rewrite dropped with
reason. Rule: **no prose change ships without a corresponding log line**, so any
later objection is traceable to the exact rewrite, preset, and run.

---

## Deterministic helper: `scripts/measure.py`

Read-only register/narrativity metrics to make presets measurable rather than
subjective: sentence-length mean/variance, nominalisation-suffix density, hedging and
metadiscourse density, first-person presence, em/en-dash counts. It reports numbers
and (optionally) flags where a file sits relative to a preset's indicative ranges. It
never edits source files and never decides — it informs the diagnosis.

```bash
python scripts/measure.py --input <folder-or-glob> --preset narrative-academic-european \
    --out metrics.md --log RUN_LOG.md
```

---

## When NOT to use

- Spelling / terminology / citation-format consistency → `academic-english-consistency`.
- Changing meaning, theory, argument, data, or any scholarly content.
- Translation.

## Files

- `references/research_basis.md` — the cited evidence base (confidence-rated).
- `references/style_presets.md` — preset definitions + measurable dial settings.
- `references/protected_content.md` — fidelity zone (content/theory/citations).
- `references/run_log_template.md` — audit-trail format → `RUN_LOG.md`.
- `scripts/measure.py` — read-only register/narrativity metrics.
