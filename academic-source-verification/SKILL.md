---
name: academic-source-verification
description: >-
  Kilde- og citationsverifikation for akademiske manuskripter (lærebøger, monografier)
  med et transparent revisionsspor — et ansvarlighedsinstrument over for forlag og
  læser. Brug, når brugeren vil verificere, at bogens kilder (a) findes og har korrekt
  metadata (forfatter/titel/journal/år/DOI), (b) ikke er trukket tilbage, og (c) faktisk
  siger det, teksten påstår — og vil have det DOKUMENTERET i en hovedbog (regneark) plus
  en afledt AI-/kildedeklaration. Producerer og vedligeholder reference-audit-regnearket
  med provenans pr. kilde: metoder, evidens (DOI/URL), antal kilder, retraktionsstatus,
  claim-støtte, menneskelig sign-off, værktøj+dato. Triggere: 'kilde-verifikation',
  'verificér kilderne', 'opdatér reference-regnearket', 'T1-verifikation', 'tjek for
  tilbagetrukne kilder', 'lav AI-deklaration'. OPT-IN. FLAGGER og foreslår — ændrer
  aldrig kilde, citation eller tal uden eksplicit OK; læs-kun. IKKE til intern
  konsistens/krydsref (det er pm-konsistens-audit); IKKE til oversættelse eller register.
license: MIT
metadata:
  family: academic-book
  siblings: pm-konsistens-audit
  related: cbs-libsearch (fuldtekst-/annotationsbackend), academic-english-consistency, academic-danish-consistency
  version: 0.1.3
---

# Akademisk kilde-verifikation (ekstern sandhed + revisionsspor)

Standalone, disciplin-agnostisk skill, der besvarer ét spørgsmål og dokumenterer svaret:
**"Er bogens kilder virkelige, korrekte, pålidelige — og siger de det, vi påstår? Og kan
vi bevise, at vi har tjekket det?"**

Skillen har to sideordnede formål — verifikationen OG dokumentationen af den:

1. **Verifikation (ekstern sandhed).** For hver citeret kilde: findes den? er metadata
   korrekt? er den trukket tilbage/korrigeret? støtter den faktisk tekstens påstand?
2. **Revisionsspor (ansvarlighed).** Alt ovenstående registreres pr. kilde i en
   **hovedbog (regneark/ledger)** med provenans, så et forlag eller en kritisk læser
   kan se *hvordan* hver kilde er efterprøvet — og så forfatteren kan skrive en sand
   AI-/kildedeklaration og stå inde for den.

## Forhold til søsteren (grænsen er skarp)

- **`pm-konsistens-audit`** (søster) — *intern* sandhed: hænger bogen sammen med sig
  selv? Fortløbende numre, dangling krydsref, at hver in-text-citation *resolver* til en
  bib-nøgle (fantom-/forældreløs-detektion), at gengivelser i tabeller matcher
  `references.bib` (implementeret i `pm-konsistens-audit/scripts/audit_all.py --bib`, sektion 3;
  fanger nu også dublet-poster og nøglenavn↔år-mismatch). Offline, deterministisk. **Fantom-/forældreløs-fund derfra FODRER
  denne skill** (kun faktisk citerede, resolvbare kilder verificeres eksternt).
- **`academic-source-verification`** (denne) — *ekstern* sandhed + deklaration: findes
  kilden i verden, er den rigtig, pålidelig, og siger den det påståede. Kræver web/DB/
  dømmekraft.

Fantom-"Chan (2014)" fanges af søsteren (ingen bib-nøgle). "Bib-post findes, men journal
er forkert / kilden er trukket tilbage / kilden siger ikke det påståede" fanges her.

---

## Rækkefølge — kør SENT, efter tekst-fryse (kritisk)

Verifikation efterprøver **den endelige, gengivne tekst** — ikke et tidligt udkast.
Kilde-fakta gengives ofte i hånden ude i brødtekst, kildelinjer og oversigtstabeller, og
de gengivelser *driver* fra den verificerede bib-post, når teksten redigeres senere
(erfaring: en tidlig bib-verifikation blev forældet, og inline-gengivelser afveg — forkert
journal, forkert år — uden at nogen opdagede det). Derfor:

