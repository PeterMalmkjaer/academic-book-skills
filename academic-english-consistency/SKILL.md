---
name: academic-english-consistency
description: >-
  Book-wide English house-style CONSISTENCY audit for academic manuscripts
  (textbooks, monographs, multi-chapter works). Use when the user wants to enforce
  ONE consistent English style across a whole book or manuscript — spelling system
  (-ise/-ize, -isation/-ization, -our/-or), terminology/concept rendering, citation
  and cross-reference format, heading/box formatting — by DERIVING a house style
  sheet and termbase from the existing chapters and then FLAGGING deviations (never
  silently rewriting). Triggers: "consistency pass", "house style", "style sheet",
  "make the whole book consistent", "spelling/terminology/format consistency across
  the book", "audit my manuscript for consistency". OPT-IN / explicit — does NOT
  auto-run on single-document edits. NOT for improving flow, rhythm, voice or
  narrative register (that is the companion academic-english-narrative skill); NOT
  for changing meaning, theory, citations or any scholarly content; NOT for
  translation.
license: MIT
metadata:
  family: academic-english
  siblings: academic-english-narrative (planned)
  version: 0.1.0
---

# Academic English — Consistency (house-style audit)

A standalone, **discipline-agnostic** skill that runs a single, repeatable
**consistency pass** over a whole English-language academic manuscript. It is the
*enforcement* half of a two-skill family:

- **`academic-english-consistency`** (this skill) — mechanics: spelling system,
  terminology, citation/cross-reference format, box/heading formatting. Rule-based,
  deterministic, book-wide. **Flags, never silently rewrites.**
- **`academic-english-narrative`** (planned sibling) — register: flow, rhythm,
  em-dash discipline, idiom, the "narrative academic English" lift. Judgement-based,
  chapter-by-chapter. *Do not do narrative work in this skill.*

Keeping the two separate is deliberate: consistency is mechanical and safe to run
across an entire book; narrative editing is interpretive and must be reviewed per
chapter. This skill must never drift into the sibling's territory.

---

## The four hard rules (non-negotiable)

1. **Source is read-only.** Never edit, delete, or rewrite the author's files.
   Output is observations, a style sheet, a termbase, per-chapter reports, and a run
   log — nothing else.
2. **Reference & content fidelity is absolute.** No citation, author name, year,
   DOI, defined-term name, section/chapter cross-reference, quotation, box source,
   figure label, or number is ever altered or proposed for alteration. If a style
   rule would touch any of these, **skip it and log it as `verify (protected)`**.
3. **Default-trust the source.** A proofread edition is usually right. When
   something looks inconsistent, assume pedagogical intent until there is strong
   evidence. Frame flags as *observations to verify*, not *bugs*. (Observed
   false-positive rate on live academic projects: ~1 in 3.)
4. **Flag, don't change. When in doubt, leave unchanged.** Every proposal carries a
   location, current text, proposed text, the rule, and a confidence (H/M/L). Never
   propose below High confidence — anything lower becomes a `verify` item.

If a project decision log or skopos brief exists, **it wins** over this skill's
defaults. Read it first.

---

## Protected content — format-checked only, wording never touched

See `references/protected_content.md` for the full list and detection heuristics.
In short, the following are inspected **only** for formatting consistency (label
style, numbering, title-line punctuation) and their **wording is never changed**:

- Definitions, Theory/Perspective/Case/Summary boxes
- Figure & table captions and in-figure labels
- Direct quotations and epigraphs
- Citations, author names, years, DOIs, "Further Reading" entries
- Cross-references and section/chapter numbers
- Defined-term names themselves (only their bold-on-first-use *format* is checked)

---

## Workflow

Run the phases in order. **Stop after Phase 1 for sign-off** — the canonical choices
determine what later counts as a deviation, so the author must approve them first.

### Phase 0 — Intake & log open
- Identify the manuscript folder and file type (`.tex` preferred; `.md`/`.txt`/PDF
  text accepted). Confirm scope (which chapters).
