# KOERSELSLOG — academic-danish-klarsprog

Append-only revisionsspor. Én blok pr. kørsel. Overskriv aldrig tidligere blokke.
Formål: hver prosaændring skal kunne spores til den nøjagtige omskrivning, profil og
kørsel. **Ingen omskrivning leveres uden en tilsvarende loglinje.**

---

## KØRSEL <n> — <ÅÅÅÅ-MM-DD TT:MM:SS TZ>

### 1. Header
- Skill-version: 0.1.0
- Operatørens anmodning (ordret): "<indsæt præcis instruktion>"
- Målprofil: <laerebog-klarsprog | formidlende-engagerende | stram-faglig>
- Element-type-overstyringer (hvis nogen): <fx cases→formidlende-engagerende; erklæret>
- Filer i scope (sti — sha256 — ordtal):
  - <kapitelXX.tex — a1b2c3… — 4690>
- Beslutningslog / skopos-brief brugt: <sti eller "ingen">

### 2. Baseline-mål (maal.py)
- Kommando: `<præcis kommando>`  → output: `<sti>`
| fil | LIX | sætn.længde middel | sætn.SD | nominal/1k | anglicismer | du/vi/man-tiltale |
|---|---:|---:|---:|---:|---:|---:|
| | | | | | | |

### 3. Fase 1 — diagnose mod profilen
- <kapitel/afsnit — hvilke dials afviger og hvordan>

### 4. Fase 2 — omskrivninger
| placering | før | efter | dial(s) | konfidens | note |
|---|---|---|---|---|---|
| | | | | | |

### 5. Fase 3 — menings-troskabstjek
- Omskrivninger vurderet: <N>
- Droppet (fejlede troskab), med årsag:
  - <placering — årsag, fx: omskrivning svækkede et forbehold>
- Resultatlinje: `Troskabstjek bestået: <N> omskrivninger, 0 påstande ændret, 0 beskyttede tokens rørt.`

### 6. Fase 4 — post-mål & overlevering
- Post maal.py: <bevægelse mod profilen; bemærk: LIX aldrig auto-handlet>
- Konsistens-overlevering anbefalet? <Ja/Nej — kør academic-danish-consistency bagefter>

### 7. Spring & ikke-handlinger
- <felt/sætning ikke omskrevet og hvorfor: beskyttet / præcision-over-flow / lav konfidens / LIX-symptom ikke handlet>

### 8. Output skrevet denne kørsel
- diagnose_kapitelXX.md
- omskrivninger_kapitelXX.md (før/efter)
- maal_foer.md / maal_efter.md
- denne logblok

---
<!-- næste kørsel appender herunder; redigér ikke blokke ovenfor -->