```
A. Indhold & korrekthed  (oversættelse → fakta → register → grammatik)
B. Konsistens            (stavning/husstil; pm-konsistens-audit: numre, krydsref, fantom/forældreløs)
   ▶▶▶  TEKST-FRYSE  ◀◀◀
C. Kilde-verifikation    (DENNE skill — på den frosne tekst) + deklaration
D. Form & layout, endelig build
```

**Jernregel:** enhver sen tekst-ændring, der rører en citation eller en påstand knyttet til
en kilde, invaliderer den kildes verifikation — den skal re-verificeres og hovedbogen
opdateres (ny dato + sign-off).

---

## De hårde regler (ufravigelige)

1. **Manuskriptet er læs-kun.** Redigér, slet eller omskriv aldrig forfatterens filer.
   Output er hovedbogen (ledger), en logfil og deklarationsudkast. Rettelser i selve
   bogen sker kun via en separat, godkendt GATE (backup → edit → diff → build → log).
2. **Flag, ret ikke. Human in the loop.** Skillen foreslår og dokumenterer; **mennesket
   verificerer og hæfter.** Hver dom bærer konfidens (H/M/L). Det matcher forlagenes
   krav (COPE, Taylor & Francis, Edinburgh UP m.fl.): forfatteren er ansvarlig for
   referencerne; AI-output er et udkast, der skal efterprøves af et menneske.
3. **Fabrikér aldrig.** Ingen opdigtede DOI'er, kilder, journaler, år. Kan noget ikke
   verificeres, mærkes det eksplicit `requires verification` — aldrig gættet.
4. **Evidensstandard.** En "forkert"-dom kræver **≥3 uafhængige, verificerbare kilder**;
   en "korrekt"-dom mindst den kanoniske kilde (DOI-resolver / forlag / indekseret post).
   Registrér altid *hvilke* kilder og *hvor mange*. (Præcedens: journal-fejlen krævede 6
   kilder, før den blev flagget.)
5. **Registrér provenans pr. kilde:** metode(r), evidens (DOI/URL/bog-sted), antal kilder,
   retraktionsstatus, claim-støtte, hvem der signerede (menneske) + om AI assisterede,
   værktøj+version, dato. Dette ER revisionssporet.

Findes en projekt-beslutningslog / skopos-brief, **vinder den** over skillens defaults.

---

## De tre tjek

**Tjek 1 — Reference-korrekthed (findes kilden? er metadata rigtig?)**
For hver bib-nøgle: eksisterer værket? forfatter/titel/journal/år/DOI korrekt og indbyrdes
konsistente? Backends: CrossRef/DOI-resolver, OpenAlex, Semantic Scholar, forlagsside.

**Tjek 2 — Pålidelighed (trukket tilbage/korrigeret?)**
Er kilden retracted, corrected, erratum, expression of concern? Backends: Retraction Watch,
Crossref Crossmark, scite Reference Check. Sæt `retraktionsstatus`.

**Tjek 3 — Claim–kilde-troskab (siger kilden det, teksten påstår?)**
Det dybeste og mest værdifulde tjek: matcher tallet/pointen/attributionen kildens faktiske
indhold? Kræver at *læse* kilden. Backends: primærkilde/bog, Elicit, scite, cbs-libsearch
(CBS-fuldtekst + highlight/annotation i artiklen). Sæt `claim_støttet` + `annotation_ref`.

`in_text_match` (om inline/tabel-gengivelse matcher bib) tjekkes i søsteren
`pm-konsistens-audit`; her registreres blot resultatet (match / drift-rettet / na).

---

## Hovedbogen (regnearket) — outputformat = revisionssporet

Skillen producerer og vedligeholder reference-audit-regnearket. **Skemaet (fulde
kolonne-definitioner, tilladte værdier, udfyldningsregler og eksempler) står i
`references/ledger_schema.md`.** Kort: de eksisterende identifikations- og
vurderingskolonner (`Kapitel, Bib-nøgle, Reference, Tier, p_correct/…,
Verificeringskommentar`) + provenans-kolonnerne (`verifikationsmetoder, antal_kilder,
kilde_evidens, annotation_ref, retraktionsstatus, claim_støttet, in_text_match,
verificeret_af, verifikationsdato, værktøj_version`).

