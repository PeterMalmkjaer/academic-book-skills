# Changelog

All notable changes to the `academic-book-skills` repo are documented here.
Format loosely follows [Keep a Changelog].

## [0.7.3] — 2026-07-11

### Documented
- `pm-konsistens-audit` (`audit_all.py`): added an inline rationale above `LABELMAP` recording WHY
  `Case`, `Example` and `Eksempel` all map to one `Case/Eksempel` category. **Case = a real-world
  situation; Example/Eksempel = a constructed/hypothetical illustration** — two deliberate labels that
  deliberately share one casebox counter per chapter. They must NOT be merged in the manuscript or
  concept register (the naming carries meaning), but for numbering they are one continuous series. This
  prevents a future maintainer from "simplifying" the dual labels or the shared-counter mapping. No code
  behaviour change.

## [0.7.2] — 2026-07-10

### Fixed
- `pm-konsistens-audit` (`audit_all.py`): the numbering audit now covers **two-word box labels** —
  "Theory Box X.Y" and "Perspective Box X.Y". The box regex previously captured only a single word
  before the number, so English two-word labels were read as "Box", mapped to nothing, and the Theory
  Box and Perspective Box series were silently NOT validated (only Definition and Case/Example were).
  Widened the label capture to an optional second word and mapped `'Theory Box'→Teoriboks`,
  `'Perspective Box'→Perspektivboks` (plus their cross-reference patterns). Verified on the live EN
  textbook: all six categories (Definition, Theory Box, Perspective Box, Case/Example, Figure, Table)
  are now validated and consecutive; audit clean. Independent manual check confirmed both series run
  1..n in every chapter.

## [0.7.1] — 2026-07-10

### Fixed
- `pm-konsistens-audit` (`audit_all.py`): the Case numbering series now recognises the **English label
  "Example"** (previously only Danish `Case`/`Eksempel` were mapped). Books that use one shared casebox
  series with mixed "Case X.Y" and "Example X.Y" titles were false-flagged as having numbering gaps —
  e.g. a chapter with Example 5.1 + Case 5.2–5.4 was read as Case [2,3,4] and reported as "missing 1".
  Added `'Example'` to `LABELMAP` and to the Case cross-reference pattern. Verified on the live EN
  textbook: **4 false-positive numbering flags → 0** (audit now fully clean). No manuscript change — the
  book's numbering was already correct; renumbering would have broken the valid sequence.

## [0.7.0] — 2026-07-10

