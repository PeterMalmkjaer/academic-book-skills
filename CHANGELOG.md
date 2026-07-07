# Changelog

All notable changes to the `academic-book-skills` repo are documented here.
Format loosely follows [Keep a Changelog].

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
