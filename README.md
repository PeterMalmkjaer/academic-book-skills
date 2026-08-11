# academic-book-skills

Book-production **and** editing/audit skills for writing, structuring, quality-assuring and
typesetting academic textbooks and monographs in LaTeX. The repo carries both the
**form/production** skills and — as a publication snapshot accompanying the article
*Writing a Scholarly Book with AI* — the full editing/audit **skill chain** the article
documents (text audits, register lifts, consistency audits, AI-tell and engagement audits,
and the DA→EN translation workflow). The content-editing families are developed in
[`academic-english-skills`](https://github.com/PeterMalmkjaer/academic-english-skills) and
[`academic-danish-skills`](https://github.com/PeterMalmkjaer/academic-danish-skills); the copies
here are the versions used and cited in the article.

## Please read before you install

**This is an experiment, shared as-is.** These skills were built for one real book project and
are published in case they are useful to someone else — not as a finished product. There is no
warranty of any kind, no support, and **no liability whatsoever** for anything produced with
them, including errors in a manuscript, a citation, a build, or a published book.

**Responsibility sits with whoever runs the skill — entirely.** Every obligation attaching to
your work stays yours: research integrity, your institution's rules on AI use, your publishing
contract and its disclosure policy, copyright clearance, GDPR, library licence terms,
examination rules, and the accuracy of every fact and citation. The developer of these skills
carries none of it, has no duty of care towards your manuscript, no reviewing or supervisory
role, and gives no assurance about your work. Running a skill is never evidence that you have
complied with anything. Machine-assisted checking is not verification, and the absence of a flag
is not evidence that nothing is wrong. See
[TERMS.md §6](./TERMS.md#6-responsibility-rests-entirely-with-the-user-of-the-skill) for the detail.

**Written for CBS, usable beyond it.** These skills were built in a Copenhagen Business School
context and are recommended primarily for **academics at CBS**, who will have the library access
the verification workflow assumes. They are published openly because the method is not
CBS-specific — see the note on institutional access below.

**Full terms are in [`TERMS.md`](./TERMS.md)** — the licence, what is *not* licensed, the
warranty and liability disclaimers, your responsibility as the user, and the confidentiality and
publisher-terms cautions around sending manuscript text to third-party services. This summary is
a summary only; `TERMS.md` governs. Read it before using these on anything you intend to publish
or submit.

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
| `akademisk-tekstaudit` | DA | Evidensbaseret kvalitetsaudit af danske akademiske tekster — 5 dimensioner, BARS-forankret 0–4-rubrik, konfidensbånd og tekstbelæg pr. score. Måler og flager; omskriver aldrig. |
| `academic-english-text-audit` | EN | Evidence-based quality audit of English academic prose — 5 dimensions, anchored 0–4 rubric, confidence bands and verbatim evidence per score. Measures and flags; never rewrites. |
| `academic-translation-da-en` | DA→EN | Craft-level workflow for translating Danish academic books into English: decision log, termbase/anchor sign-off, per-section workflow, citation fidelity as a hard rule. |
| `academic-danish-klarsprog` | DA | Register- og klarsprogsløft for danske akademiske manuskripter via valgbare stilprofiler (LIX, nominal/verbalstil, anglicismer, sætningsrytme). Rører aldrig mening, tal eller citater. |
| `academic-danish-consistency` | DA | Bogdækkende dansk house-style-konsistensaudit: udleder stilark og termbase fra kapitlerne og flager afvigelser — omskriver aldrig stiltiende. |
| `academic-english-narrative` | EN | Register and narrative-voice editing for English academic manuscripts through selectable style presets calibrated against measurable features. Body prose only; never alters meaning, citations or numbers. |
| `academic-english-consistency` | EN | Book-wide English house-style consistency audit: derives a style sheet and termbase from the chapters and flags deviations — never silently rewrites. |
| `academic-danish-ai-tell-audit` | DA | Måler tætheden af LLM-stilmarkører i dansk akademisk prosa og anbefaler reduktioner, der respekterer tekstens egen stemme. Måler og flager — omskriver aldrig; ikke en AI-detektor. |
| `academic-english-ai-tell-audit` | EN | Measures the density of LLM-overused style markers in English academic prose and recommends reductions that respect the text's own voice. Measures and flags — never rewrites; not an AI detector. |
| `academic-danish-engagement-audit` | DA | Rapportérbar læse-engagement-score for dansk akademisk prosa med registerbevidste anbefalinger. Måler kun; ingen dekorative virkemidler (seductive details skader læring). |
| `academic-english-engagement-audit` | EN | Reportable reading-engagement score for English academic prose with register-aware recommendations. Measures only; no decorative 'interest' (seductive details harm learning). |

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

**Before running the DOI/metadata scripts**, set your own e-mail address — Crossref's polite pool
uses it to identify who is calling, so it must be yours:

```
export CROSSREF_MAILTO='you@example.org'
```

The scripts stop with an explanatory message rather than run without it. Nothing else is
required, and nothing leaves your machine except read-only lookups to Crossref — see
[TERMS.md §7](./TERMS.md#7-where-your-material-goes--and-where-it-does-not).

## Updating

Bump the `version` in the relevant `<skill>/.claude-plugin/plugin.json`, commit and push, then
`claude plugin marketplace update academic-book-skills` (or click **Update** on the marketplace in Cowork).

## Terms

Full terms — licence, what is *not* licensed, warranty and liability disclaimers, your
responsibility as the user, and how your material is handled — are in **[`TERMS.md`](./TERMS.md)**.
The summary at the top of this README is a summary only; `TERMS.md` governs.

## Citation

If you use or adapt these skills, please cite — see [`CITATION.cff`](./CITATION.cff).
