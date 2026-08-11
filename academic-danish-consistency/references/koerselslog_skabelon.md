# KOERSELSLOG — academic-danish-consistency

Append-only revisionsspor. Én blok pr. kørsel. Overskriv aldrig tidligere blokke.
**Ingen kildeændring foreslås uden en tilsvarende loglinje.**

---

## KØRSEL <n> — <ÅÅÅÅ-MM-DD TT:MM:SS TZ>

### 1. Header
- Skill-version: 0.1.0
- Operatørens anmodning (ordret): "<indsæt præcis instruktion>"
- Fase(r) kørt: <0 / 1 / 2 / 3 / 4>
- Filer i scope (sti — sha256 — ordtal):
  - <kapitelXX.tex — a1b2c3… — 4690>
- Projekt-beslutningslog / skopos-brief brugt: <sti eller "ingen">

### 2. Input
- scan_da.py-kommando: `<præcis kommando>`  → output: `<sti>`
- Råtal: <fx Figure: 1 / Boks-hybrid: 3 ; Title-Case-overskrifter: n ; punktum-decimaler: n>

### 3. Fase 1 — kanoniske beslutninger
| Punkt | Kanonisk valgt | Split-tal | Konfidens | Begrundelse |
|---|---|---|---|---|
| | | | | |
- Forfatter-godkendelse: <navn> @ <tidsstempel>  (KRÆVET før Fase 3)

### 4. Fase 2 — termbase-afvigelser
| Begreb | Kanonisk | Variant fundet | Placering | Handling |
|---|---|---|---|---|
| | | | | flag / tjek |
- Dansk/engelsk-politik besluttet: <kort>

### 5. Fase 3 — flag (pr. kapitel)
| fil | placering | nuværende | foreslået | regel | konf. | beskyttet? | status |
|---|---|---|---|---|---|---|---|
| | | | | | | N | foreslået |
| | | | | | | J | tjek (beskyttet) |

### 6. Fase 4 — troskabs-selvtjek
- Forslag vurderet: <N>
- Droppet (fejlede troskab), med årsag:
  - <placering — årsag>
- Resultatlinje: `Troskabstjek bestået: <N> forslag, 0 beskyttede tokens ændret.`

### 7. Spring & ikke-handlinger
- <punkt — hvorfor ikke tjekket: beskyttet / lav konfidens / allerede konsistent>

### 8. Output skrevet denne kørsel
- STILARK.md (<udkast|godkendt>)
- TERMBASE.md
- rapport_kapitelXX.md
- denne logblok

---
<!-- næste kørsel appender herunder; redigér ikke blokke ovenfor -->
