---
name: academic-danish-klarsprog
description: >-
  Register- og klarsprogsløft for DANSKE akademiske manuskripter (lærebøger,
  monografier, kapitler). Brug, når brugeren vil løfte dansk fagprosa mod et valgt
  målregister — "gør teksten klarere", "for tung/nominal", "substantivsyge",
  "verbalstil", "mere læsevenlig/motiverende", "luk anglicismerne", "for høj LIX".
  Arbejder gennem valgbare STILPROFILER kalibreret mod målbare træk (LIX,
  nominal/verbalstil-balance, anglicisme-tæthed, sætningsrytme, kohæsion,
  læser-tiltale, konkretisering/læsemotivation). OPT-IN / eksplicit. Den foreslår
  omskrivninger af BRØDTEKST og ændrer ALDRIG mening, teori, begreber, citationer,
  krydshenvisninger, tal eller ordlyd i bokse/citater/figurer. IKKE til
  stavning/komma/term-konsistens (det er søsteren academic-danish-consistency);
  IKKE til oversættelse (brug academic-translation-da-en).
license: MIT
metadata:
  family: academic-danish
  siblings: academic-danish-consistency
  related: academic-english-narrative (engelsk pendant), academic-translation-da-en
  version: 0.1.0
  evidence_base: references/forskningsgrundlag.md
---

# Akademisk dansk — klarsprog (register- og stemmeløft)

*Løfte*-halvdelen af `academic-danish`-familien. Hvor `academic-danish-consistency`
håndhæver ét mekanisk house-style (flag, ret ikke), **omskriver denne skill
brødtekst** mod et valgt **målregister** — klart, levende, motiverende akademisk
dansk uden tab af faglig præcision.

To designvalg gør den seriøs og sikker:

1. **Register er et valg, ikke smag.** Skillen eksponerer navngivne **stilprofiler**,
   hver defineret som indstillinger på *målbare* danske dials (se forskningsgrundlaget).
   Forfatteren vælger målet; skillen sigter efter det.
2. **Den omskriver prosa, aldrig indhold.** Samme beskyttede-indhold-disciplin som
   søsteren: teori, begreber, citationer, krydshenvisninger, tal og defineret
   terminologi samt al ordlyd i bokse/citater/figurer bevares uændret
   (`references/beskyttet_indhold.md`).

To mål, ikke ét: skillen tjener både **forståelse** (klarhed/læsbarhed) og
**læsemotivation** (lyst til at læse og synes om bogen) — to akser, der er empirisk
adskilte (se forskningsgrundlaget, §3).

---

## Designovervejelser og evidensgrundlag (læs her)

Skillen hviler på forskning, ikke på smag. Det fulde, kildebelagte grundlag med
konfidens-mærkning står i `references/forskningsgrundlag.md`. Hovedovervejelserne:

- **Verbalstil over nominalstil — fordi nominalisering belaster forståelsen.**
  Verbalsubstantiver ("træfældningen" frem for "at fælde træet") er en velkendt kilde
  til *krævende syntaks* i danske fagtekster (NyS/Nydanske Sprogstudier; Fang 2012;
  Snow 2010; Uccelli et al. 2015). Lektion: verbalisér, hvor det ikke koster
  fagpræcision — men ikke pr. automatik (nominalisering er også et nødvendigt
  fagredskab).
- **LIX er rådgivende — aldrig et mål i sig selv.** Björnsson advarede selv: jagter
  man LIX mekanisk, opstår en "mekanisk stil"; sproget forarmes (Björnsson 1971; jf.
  Rask; Reinholt). Lektion: brug LIX som *symptom*, prioritér *læseværdighed* over
  *læsbarhed*. Dialen viger for dømmekraften.
- **Læsemotivation er en selvstændig løftestang.** Situationel/tekstbåren interesse
  (konkretisering, "menneskeligt ansigt", fortælling, relevans, overraskelse) driver
  engagement og på sigt varig læselyst (Hidi & Renninger 2006; Guthrie et al. 2006;
  Hidi & Baird 1988). Det er "motivation til at synes om bogen" — nu forankret.
- **Præcision slår altid stil.** Hvis et klarheds- eller motivationsgreb ville sløre
  en påstand, bevares den præcise original.

Overvejelserne er bevidst synlige, så enhver læser — eller bedømmer ved en
offentliggørelse — kan se *hvorfor* skillen gør, som den gør.

---

## De hårde regler (arvet, ufravigelige)

1. **Kilden er læs-kun.** Foreslå omskrivninger; overskriv aldrig forfatterens filer
   stiltiende. Lever før/efter, så ændringer kan gennemses og fortrydes.
2. **Indholds- og referencetroskab er absolut.** En omskrivning bevarer det
   propositionelle indhold nøjagtigt: ingen påstand tilføjet, fjernet, styrket eller
   svækket. Hver citation, forfatter, år, DOI, `(afsnit x.y)`, tal og defineret
   term er byte-identisk. Ordlyd i bokse, citater og figurer omskrives aldrig.
