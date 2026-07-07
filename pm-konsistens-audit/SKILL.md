---
name: pm-konsistens-audit
description: >-
  Konsistens- og referenceaudit af en LaTeX-fagbog/lærebog (dansk), med fokus på at
  numre er FORTLØBENDE pr. kapitel og at ALLE numeriske + semantiske henvisninger er
  korrekte. Brug når brugeren vil verificere/rette: fortløbende nummerering af
  Definition/Teoriboks/Perspektivboks/Case/Eksempel/Figur/Tabel; dangling
  krydshenvisninger (afsnit/Boks/Case/Figur/Tabel X.Y); at konceptregister og
  teorioversigt (Appendix) peger på RETTE afsnit/definitioner/bokse/floats; og at
  citationer i oversigtstabeller matcher references.bib. Triggere: "kategori-audit",
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
3. **Verificér semantik manuelt** for hvert flag (skillen foreslår, beslutter ikke).
   Byg begreb→afsnitstitel-kort fra `\section`-titler; sammenlign mod henvisningens mål.
4. **Ret transaktionelt.** For hver rettelse: assertér at ankeret (begreb + gammelt
   nummer) findes PRÆCIS 1 gang; erstat kun tallet; byte-diff skal vise KUN tilsigtede
   tegn, uændret linjetal, intakte danske tegn (øæå = c3 b8 / c3 a6 / c3 a5). Backup
   pr. batch. Log hver ændring.
5. **Genbyg og verificér i PDF** (pdftotext): nye værdier til stede, gamle værdier =
   0 forekomster, ingen fantom-referencer.

## Rør-ikke / beskyttet
Citater, citationer/forfattere/år/DOI, definerede term-navne, boks-ordlyd, tal.
Ret aldrig en citation uden eksplicit brugerbeslutning (flag som "beskyttet").

## Filer
- `scripts/audit_all.py` — deterministisk auditor (parametre: --src-glob, --register,
  --appendix, --aux). Skriver markdown-rapport.
