# Dimension D — Discourse and power reflexivity (v1.1 addendum)

## Status and safety valves (read BEFORE use)

Dimension D differs in principle from S/H/T/M/F: it assesses the text's *reflexivity about
power, positionality and framing* — not the text's positions. Precisely because that
distinction is hard for an LLM judge (the risk: scoring politics instead of quality), four
hard valves apply:

1. **OPT-IN per run.** D runs only when the user explicitly asks for it. The default is OFF,
   and the report always states whether D was included or not.
2. **FLAG mode is the default.** D is reported as structured findings WITHOUT a score.
   Scored mode (0–4 per criterion) requires the user's explicit request and then enters
   with a weight of at most 0.05 (renormalise the other weights).
3. **Confidence cap: medium** — as for H1/H2. Discourse findings are disciplined judgment,
   not measurement.
4. **Position neutrality:** A text may take ANY position and reach the top level, provided
   the position is declared, alternatives are acknowledged, and the framing is marked. The
   judge must NEVER reward or punish the position itself. Findings are phrased as "the text
   does not mark X" — never as "the text ought to hold Y".

**Rationale for inclusion (documented design history):** The dimension was absent from v1.0
even though discourse/power was the most productive finding class in the cross-model review
the skill was formalised from (lowest score; prompted substantial development of the work).
The omission was undocumented. v1.1 adopts the dimension with the valves above rather than
leaving the instrument blind to its own most value-creating finding class. Evidential
caveat: the D criteria have weaker psychometric grounding than the S/T criteria (critical
discourse analysis is an interpretive tradition, not a measurement standard — Fairclough
1992; framing evidence: Thibodeau & Boroditsky 2013; Entman 1993); this must be stated in
the method box of every D run.

*Terminology note (sister-skill port):* This rubric is a translation of the Danish
`rubrik_D_diskurs.md`, adapted — not mirrored verbatim — to established English usage:
*positionality* (declared standpoint), *definitional authority*, *voice and absence*,
*framing*.

## Criteria (observable anchors — score only what you can point to)

**D1 Declared positionality**
- 0: The text advances contested judgments with no marking of its own standpoint or interest.
- 2: The standpoint is marked in places (e.g. in methods or limitations sections), but not
  where the contested judgments are actually advanced.
- 4: At every contested judgment, the text's position and any self-interest are declared in
  or near the passage; the reader can always see who is speaking and what the speaker's
  interest is.

**D2 Definitional authority**
- 0: The text's load-bearing categories ("quality", "integrity", "readiness" or similar)
  are treated as given; who defined them is never thematised.
- 2: The origin of some categories is stated; other central categories remain unmarked.
- 4: The text states who defines the load-bearing categories, and marks where definitional
  authority is contested or rests with the text itself.

**D3 Voice and absence**
- 0: Parties affected by the text's argument appear neither with a voice nor as a marked
  absence.
- 2: The most important parties are represented or mentioned, but at least one affected
  party is absent without marking.
- 4: Affected parties are represented, OR their absence is explicitly marked with a reason
  ("X's perspective is not included because …").

**D4 Framing of contested matters** *(extends M4 beyond metaphors)*
- 0: Value-laden word choices (not only metaphors) frame contested matters without marking,
  and the text never shifts perspective.
- 2: The framing is reasonable for the genre but unreflected; some unmarked loaded choices.
- 4: On contested matters the text shows framing awareness: it chooses, marks or
  counterbalances its wording, possibly with an explicit shift of perspective.

## Reporting (flag mode, default)

Per criterion: 1–3 verbatim quotes with location, one analysis (what is marked/unmarked),
and any flag phrased as an *observation plus a question to the author* — never as a
prescription of position. D findings enter "Prioritised flags" on equal footing but are
tagged [D] and do not count in the score. Add to the method box: "Dimension D run in flag
mode (unscored); D criteria have weaker evidential grounding than S/T; confidence cap
medium; position neutrality required."