- Open a run log from `references/run_log_template.md` → `RUN_LOG.md` in the output
  folder. Record: timestamp, files in scope, file hashes (for traceability), skill
  version, and any project decision-log found.
- Optionally run `scripts/scan.py` to gather deterministic counts (see below). Log
  the exact command and its output path.

### Phase 1 — Derive the style sheet  *(then STOP for sign-off)*
Scan every chapter and infer the **dominant** convention for each item in
`references/checkable_items.md`. Where the book is split, report the split **with
counts** and recommend ONE canonical choice. Produce `MASTER_STYLE_SHEET.md` from
`references/style_sheet_template.md`. Do not proceed until the author signs off.

### Phase 2 — Build the termbase
List every recurring concept/term and the surface forms it appears in across
chapters (e.g. "algorithmic performance management / algorithmic PM / people
analytics"). Mark the canonical form; flag deviations. Same for author-name
spellings and acronyms. Never propose merging forms that live inside protected
content. Produce `TERMBASE.md`.

### Phase 3 — Per-chapter violation report
For each chapter, output a table:

`file | location | current | proposed | rule | confidence | in_protected?(Y/N)`

Only list deviations from the signed-off style sheet and termbase, **in body prose**.
Any deviation inside protected content is reported as `verify (protected)` with **no
proposed change**. Group by rule; end each chapter with counts per category. Append
every row to the run log.

### Phase 4 — Fidelity self-check  *(before delivering each report)*
For every proposed change, verify and assert:
- it touches ONLY the targeted spelling/format token;
- all citations, author names, years, `(Section x.y)` refs, numbers, and
  defined-term names are byte-identical between `current` and `proposed`;
- no proposal falls inside protected content.

Drop any item that fails (move it to `verify`) and log the failure with reason.
State explicitly in the report and log:
`Fidelity check passed: N proposals, 0 protected tokens altered.`

---

## The run log (error traceability)

Every run writes/append-updates `RUN_LOG.md` (template in `references/`). It is the
audit trail that makes any later error traceable to the exact rule and run that
produced it. It records, in order:

1. **Run header** — timestamp, skill version, operator request verbatim, files in
   scope + content hashes.
2. **Inputs** — project decision log / skopos brief used (if any); `scan.py` command
   and output.
3. **Phase 1 decisions** — every canonical choice, the split counts behind it, and
   the author's sign-off timestamp.
4. **Flags** — every proposed change and every `verify` item, with rule + confidence.
5. **Fidelity check** — pass/fail line per chapter; every dropped proposal with
   reason.
6. **Skips** — anything not checked and why (e.g. protected content, low confidence).

Rule: **nothing changes the source without a corresponding log line.** If a later
review finds a wrong flag, the log shows which rule, which run, and which confidence
produced it — so the rule can be corrected once and re-run.

---

## Deterministic helper: `scripts/scan.py`

Mechanical, read-only counter for the objective checks (spelling-system tallies,
cross-reference format regexes, `&` vs `and` in citations, straight vs curly quotes,
dash usage, double spaces). It produces counts and line-located hits to seed Phase 1
and Phase 3 — but it is an **aid, not the authority**: the LLM still confirms
protected-content status and judgement calls. Usage:

```bash
python scripts/scan.py --input <folder-or-glob> --out <report.md> --log <RUN_LOG.md>
```

The script never writes to source files.

---

## When NOT to use

- Improving flow, rhythm, voice, or narrative register → use the planned
  `academic-english-narrative` sibling.
- Single-document copy-edits where book-wide consistency is not the point.
- Changing meaning, theory, argument, or any scholarly content.
- Translation (use a translation skill).

## Files

- `references/checkable_items.md` — the rule catalogue (what Phase 1 decides).
- `references/style_sheet_template.md` — the decision template → `MASTER_STYLE_SHEET.md`.
- `references/protected_content.md` — the never-touch zone + detection heuristics.
- `references/run_log_template.md` — the audit-trail format → `RUN_LOG.md`.
- `scripts/scan.py` — deterministic mechanical checks (read-only).
