# Kalibrering: genreprofil + niveau-baseline

To uafhængige parametre fastlægges FØR scoring. Scores er kun sammenlignelige ved identisk
kalibrering (samme profil OG samme baseline). Ved bogdækkende brug: lås baseline på tværs af kapitler.

## Parameter 1: Genreprofil

Profilen bestemmer dimensionsvægte v, aktive dimensioner og tolerance-justeringer.
Kriterievægte w inden for en dimension er lige, medmindre profilen siger andet.
Evidens for opgavespecifikke rubrikker: Jonsson & Svingby (2007).

| Dimension | Lærebogskapitel | Metodekapitel | Efterskrift/forord | Monografikapitel | Tidsskriftartikel |
|---|---|---|---|---|---|
| S Semantisk | 0,25 | 0,35 | 0,20 | 0,25 | 0,30 |
| H Hermeneutisk | 0,20 | 0,10 | 0,35 | 0,30 | 0,25 |
| T Teknisk | 0,20 | 0,25 | 0,20 | 0,20 | 0,25 |
| M Metafor | 0,15 | 0,10 | 0,25 | 0,10 | 0,05 |
| F Tabeller/figurer | 0,20 | 0,20 | — | 0,15 | 0,15 |

**F-reglen (to retninger):**
- Har teksten ingen tabeller/figurer, udgår F, og F-vægten fordeles proportionalt på de
  øvrige dimensioner (renormalisér så Σv = 1).
- Har teksten tabeller/figurer, men profilen ekskluderer F (fx efterskrift/forord),
  AKTIVERES F med vægt 0,10, og de øvrige vægte renormaliseres proportionalt.
  Et efterskrift med en tabel skal have tabellen vurderet — genren fritager ikke apparatet.

Rapportér altid de faktisk anvendte vægte og notér enhver F-aktivering/-deaktivering
i metodeboksen.

**Tolerance-justeringer pr. profil:**
- *Efterskrift/forord:* Personlig stemme og "vi"-tiltale er genrekorrekt — træk ikke ned for det
  under S4/T3. Metafortæthed må være høj; M-kriterierne vurderer kvalitet, ikke antal.
  H1-forventningen skærpes: et efterskrift, der kun opsummerer, er en 0–1 på H1.
- *Metodekapitel:* S1/S2 skærpes — én udefineret nøgleterm er allerede en 2 på S1.
  Metaforer forventes få; en enkelt upræcis afbildning vejer tungere (M2).
- *Lærebogskapitel:* Pædagogiske gentagelser er ikke T4-brud, hvis de er funktionelle
  (opsummeringsbokse o.l. er apparat, ikke brødtekst).
- *Tidsskriftartikel:* IMRaD-konventioner overtrumfer generiske T1-forventninger;
  scor T1 mod genrens skabelon.
- *Tidsskriftartikel (empirisk) — metodeblok (v1.4):* Fem tjekpunkter, der scores som
  del af S-dimensionen (S1/S4-belæg) og altid rapporteres som selvstændige flag:
  (1) **Søgedokumentation:** bærer teksten en litteratur-dækningspåstand ("intet findes"),
  skal søgestrenge, datoer og inklusionskriterier være angivet (evt. i supplement).
  (2) **Operationalisering:** skøn og vægte (fx indsatsandele) skal have angivet indikatorer
  og kombinationsregel — eller rapporteres som intervaller frem for punktestimater.
  (3) **Design-eksplicitering:** casens enheder (overordnet case + indlejrede analyseenheder)
  skal være navngivet, hvis designet reelt er indlejret.
  (4) **Selvvaliderings-afgrænsning:** hvor validering er udført af samme system/modelfamilie,
  skal teksten selv afgrænse, hvad der ville kræve eksternt (menneskeligt) blik.
  (5) **Restfejls-dækning:** formuleringer af typen "alle kendte fejl" skal ledsages af et
  dækningsgreb (stikprøve, blind re-audit eller estimeret restfejlsrate) eller en eksplicit
  afgrænsning af, hvad formuleringen ikke kan sige.
  **S4-skærpelser for genren:** ud over formuleringsstyrke mod belægsstyrke tjekkes
  (a) generaliserings-scope — påstande, der glider fra casen til det generelle, uden at
  afgrænsningen er markeret — og (b) institutionel præcision — påstande om produkter/
  resultater skal afspejle deres faktiske institutionelle status (fx manuskript over for
  udgivet, fagfællebedømt værk).
- *Monografikapitel:* Kapitlet skal både stå selv og bære værkets røde tråd — T3 vurderer
  også krydshenvisninger til andre kapitler.