Regel: **ingen kilde markeres verificeret uden en tilsvarende, provenans-fyldt række.**

---

## Præsentation — hovedbogen skal være overskuelig

Hovedbogen er et revisionsspor, forlag og læsere kan blive bedt om at se; derfor skal det
emitterede regneark være **pænt og overskueligt**, ikke bare korrekt. Konventionen
(obligatorisk; anvendes deterministisk af `scripts/ledger_format.py`, fuld spec i
`references/regneark_layout.md`):

- **Fane-rækkefølge:** `Læsevejledning` (forrest) → `Oversigt` → datafaner → `Fejl fundet & rettet` (bagerst).
- **Læsevejledning** forrest: fane-indhold + fuld kolonne-legende + udfoldede metode-koder +
  værdi-vokabularer + note om, at `ikke tjekket` er et *ærligt* signal. **Ingen forkortelse
  uden forklaring** — brug forkortelser, en læser forstår.
- **Datafaner:** stylede, frosne overskrifter, autofilter, tilpassede kolonnebredder,
  tekstombrydning på lange felter, let stribning.
- **Fejl-/rapportside bagerst:** kort rapporttekst + fejltabel (`# · Type · Kilde/sted ·
  Kapitel · Hvad var forkert · Rettelse · Verificeret via · Konfidens · Delt m. DA? ·
  DA-pendant · RUN · Status`).

Skriv aldrig til masteren; formatér altid en versioneret kopi.

---

## Deklarationsprodukter (afledt af hovedbogen)

Genereres fra hovedbogen, så bogen opfylder forlagenes transparens-/ansvarlighedskrav:

1. **In-book erklæring** (forord/kolofon) — kort "Declaration of AI technologies / kilde­
   verifikation": hvilke værktøjer (navn+version), hvordan, og at forfatteren har
   efterprøvet og hæfter. Følg dit forlags konkrete formulering.
2. **Valgfrit verifikations-/AI-appendiks** — hvis forlaget beder om det (fx ved omfattende
   brug): metode, dækning, backends, hvad der blev flagget og rettet, med tal.
3. **Internt metodenotat** — til forlagets egen due diligence (mange forlag kører selv
   reference-/retraktionstjek ved indlevering; et klart spor letter det).

> Forlagspolitik varierer (in-book erklæring? opbevaret dokumentation? appendiks?).
> Bekræft dit konkrete forlags krav; postulér det aldrig.

---

## Arbejdsgang

### Fase 0 — Indtag, backup, log
Identificér manuskript + `references.bib` + evt. eksisterende hovedbog. **Backup først.**
Åbn `KOERSELSLOG.md`: tidsstempel, filer + hashes, skill-version, backends til rådighed.

### Fase 1 — Seed hovedbogen (deterministisk)
Fra `references.bib`: én række pr. bib-nøgle. Fra manuskript-`.tex`: udtræk in-text
`(Forfatter, År)` og (via/parallelt med `pm-konsistens-audit`) markér fantomer/forældreløse.
Kun resolvbare, faktisk citerede kilder går videre til ekstern verifikation.

### Fase 2 — Verificér (de tre tjek)  *(stop for GATE efter en batch)*
Kør tjek 1–3 pr. kilde med de tilgængelige backends. Degradér yndefuldt: mangler en backend,
mærk feltet `requires verification` frem for at gætte. Fyld provenans-kolonnerne løbende.

### Fase 3 — Menneskelig sign-off
Forfatteren gennemgår hver dom; sæt `verificeret_af` (initialer) + AI-assisteret (ja/nej) +
`verifikationsdato`. Uden sign-off er en kilde ikke "verificeret".

### Fase 4 — Emittér hovedbog + deklaration
Skriv den opdaterede ledger (xlsx + json, versioneret; master røres ikke uden GATE) og
generér deklarationsudkastene fra den.

### Fase 5 — Troskabs-selvtjek + log
Bekræft: intet kildefelt fabrikeret; hver "forkert" har ≥3 kilder; hver verificeret række
har provenans + sign-off; manuskriptet er urørt. Log resultatet. Rettelser i bogen kun via
separat GATE.

