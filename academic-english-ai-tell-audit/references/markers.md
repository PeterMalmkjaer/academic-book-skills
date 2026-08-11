# English marker lexicon (versioned) — v0.1.0

Evidence-informed list of LLM-overused style markers (Kobak 2025; Liang 2024; plus
widely reported tells). **These are legitimate words in moderation** — the skill scores
*density/over-use*, never presence. Update this list as models and usage shift; bump the
version and log it.

## Verbs (often inflated / promotional)
delve, delves, delving, delved; underscore(s/d/ing); showcase(s/d), showcasing;
leverage(s/d); harness(es/ed); foster(s/ed); align(s/ed); boast(s/ed); encompass(es/ed);
surpass(es/ed); unlock(s/ed); illuminate(s/d); garner(s/ed); spearhead(s/ed);
navigate(s/d) [figurative]

## Adjectives / adverbs
crucial, pivotal, intricate, meticulous, commendable, comprehensive, notable, notably,
robust, seamless, seamlessly, nuanced, multifaceted, invaluable, paramount, versatile,
innovative, cutting-edge, holistic, ever-evolving, additionally, moreover, furthermore

## Nouns / abstractions
potential, findings, insights, realm, landscape [abstract], tapestry, testament,
paradigm, synergy, cornerstone, interplay

## Fixed phrases
"a wide range of"; "plays a pivotal/crucial role"; "it is worth noting (that)"; "it is
important to note"; "in the realm of"; "a testament to"; "sheds light on"; "paves the
way (for)"; "in today's ... world"; "the ever-evolving"; "at the forefront of"

## Structural tells (detected by the script)
- **Rule-of-three** padding: "X, Y, and Z" strings of parallel adjectives/nouns.
- **Negative parallelism**: "not only ... but also", "not just ... but".
- **Boilerplate emphasis**: "it is worth noting", "it is important to note",
  sentence-initial "Notably,", "Importantly,".
- **Connective openers**: sentences starting "Moreover", "Furthermore", "Additionally",
  "In particular" (esp. consecutive).
- **Formulaic closers**: "In conclusion,", "In summary,".
- **Em-dash density**: high em-dash counts (a reported LLM texture).

> Note: this list is calibrated to English biomedical/ML findings (Kobak; Liang). For
> other disciplines, treat as a starting point and confirm against a domain baseline.
