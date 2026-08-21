---
name: pm-konsistens-audit
description: >-
  Konsistens- og referenceaudit af en LaTeX-fagbog/lærebog (dansk): fortløbende nummerering
  pr. kapitel af Definition/Teoriboks/Perspektivboks/Case/Eksempel/Figur/Tabel; dangling
  krydshenvisninger (afsnit/Boks/Case/Figur/Tabel X.Y); at konceptregister og teorioversigt
  (Appendix) peger på RETTE afsnit/definitioner/bokse/floats; citationer i oversigtstabeller
  mod references.bib; REFERENCE-INTEGRITET (prosa-citationer uden bib-nøgle, dubletter,
  orphan-nøgler, nøglenavn↔år-mismatch); UREFEREDE FLOATS (label uden ref-henvisning);
  og EPIGRAFER (kapitelåbningens citat: ordret citat uden kildeår, kildeår uden bib-post,
  attributions- og citationstegns-konvention).
  Triggere: "kategori-audit", "reference-integritet", "dublet reference", "bib-audit", "tjek henvisninger", "konceptregister
  konsistens", "Appendix B konsistens", "dangling
  references", "ureferede figurer", "kryds-udgave krydsref", "epigraf", "kapitelcitat", "motto uden kilde". OPT-IN. Flagger og foreslår — ændrer aldrig
  mening/tal/citater uden eksplicit OK.
metadata:
  version: 0.12.0
---

# PM-konsistens-audit

Regelbaseret, deterministisk audit der bruger bogens **main.aux** (fra en ren
biber-build) som facit for auto-nummererede floats, og kildens boks-titler som facit
for manuelt nummererede kategorier.

## Kerneindsigter (hvorfor denne skill findes)
Erfaring fra PM-bogen: **positions-referencer** (afsnit X.Y i brødtekst, § i
konceptregister, kapitel-mapninger) er sårbare over for FORÆLDET nummerering, når
afsnit/bokse omrokeres — de opdaterer sig ikke selv. **Item-referencer** (Definition
X.Y, Box-titler) følger med elementet og er robuste. Typiske fejlmønstre: 7.2↔7.3-
ombytninger, off-by-one efter indsat afsnit, cyklisk forskydning i én kapitels
box/figur-serie, dublet-rækker og case-illustrationer uden figurnummer i registeret.

## Rækkefølge — kør EFTER tekst-fryse, FØR typografi (kritisk)

Denne skill auditerer **nummerering (Definition/Boks/Case/Figur/Tabel), float-kontinuitet
og krydshenvisninger** — det hører til **FASE C1**: efter tekst-fryse, før typografi/overfull.
Numre, floats og §-henvisninger afhænger af den endelige struktur, så kør denne audit først
når indhold, register og konsistens er låst — og før overfull/pagination-passet.

```
A. Indhold & korrekthed → B. Konsistens → ▶ TEKST-FRYSE ◀ → C1: DENNE skill → C2 typografi → C3 cover → D build
```

**Jernregel:** enhver senere tekst-ændring kan renummerere eller flytte floats — kør denne
audit (og derefter typografi + build) igen.

---

## Arbejdsgang
1. **Kræv en ren build først.** `main.aux` skal være fra `xelatex→biber→xelatex→xelatex`
   (ellers er float-numre stale). Uden aux: kør kun de manuelle/kilde-baserede tjek.
