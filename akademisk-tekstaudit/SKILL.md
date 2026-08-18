---
name: akademisk-tekstaudit
description: >-
  Evidensbaseret kvalitetsaudit af DANSKE akademiske tekster (kapitler, efterskrifter,
  monografier, artikeludkast) på fem dimensioner — semantisk indhold, hermeneutisk indhold,
  teknisk opbygning, metaforbrug samt tabeller/figurer — med forankret 0–4-rubrik,
  to-parameter-kalibrering (genreprofil + niveau-baseline), vægtet aggregering, konfidensbånd
  og tekstbelæg pr. score. Den MÅLER og FLAGER — den omskriver aldrig (omskrivning henvises
  til academic-danish-klarsprog). OPT-IN ONLY: kør kun ved eksplicit anmodning. Triggere
  (kun på direkte anmodning): "tekstaudit", "kvalitetsaudit", "femdimensionsanalyse",
  "scor teksten/kapitlet", "audit efterskriftet", "semantisk/hermeneutisk analyse med score".
  Scorer BRØDTEKST plus tekstens egne tabeller/figurer; citater, bokse og litteraturlisten
  vurderes ikke som prosa.
---

# Akademisk tekstaudit (dansk)

## Hvad denne skill er — og ikke er

Skill'en producerer en **struktureret second opinion** på en akademisk teksts kvalitet:
en analytisk rubrik-vurdering med 19 kriterier i 5 dimensioner, hvor hver score er bundet
til ordret tekstbelæg. Den er IKKE et psykometrisk valideret måleinstrument, og det skal
stå i rapportens metodeboks. Den omskriver ALDRIG tekst — den flager og prioriterer, og
omskrivning overlades til klarsprog-/narrative-skills. Grunden til denne arbejdsdeling:
en bedømmer, der også må omskrive, mister sin uafhængighed og begynder at score sine egne
præferencer i stedet for teksten.

Evidensgrundlaget (fuld referenceliste i `references/referencer.md`) er kort fortalt:
forankrede, opgavespecifikke rubrikker scorer mere pålideligt end frie helhedsvurderinger
(Jonsson & Svingby 2007); "analysér før du scorer" forbedrer LLM-bedømmeres overensstemmelse
med mennesker (Liu et al. 2023, G-Eval); og LLM-bedømmere har dokumenteret score-inflation,
halo-tendens og ustabilitet, som workflowet nedenfor er designet til at modvirke
(Zheng et al. 2023; Lai et al. 2014).

## Workflow

### Trin 0 — Kalibrering (obligatorisk, FØR læsning af teksten)

Stil to spørgsmål, og accepter ikke at springe dem over — uden dem er scoren bundet til en
implicit, ustabil norm og kan ikke sammenlignes med andre kørsler:

1. **Genreprofil** (hvilke kriterier og vægte gælder): lærebogskapitel, metodekapitel,
   efterskrift/forord, monografikapitel eller tidsskriftartikel.
2. **Niveau-baseline** (hvad trin 2 "normalforventningen" betyder): udkast til intern
   review, publiceringsklar dansk lærebog, eller internationalt tidsskriftniveau.

Et tredje, VALGFRIT parameter: **Dimension D (diskurs- og magtrefleksivitet)** — spørg kun,
hvis brugeren selv har bragt diskurs/magt på bane, og kør den ellers IKKE. Default: FRA.
Aktiveres den, gælder flag-tilstand (uscoret) som default — se `references/rubrik_D_diskurs.md`.

Detaljer, vægtsæt og eksemplar-ankre: læs `references/kalibrering.md` nu.
Hvis brugeren har angivet begge parametre i sin anmodning, bekræft dem kort i stedet for at spørge.
Kører auditten på flere kapitler i samme værk, skal baseline være identisk på tværs — ellers
er kapitelscorerne ikke sammenlignelige.

### Trin 1 — Afgræns scoringsmaterialet

