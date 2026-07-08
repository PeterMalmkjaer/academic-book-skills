---
name: academic-book
description: Helps write, structure, and produce an academic textbook or monograph in the social sciences — especially in LaTeX. Use this skill when the user mentions a book project, textbook, monograph, chapter structure, LaTeX compilation, reference management, concept register, preface, copyright, front matter, print quality, or translation of an academic book. Also use when the user mentions AI-assisted academic writing, terminological key, red thread in a book, chapter template, or numbering system for boxes and cases.
---

# Academic Book — Templates and Best Practices

A skill for supporting all phases of writing an academic textbook or monograph.
Developed and tested on the PM-book (Performance Management, CBS, 2026) — 369 pages, 17 chapters, LaTeX.

> **Beta note:** These templates are distilled from one concrete book project. They are offered as practical starting points, not universal rules. Adapt to your context, discipline, and tools.

---

## Pipeline ordering — typography/cover run LAST (critical)

This skill covers **LaTeX build, typography, overfull/pagination, floats and cover** —
the **form phase** of a book. Form depends on the final text flow, so run these steps
**only after the text is frozen**:

```
A. Content & correctness  (translation → facts/citations → cross-references → register/narrative → grammar)
B. Consistency            (spelling/house-style)
   ▶▶▶  TEXT FREEZE  ◀◀◀
C. Form & layout — THIS skill:  numbering/float continuity → typography/overfull → cover
D. Final build            (real build: pages, 0 undefined, overfull count, visual check)
```

**Iron rule:** never run overfull-triage or cover insertion before content, register and
consistency are locked. Any later word-count change reflows the book and invalidates a prior
typography pass — re-run typography + build. (Learned the hard way on a live textbook where
typography was run before the grammar/citation pass; the verification went stale and a late
layout bug slipped through.)

---

## The 12 Templates

Three levels: **Strategic** (decide before chapter 1), **Ongoing** (maintain throughout), **Reflective** (conscious choices).

---

### STRATEGIC TEMPLATES (decide BEFORE chapter 1)

**Template 1 — Define the book's dual identity**
Clarify whether the book is a monograph (one progressive argument), a textbook (didactic progression), or deliberately both. Write ½ page answering:
- Who is the primary reader, and what should they be able to do after reading the book?
- What is the book's overall argument — the one that cannot be reduced to a single chapter?
- Is this primarily a textbook, a monograph, or deliberately both?

Return to this document halfway through the project.

**Template 2 — Build a terminological key from day one**
Spreadsheet with columns: `Concept | Definition | Primary source (author, year) | Foreign language equivalent | Chapters`
Update at each new central concept. Use as a checklist during proofreading.
*Critical for translation:* "incitamentsintensitet" (Danish) = "incentive intensity" in Lazear & Gibbs — not "incentive strength" or "reward intensity".