2. **Kør `scripts/audit_all.py`** (læs-kun). Den rapporterer:
   - Fortløbende numre pr. kapitel for Definition/Teoriboks/Perspektivboks/Case+Eksempel
     (kilde) og Figur/Tabel (aux) — huller/dubletter/starter-ikke-ved-.1.
   - Dangling hårdkodede henvisninger (kategori X.Y der ikke findes).
   - Konceptregister: §→afsnitstitel, Def→definitionstitel, Box→boks-titel,
     Fig/Tabel→float (via aux+caption). Flagger navn↔nummer-mismatch.
   - **Reference-integritet (sektion 3, kræver --bib):** prosa-citationer krydstjekket mod
     references.bib-nøgler. Se dedikeret afsnit nedenfor.
   - **Kapitel-skabelon-konsistens (sektion 4):** udleder den modale åbningsstruktur og flager
     kapitler der bryder den (fx læringsmål før 'Hvad dette kapitel handler om'). Se afsnit nedenfor.
   - **Typeløse box-pointere (sektion 5):** flager bar `Box N.N` (anglicisme + ikke type-kvalificeret)
     og eskalerer til HARDT FLAG når N.N er tvetydigt (findes som både Teoriboks og Perspektivboks).
     Scanner kilde + `--register` + `--appendix`. Se afsnit nedenfor.
   - **Afsnits-/kapitel-prosa-henvisninger (sektion 6):** validér at hvert hårdkodet
     "Section/Afsnit X.Y" og "Chapter/Kapitel N" i prosaen findes (ikke `\ref`, så LaTeX
     validerer dem ikke). Dangling = HARDT FLAG. Case-insensitivt (dækker EN + DA).
   - **Unummererede `\chapter*` header-mærke (sektion 7, valgfri `--structure`):** flager
     `\chapter*{Titel}` uden efterfølgende `\markboth` (→ stale løbende header fra forrige
     nummererede kapitel) og manglende `\addcontentsline{toc}` (REVIEW). `\section*` er
     bevidst ude. Angiv front/bag-matter via `--structure` (de unummererede overskrifter
     ligger uden for `kap*_body`).
3. **Verificér semantik manuelt** for hvert flag (skillen foreslår, beslutter ikke).
   Byg begreb→afsnitstitel-kort fra `\section`-titler; sammenlign mod henvisningens mål.
4. **Ret transaktionelt.** For hver rettelse: assertér at ankeret (begreb + gammelt
   nummer) findes PRÆCIS 1 gang; erstat kun tallet; byte-diff skal vise KUN tilsigtede
   tegn, uændret linjetal, intakte danske tegn (øæå = c3 b8 / c3 a6 / c3 a5). Backup
   pr. batch. Log hver ændring.
5. **Genbyg og verificér i PDF** (pdftotext): nye værdier til stede, gamle værdier =
   0 forekomster, ingen fantom-referencer.

## Reference-integritet (prosa ↔ references.bib)

Gælder bøger med **tekstuelle** referencer (forfatter-år skrevet i prosaen) + `\nocite{*}`
— IKKE `\cite`. Her kan en numre-/float-audit pr. konstruktion ikke fange en citation der
peger på en **ikke-eksisterende** bib-nøgle. `audit_all.py --bib references.bib` tilføjer
**sektion 3** med fire kategorier:

| Kat. | Fund | Sikkerhed |
|---|---|---|
| **C** | Dublet-poster (samme DOI, eller samme titel + samme år) | HØJ — hardt flag |
| **D** | Nøglenavn-år ≠ `year`-felt | HØJ — hardt flag |
| **A** | Prosa-citation uden matchende nøgle (delt: "efternavn slet ikke i bib" = høj signal; "år-mismatch" = ofte co-forf.-støj) | LAV/BLANDET — review |
| **B** | Bib-nøgle uden citation i prosa (orphan) | LAV — review |

Kun **C+D tæller som harde flag** (deterministiske). A og B er iboende støjende
(co-forfattere, virksomheds-/magasinnavne, genitiver, diakritik) og listes som
review-kandidater der IKKE fælder "RENT ✓". Scriptet deaccenter prosaen (ö→o, é→e),
fjerner genitiv-'s, fjerner LaTeX-kommentarer, og filtrerer via en stopliste for at dæmpe
falske positiver — men A-listen kræver altid menneskelig filtrering.

