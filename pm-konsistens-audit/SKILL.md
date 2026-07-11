---
name: pm-konsistens-audit
description: >-
  Konsistens- og referenceaudit af en LaTeX-fagbog/lærebog (dansk), med fokus på at
  numre er FORTLØBENDE pr. kapitel og at ALLE numeriske + semantiske henvisninger er
  korrekte. Brug når brugeren vil verificere/rette: fortløbende nummerering af
  Definition/Teoriboks/Perspektivboks/Case/Eksempel/Figur/Tabel; dangling
  krydshenvisninger (afsnit/Boks/Case/Figur/Tabel X.Y); at konceptregister og
  teorioversigt (Appendix) peger på RETTE afsnit/definitioner/bokse/floats; og at
  citationer i oversigtstabeller matcher references.bib; samt REFERENCE-INTEGRITET: prosa-
  citationer (forfatter-år) der mangler en references.bib-nøgle, dublet-poster (samme DOI/titel),
  orphan-nøgler, og nøglenavn↔år-felt-mismatch. Triggere: "kategori-audit", "reference-integritet",
  "prosa citation uden nøgle", "dublet reference", "bib-audit",
  "fortløbende numre", "tjek henvisninger", "konceptregister konsistens", "Appendix B
  konsistens", "peger figur/tabel-referencer rigtigt", "dangling references".
  OPT-IN. Flagger og foreslår — ændrer aldrig mening/tal/citater uden eksplicit OK;
  redigerer transaktionelt med assertion pr. linje + byte-diff-verifikation.
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
review-kandidater der IKKE fælder "RENT ✓". Scriptet deaccenter prosaen (ö→o, é→e) og
fjerner genitiv-'s før navne-udtræk for at dæmpe falske positiver — men A-listen kræver
altid menneskelig filtrering.

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

## Rør-ikke / beskyttet
Citater, citationer/forfattere/år/DOI, definerede term-navne, boks-ordlyd, tal.
Ret aldrig en citation uden eksplicit brugerbeslutning (flag som "beskyttet").

## Filer
- `scripts/audit_all.py` — deterministisk, læs-kun auditor. Parametre: `--src` (glob, default
  `kap*_body.tex`), `--aux` (default `main.aux`; springes over hvis fraværende), `--bib` (default
  `references.bib`; aktiverer sektion 3 reference-integritet), `--register` (default
  `konceptregister_body.tex`) og `--appendix` (default `09_Back_Matter/appendiks_b_teorioversigt.tex`)
  til sektion 5 typeløse box-pointere; `--out` (markdown-rapport).
  Sektion 4 (kapitel-skabelon) + sektion 5 (typeløse box-pointere) kører altid — kræver kun `.tex`.
  Eksempel: `python3 scripts/audit_all.py --src "kap*_body.tex" --aux main.aux --bib references.bib --register konceptregister_body.tex --appendix 09_Back_Matter/appendiks_b_teorioversigt.tex --out KATEGORI_AUDIT.md`