## Parameter 2: Niveau-baseline

Baseline definerer, hvad trin 2 ("normalforventningen") betyder. Kriterie-baseret måling
kræver ekspliciteret standard (Glaser 1963); standarder kommunikeres bedst via eksemplarer
(Sadler 1989). Spørg brugeren; gæt aldrig.

**(a) Udkast til intern review.** Trin 2 = et ærligt arbejdsudkast: argumentet står,
men definitioner kan mangle, overgange kan være rå. Eksemplar-anker for "2 på S1":
nøglebegreberne er nævnt og delvist indkredset, men 1–2 definitioner udestår.
Brug denne baseline til formativ feedback tidligt i skriveprocessen.

**(b) Publiceringsklar dansk lærebog.** Trin 2 = niveauet i en gennemsnitlig udgivet dansk
samfundsvidenskabelig lærebog. Eksemplar-anker for "2 på S1": alle nøglebegreber defineres,
men nogle først et stykke inde, og afgrænsninger ("hvad falder udenfor") mangler stedvist.
Default-baseline for bogmanuskripter sent i processen.

**(c) Internationalt tidsskriftniveau.** Trin 2 = hvad der overlever review i et solidt
internationalt tidsskrift i feltet. Eksemplar-anker for "2 på S1": definitioner på plads
ved første brug; det, der mangler for en 3–4, er eksplicitte scope conditions og
relationer til nabobegreber (Suddaby-standarden). Den hårdeste baseline — samme tekst
scorer typisk 10–20 pp lavere end mod (b), og det er korrekt, ikke en fejl.

**Kommunikationsregel:** Rapporten skal minde læseren om, at en score kun gælder mod den
valgte standard: "82 % mod baseline (b)" og "68 % mod baseline (c)" kan beskrive samme tekst,
og ingen af tallene er "det rigtige" i absolut forstand.

## Fortolkningsskala: hvad tallene betyder

Procenterne her følger IKKE skoleskalaen. Skoleintuitionen "80 % = tilstrækkeligt,
90–100 % = målet" stammer fra mastery learning-traditionen, hvor 80–90 % rigtige på en
formativ test er mestringstærsklen (Bloom via Guskey 2007; Kulik et al. 1990) — dér er
100 % at "kunne det hele". I denne skala er 100 % noget andet: ALLE kriterier på
eksemplar-niveau (4/4), og trin 2 — midten — er pr. definition den valgte baselines
standard. Nulpunktet ligger altså et andet sted, og cut-scores er under alle
omstændigheder deklarerede konventioner, ikke naturgivne grænser (standard
setting-traditionen: Cizek 2013).

| Score (dimension/samlet) | Gnsn. kriterieniveau | Betydning mod den valgte baseline |
|---|---|---|
| 100 % | 4,0 | Teoretisk maksimum: hvert kriterium kunne tjene som eksemplar. Ikke et arbejdsmål. |
| 90–99 % | ≥ 3,6 | Eksemplar-zone: teksten kan bruges som forbillede for andre kapitler. Sjælden pr. design — hyppige 90+-scorer er tegn på score-inflation (tjek halo-alarmen). |
| 75–89 % | 3,0–3,5 | Stærk tekst, markant over baseline-standarden. Realistisk sigtezone for et flagskibskapitel eller efterskrift. |
| 50–74 % | 2,0–2,9 | På eller over baseline-standarden — dvs. "tilstrækkeligt" mod den valgte standard. Publicérbar, NÅR de bindende begrænsninger er tomme. |
| 25–49 % | 1,0–1,9 | Under standarden: væsentlig omarbejdning på de flagede punkter. |
| 0–24 % | < 1,0 | Strukturelle problemer på tværs af dimensioner. |

**Gate-reglen (tallet udløser aldrig "klar til tryk" alene):** Uanset score er teksten
først klar, når (1) produktionsfundene er ryddet, (2) ingen bærende påstand står
fejlkalibreret i påstandstabellen, og (3) listen over bindende begrænsninger er tom.
En efterladt produktionsnote kan ikke opvejes af 90 %.

**Vejen til højere tal går KUN gennem forankringerne.** Hver kriterievurdering skal
forklare "hvorfor x og ikke x+1" — dét er opskriften. De bindende begrænsninger er
dermed køreplanen: løs det øverste flag, og rapporten fortæller, hvad det næste er.
At jagte 90+ på alle dimensioner er fejlkalibreret ambition; målet er en tom liste af
bindende begrænsninger på den baseline, udgivelsen kræver.
