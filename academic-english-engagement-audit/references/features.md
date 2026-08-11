# Scored features — v0.1.0

The engagement score combines one validated formula and three evidence-informed proxies.
Only Human Interest is a validated instrument; treat the proxies as directional.

## 1. Human Interest (HI) — validated (Flesch)
`HI = 3.635 * (personal_words / words * 100) + 0.314 * (personal_sentences / sentences * 100)`
- **Personal words**: personal pronouns (I, me, my, we, us, our, you, your, he, she, him,
  her, they, them, their, …), gendered person-nouns and names (approximated by a
  person-noun list: people, folks, man, woman, boy, girl, mother, father, child, …; proper
  names are under-counted — a known proxy limitation), 
- **Personal sentences**: sentences that are quoted, questions (?), exclamations (!),
  direct address (contain "you/your"), or grammatically incomplete (approximated).
- Bands (Flesch): ~30 interesting, 50 very interesting, 80 dramatic. Academic expository
  prose typically scores LOW — this is genre-appropriate, not a defect.

## 2. Concreteness proxy (Sadoski) — per 1,000 words
Example/imagery markers: "for example", "for instance", "e.g.", "such as", "consider",
"imagine", "picture", "take the case of", "example", "case", "story", "scenario".

## 3. Reader-engagement proxy (Schraw & Lehman) — per 1,000 words
Questions ("?"); direct address (you, your, we, our, us, reader); rhetorical hooks.

## 4. Narrativity proxy (Dahlstrom; Hidi) — per 1,000 words
Temporal/event markers (then, when, after, before, during, suddenly, first, next,
finally); simple past-tense event verbs (approximate).

## Overall band (advisory)
Derived mainly from HI and concreteness, read in the light of genre. Never optimise a
single number; and never raise interest with irrelevant detail (seductive-details effect).
