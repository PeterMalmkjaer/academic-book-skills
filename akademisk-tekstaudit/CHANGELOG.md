# Changelog — akademisk-tekstaudit

## 1.5 (2026-08-17)
- **Kildevariations-regel for case-fakta** (Grænser) — flag aldrig et virkeligheds-casefaktum
  som "fejl", alene fordi ét sekundærværk angiver andre tal; tjek samtidige primær-/pressekilder
  og formulér fundet som "kilder varierer — verificér". Tilføjet efter at PM-bogens kvalitetsgate
  gav et falsk positiv på Enrons 20/70/10-fordeling.
  (Flettet hertil fra academic-book-skills@5687513.)

## 1.4 (2026-08-07)
- Nyt **Trin 2d: AI-indsættelses-tjek** — målrettet stikprøve af netop AI-indsatte/omskrevne
  passager for naboafsnits-ekko, metafor-rester fra AI-registeret og manglende idiomatisk
  hjemmel. Flag-mode. Udledt af sprogtesten i artikel-casen (7 fund i én frisk passage).
- **Genreprofil "tidsskriftartikel (empirisk)": metodeblok** (kalibrering.md) — fem tjekpunkter
  (søgedokumentation, operationalisering, design-eksplicitering, selvvaliderings-afgrænsning,
  restfejls-dækning) + S4-skærpelser (generaliserings-scope, institutionel præcision). Udledt
  af gap-analyse af 30 eksterne reviewfund: 6 reelle gaps lå samlet i metodisk efterprøvelighed.
- **Batteri-anbefaling** (ny sektion): ai-tell-audit + engagement-audit + frit kryds-model-
  review som dokumenteret komplementært batteri; handoff kan anbefale påstandstabellen
  publiceret i selve teksten. Grundlag: 5 af 30 eksterne fund dækkedes af søster-skills,
  der ikke var kørt.

## 1.3 (2026-08-05)
- Nyt **Trin 2c: Terminologisk forankring** — tjek af (a) egenudviklede termer, der dækker
  fænomener med etablerede fagtermer (brug termen eller forankr egenbegrebet eksplicit), og
  (b) oplagte, men fraværende ankertermer, som en fagfællebedømmer ville forvente. Flag-mode,
  ingen selvstændig score; kalibreringsregel mod jargon-inflation.
- Designhistorik udvidet med v1.3-begrundelsen: begge fundklasser blev fundet af et frit
  gennemsyn, EFTER at to fulde rubrik-kørsler havde overset dem — fravær af noget forventeligt
  kræver et trin, der eksplicit spørger til fraværet.

## 1.2 (2026-08-05)
- Nyt **Trin 2b: Intern fakta-konsistens** — deterministisk fejning FØR beregning: tal mod tal
  (samme referent, forskellige tal), ord mod faktum (kvalitative tids-/mængdeord mod tekstens
  egne datoer og optællinger), løfte mod leverance i tal (overskrifters tællinger mod det
  leverede). Fund → produktionsfund/S2-belæg; ingen selvstændig score.
- Designhistorik udvidet med v1.2-begrundelsen: to blinde kørsler overså en ord-mod-faktum-fejl,
  som et frit kryds-model-review fandt — rubrik-opmærksomhed er systematisk blind uden for
  rubrikken; deterministiske tjek skal dække resten.

## 1.1 (2026-08-04)
- Ny valgfri **Dimension D: diskurs- og magtrefleksivitet** (D1 deklareret ståsted, D2 definitionsmagt,
  D3 stemme og fravær, D4 framing) — `references/rubrik_D_diskurs.md`.
- Fire sikkerhedsventiler: opt-in pr. kørsel (default FRA); flag-tilstand uden score som default
  (scoret tilstand kræver eksplicit anmodning, vægt ≤ 0,05); konfidens-loft middel; positionsneutralitet
  (fund = observation + spørgsmål, aldrig holdningsanvisning).
- Ny sektion "Designhistorik" i SKILL.md: dimensionsvalg skal fremover begrundes dér.
- Metodeboks udvidet med D-forbehold (svagere evidensforankring end S/T).

## 1.0 (2026-07-22)
- Første version: femdimensionsaudit (S semantik, H hermeneutik, T teknisk, M metafor, F tabeller/figurer),
  19 kriterier med BARS-forankringer, to-parameter-kalibrering (genreprofil + niveau-baseline),
  analysér-før-scor-workflow, konfidensbånd, halo-/stabilitetstjek, fast rapportskabelon.