### Added
- `pm-konsistens-audit`: **kapitel-skabelon-konsistens-tjek (sektion 4)** i `audit_all.py`. Udleder den
  MODALE åbningsstruktur fra flertallet af kapitler (`\chapter` → `\chaprule` → epigraf → "Hvad dette
  kapitel handler om"-boks → læringsmål → første `\section`) og **flager kapitler der bryder rækkefølgen**
  (relativ rækkefølge, ikke linjenumre → epigraf-eller-ej giver ikke falske positiver), **manglende
  påkrævede landemærker** (H/L påkrævet hvis ≥50 % har dem), og **afvigende læringsmål-indledning**
  (modal frase udledes; review). Harde flag = rækkefølge + manglende. Baggrund: PM-bogen — en læser fandt
  at kap16/17 åbnede med læringsmål FØR "Hvad dette kapitel handler om" (de 15 øvrige omvendt) + brugte en
  anden indlednings-frase; sektion 4 reproducerer begge fund deterministisk (bevist mod før/efter-versioner).
  Numre-/reference-tjek ser ikke denne fejlklasse.

## [0.6.1] — 2026-07-10

### Fixed
- `academic-source-verification`: **`ledger_build.py`s in-text-scanner var svag** — den fangede kun den
  parentetiske form `(Forfatter, år)`, ikke den narrative `Forfatter (år)` (den dominerende i
  tekstuelle-reference-bøger). På PM-bogen betød det 22 fundne citationer og 196 "forældreløse" (falsk).
  Porteret `pm-konsistens-audit/audit_all.py`s robuste logik: begge citationsformer, deaccent (ö→o, é→e),
  genitiv-'s-fjernelse, og matchning mod ALLE forfatter-efternavne (ikke kun første). Resultat på PM-bogen:
  311 citationer, 32 reelle forældreløse. Phantom-detektion opdelt i **"efternavn slet ikke i bib" (høj
  signal)** vs **"år-mismatch" (co-forf.-støj)** — så de to søster-skills nu er enige om citations-modellen.

## [0.6.0] — 2026-07-10

### Added
- `pm-konsistens-audit`: **reference-integritets-tjek (prosa ↔ references.bib)** — implementerer
  det hidtil dokumenterede-men-manglende "fantom-/forældreløs"-kontraktpunkt som
  `academic-source-verification` allerede henviste til. `scripts/audit_all.py` får en `--bib`-parameter
  og en ny **sektion 3** med fire kategorier: **A** prosa-citation uden matchende bib-nøgle (delt i
  "efternavn slet ikke i bib" = høj signal vs. "år-mismatch" = co-forf.-støj), **B** orphan-nøgler,
  **C** dublet-poster (samme DOI, eller samme titel + samme år — forskellige udgaver springes over),
  **D** nøglenavn-år ≠ `year`-felt. Kun **C+D tæller som harde flag**; A+B er review-kandidater der ikke
  fælder "RENT ✓". Prosaen deaccentes (ö→o, é→e) + genitiv-'s fjernes før navne-udtræk for at dæmpe
  falske positiver. Gælder bøger med **tekstuelle** referencer + `\nocite{*}` (ikke `\cite`), hvor en
  numre-/float-audit pr. konstruktion ikke kan fange en citation der peger på en ikke-eksisterende nøgle.
  SKILL.md får en "Reference-integritet"-sektion med **P1/P2/P3-triage** (læser-synlige fejl → integritet →
  kosmetisk) og forbehold. Baggrund: PM-bogen (2026-07) — fandt 12 manglende referencer, 4 dublet-poster
  og flere skjulte prosa/år-fejl som de øvrige tjek ikke så.

### Fixed
- `pm-konsistens-audit`: SKILL.md "Filer" listede forkerte parametre (`--register`, `--appendix` findes ikke
  i `audit_all.py`); rettet til de faktiske: `--src`, `--aux`, `--bib`, `--out`.

### Changed
- `academic-source-verification`: krydsreference til søster-skillen præciseret — fantom-/forældreløs-detektionen
  er nu faktisk implementeret (`audit_all.py --bib`, sektion 3) og dækker desuden dublet + nøgle/år.

## [0.5.0] — 2026-07-08

### Added
- `faglig-bog` (Danish sibling of `academic-book`): **mirrored the two 0.4.0 layout additions into
  Danish** so the sibling skills do not drift apart. SKILL.md gains a Danish "Tabel-kolonnejustering
  — foretræk ragged-right" section (same ragged-right rule + the honest note that it fixes in-column
  overflow but does NOT zero a book's overfull count), and a new `faglig-bog/references/
  prepress_pdf_checklist.md` (Danish pre-press checklist: trim, ≥300 dpi, font embedding, PDF/X
  [ISO 15930] / PDF/A [ISO 19005] / PDF/UA [ISO 14289], CMYK, bleed, tagging), with a pointer from
  Skabelon 9. Principle recorded: language-agnostic learnings (layout, pre-press, build) go into
  BOTH `academic-book` and `faglig-bog`.

## [0.4.0] — 2026-07-08

### Added
- `academic-book`: **table column-alignment rule** + **pre-press/PDF-format checklist**.
  SKILL.md gains a "Table column alignment — prefer ragged-right" note (narrow/multi-column
  `p{}`/`X` tables must use `>{\raggedright\arraybackslash}`: justification in narrow columns
  causes rivers, hyphenation, in-column overflow, and makes the last word of a column hug the next
  column so they read as "merged"; fixes the column-level bunching with no content change, but
  note it does NOT zero a book's overfull count — remaining overfull boxes usually sit in wide
  figures/tables/math elsewhere). New `references/prepress_pdf_checklist.md` — a reusable
  pre-press checklist (trim size, image ≥300 dpi, font embedding+subsetting, PDF/X [ISO 15930]
  vs PDF/A [ISO 19005] vs PDF/UA [ISO 14289], CMYK for offset, bleed + crop marks, tagging,
  metadata), with the ordering rule that trim/geometry must be settled BEFORE the final
  typography pass (a trim change reflows the book). Pointer added from Template 9 (print quality).
  Both distilled from a live DA→EN textbook production pass.

## [0.3.0] — 2026-07-08

### Added
- `academic-book`: **term-gloss / parenthetical house-style convention**. New
  `references/gloss_and_parenthesis_convention.md` — a five-category decision tree for the common
  situation where a term is followed by another term in parentheses (frequent as a leftover
  translation artifact): redundant self-gloss → delete; genuine synonym → keep + italicise (gloss
  once, at first use); false calque (source-language equivalent that is not an established
  target-language term, e.g. "the Pawl Effect" for *the ratchet effect*) → delete; missing
  synonym/abbreviation → add; true non-gloss parentheticals → leave. Encodes two error-preventing
  rules: **never invent a synonym** (verify every alternative name via Elicit/Scite/Exa/CrossRef),
  and **precision over label** (keep related-but-distinct terms distinct — *target ratcheting* the
  practice vs *the ratchet effect* the consequence; a rational effect is not a cognitive bias).
  Style basis: APA/Chicago/Turabian (italicise a term at first use) + Farkas (1983). Pointer added
  from SKILL.md (Template 2). Distilled from a live DA→EN textbook pass.

## [0.2.3] — 2026-07-08

### Added
- `academic-source-verification`: **operationalised tjek #3 (claim-support / correct use of source)**.
  Added `scripts/annotate_claims.py` (highlights the claim-supporting passages in a source PDF →
  `*_ANNOTATED.pdf`; reports phrases it cannot find = candidates for "wrong source"),
  `references/annotation_record.md` (the claim → quote → verdict record format), and a "Claim-støtte
  / korrekt brug — arbejdsgang" section in SKILL.md. Encodes the lesson: metadata/DOI being correct
  does NOT prove the manuscript uses the source correctly; if a claim is unsupported, find another
  source — never just fix metadata to "rescue" a wrong source. Skill bumped to 0.1.3.

## [0.2.2] — 2026-07-08

### Added
- `academic-source-verification`: a **reference-integrity module** — three read-only CrossRef
  scripts bundled under `scripts/`: `check_dois.py` (DOI resolution + title match),
  `find_dois.py` (propose the correct DOI for bad ones), and `metadata_check.py` (field-by-field
  verification of author/journal/volume/pages/year). Battle-tested on a live 206-entry
  bibliography: caught 27 bad DOIs (dead/wrong-target) and, after removing a false-positive class,
  2 genuine metadata errors — including entries with fabricated titles/journals and wrong
  volume/pages that a bib-only or title-only check missed. Key lesson encoded: `metadata_check.py`
  must NOT field-compare against a low-confidence title match (DOI-less books/cases), or it emits
  false positives. Skill bumped to 0.1.2.

## [0.2.1] — 2026-07-07

### Added
- `academic-source-verification`: a **presentation convention** for the emitted ledger so the
  regneark is readable, not just correct — front `Læsevejledning` legend sheet (tab index + full
  column/abbreviation legend), styled/frozen/filtered data sheets with tuned widths + wrapping +
  banding, and a back `Fejl fundet & rettet` report sheet. New `references/regneark_layout.md`
  (the spec) and `scripts/ledger_format.py` (deterministic formatter; writes a versioned copy,
  never the master). Added a "Præsentation" section to SKILL.md; skill bumped to 0.1.1.

## [0.2.0] — 2026-07-07

### Added
- New skill **`academic-source-verification`** (DA) — source & citation verification (external
  truth) plus a transparent, reproducible **audit ledger** used as an accountability instrument
  toward publisher and reader. Three checks: (1) reference correctness (CrossRef/DOI/OpenAlex/
  Semantic Scholar), (2) retraction/reliability (Retraction Watch/Crossmark/scite), (3) claim–
  source fidelity (primary source/Elicit/scite/cbs-libsearch annotations). Produces/maintains the
  reference-audit ledger with per-source provenance (methods, evidence, n-sources, retraction
  status, claim support, human sign-off, tool+version, date) and derives the in-book AI/source
  declaration. Includes `references/ledger_schema.md`, `references/declaration_templates.md`, and
  a read-only `scripts/ledger_build.py` (seeds the ledger, extracts in-text cites, flags phantom/
  orphan). Runs at the text-freeze boundary; companion to `pm-konsistens-audit` (internal
  consistency). Prompted by three citation errors that a bib-only audit could not catch (an inline
  journal misattribution, an appendix table year, and a phantom citation with no bib entry).

## [0.1.0] — 2026-07-07

### Added
- Initial repository. Brought four previously local-only, unpublished skills under version
  control: `academic-book`, `faglig-bog`, `pm-bog`, `pm-konsistens-audit`
  (incl. `pm-konsistens-audit/scripts/audit_all.py`).
- Added a **"Pipeline ordering"** note to every skill: these are form-phase skills
  (typography / overfull / pagination / cover, or numbering/float audit) and must run
  **after the text is frozen** — never before content, register and consistency are locked.
  A later word-count change invalidates a prior typography pass (re-run typography + build).
  Prompted by a live textbook where typography was run before the grammar/citation pass and
  the verification went stale (a late all-black blank back-cover page slipped through).