**v0.9.2 (2026-07-24) — review-synlighed (så "0 flag" ikke vildleder).** Erfaring: en operatør
læste kun "0 flag" (harde C+D) og overså §3.A-review-listen, hvor 7 citerede-men-manglende
referencer i praksis lå (fx Dutton/Dukerich/Harquail 1994, Harris & Schaubroeck 1988, Aguinis/Joo/
Gottfredson 2011; + år-mismatch Bol 2011, Buckingham & Goodall 2019). Rettelser: (1) A2-år-mismatch-
listen skrives nu FULDT ud i rapporten (før: "se fuld liste ved behov" — dér lå Bol/Goodall skjult);
(2) terminal-output og Konklusion viser nu eksplicit antal §3.A-review-kandidater, med påmindelse om
at bogen bruger tekstuelle forfatter-år-refs + `\nocite{*}` (ingen `\cite`), så citerede-men-manglende
referencer KUN dukker op i §3.A, aldrig som hardt flag. Ingen ændring i, hvad der tælles som flag.

**v0.9.1 (2026-07-24) — A-liste-støjreduktion.** Stoplisten `_NOISE` er udvidet med
struktur-navigations-ord (Section/Afsnit/Figur/Tabel/Kapitel/Appendiks) og tidsskrift-/
titel-ord (Management/Appraisal/Review/…), fordi parentes-med-årstal-regexen ellers
læser fx "(Section 6.3; Holmström, 1979)" som forfatteren "Section (1979)". Desuden en
partikel-suffix-match: prosa fanger kun sidste led af flerleddede navne ("Van der Stede"
→ "Stede"), men bib har hele navnet — sådanne flyttes fra høj- til lav-signal. Effekt på
PM-bogen (EN): A-højsignal 24 → 3 (kun ægte huller tilbage), 0 falske C/D.

### Prioritering af fund (triage)
- **P1 — læser-synlige fejl (ret først):** C-dubletter (dobbelt-trykt i litteraturlisten);
  prosa/år-uoverensstemmelser hvor `year`-feltet er korrekt (prosaen viser forkert år);
  A-"efternavn slet ikke i bib" for et reelt citeret værk (uslåbar reference).
- **P2 — integritet, usynlig men forkert:** forkert DOI på en post; `year`-felt forkert.
- **P3 — kosmetisk:** nøglenavn≠`year`-felt hvor feltet ER korrekt (usynligt i output for
  tekstuelle refs); orphan-nøgler (harmløse — `\nocite{*}` trykker dem alligevel).

### Forbehold (samme "flag, ret ikke")
Opret aldrig en reference med opdigtet DOI/sider — verificér metadata (CrossRef/Scite/Exa/
bibliotek); bøger uden DOI angives med forlag/sted/år. Vælg den udgave hvis årstal matcher
prosaen (fx et bogkapitel frem for et working paper med andet år). Ret transaktionelt:
backup → assertion pr. forekomst → byte-diff → build → log.

Reference-integritet læser kun `.bib` + `.tex` (ingen `main.aux`/build nødvendig), så den
kan køres tidligt — også før den fulde numre-/float-audit.

---

## Kapitel-skabelon-konsistens (åbningsstruktur)

En lærebog har typisk et fast **kapitel-skelet**: `\chapter` → undertitel → `\chaprule` →
(epigraf) → **"Hvad dette kapitel handler om"-boks** → **læringsmål** → første `\section`.
Numre-/reference-tjek ser IKKE om et kapitel bryder dette mønster — derfor kan en afvigelse
(fx læringsmål FØR handler-om-boksen) nå læseren. `audit_all.py` **sektion 4** fanger det:

- **Udleder den MODALE rækkefølge** af landemærkerne fra flertallet af kapitler (fx H før L,
  hvor H = "Hvad dette kapitel handler om", L = læringsmål) og **flager afvigere** (relativ
  rækkefølge, ikke eksakte linjenumre → epigraf-eller-ej giver ikke falske positiver).
- **Tilstedeværelse:** H og L behandles som påkrævet hvis ≥50 % af kapitlerne har dem; flager
  kapitler der mangler et påkrævet landemærke.