---

## Backends (pluggbare — værktøjs-agnostisk kerne)
CrossRef/DOI · OpenAlex · Semantic Scholar · Retraction Watch · Crossref Crossmark ·
scite (Reference Check) · Elicit · cbs-libsearch (CBS-fuldtekst + annotation) · Exa/web.
Kernen beskriver *metoden*; det konkrete værktøj er udskifteligt. Ingen enkelt backend er
autoritativ alene — konvergens mellem flere er standarden.

## Hvornår IKKE
- Intern konsistens/numre/krydsref/fantom-detektion → `pm-konsistens-audit`.
- Omskrivning af tekst, register, stavning → de respektive skills.
- Oversættelse → `academic-translation-da-en`.
- At *rette* i bogen (skillen flagger + dokumenterer; rettelser kører som separat GATE).

## Filer
- `references/ledger_schema.md` — fulde kolonne-definitioner + tilladte værdier + eksempler.
- `references/regneark_layout.md` — layout- & præsentationskonvention (faner, legende, formatering, fejlside).
- `references/declaration_templates.md` — skabeloner: in-book erklæring, AI-appendiks, metodenotat.
- `scripts/ledger_build.py` — læs-kun hjælper: seeder ledger fra `references.bib`, udtrækker
  in-text-cites, flagger fantom/forældreløs, emitterer ledger-skelet med provenans-kolonner.
- `scripts/ledger_format.py` — anvender præsentationskonventionen (styling + Læsevejledning +
  fejl-/rapportside) på en versioneret kopi; skriver aldrig til master.

### Reference-integritets-modul (CrossRef; kør på maskine med internet)
- `scripts/check_dois.py` — DOI-resolution + titel-match mod CrossRef → flag døde/forkerte DOI'er (tjek #1/#2). Læs-kun.
- `scripts/find_dois.py` — foreslår korrekt DOI (CrossRef titel-søgning) for de flagede → REPLACE eller REMOVE. Læs-kun.
- `scripts/metadata_check.py` — felt-for-felt verifikation (forfatter/journal/bind/sider/år) mod CrossRef. **Vigtigt:** felt-sammenlign ALDRIG mod et lav-konfidens titel-match (DOI-løse bøger/cases → falske positiver); flag i stedet "NO RELIABLE MATCH — verify manually". Læs-kun.
- Alle tre skriver rapporter (`DOI_CHECK_REPORT.md`, `DOI_FIX_PROPOSALS.md`, `METADATA_CHECK_REPORT.md`) og fødes ind i hovedbogen (ledger). Rettelser i bib/prosa kører altid som separat GATE (backup → assertion pr. edit → byte-diff → build → log).

### Claim-støtte / korrekt brug (tjek #3) — arbejdsgang
Metadata + DOI siger, at kilden ER den rigtige og korrekt beskrevet. **Tjek #3 siger, at
manuskriptet BRUGER den rigtigt** — det dybeste og mest oversete tjek. Manuel/LLM-drevet (kræver
at læse kilden), men fast metode:
1. Udtræk hver in-text-påstand knyttet til kilden ("Forfatter (år) viser, at …").
2. Find det konkrete understøttende sted i kilde-fuldteksten (PDF / `cbs-libsearch`).
3. Verdikt pr. påstand: **støttet / delvist / ikke støttet**. Ved *ikke støttet* → kilden er forkert
   for den påstand → **find en anden kilde**. Ret ALDRIG bare metadata for at "redde" en forkert kilde.
4. Dokumentér i en annoterings-record (`references/annotation_record.md`: påstand → citat → verdikt);
   fyld `claim_støttet` + `annotation_ref` i hovedbogen.
5. `scripts/annotate_claims.py` highlighter de understøttende passager fysisk i kilde-PDF'en →
   `*_ANNOTATED.pdf` (auditerbart bevis; rapporterer fraser den ikke kan finde = kandidat til "forkert kilde").
- `references/annotation_record.md` — format for claim-støtte-record.
- `scripts/annotate_claims.py` — highlighter claim-understøttende passager i kilde-PDF (PyMuPDF).
