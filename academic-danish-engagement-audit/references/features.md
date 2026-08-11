# Scored features (Danish) — v0.1.0  [adaptation — calibrate]

Only the Human-Interest *logic* is validated (English coefficients); the Danish number is a
relative adaptation. Proxies are directional.

## 1. Human-Interest-style (adapted Flesch)
`HI = 3.635 * (personal_words/100 words) + 0.314 * (personal_sentences/100 sentences)`
- **Personal words** (Danish): jeg, mig, min, mit, mine, vi, os, vores, du, dig, din, dit,
  dine, I, jer, jeres, han, ham, hans, hun, hende, hendes, de, dem, deres, man, sig; plus
  person-nouns: folk, mennesker, menneske, mand, kvinde, barn, børn, mor, far, læser, ...
- **Personal sentences**: quoted, questions (?), exclamations (!), or direct address ("du").
- Report as a **relative** index; do not read Flesch's English bands literally.

## 2. Concreteness proxy (Sadoski) — per 1,000 words
"for eksempel", "f.eks.", "såsom", "forestil dig", "tænk på", "eksempel", "case",
"tilfælde", "historie", "scenarie", "antag", "betragt".

## 3. Reader-engagement proxy (Schraw & Lehman) — per 1,000 words
Questions ("?"); direct address (du, dig, din, vi, os, vores, læser, læseren).

## 4. Narrativity proxy (Dahlstrom; Hidi) — per 1,000 words
Temporal/event markers: så, da, når, efter, før, pludselig, først, dernæst, til sidst,
senere, imens, efterhånden.

## Overall band (advisory)
Derived mainly from the HI-style number + concreteness, read in the light of genre. Never
optimise a single number; never raise interest with irrelevant detail (seductive details).