> **Term glosses & parentheticals** — when a term is followed by another term in parentheses
> (`agency theory (principal-agent theory)`), classify before touching it: redundant self-gloss →
> delete; genuine synonym → keep + italicise (gloss once, at first use); false calque (a
> source-language equivalent that is not an established term in the target language, e.g. "the
> Pawl Effect" for *the ratchet effect*) → delete; missing synonym/abbreviation → add — but only
> after verifying the alternative name is real in the literature (never invent one), and keeping
> related-but-distinct terms distinct (*target ratcheting* the practice vs *the ratchet effect* the
> consequence). Full decision tree, style basis and worked examples:
> [`references/gloss_and_parenthesis_convention.md`](references/gloss_and_parenthesis_convention.md).

**Template 3 — Clarify reference strategy and verify as you go — not at the end**
For each chapter: mini reference document with `Reference | Verified (yes/no/partial) | Specific use in text`
Verify before moving to the next chapter. 15–30 min per chapter. Saves hours at final proofreading.
*Source types:* peer-reviewed (free citation) / published working paper (free citation) / HBS cases (commercially licensed — avoid reproduction).

**Template 4 — Design the chapter template as a formal contract with the reader**
One-page document at project start: which fixed elements each chapter contains.
*PM-book template:* learning goals → perspective box → body text (definition boxes + theory boxes) → summary → perspective section → discussion questions.
Deviations from the template require a conscious decision — not a forgotten obligation.

**Template 5 — Establish the red thread as an explicit document**
For each chapter write one sentence:
> *"This chapter presupposes [X] from chapter [N] and introduces [Y] which is used in chapter [M]."*

If the sentence cannot be written, the chapter's placement is probably wrong.
Collect all sentences in one document — this is the book's internal architecture.

---

### ONGOING TEMPLATES (maintain consistently)

**Template 6 — Use AI as a structural partner — not as author**
Write a ½-page AI policy at project start:
- What AI is used for: structuring, formulating drafts, numbering checks
- What AI is NOT used for: academic judgement, originality of argument, deciding whether an analysis is correct
- How AI use is documented (e.g., in preface or genesis section)

Revise the policy halfway through — experience will have changed practice.

**Template 7 — Build a numbering system early and enforce it globally**
Spreadsheet with one tab per element type: `Chapter | No. | Title | Line in file`
Update at each new element (case, definition box, theory box, figure, table).
*Consequence of poor discipline:* retrospective correction of 48 cases and 52 theory boxes across 17 chapters.

**Template 8 — Handle copyright actively and document as you go**
Add a column to the reference document: `Source type (peer-reviewed / working paper / HBS case / annual report)`
Flag all commercially licensed cases explicitly at the point of insertion.
Decide strategy from the start: avoid / write own case / obtain permission.

**Template 9 — Plan print quality from compilation 1 — not compilation 25 (LaTeX)**
After every 3 chapters: run a full compilation and resolve all overfull hbox warnings > 20pt.
Keep a log: `Problem | Chapter | Status (open/resolved/accepted) | Reason if accepted`
*Concrete fixes:* soft hyphens (`\-`) in long compound words, `\texorpdfstring` for maths in section titles, column widths in longtable, `\chapter[short]{long}` for long titles.

> **Print-ready PDF:** compiling cleanly is not the same as print-ready. For trim size, image
> dpi, font embedding, PDF/X vs PDF/A, CMYK, bleed and tagging, see
> [`references/prepress_pdf_checklist.md`](references/prepress_pdf_checklist.md). Settle trim
> size BEFORE the final typography pass — a trim change reflows the whole book.

**Template 10 — Concept register as a living document**
For each new element (definition, theory box, case, figure): add to register IMMEDIATELY. 30 seconds per element.
*Consequence of waiting:* retrospective addition of 83 definitions and 52 theory boxes requires reviewing all chapters.

---

### REFLECTIVE TEMPLATES (conscious choices)

**Template 11 — Write front matter last — but plan it first**
Write a placeholder preface at start: who is the reader / what is the argument / my background.
Write the final version LAST. Expect the final version to share little with the placeholder.
*Elements that can only be written retrospectively:* the book's dual character, reflection on AI use, precision about the author's background.

**Template 12 — Central documentation file updated at every session**
One file with three sections:
1. **Current status:** version number, page count, latest output, next steps
2. **Open items:** prioritised list, what is accepted and why
3. **Chronological log:** date, what was done, decisions made (not just actions)

---

## LaTeX-Specific Recommendations

### Document class and structure
```latex
\documentclass[11pt,a4paper,twoside,openright]{book}
\usepackage{fontspec}
\usepackage{polyglossia}
\setdefaultlanguage{danish}  % or relevant language
```

`openright` = chapters always start on a right-hand (odd) page → 18 blank left-hand pages in a 17-chapter book is correct and normal for professional printing.

### Box environments (tcolorbox)
```latex
\newtcolorbox{definitionbox}[1][]{ ... }
\newtcolorbox{theorybox}[1][]{ ... }
\newtcolorbox{casebox}[1][]{ ... }
\newtcolorbox{perspectivebox}[1][]{ ... }
```

### Common print-fix issues
| Problem | Fix |
|---------|-----|
| Long chapter title overflows header | `\chapter[Short version]{Full long title}` |
| Mathematical symbol in PDF bookmark | `\texorpdfstring{$\beta$}{beta}` |
| Long compound words (e.g. German/Danish) | Soft hyphens: `med\-ar\-bej\-der\-til\-freds\-heds\-må\-lin\-gen` |
| Narrow table column | Adjust `p{2.2cm}` → `p{3.5cm}` in longtable |
| Line break in body text | Rewrite to shorter sentences — `\\` does not work in body text |

### Table column alignment — prefer ragged-right in narrow/multi-column tables

Narrow, multi-column tables set with **justified** `p{}`/`X` columns look bunched: justification
stretches short cell text to the right edge, so the last word of one column hugs the next column
(they read as "merged"), and it forces rivers, heavy hyphenation, and overfull `\hbox`es. Fix —
make text columns **ragged-right** by prefixing each with `>{\raggedright\arraybackslash}`
(`\arraybackslash` restores `\\` inside `p{}`; needs the `array` package, which `tabularx` loads):

```latex
% before: \begin{tabular}{p{2.5cm}p{3.5cm}p{3.7cm}}
% after:
\begin{tabular}{>{\raggedright\arraybackslash}p{2.5cm}%
                >{\raggedright\arraybackslash}p{3.5cm}%
                >{\raggedright\arraybackslash}p{3.7cm}}
% tabularx X column:  {l >{\raggedright\arraybackslash}X}
```

Make ragged-right the house default for reference/overview tables and apply it consistently
across chapters *and* appendices. On a live 400-page textbook this removed **all** overfull
boxes (19 → 0) with zero content change — the justification was itself the source of the overflow.

### Build command
```bash
xelatex -interaction=nonstopmode main.tex
# Check log:
grep -E "Overfull|^!" main.log
```

---

## Reference Management — Verification Levels

| Level | Label | Requirement |
|-------|-------|-------------|
| T1 | Content verified | Read and verified against primary source |
| T2 | Metadata only | Title/author/year verified, content not checked |

Goal: all references at T1 before delivery to printer.

---

## Translation Strategy (source language → English)

Recommended stylistic reference: CBS working papers (Friis, Boe & Hansen 2023 / Hansen 2019).
This is the Continental European management accounting style — explanatory, structured, proposition-driven.
*Not* the compressed AER/JPE style.

Target audience for English version: European academics with English as 2nd/3rd language.
Requirement: terminological precision + grammatical correctness. Native feel is not critical.

Terminological key (examples):
| Danish | English (correct field term) |
|--------|------------------------------|
| Incitamentsintensitet | Incentive intensity (β) |
| Ratchet-effekt | Ratchet effect |
| Crowding out | Motivation crowding-out |
| Moral hazard | Moral hazard |
| Præstationsbaseret løn | Pay for performance |
| Selvselektionseffekt | Self-selection |
| Informationsprincippet | Holmström's informativeness principle |
| Organisatorisk retfærdighed | Organizational justice |

---

## Copyright — Quick Reference

| Source type | Use | Requires |
|-------------|-----|----------|
| Peer-reviewed article | Free citation with reference | Correct attribution |
| Published working paper | Free citation with reference | Correct attribution |
| HBS cases | Commercially licensed | Avoid reproduction — write own cases |
| Figures from books | Restricted | Permission for commercial publication |
| Theoretical concepts | Free | Concepts are not copyrightable |

Working papers are published documents — they can and should be cited with correct attribution.
In Danish (and most European) academia, copyright belongs to the authors, not the institution.

---

## Priority Checklist at Project Start

- [ ] Write the book identity document (Template 1)
- [ ] Create terminological key spreadsheet (Template 2)
- [ ] Create numbering system spreadsheet (Template 7)
- [ ] Write chapter template (Template 4)
- [ ] Write red thread for all planned chapters (Template 5)
- [ ] Write AI policy (Template 6)
- [ ] Create MASTER_TODO file with the three sections (Template 12)
- [ ] Write placeholder preface (Template 11)

---

## The Single Most Important Template

**Template 3 (verify references as you go)** is the most important.
It takes 15 min per chapter — and grows to many hours of work if postponed.

**Template 5 (the red thread)** is what distinguishes a collection of essays from a book.