Brødtekst plus tekstens egne tabeller/figurer er materialet. Direkte citater, bokse med
fremmed ordlyd, litteraturliste og apparat scores ikke som prosa (men en fejlplaceret
henvisning TIL en boks/figur er et T- eller F-fund). Notér omfang (ord/afsnit) til metodeboksen.

### Trin 1b — Argumentrekonstruktion (før al scoring)

Rekonstruér tekstens argument, FØR du åbner rubrikken — en bedømmer, der ikke har forstået
argumentet, scorer overflade i stedet for substans:

1. **Hovedtese:** formuler tekstens centrale påstand i én sætning.
2. **Påstandsstruktur:** list de 3–8 bærende delpåstande og deres indbyrdes afhængighed.
3. **Betydningsniveauer:** notér hvilke niveauer teksten arbejder på (fx empirisk, teoretisk,
   normativt, ontologisk), og om teksten selv markerer skiftene.

Rekonstruktionen indgår i rapporten og føder S3 (begrebsrelationer), S4 (påstandstabellen),
H1–H2 og T1. Uenighed mellem din rekonstruktion og tekstens egen selvbeskrivelse
(fx "fire kritikpunkter" i indledningen mod seks reelle delpåstande) er et selvstændigt fund.

### Trin 2 — Analysér og scor pr. kriterium

Læs `references/rubrikker.md` (alle 19 kriterier med forankringer 0/2/4). For HVERT aktivt
kriterium, i denne rækkefølge — analysen skal stå FØR scoren, fordi omvendt rækkefølge
dokumenteret giver dårligere kalibrerede tal:

1. **Belæg:** citer 1–3 ordrette passager med stedsangivelse (afsnit/sidetal).
2. **Analyse:** hvad viser belægget i forhold til kriteriets forankringer?
3. **Score:** 0–4 (heltal; 1 og 3 er mellemtrin mellem de beskrevne niveauer).
4. **Konfidens:** høj/middel/lav. Uden mindst ét ordret belæg: scoren markeres "skøn"
   og konfidens sættes automatisk til lav. H1 og H2 kræver mindst to belæg og kan aldrig
   få højere konfidens end middel (fortolkningsdybde er disciplineret skøn, ikke måling).

To kriterier scorer på under-niveau, fordi aggregatet ellers skjuler profilen:

- **S4 scorer pr. central påstand** (påstandstabellen fra trin 1b): for hver bærende påstand
  vurderes formuleringsstyrke (afdæmpet/kalibreret/absolut) mod belægsstyrke
  (svag/moderat/stærk). Kombinationen "absolut formulering + moderat belæg" er et flag;
  S4-scoren følger af, hvor mange påstande der er fejlkalibrerede.
- **M-kriterierne scorer pr. bærende metafor** (metafor-inventaret): hver bærende metafor får
  funktion, afbildningstjek, konsistens og framing-risiko vurderet for sig; M-dimensionens
  kriteriescorer aggregeres derfra (svageste bærende metafor trækker mest — én defekt
  mastermetafor skader mere end tre svage bimetaforer).

Skala-disciplin, fordi LLM-bedømmere dokumenteret klumper i toppen: 2 er normalforventningen
for et solidt udkast mod den valgte baseline; 3 er en stærk tekst; 4 er forbeholdt passager,
der kunne bruges som eksemplar. Giv aldrig hele dimensionen samme score af bekvemmelighed —
kriterierne er designet til at kunne divergere.

### Trin 2b — Intern fakta-konsistens (deterministisk fejning)

Kør — FØR beregningen — en mekanisk konsistensfejning på tværs af hele materialet. Fund
rapporteres under produktionsfund og/eller som belæg til begrebskonsistens (S2); fejningen
har ingen selvstændig score:

1. **Tal mod tal:** Samme artefakt eller mængde omtalt med forskellige tal (fx "245 poster"
   ét sted, "277 termer" et andet). List alle talpar om samme referent og sammenhold dem.
