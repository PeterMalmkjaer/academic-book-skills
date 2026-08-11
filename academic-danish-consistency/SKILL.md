---
name: academic-danish-consistency
description: >-
  Bogdækkende dansk house-style-KONSISTENS-audit for akademiske manuskripter
  (lærebøger, monografier, flerkapitelværker). Brug, når brugeren vil håndhæve ÉT
  konsistent dansk skriftbillede på tværs af en hel bog — retskrivning, komma,
  dansk/engelsk-håndtering af fagtermer (hvornår oversættes/beholdes/forklares),
  labels (Figur/Boks/Tabel), overskrifts-konvention (sætningscase), citations- og
  krydshenvisningsformat, decimalkomma — ved at UDLEDE et stilark og en termbase fra
  kapitlerne og derefter FLAGGE afvigelser (aldrig stiltiende omskrive). Triggere:
  "konsistens-gennemgang", "house style", "stilark", "dansk/engelsk-håndtering",
  "ensret hele bogen", "term-/format-konsistens". OPT-IN / eksplicit — kører ikke
  automatisk på enkeltdokument-redigering. IKKE til flow/stil/register (det er
  søsteren academic-danish-klarsprog); IKKE til ændring af mening/teori/citationer;
  IKKE til oversættelse.
license: MIT
metadata:
  family: academic-danish
  siblings: academic-danish-klarsprog
  related: academic-english-consistency (engelsk pendant), academic-translation-da-en
  version: 0.1.0
---

# Akademisk dansk — konsistens (house-style-audit)

Standalone, disciplin-agnostisk skill, der kører én gentagelig **konsistens-gennemgang**
over et helt dansk akademisk manuskript. *Håndhævelses*-halvdelen af `academic-danish`-
familien:

- **`academic-danish-consistency`** (denne) — mekanik: retskrivning, komma,
  dansk/engelsk-term-håndtering, labels, overskrifts-case, citations-/henvisningsformat.
  Regelbaseret, deterministisk, bogdækkende. **Flag, omskriv aldrig stiltiende.**
- **`academic-danish-klarsprog`** (søster) — register: verbalstil, klarsprog,
  læsemotivation. Dømmekraftsbaseret, kapitel for kapitel. *Lav ikke register-arbejde her.*

Den danske familie har én akse, som den engelske ikke har: **dansk/engelsk-håndtering**
af fagtermer. Den *konsistensmæssige* del (samme begreb gengivet ens; politik besluttet
én gang; ingen danglish i labels) hører her; den *kvalitative* del (er en anglicisme
klodset?) hører i klarsprog-søsteren; selve *oversættelsen* i `academic-translation-da-en`.

---

## De fire hårde regler (ufravigelige)

1. **Kilden er læs-kun.** Redigér, slet eller omskriv aldrig forfatterens filer. Output
   er observationer, et stilark, en termbase, kapitelrapporter og en kørselslog.
2. **Reference- og indholdstroskab er absolut.** Ingen citation, forfatter, år, DOI,
   defineret-term-navn, afsnit-/kapitelhenvisning, citat, bokskilde, figurlabel eller
   tal ændres eller foreslås ændret. Ville en regel røre noget af dette, **springes den
   over og logges som `tjek (beskyttet)`**.
3. **Stol-på-kilden som udgangspunkt.** En korrekturlæst udgave har oftest ret. Ser noget
   inkonsistent ud, så antag pædagogisk hensigt, til der er stærk evidens. Formulér flag
   som *observationer til verificering*, ikke *fejl*.
4. **Flag, ret ikke. Ved tvivl: lad stå.** Hvert forslag bærer placering, nuværende
   tekst, foreslået tekst, regel og konfidens (H/M/L). Foreslå aldrig under høj konfidens.

Findes en projekt-beslutningslog / skopos-brief, **vinder den** over skillens defaults.

---

## Beskyttet indhold — kun format tjekkes, ordlyd røres aldrig

Se `references/beskyttet_indhold.md`. Kort: definitioner, teori-/perspektiv-/case-/
sammenfatningsbokse, figur-/tabeltekster og -labels, direkte citater og epigrafer,
citationer/forfattere/år/DOI, "Videre Læsning", krydshenvisninger og afsnits-/kapitel­numre,
samt defineret-term-navne (kun deres *format* — fed ved første brug — tjekkes).

---

## Arbejdsgang