3. **Respektér disciplinær norm og den valgte profil.** Overdriv ikke mod
   "letlæst" forbi målet. Når en sætnings præcision og dens "flow" er i konflikt,
   vinder præcisionen.
4. **Flag dømmekald.** Hvor en omskrivning risikerer at flytte en nuance, vis den som
   et forslag ved siden af originalen og forklar afvejningen. Konfidens H/M/L.

Findes en projekt-beslutningslog / skopos-brief, **vinder den** over profil-defaults.

---

## Stilprofiler (stemmeprofiler)

Fulde definitioner og dial-indstillinger i `references/stilprofiler.md`. Resumé:

| Profil | Til | Karakter |
|---|---|---|
| `laerebog-klarsprog` *(default)* | lærebogs-/monografi-brødtekst | klar, levende, verbal-lænende, LIX ~45–52, moderat læser-tiltale |
| `formidlende-engagerende` | introkapitler, cases, forord | varmere, mere konkretisering/"menneskeligt ansigt", højere motivationsgreb |
| `stram-faglig` | tætte teoriafsnit, metodeafsnit | mere nominal tolerance, lavere tiltale, høj præcision, LIX kan stige |

**Én default-profil pr. bog.** Variation pr. elementtype (fx cases mere
formidlende, teoriafsnit strammere) er tilladt, men skal erklæres og logges, så
bogen læses som ét værk.

---

## Arbejdsgang

### Fase 0 — Indtag, profilvalg, log åbnes
- Bekræft manuskriptmappe/filer og **målprofil** (default `laerebog-klarsprog`).
  Bekræft omfang (kapitler/afsnit).
- Åbn `KOERSELSLOG.md` fra skabelonen: tidsstempel, filer + hashes, valgt profil,
  skill-version, evt. beslutningslog.
- Kør evt. `scripts/maal.py` for baseline (LIX, nominal-suffiks-tæthed,
  anglicisme-proxy, sætningsstatistik). Log kommando og output.

### Fase 1 — Diagnose mod profilen
For hvert afsnit: identificér hvor prosaen afviger fra profilens dials (fx
substantivsyge, tung nominal-syntaks, anglicisme-klynger, flad rytme, lav
konkretisering). Lav en kort diagnose pr. kapitel knyttet til dials — ikke smag.

### Fase 2 — Foreslå omskrivninger (før/efter)
Omskriv brødtekst mod profilen. Lever hver ændring som:

`placering | før | efter | dial(s) | konfidens | note`

Rør aldrig beskyttet indhold. Hold hver omskrivning minimal — skift tekstur, ikke
mening.

### Fase 3 — Menings-troskabstjek *(før levering)*
For hver omskrivning bekræft:
- propositionelt indhold uændret (ingen påstand tilføjet/fjernet/omvægtet);
- alle citationer, henvisninger, tal, defineret-term-navne byte-identiske;
- intet beskyttet felt omskrevet.
Drop enhver omskrivning, der fejler (gendan originalen), og log årsagen. Angiv:
`Troskabstjek bestået: N omskrivninger, 0 påstande ændret, 0 beskyttede tokens rørt.`

### Fase 4 — Gen-mål & overlevering til konsistens
Kør `maal.py` igen og vis bevægelsen mod profilen. Da omskrivning kan genindføre
stave-/formatdrift, anbefal at køre **`academic-danish-consistency`** bagefter
(rækkefølge: klarsprogsløft → konsistens-oprydning).

---

## Kørselsloggen (sporbarhed)

`KOERSELSLOG.md` er revisionssporet: pr. kørsel header + filhashes, valgt profil,
baseline- og post-mål, hver omskrivning med dials + konfidens, troskabsresultatet og
hver droppet omskrivning med årsag. Regel: **ingen prosaændring leveres uden en
tilsvarende loglinje.**

## Hjælpescript: `scripts/maal.py`

Læs-kun danske mål, så profilerne er målbare frem for subjektive: LIX,
gennemsnitlig sætningslængde/varians, nominal-suffiks-tæthed (verbalsubstantiver),
anglicisme-proxy (ordliste), passiv-proxy (s-passiv/blive-passiv), læser-tiltale
(du/vi/man). Rapporterer tal og (valgfrit) hvor en fil ligger ift. en profils
vejledende bånd. Skriver aldrig til kildefiler.

```bash
python scripts/maal.py --input <mappe-eller-glob> --profil laerebog-klarsprog \
    --out maal.md --log KOERSELSLOG.md
```

## Hvornår IKKE
- Stavning/komma/term-/formatkonsistens → `academic-danish-consistency`.
- Ændring af mening, teori, data eller fagligt indhold.
- Oversættelse → `academic-translation-da-en`.

## Filer
- `references/forskningsgrundlag.md` — kildebelagt evidens (konfidens-mærket).
- `references/stilprofiler.md` — profiler + målbare dials.
- `references/beskyttet_indhold.md` — troskabszone (indhold/teori/citationer).
- `references/koerselslog_skabelon.md` — revisionsspor → `KOERSELSLOG.md`.
- `scripts/maal.py` — læs-kun danske register-/læsbarhedsmål.
