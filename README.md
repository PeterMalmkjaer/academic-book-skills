# academic-book-skills

Book-production skills for writing, structuring and typesetting academic textbooks and
monographs in LaTeX — the **form / production** side of a book project. Companion to the
content-editing families [`academic-english-skills`](https://github.com/PeterMalmkjaer/academic-english-skills)
and [`academic-danish-skills`](https://github.com/PeterMalmkjaer/academic-danish-skills).

## Skills in this repo

| Skill | Language | Purpose |
|---|---|---|
| `academic-book` | EN | Chapter structure, box/case numbering, LaTeX build, front/back matter, cover, print quality — templates and best practices. |
| `faglig-bog` | DA | Danish sibling of `academic-book`: skabeloner og praksis for faglig bog/monografi i LaTeX. |
| `pm-bog` | DA | OPT-IN. Project-specific baseline for the Performance-Management textbook (chapter structure, build, box definitions, workflow). |
| `pm-konsistens-audit` | DA | Numbering / float-continuity / cross-reference audit of a LaTeX book (fortløbende numre; dangling §/Boks/Case/Figur/Tabel-henvisninger; register- og appendiks-konsistens). Includes `scripts/audit_all.py`. |
| `academic-source-verification` | DA | Source & citation verification (external truth) **plus a transparent, reproducible audit ledger** — an accountability instrument for publisher/reader. Three checks: reference correctness, retraction/reliability, claim–source fidelity. Produces/maintains the reference-audit ledger (provenance per source) + derives the in-book AI/source declaration. Companion to `pm-konsistens-audit` (which owns internal consistency + phantom/orphan detection). |

## Pipeline ordering (read this first)

These are **form-phase** skills. They depend on the final text flow, so run them **after the
text is frozen** — never before content, register and consistency are locked:

```
A. Content & correctness  (translation → facts/citations → cross-references → register/narrative → grammar)
B. Consistency            (spelling / house-style; pm-konsistens-audit: numbers, cross-refs, phantom/orphan)
   ▶▶▶  TEXT FREEZE  ◀◀◀
C. Source verification    (academic-source-verification — external truth on the frozen text + declaration)
D. Form & layout          (academic-book/faglig-bog/pm-bog: typography/overfull → cover)
E. Final build            (real build: pages, 0 undefined, overfull count, visual check)
```

`academic-source-verification` runs at the text-freeze boundary: it checks the *final*
restated text against external sources (a late citation edit re-opens verification), and it
consumes phantom/orphan flags from `pm-konsistens-audit`.

**Iron rule:** any word-count change made *after* a typography pass reflows the book and
invalidates it — re-run typography + build. Each SKILL.md carries this note.

*Origin:* this rule was learned on a live textbook (the PM textbook, EN edition) where
typography was run before the grammar/citation pass; the verification went stale and a late
layout bug slipped through.

## Install

Copy or symlink the desired skill folder(s) into your Claude skills directory
(`~/.claude/skills/`), or package as a plugin/marketplace.

## Licence

MIT — see `LICENSE`.
