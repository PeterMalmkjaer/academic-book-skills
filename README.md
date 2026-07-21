# academic-book-skills

Book-production skills for writing, structuring and typesetting academic textbooks and
monographs in LaTeX — the **form / production** side of a book project. Companion to the
content-editing families [`academic-english-skills`](https://github.com/PeterMalmkjaer/academic-english-skills)
and [`academic-danish-skills`](https://github.com/PeterMalmkjaer/academic-danish-skills).

## Please read before you install

**This is an experiment, shared as-is.** These skills were built for one real book project and
are published in case they are useful to someone else — not as a finished product. There is no
warranty of any kind, no support, and **no liability whatsoever** for anything produced with
them, including errors in a manuscript, a citation, a build, or a published book. You are
responsible for checking every output. Nothing here removes the author's own responsibility for
their work. Machine-assisted checking is not verification, and the absence of a flag is not
evidence that nothing is wrong.

**Written for CBS, usable beyond it.** These skills were built in a Copenhagen Business School
context and are recommended primarily for **academics at CBS**, who will have the library access
the verification workflow assumes. They are published openly because the method is not
CBS-specific — see the note on institutional access below.

**Full terms:** [Copyright, licence, warranty and liability](#copyright-licence-warranty-and-liability)
sets out the licence, what is *not* licensed, the warranty and liability disclaimers, your
responsibility as author, and the confidentiality and publisher-terms cautions around sending
manuscript text to third-party services. Read it before using these on anything you intend to
publish or submit.

**Institutional library access.** `academic-source-verification` verifies whether a source
actually supports the claim made about it, which means reading the source full text. It is
written around `cbs-libsearch`, a full-text/annotation backend tied to a **Copenhagen Business
School login**, which you will not have.

This does not make the skill unusable elsewhere — the full-text step is one backend among
several, and the skill also drives scite, Elicit and open web/Exa lookups, which need no
institutional login. Most universities provide equivalent online library access (EZproxy,
OpenAthens, Shibboleth, or a publisher-federated login). If you have that, substitute your own
library's full-text route where the skill says `cbs-libsearch`; the method, the ledger format
and the three checks are unchanged. If you have no institutional access at all, the metadata
and retraction checks still work — the claim-fidelity check will fall back to whatever full
text is openly available.

**`pm-bog` is not for you.** It is a project baseline for one specific textbook and is opt-in by
name. It is in this repo for reproducibility, not reuse.

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

This repo is a **Claude plugin marketplace**. Add it once, then install the skills you want.

**Claude Code (CLI):**

```
claude plugin marketplace add PeterMalmkjaer/academic-book-skills
claude plugin install pm-konsistens-audit@academic-book-skills
# other skills: academic-book, faglig-bog, academic-source-verification, pm-bog
```

**Cowork:** Customize → Plugins → **Add marketplace** → `PeterMalmkjaer/academic-book-skills`,
then install the individual skills.

You can also run a script directly without installing, e.g.
`python3 pm-konsistens-audit/scripts/audit_all.py --help`.

## Updating

Bump the `version` in the relevant `<skill>/.claude-plugin/plugin.json`, commit and push, then
`claude plugin marketplace update academic-book-skills` (or click **Update** on the marketplace in Cowork).

## Copyright, licence, warranty and liability

Please read this section in full before using these skills on a manuscript intended for
publication or assessment. It expands on the summary at the top of this README.

### 1. Licence

The **code and documentation in this repository** are released under the MIT Licence — see
[`LICENSE`](./LICENSE). Copyright © 2026 Peter Malmkjær.

The MIT Licence grants broad permission to use, copy, modify, merge, publish, distribute,
sublicense and sell copies, subject to including the copyright notice and licence text. It also
contains the warranty and liability disclaimers reproduced and expanded below. Where anything in
this README appears to conflict with `LICENSE`, the text of `LICENSE` governs the licence grant
itself.

### 2. Scope of the copyright claim, and institutional rights

The copyright notice covers the author's own contribution: the skill instructions, prompts,
scripts, templates and documentation in this repository.

The material was developed by the author in the course of academic work at Copenhagen Business
School. **The allocation of rights between the author and the institution has not been formally
settled.** Depending on Danish law, CBS policy and any applicable employment or collective
agreement, an institution may hold rights in works created by an employee in the course of
employment. Nothing in this repository is intended to assert rights beyond those the author
actually holds, to prejudice any institutional claim, or to waive any institutional right. If
and to the extent that CBS or any other party holds rights in any part of this material, that
allocation prevails over the notice above, and this repository will be corrected accordingly.

Users who intend to rely on the licence commercially, or to redistribute the material, should
be aware of this open question and are advised to seek their own confirmation first.

### 3. What is *not* licensed

The MIT grant covers this repository only. It expressly does **not** extend to:

- **The textbook, monograph or manuscript the skills were developed on**, including its text,
  structure, figures, tables, boxes, cases and pedagogical apparatus. `pm-bog` documents a
  workflow and a set of baseline facts for reproducibility; it conveys no rights in the book.
- **Third-party works** referenced, quoted, cited or verified using these skills. Copyright in
  sources remains with their rightsholders. Nothing here grants permission to reproduce,
  redistribute or store third-party full texts.
- **Names and trademarks** of third parties. Copenhagen Business School, scite, Elicit, Exa,
  Crossref, LaTeX, Anthropic and Claude are the property of their respective owners. This
  repository is an independent, personal project. It is **not affiliated with, endorsed by,
  sponsored by, or an official product of** Copenhagen Business School or any other named
  organisation, and must not be presented as such.

### 4. No warranty

The material is provided **"as is" and "as available", without warranty of any kind**, express,
implied or statutory. This includes, without limitation, any implied warranty of
merchantability, fitness for a particular purpose, title, accuracy, completeness, currency,
reliability, or non-infringement.

In particular, and without limiting the generality of the above, there is **no warranty that**:

- the skills will detect any given error, inconsistency, dangling cross-reference, numbering
  fault, phantom or orphan reference in a manuscript;
- a citation reported as verified is in fact correct, or that the source genuinely supports the
  claim made about it;
- a retracted, withdrawn, corrected or otherwise unreliable source will be identified as such;
- metadata retrieved from any external service is accurate or current;
- the audit ledger is complete, correct, or adequate as evidence for any purpose;
- any output satisfies the requirements of a publisher, funder, employer, examination board,
  research-integrity body or legal obligation;
- the skills will function at all, function without interruption, or continue to function as
  external services, models, tools or file formats change.

The skills operate in part through large language models and third-party services. Such systems
can produce output that is confidently stated and wrong, can miss what they were asked to find,
and can behave differently on identical input. **Absence of a flag is not evidence of absence of
a problem.**

### 5. Limitation of liability

To the maximum extent permitted by applicable law, the author shall **not be liable for any
claim, damages, loss or other liability**, whether in an action of contract, tort (including
negligence), warranty or otherwise, arising from, out of, or in connection with the material or
its use, including without limitation:

- errors, omissions, inaccuracies or fabrications in any manuscript, citation, reference list,
  bibliography, audit ledger, declaration, figure, table or build output;
- an incorrect, incomplete, misattributed, retracted or fabricated source surviving into a
  published work;
- consequences of publication, including corrections, errata, retraction, withdrawal, rejection,
  loss of funding, contractual or reputational harm, or allegations concerning research
  integrity, plagiarism or misconduct;
- consequences of assessment, examination or peer review;
- loss or corruption of data, manuscripts, repositories or work product;
- costs of re-verification, re-typesetting, reprinting or re-publication;
- any indirect, incidental, special, consequential, punitive or exemplary damages, and any loss
  of profit, revenue, time, goodwill or opportunity, whether or not foreseeable and whether or
  not the author has been advised of the possibility.

Nothing in this section excludes or limits liability that cannot lawfully be excluded or limited.

### 6. Your responsibility as author

**These skills do not verify anything on your behalf, and using them does not discharge any duty
you owe.** The author of a manuscript remains solely and fully responsible for its content,
including every factual claim, quotation, citation, reference and permission.

Specifically:

- Machine-assisted checking **is not verification**. Every result — flagged or unflagged — must
  be confirmed by a human against the actual source.
- The audit ledger documents **what was done**, not what is true. It is a record of process, and
  is only as good as the human sign-off recorded in it.
- The derived AI/source declaration is a **template based on your own entries**. You are
  responsible for its accuracy and for its adequacy under your publisher's, institution's or
  funder's policy on AI use.
- These skills are **not** legal, publishing, contractual, research-integrity or professional
  advice, and are no substitute for peer review, professional proofreading, a publisher's own
  processes, or your institution's rules.

### 7. Third-party services, data and confidentiality

Running these skills may transmit parts of your manuscript, your queries, source metadata and
excerpts to third-party services — including model providers and literature or web services such
as scite, Elicit, Crossref and Exa — each governed by its own terms and privacy policy, over
which the author has no control and for which the author accepts no responsibility.

Before use, consider that:

- **unpublished manuscripts, peer-review material, embargoed content, work under a publishing
  contract or non-disclosure agreement, personal data, and confidential or sensitive research
  data** may be inappropriate or unlawful to transmit to external services;
- your institution's information-security, data-protection and GDPR obligations apply to you,
  not to this repository;
- access to licensed full text through an institutional login is governed by **your library's
  licence agreements with publishers**. Automated, bulk or systematic downloading commonly
  breaches those terms and can result in access being suspended for you or for your entire
  institution. Use full-text access manually and within the terms you are bound by.

You are responsible for determining what you may lawfully and permissibly send, and to where.

### 8. Intended audience and support

The material was written for the author's own book project in a Copenhagen Business School
context, and is **recommended primarily for academics at CBS**, who will have the institutional
library access the source-verification workflow assumes. It is published openly because the
method is not CBS-specific: colleagues at other institutions with equivalent online library
access (EZproxy, OpenAthens, Shibboleth, or publisher-federated login) can substitute their own
route and use it unchanged. This is a description of the intended audience, not a restriction on
use.

There is **no support, no service level, and no maintenance commitment**. The repository is a
by-product of an ongoing book project. Skills may change substantially, be renamed, or be
withdrawn at any time without notice, and no backward compatibility is promised. Issues and pull
requests may go unanswered.

### 9. Feedback

Bug reports and improvements are welcome via GitHub issues, but see the previous paragraph: no
response is guaranteed. Please do not include confidential or unpublished manuscript material in
an issue.

## Citation

If you use or adapt these skills, please cite — see [`CITATION.cff`](./CITATION.cff).
