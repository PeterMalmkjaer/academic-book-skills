# Protected content & meaning fidelity — academic-english-narrative

This skill **rewrites body prose**, so its fidelity rule is stricter than a format
audit: it must change *texture* while preserving *meaning and every reference exactly*.

## Absolute rule

A rewrite is valid only if BOTH hold:
1. **Propositional content is identical** — no claim added, removed, strengthened,
   weakened, or re-scoped. Paraphrase may change wording and structure; it may never
   change what is asserted, including hedged force (a "may" stays a "may").
2. **All references are byte-identical** — every citation, author name, year, DOI,
   `(Section x.y)` / `Chapter n` / `Figure/Table n`, every number/statistic/currency,
   and every **defined-term name** appears verbatim in the rewrite.

## Never rewritten at all (wording untouchable)

Only the *surrounding* narrative prose is in scope. The following are left exactly as
written (a rewrite may not enter them):
- Definitions, Theory/Perspective/Case/Summary boxes and any framed element
- Direct quotations and epigraphs
- Figure/table captions, in-figure labels, table cells
- "Further Reading", reference lists, citation strings
- Equations, code/verbatim, math

## Defined terms

The *name* of a defined concept (e.g. *plausible deniability*, *the six R's*,
*organizational truce*) is fixed. Narrative rewriting may improve the sentence around
it but must reproduce the term verbatim and must not redefine, gloss-shift, or rename
it. Coordinate with the termbase from `academic-english-consistency` if present.

## Detection heuristics

Same as the consistency sibling (LaTeX environments, `\cite*`, `\ref*`, quote
environments, floats, math) — see that skill's `protected_content.md`. When uncertain
whether a span is protected, **treat it as protected and do not rewrite it.**

## Phase 3 meaning-fidelity self-check (assert before delivery)

For every proposed rewrite:
- [ ] same claims, same epistemic force (no added/dropped/re-weighted assertion)
- [ ] citations / authors / years / DOIs byte-identical
- [ ] section & figure cross-references byte-identical
- [ ] numbers, statistics, currencies byte-identical
- [ ] defined-term names byte-identical
- [ ] no protected span entered

Any failure → drop the rewrite, restore the original, log the reason. Deliver the
explicit line:
`Fidelity check passed: N rewrites, 0 claims altered, 0 protected tokens changed.`