- **Frase-konsistens (review):** læringsmål-indledningen (fx "Efter at have læst dette kapitel
  vil du kunne:") — modal frase udledes; afvigere listes (fanger fx "Efter dette kapitel kan du:").

Harde flag = rækkefølge-afvigelser + manglende påkrævede landemærker. Frase-afvigelser = review.
Baggrund: PM-bogen (2026-07) — en læser fandt at kap16/17 åbnede med læringsmål før handler-om-
boksen; de øvrige 15 kapitler havde omvendt. Sektion 4 reproducerer det fund deterministisk.

Kan udvides til kapitel-*slutningen* (opsummering, spørgsmål, videre læsning) efter samme princip.

---

## Typeløse box-pointere (sektion 5)
Bogen har **separate tællere pr. bokstype pr. kapitel**, så samme nummer kan være BÅDE en Teoriboks
og en Perspektivboks (kollisionsnumre). En bar `Box N.N` uden typepræfiks er derfor (a) en **anglicisme**
— danske labels er `Teoriboks`/`Perspektivboks` — og (b) **tvetydig** når N.N er et kollisionsnummer.
Sektion 5 scanner kilde + `--register` + `--appendix`, matcher standalone `Box N.N` (de engelske typede
former `Theory Box`/`Perspective Box` udelukkes), og:
- **HARDT FLAG:** N.N findes som både Teoriboks og Perspektivboks (reelt tvetydigt for læseren).
- **REVIEW:** øvrige typeløse `Box N.N` (entydige, men bør stadig type-kvalificeres af house-style-hensyn).

Type-mappen udledes fra de **faktiske** boks-titler i kilden (ikke fra en handover/tabel — numre driver).
Baggrund: PM-bogens konceptregister havde 52 bare `Box N.N`, hvoraf 14 registerlinjer (13 kollisionsnumre,
16.1 to gange) var reelt tvetydige. Rettet 2026-07-11; sektion 5 reproducerer fundet deterministisk.

---

## Epigrafer (sektion 9)

Kapitelåbningens citat står i `\begin{quote}` **før** brødteksten og bærer aldrig `\cite`.
Den er derfor usynlig for både §3 (prosa↔bib) og enhver citations-scanning — samtidig med at
den er bogens mest eksponerede citat. En anmelder slår netop epigrafen efter.

**v0.10.0 (2026-08-19) — hvorfor tjekket findes.** I PM-bogen viste en manuel gennemgang, at
tre af fjorten epigrafer var forkerte: én var en parafrase sat i citationstegn (verbet var
skiftet ud), én bar forkert årstal **både i epigrafen og i `references.bib`**, og én havde
ingen kilde overhovedet — mens den eneste bib-post for forfatteren pegede på et andet værk.
Yderligere fire stod som ordrette citater helt uden år. Hverken kildeverificeringen,
korrekturen eller nogen tidligere audit-kørsel havde set dem. Årsagen er strukturel, ikke
menneskelig: værktøjerne scannede brødtekst og litteraturliste, og epigrafen er hverken.

**Hvad §9 flager**

| Kode | Type | Regel |
|---|---|---|
| 9A | HARDT | Teksten står i citationstegn, men attributionen har **intet årstal** → citatet kan ikke slås efter. Undtaget: markeret parafrase (`Frit efter …`, `After …`, `Adapted from …`) og selv-attribution (`Forfatteren`, `The author`). |
| 9B | HARDT | Attributionen har et årstal, men **ingen bib-post** matcher efternavn+år (eller `\citeyear`-nøglen findes ikke) → hængende kilde. |
| 9C | REVIEW | Attributions-formatet er ikke ensartet (nogle epigrafer med år, andre uden). |
| 9D | REVIEW | Citationstegns-konventionen er ikke ensartet på tværs af epigraferne (``` ``…'' ``` vs `` `…' ``). |

**Escape-hatchen er bevidst.** En epigraf, der ærligt er en omskrivning, skal markeres som
sådan — `--- Frit efter W. Edwards Deming (\citeyear{Deming1982}, s.~270)` er korrekt praksis
og udløser intet flag. Det, §9 rammer, er en omskrivning, der *udgiver sig for* at være ordret.

**Grænser.** §9 læser kun den **første** `\begin{quote}` inden for filens første 25 linjer —
altså kapitelåbningen, ikke blokcitater i brødteksten. Den verificerer ikke ordlyden mod kilden;
det kan kun et menneske eller et opslag. Den siger: *dette citat kan ikke slås efter* — og det
er den påstand, der har vist sig at være den dyre.

### Sektion 10 — epigrafer PAA TVAERS af udgaver (`--mirror`)

**v0.11.0 (2026-08-19).** §9 ser kun én udgave. Den fejl, hvor DA og EN har *forskellige*
epigrafer, er derfor usynlig for begge kørsler. Præcis den fejl fandtes i PM-bogen: DA's kap02
havde en markeret parafrase med 94 %/6 %, EN et ordret citat med 85 % — forskelligt tal,
forskellig status. Den blev fundet, fordi udgaverne blev lagt ved siden af hinanden i hånden.

`--mirror "<glob til den anden udgaves kapitelfiler>"` parrer filerne på kapitelnummeret og
sammenligner fire ting:

| Kode | Regel |
|---|---|
| 10A | Epigrafen findes kun i den ene udgave. |
| 10B | Den ene præsenterer epigrafen som ordret citat, den anden ikke. Samme kilde kan ikke både være og ikke være ordret. |
| 10C | Årstallene afviger. `\citeyear`-nøgler slås op i `--bib`, så DA's `\citeyear{Deming1982}` og EN's `(1982)` sammenlignes som *årstal* og ikke som forskellige strenge. |
| 10D | Tallene i selve epigrafteksten afviger. |

**Grænser, som er værd at kende.** 10D sammenligner *cifre*. Et tal skrevet med bogstaver
("Eighty-five percent") registreres som fraværende, ikke som 85 — det giver stadig et udslag,
men det er "den ene har tal, den anden ikke", ikke "94 mod 85". Efternavne sammenlignes ikke
på tværs: attributionerne er sprogligt forskellige ("Frit efter" mod "Adapted from"), og
begge udledes af samme funktion, så en sammenligning ville være cirkulær.

**Regressionstestet mod den faktiske fejl:** kørt mod EN-kildens tilstand FØR rettelsen udløser
den 10B og 10D på kap02; kørt mod den rettede tilstand melder den 0 afvigelser. 10C udløses
korrekt IKKE, fordi nøgleopslaget opløser begge udtryk til 1982.

Kørslen er ét-vejs: du kører den fra den ene udgave og peger `--mirror` på den anden. Der er
bevidst kun ÉN implementation — den engelske søsterskill henviser hertil frem for at have sin
egen, så de to ikke kan divergere (det skete for `scan.py` i juli, jf. CHANGELOG).

```bash
python3 scripts/audit_all.py --src "kap*_body.tex" --bib references.bib \
    --mirror "../PM_Textbook(EN)/kap*_body_EN.tex" --out KATEGORI_AUDIT.md
```

**Nyt i §9 samtidig:** `--epigraph-head N` gør de 25 linjer konfigurerbare, og **9E** rapporterer
nu hvilke kildefiler der slet INGEN epigraf har — før blev de sprunget lydløst over, så en
glemt epigraf var usynlig.


## Sektion 11 — krydshenvisninger PAA TVAERS af udgaver (`--mirror`)

**v0.12.0 (2026-08-21) — den fejlklasse, sektion 2 og 6 er blinde over for.**
I PM-bogen henviste den engelske kap17 ti steder til forkerte afsnit i kapitel 14:
"Section 14.3" hvor der skulle staa 14.2, "Section 14.4" hvor der skulle staa 14.1.
Auditten meldte samtidig "425 prosa-henvisninger, alle findes ✓" — og den havde ret.
**§14.3 findes. Den er bare ikke det afsnit, saetningen handler om.**
Sektion 2 og 6 verificerer EKSISTENS, ikke KORREKTHED, og kan aldrig fange dette alene.

Men i et spejlet tosproget vaerk findes der en deterministisk vej: de to udgaver har
samme kapitelstruktur og SKAL derfor henvise til de samme numre. Sektion 11
sammenligner fordelingen af afsnits-, float- og boks-henvisninger kapitel for kapitel
mellem `--src` og `--mirror`. Divergensen i PM-bogen sprang frem med det samme:
kap17 havde `14.3x4, 14.4x5` i EN mod `14.1x5, 14.2x3, 14.5x1` i DA.

**Tjekket doemmer ikke mening.** Det sammenligner to artefakter, der skal stemme, og
siger hvor de ikke goer. Hvilken udgave der har ret, afgoer mennesket — normalt
facit-udgaven. Divergenser er KANDIDATER, ikke domme: en bevidst udgave-specifik
henvisning vil ogsaa blive flaget, og det er korrekt opfoersel.

```bash
python scripts/audit_all.py --src "kap*_body_EN.tex" --aux main_EN.aux --bib references.bib \
    --register <register> --appendix <appendiks> \
    --mirror "../PM_Textbook(master)/kap*_body.tex" --out AUDIT.md
```

### v0.12.0 — to huller lukket i sektion 2

**(a) Konceptregisteret blev aldrig scannet som henvisningsflade.** `--register` gik
udelukkende til sektion 5 (typeloese box-pointere). Sektion 2 saa kun kapitelfilerne.
Konsekvens i PM-bogen: da en figur blev slettet, blev registerets "Fig 14.2" dinglende,
og auditten meldte "0 dangling ✓". Maalt, ikke antaget: koert mod prae-fix-tilstanden
gav den gamle version 0 flag, den nye 1 flag med fil og linjenummer.
Nu scannes register og appendiks paa lige fod med kapitlerne.

**(b) Float-moenstret var kun dansk.** `pat` matchede `Figur`/`Tabel` — ikke den
engelske udgaves `Figure`/`Table` og ikke registerets forkortede `Fig N.M`.
Omfang i PM-bogen: **151 haardkodede floathenvisninger i de to registre**
(DA 52 `Fig` + 29 `Tabel`, EN 45 `Fig` + 25 `Table`) havde aldrig vaeret kontrolleret.
Nu daekker moenstret `Figur|Figure|Fig.?` og `Tabel|Table`.

### Hvad sektion 11 IKKE kan
Den fanger uenighed mellem udgaver. Den fanger ikke en fejl, der staar ENS begge steder,
og den siger intet om, hvorvidt en henvisning peger paa det rigtige INDHOLD, naar begge
udgaver er enige om nummeret. Til det findes der ingen automatik — kun laesning.
Se ogsaa metodenoten under "Forbehold".

## Rør-ikke / beskyttet
Citater, citationer/forfattere/år/DOI, definerede term-navne, boks-ordlyd, tal.
Ret aldrig en citation uden eksplicit brugerbeslutning (flag som "beskyttet").

## Filer
- `scripts/audit_all.py` — deterministisk, læs-kun auditor. Parametre: `--src` (glob, default
  `kap*_body.tex`), `--aux` (default `main.aux`; springes over hvis fraværende), `--bib` (default
  `references.bib`; aktiverer sektion 3 reference-integritet), `--register` (default
  `konceptregister_body.tex`) og `--appendix` (default `09_Back_Matter/appendiks_b_teorioversigt.tex`)
  til sektion 5 typeløse box-pointere; `--structure` (komma-separerede globs af front/bag-matter
  `.tex` til sektion 7 `\chapter*`-header-tjek); `--out` (markdown-rapport).
  Sektion 4 (kapitel-skabelon), 5 (typeløse box-pointere), 6 (prosa-henvisninger), 7
  (`\chapter*`-headers), 8 (ureferede floats) + 9 (epigrafer) kører altid — kræver kun `.tex`.
  Sektion 9's del B (kildeår↔bib) kræver dog `--bib`; sektion 10 kræver `--mirror`
  (glob til den anden udgaves kapitelfiler) og bruger `--bib` til nøgleopslag.
  `--epigraph-head N` styrer, hvor mange linjer i filens top §9/§10 leder i (default 25).
  Eksempel: `python3 scripts/audit_all.py --src "kap*_body.tex" --aux main.aux --bib references.bib --register konceptregister_body.tex --appendix 09_Back_Matter/appendiks_b_teorioversigt.tex --structure "afterword_body.tex,00_Front_Matter/*.tex" --out KATEGORI_AUDIT.md`
