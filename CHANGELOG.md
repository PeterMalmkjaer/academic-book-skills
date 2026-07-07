# Changelog

All notable changes to the `academic-book-skills` repo are documented here.
Format loosely follows [Keep a Changelog].

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