2. **Ord mod faktum:** Kvalitative tids- og mængdeord ("flerårig", "årtier", "hovedparten",
   "alle", "de fleste") holdes mod tekstens egne dokumenterede datoer, varigheder og
   optællinger — "flerårigt samarbejde" i en case, teksten selv daterer til otte måneder,
   er et fund, som ingen rubrik-linje fanger.
3. **Løfte mod leverance i tal:** Overskrifters og roadmaps tællinger ("fem episoder",
   "ni faser") mod det faktisk leverede antal i teksten.

Begrundelsen står i Designhistorikken (v1.2): Rubrik-forankring styrer opmærksomheden og er
derfor systematisk blind for fundklasser uden for rubrikken. Fejningen er rubrikkens
deterministiske sikkerhedsnet — den kræver ingen dømmekraft, kun systematik, og må derfor
aldrig springes over af tidshensyn.

### Trin 2c — Terminologisk forankring (manglende etablerede fagtermer)

Kør — sammen med trin 2b — et forankringstjek af tekstens begrebsapparat. Fund rapporteres
som flag under semantisk indhold (S2/S3-belæg) og i "Prioriterede flag"; tjekket har ingen
selvstændig score:

1. **Egenopfundne termer mod etablerede:** List tekstens bærende egenudviklede begreber og
   metaforer. Spørg for hver: Findes der en ETABLERET fagterm i litteraturen for (dele af)
   samme fænomen? Hvis ja, er det et flag — enten bør den etablerede term bruges, eller også
   bør den egenopfundne term eksplicit forankres i den ("det, litteraturen kalder X, kaldes
   her Y, fordi …"). En tekst, der opfinder ord for kendte fænomener uden at markere det,
   taber præcision OG signalerer manglende litteraturkendskab.
2. **Oplagte, men fraværende ankertermer:** Spørg omvendt: Hvilke fagtermer ville en
   fagfællebedømmer FORVENTE at møde i en tekst om dette emne (fx *stage-gate* og
   *human-in-the-loop* i en tekst om gate-styrede menneske–AI-processer)? Fravær af en
   oplagt ankerterm er et flag — også når tekstens eget ordvalg er forståeligt.
3. **Kalibrering af mængden:** Tjekket måler forankring, ikke jargontæthed. Anbefal aldrig
   at erstatte et velfungerende, defineret egenbegreb med en dårligere passende fagterm —
   flagget er en observation plus et spørgsmål til forfatteren, ikke et påbud.

Begrundelsen står i Designhistorikken (v1.3): begge fundklasser (uforankrede egenbegreber
og fraværende ankertermer) blev fundet i praksis af et frit gennemsyn, EFTER at to fulde
rubrik-kørsler havde overset dem.

### Trin 2d — AI-indsættelses-tjek (frisk indsat tekst)

Er dele af teksten netop tilføjet eller omskrevet med AI-assistance (forfatteren oplyser
hvilke, eller versionsnoten viser det), auditeres NETOP disse passager særskilt — ud over
den almindelige scoring — for tre fundklasser, som samlet set er signaturen for frisk
AI-produceret prosa i en ellers gennemarbejdet tekst:

1. **Naboafsnits-ekko:** ord- og vendingsgentagelser på tværs af den nye passage og dens
   nabopassager (samme adjektiv, samme verbalfrase, samme rammekonstruktion inden for en
   side). Den slags ekko opstår, når ny tekst genereres med nabopassagen i kontekst.
2. **Metafor-rester fra AI-registeret:** billedsprog, der ikke hører hjemme i tekstens
   etablerede register (fx procesmetaforik som "destilleret", "strøm af", personificeringer
   som viden der "bor"). Sammenhold med tekstens egen metaforpraksis (M-dimensionen).
3. **Idiomatisk hjemmel:** konstruktioner, der er grammatisk mulige, men ikke idiomatiske
   på dansk (fx skæve præpositionsforbindelser). Flag med forslag om naturligt fagsprog.

Tjekket er flag-mode uden selvstændig score. Det erstatter ikke ai-tell-audit (som måler
tæthed over hele teksten) — det er en målrettet stikprøve dér, hvor risikoen er størst:
i det senest indsatte. Begrundelse i Designhistorikken (v1.4).

### Trin 3 — Beregn

- Kriteriescore s ∈ {0,1,2,3,4}; kriterievægte w (default lige) fra genreprofilen.
- Dimensionsscore: `D_j = (Σ w·s) / (4·Σ w) · 100 %`.
- Samlet: `Total = Σ v_j · D_j` med genreprofilens dimensionsvægte v (rapportér altid vægtene).
- Konfidensbånd pr. dimension: alle kriterier høj → ±3 pp; mindst ét middel → ±6 pp;
  mindst ét lav → ±10 pp. Båndene er konventioner, ikke statistik — skriv det i metodeboksen.

### Trin 4 — Stabilitets- og halo-tjek

- **Halo-alarm:** ligger alle D_j inden for et 10 pp-bånd, tilføj en advarsel i rapporten om
  mulig halo-effekt, og genbesøg de to kriterier med tyndest belæg.
- **Stabilitetstjek (når brugeren beder om det, eller ved bogdækkende brug):** kør trin 2–3
  igen i en frisk kontekst (subagent uden adgang til første gennemløbs scorer), og rapportér
  |ΔD_j|. Divergens > 8 pp på en dimension → markér dimensionen "ustabil — kræver menneskeligt blik".

### Trin 5 — Rapportér

Følg skabelonen i `references/rapportskabelon.md` NØJAGTIGT — fast format er det, der gør
kørsler sammenlignelige over tid. Rapporten indledes altid med kalibreringsblokken og
afsluttes altid med metodeboksen. Forbedringsforslag formuleres som prioriterede FLAG
("S2, afsnit 4: 'performance' bruges i tre betydninger — overvej terminologisk nøgle"),
aldrig som færdige omskrivninger.

Fire elementer ud over kriterievurderingerne:

- **Produktionsfund (ikke-scoret):** produktionsrester (interne noter, versionsmarkeringer),
  orddelings-/parsing-artefakter, tomme sider, tabel-/figurformatering, dangling numre.
  De indgår IKKE i scoren (de er manuskriptteknik, ikke tekstkvalitet), men rapporteres altid —
  en efterladt produktionsnote er ofte det vigtigste enkeltfund før udgivelse. Bogdækkende
  nummer-/krydshenvisningskontrol henvises til pm-konsistens-audit.
- **Bindende begrænsninger:** udpeg pr. dimension det eller de flag, der aktuelt holder scoren
  nede ("S løftes ikke over 60 %, før S2-glidningen er løst"). Det giver samme information som
  en "parathed før/efter"-procent, men uden at opfinde et tal, der ikke kan begrundes.
- **"Hvad teksten ikke påstår" (valgfrit flag):** hvis teksten er polemisk udsat, foreslå at
  forfatteren tilføjer en eksplicit afgrænsning af, hvad argumentet IKKE hævder — men skriv
  den ikke selv.
- **Handoff-pakke:** afslut med præcise omskrivningsbriefs til de relevante skills
  (academic-danish-klarsprog / academic-english-narrative m.fl.): hvilke passager, hvilket
  problem, hvilken retning — men ingen færdig ordlyd. Sådan bevares nytten af konkrete
  anvisninger uden at bedømmeren selv skriver om.

### Formidlingsregler (gælder hele rapporten)

- **Rapporten indledes ALTID med "Sådan læses denne rapport"-blokken** fra skabelonen —
  fortolkningsskalaen og sprogmodellens begrænsninger skal stå dér, hvor læseren møder
  tallene, ikke kun i en skill-fil, læseren aldrig ser.
- **Få forkortelser.** Brug fulde kriterienavne med koden i parentes — "begrebskonsistens
  (S2)", ikke "S2". Enhver forkortelse forklares ved første brug. Procentpoint skrives
  helst ud. Læseren af rapporten kender ikke skill'ens interne koder.
- **Auditten er et dialogværktøj.** Formulér fund som bidrag til en samtale ("dette taler
  for at …; vurdér selv om …"), ikke som domme. Sprogmodellen kan fejllæse — rapporten
  skal invitere til efterprøvning, og det skal fremgå både i indledningsblokken og i
  metodeboksen.

## Samspil med søster-skills (batteri-anbefaling)

Ved AI-assisterede manuskripter bør auditten ikke stå alene. Anbefal — og notér i
metodeboksen, om det er sket — et batteri med arbejdsdeling dokumenteret i praksis:
den forankrede rubrik fanger det mekanisk verificerbare og det, der kræver dømmekraft
inden for rubrikkens spørgsmål; **ai-tell-audit** måler prosarytme og LLM-stilmarkører
(fx em-dash-tæthed), som rubrikken ikke spørger om; **engagement-audit** vurderer narrativ
bue og læsemotivation; et frit kryds-model-review supplerer med det strategisk-metodologiske
blik, ingen rubrik kan planlægge. I casen, skillen er udviklet på, blev 5 af 30 eksterne
reviewfund dækket af søster-skills, der fandtes, men ikke var kørt — batteriet er altså
ikke en luksus, men lukningen af en dokumenteret fundklasse. Handoff-pakken (Trin 5) kan
desuden anbefale, at påstandstabellen (S4) publiceres som element i selve teksten — i
artikel-casen blev den til manuskriptets egen evidenstabel.

## Grænser

- Aflever aldrig en score uden belæg uden at mærke den som skøn.
- Ændr aldrig i teksten; foreslå aldrig konkret ny ordlyd (det er klarsprog-skill'ens job).
- Sammenlign aldrig scorer på tværs af forskellige kalibreringer.
- Ved tvivl om et kriteriums anvendelse på genren: notér tvivlen i metodeboksen frem for
  at score lavt "for en sikkerheds skyld".
- Dimension D vurderer refleksivitet om position og framing — ALDRIG positionen selv.
  D-fund formuleres som observation + spørgsmål til forfatteren, aldrig som holdningsanvisning.
  D er opt-in, uscoret som default, konfidens-loft middel, og ved scoret tilstand vægt ≤ 0,05.
- **Case-fakta om virkelige virksomheder/begivenheder:** flag ALDRIG som "fejl", alene fordi
  ét sekundærværk angiver andre tal — sekundærlitteraturen varierer ofte. Tjek samtidige
  primær-/pressekilder, og formulér fundet som "kilder varierer — verificér" med den konkrete
  modkilde og dens år. "Afviger fra én kilde" er ikke det samme som "forkert".


## Designhistorik (dimensionsvalg SKAL begrundes her)

- **v1.0 (juli 2026):** Fem dimensioner (S/H/T/M/F), formaliseret fra et kryds-model-review-
  eksperiment. Diskurs/magt-dimensionen fra det oprindelige helbogs-review blev IKKE medtaget,
  og udeladelsen var udokumenteret — en fejl i designdisciplinen.
- **v1.1 (august 2026):** Dimension D (diskurs- og magtrefleksivitet) optaget som valgfri
  flag-dimension med fire sikkerhedsventiler (opt-in; uscoret default; konfidens-loft middel;
  positionsneutralitet). Begrundelse: diskurs/magt var det mest produktive fund i det review,
  skillen blev formaliseret fra — instrumentet må ikke være blindt for sin mest værdiskabende
  fundklasse. Modhensyn (derfor ventilerne): risiko for at en LLM-bedømmer scorer holdninger
  frem for kvalitet, og for pseudo-kvantificering af det sværest målbare. Evidensforankringen
  for D er svagere end for S/T og deklareres i hver rapport.
- **v1.2 (august 2026):** Deterministisk fakta-konsistensfejning (Trin 2b) tilføjet, efter at
  to uafhængige, blinde kørsler af v1.1 overså en ord-mod-faktum-fejl ("flerårigt samarbejde"
  om et forløb, teksten selv daterede til otte måneder), som et frit kryds-model-review fandt
  spontant. Lærdom: Forankrede rubrikker køber reliabilitet ved at styre opmærksomheden — og er
  derfor systematisk blinde for fundklasser uden for rubrikken. Alt, der kan tjekkes
  deterministisk, skal tjekkes deterministisk; rubrikken dækker kun det, der kræver dømmekraft.
  Komplementaritetsfundet (rubrikken fangede tal-mod-tal-fund, fritekst-reviewet fangede
  ord-mod-faktum) er dokumenteret i casens kryds-model-sammenligning.
- **v1.3 (august 2026):** Terminologisk forankringstjek (Trin 2c) tilføjet, efter at et frit
  gennemsyn af artikel-casen fandt to fundklasser, som to fulde rubrik-kørsler havde overset:
  (a) 18 egenudviklede termer, hvoraf flere dækkede fænomener med etablerede fagtermer
  (fx gate-begrebet ↔ *stage-gate*/Cooper 1990; snyde-følelsen ↔ *impostor phenomenon*/
  Clance & Imes 1978 — med skelnen), og (b) seks oplagte, men fraværende ankertermer
  (*human-in-the-loop*, *quality by design*, *poka-yoke* m.fl.), hvis indsættelse løftede
  tekstens faglige forankring markant. Lærdom som v1.2: rubrikken ser kun, hvad den spørger
  om — fravær af noget forventeligt kræver et eksplicit trin, der spørger til fraværet.
- **v1.4 (august 2026):** (a) AI-indsættelses-tjek (Trin 2d) tilføjet, efter at en sprogtest
  af netop AI-indsatte passager i artikel-casen fandt syv fund i én passage (metafor-rester,
  naboafsnits-ekko, uidiomatisk konstruktion), som hverken rubrikken eller de deterministiske
  fejninger spørger om — fundklassen er lokaliseret (frisk indsat tekst), ikke tekstdækkende,
  og kræver derfor en målrettet stikprøve. (b) Genreprofilen "tidsskriftartikel (empirisk)"
  udvidet med metodeblok og S4-skærpelser (kalibrering.md), efter at en systematisk
  gap-analyse af 30 eksterne reviewfund mod skillens kriterier viste, at 6 reelle gaps lå
  samlet i metodisk efterprøvelighed (søgedokumentation, operationalisering,
  design-eksplicitering, selvvaliderings-afgrænsning, restfejls-dækning) — en dimension,
  rubrikken ikke havde for empiriske artikler. (c) Batteri-anbefalingen gjort eksplicit
  (5 af 30 eksterne fund dækkedes af søster-skills, der ikke var kørt).
- **v1.5 (august 2026):** Kildevariations-regel for case-fakta tilføjet (Grænser), efter at
  PM-bogens kvalitetsgate viste et falsk positiv: en auditor flagede Enrons 20/70/10-fordeling
  som GE-transplantat, men samtidig presse (TIME, 2001) dokumenterer netop denne inddeling for
  Enron — sekundærlitteraturen varierer (PRC 1-5 med ~15 % i bunden findes også). Lærdom: for
  virkeligheds-cases skal "afviger fra én kilde" skelnes fra "forkert"; flag-formuleringen er
  "kilder varierer — verificér". Samtidig bekræftede gaten F1/F4-kriteriets værdi (14 ureferede
  floats fundet) — det tjek er nu også deterministisk i pm-konsistens-audit (§8).
- Fremtidige til- eller fravalg af dimensioner skal begrundes i denne sektion.