Kør faserne i rækkefølge. **Stop efter Fase 1 for godkendelse** — de kanoniske valg
afgør, hvad der siden tæller som afvigelse.

### Fase 0 — Indtag & log
- Identificér manuskriptmappe og filtype (`.tex` foretrukket; `.docx`/`.md`/`.txt`/PDF-
  tekst accepteres). Bekræft omfang.
- Åbn `KOERSELSLOG.md`: tidsstempel, filer + hashes, skill-version, evt. beslutningslog.
- Kør evt. `scripts/scan_da.py` for deterministiske tællinger. Log kommando + output.

### Fase 1 — Udled stilarket  *(stop derefter for godkendelse)*
Scan alle kapitler og udled den **dominerende** konvention for hvert punkt i
`references/tjekpunkter.md`. Hvor bogen er splittet, rapportér splittet **med tal** og
anbefal ÉT kanonisk valg. Producér `STILARK.md` fra skabelonen. Fortsæt ikke uden
forfatterens godkendelse.

### Fase 2 — Byg termbasen
Notér hvert tilbagevendende begreb og de overfladeformer, det optræder i (fx
"performance management / PM"; "intrinsisk / indre motivation"; engelsk fagterm vs.
dansk gengivelse). Markér den kanoniske form; flag afvigelser. Samme for
forfatternavne og forkortelser. **Beslut dansk/engelsk-politikken eksplicit** (hvilke
termer beholdes på engelsk, hvilke fordanskes, hvilke forklares ved første brug).
Producér `TERMBASE.md`.

### Fase 3 — Afvigelsesrapport pr. kapitel
Pr. kapitel en tabel:

`fil | placering | nuværende | foreslået | regel | konfidens | beskyttet?(J/N)`

Kun afvigelser fra det godkendte stilark og termbasen, **i brødtekst**. Afvigelser i
beskyttet indhold rapporteres som `tjek (beskyttet)` uden forslag. Grupper efter regel;
afslut hvert kapitel med tal pr. kategori. Append hver række til loggen.

### Fase 4 — Troskabs-selvtjek  *(før levering)*
For hvert forslag bekræft: det rører kun det målrettede retskrivnings-/formattoken; alle
citationer, forfattere, år, `(afsnit x.y)`-henvisninger, tal og defineret-term-navne er
byte-identiske; intet forslag ligger i beskyttet indhold. Drop fejlende (flyt til `tjek`)
og log årsagen. Angiv: `Troskabstjek bestået: N forslag, 0 beskyttede tokens ændret.`

---

## Kørselsloggen (sporbarhed)
`KOERSELSLOG.md` er revisionssporet: header + filhashes, Fase 1-beslutninger med
godkendelses-tidsstempel, hvert flag + konfidens, troskabsresultatet, og alt sprunget
over med årsag. Regel: **ingen kildeændring uden en tilsvarende loglinje.**

## Deterministisk hjælper: `scripts/scan_da.py`
Læs-kun tæller for de objektive tjek: dansk/engelsk-signaler (danglish labels
"Figure"/"Box", engelske ord midt i dansk via ordliste), overskrifts-case (Title Case
vs. sætningscase), decimal-separator (komma vs. punktum), krydshenvisningsformat,
anførselstegn, dobbeltmellemrum. Producerer tal + linjeplacerede hits til Fase 1/3 —
men er en **hjælp, ikke autoritet**: LLM-laget bekræfter beskyttet-status og dømmekald.

```bash
python scripts/scan_da.py --input <mappe-eller-glob> --out <rapport.md> --log <KOERSELSLOG.md>
```

## Hvornår IKKE
- Flow/rytme/register/verbalstil → `academic-danish-klarsprog`.
- Enkeltdokument-korrektur uden bogdækkende sigte.
- Ændring af mening, teori, argument eller indhold.
- Oversættelse → `academic-translation-da-en`.

## Filer
- `references/tjekpunkter.md` — regelkatalog (hvad Fase 1 beslutter).
- `references/stilark_skabelon.md` — beslutningsskabelon → `STILARK.md`.
- `references/beskyttet_indhold.md` — rør-ikke-zone + detektionsheuristik.
- `references/koerselslog_skabelon.md` — revisionsspor → `KOERSELSLOG.md`.
- `scripts/scan_da.py` — deterministiske mekaniske tjek (læs-kun).
