# Changelog

All notable changes to the `academic-book-skills` repo are documented here.
Format loosely follows [Keep a Changelog].

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
