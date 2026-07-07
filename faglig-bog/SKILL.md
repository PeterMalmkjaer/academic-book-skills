---
name: faglig-bog
description: Hjælper med at skrive, strukturere og producere en akademisk lærebog eller monografi inden for samfundsvidenskab — særligt i LaTeX. Brug denne skill når brugeren nævner bogprojekt, lærebog, monografi, kapitelstruktur, LaTeX-kompilering, referencehåndtering, konceptregister, forord, copyright, front matter, trykkvalitet eller oversættelse af en faglig bog. Brug den også når brugeren nævner AI-assisteret bogskrivning, terminologisk nøgle, rød tråd i en bog, kapitelskabelon, eller nummeringssystem for bokse og cases.
---

# Faglig Bog — Skabeloner og Praksis

En skill til at hjælpe med alle faser af at skrive en akademisk lærebog eller monografi.
Udviklet og testet på PM-bogen (Performance Management, CBS, 2026) — 369 sider, 17 kapitler, LaTeX.

---

## Rækkefølge — typografi/cover kører SIDST (kritisk)

Denne skill dækker **LaTeX-build, typografi, overfull/pagination, floats og cover** —
bogens **form-fase**. Form afhænger af den endelige tekst, så kør disse trin **først når
teksten er frossen**:

```
A. Indhold & korrekthed  (oversættelse → fakta/citation → krydsref → register/narrativ → grammatik)
B. Konsistens            (stavning/husstil)
   ▶▶▶  TEKST-FRYSE  ◀◀◀
C. Form & layout — DENNE skill:  nummerering/float-kontinuitet → typografi/overfull → cover
D. Endelig build         (ægte build: sider, 0 undefined, overfull-optælling, visuel gennemsyn)
```

**Jernregel:** kør aldrig overfull-triage eller cover-indsætning før indhold, register og
konsistens er låst. Enhver senere ord-ændring reflower bogen og invaliderer et tidligere
typografi-pass — kør typografi + build igen. (Lært på den hårde måde på en rigtig lærebog,
hvor typografien blev kørt før grammatik/citations-passet; verifikationen var forældet, og en
sen layout-fejl slap igennem.)

---

## De 12 Skabeloner

Tre niveauer: **Strategisk** (beslut ved start), **Løbende** (oprethold undervejs), **Refleksivt** (bevidste valg).

---

### STRATEGISKE SKABELONER (beslut FØR kapitel 1)

**Skabelon 1 — Bogens dobbelte identitet**
Afklar om bogen er monografi, lærebog, eller begge. Skriv ½ side der besvarer:
- Hvem er den primære læser?
- Hvad er bogens samlede argument?
- Er det monografi, lærebog, eller begge?

Returner til dette dokument halvvejs i projektet.

**Skabelon 2 — Terminologisk nøgle fra dag ét**
Regneark med kolonnerne: `Begreb | Definition | Primærkilde (forfatter, år) | Fremmedsprog ækvivalent | Kapitler`
Opdateres ved hvert nyt centralt begreb. Bruges som tjekliste ved korrektur.
*Kritisk ved oversættelse:* "incitamentsintensitet" = "incentive intensity" i Lazear & Gibbs — ikke "incentive strength".

**Skabelon 3 — Referencestrategi og verifikation undervejs**
For hvert kapitel: mini-referencedokument med `Reference | Verificeret (ja/nej/delvis) | Konkret brug`.
Verificer inden næste kapitel. 15-30 min per kapitel. Sparer timer ved slutkorrektur.
*Kildetyper:* peer-reviewed (fri citering) / working paper offentliggjort (fri citering) / HBS-cases (kommercielt licenseret — undgå reproduktion).

**Skabelon 4 — Kapitelskabelon som kontrakt med læseren**
Én-sides dokument ved start: hvilke faste elementer hvert kapitel indeholder.
*PM-bogens skabelon:* læringsmål → perspektivbox → brødtekst (definitionsbokse + theoryboxe) → sammenfatning → perspektivering → diskussionsspørgsmål.
Afvigelser kræver bevidst beslutning — ikke en glemt forpligtelse.

**Skabelon 5 — Den røde tråd som eksplicit dokument**
For hvert kapitel skriv én sætning:
> *"Dette kapitel forudsætter [X] fra kapitel [N] og introducerer [Y] som bruges i kapitel [M]."*

Kan sætningen ikke skrives er kapitlets placering sandsynligvis forkert.
Saml alle sætninger i ét dokument — det er bogens interne arkitektur.

---

### LØBENDE SKABELONER (oprethold konsekvent)

**Skabelon 6 — AI som strukturpartner, ikke forfatter**
Skriv en ½-sides AI-politik ved start:
- Hvad AI bruges til: strukturering, formulering, nummeringskontrol
- Hvad AI IKKE bruges til: faglig vurdering, argumentets originalitet, afgøre om analyse er korrekt
- Hvordan AI-brug dokumenteres (fx i forord/tilblivelsesafsnit)

Revider politikken halvvejs — erfaringen vil have ændret praksis.

**Skabelon 7 — Nummeringssystem tidligt og globalt**
Regneark med én fane per elementtype: `Kapitel | Nr | Titel | Linje i fil`
Opdateres ved hvert nyt element (case, definitionsboks, theorybox, figur, tabel).
*Konsekvens ved manglende disciplin:* retrospektiv rettelse af 48 cases og 52 theoryboxe på tværs af 17 kapitler.

**Skabelon 8 — Copyright-håndtering løbende**
Tilføj kolonne i referencedokumentet: `Kildetype (peer-reviewed / working paper / HBS-case / årsrapport)`
Markér alle kommercielt licenserede cases eksplicit ved indsættelsen.
Beslut strategi fra start: undgå / skriv egen case / indhent tilladelse.

**Skabelon 9 — Trykkvalitet fra kompilering 1 (LaTeX)**
Efter hvert 3. kapitel: kør fuld kompilering og løs alle overfull hbox > 20pt.
Hold log: `Problem | Kapitel | Status (åbent/løst/accepteret) | Begrundelse`
*Konkrete fixes:* soft hyphens (`\-`) i lange sammensatte ord, `\texorpdfstring` for matematik i section-titler, kolonnebredder i longtable, `\chapter[kort]{lang}` for lange titler.

**Skabelon 10 — Konceptregister som levende dokument**
For hvert nyt element (definition, theorybox, case, figur): tilføj i register STRAKS. 30 sekunder per element.
*Konsekvens ved at vente:* retrospektiv tilføjelse af 83 definitioner og 52 theoryboxe kræver gennemgang af alle kapitler.

---

### REFLEKSIVE SKABELONER (bevidste valg)

**Skabelon 11 — Front matter sidst, planlagt først**
Skriv placeholder-forord ved start med: hvem er læseren / hvad er argumentet / min baggrund.
Skriv den endelige version SIDST. Forventet at den endelige version ligner lidt placeholderen.
*Elementer der kun kan skrives bagfra:* bogens dobbelte karakter, refleksion over AI-brug, præcision om forfatterens baggrund.

**Skabelon 12 — Central dokumentationsfil opdateres ved hver session**
Én fil med tre sektioner:
1. **Aktuel status:** versionsnummer, sidetal, seneste output, næste skridt
2. **Åbne punkter:** prioriteret liste, hvad accepteres og hvorfor
3. **Kronologisk log:** dato, hvad der blev gjort, beslutninger (ikke kun handlinger)

---

## LaTeX-specifikke Anbefalinger

### Dokumentklasse og struktur
```latex
\documentclass[11pt,a4paper,twoside,openright]{book}
\usepackage{fontspec}
\usepackage{polyglossia}
\setdefaultlanguage{danish}  % eller relevant sprog
```

`openright` = kapitler starter altid på højreside → 18 blanke venstresider i en 17-kapitels bog er korrekt og normalt.

### Boksmiljøer (tcolorbox)
```latex
\newtcolorbox{definitionbox}[1][]{ ... }
\newtcolorbox{theorybox}[1][]{ ... }
\newtcolorbox{casebox}[1][]{ ... }
\newtcolorbox{perspectivebox}[1][]{ ... }
```

### Hyppige print-fix problemer
| Problem | Fix |
|---------|-----|
| Lang kapitel-titel i header | `\chapter[Kort version]{Lang fuld titel}` |
| Matematisk symbol i PDF-bookmark | `\texorpdfstring{$\beta$}{beta}` |
| Lange sammensatte ord | Soft hyphens: `med\-ar\-bej\-der\-til\-freds\-heds\-må\-lin\-gen` |
| Smal tabelkolonne | Justér `p{2.2cm}` → `p{3.5cm}` i longtable |
| Linjeskift i lang brødtekst | Omskriv til kortere sætninger — `\\` virker ikke i brødtekst |

### Byg-kommando
```bash
xelatex -interaction=nonstopmode main.tex
# Tjek log:
grep -E "Overfull|^!" main.log
```

---

## Referencehåndtering — Verificeringsniveauer

| Niveau | Betegnelse | Krav |
|--------|-----------|------|
| T1 | Indholdverificeret | Læst og verificeret mod primærkilde |
| T2 | Metadata kun | Titel/forfatter/år verificeret, ikke indhold |

Mål: alle referencer på T1 inden aflevering til tryk.

---

## Oversættelsesstrategi (dansk → engelsk)

Anbefalet stilistisk reference: CBS working papers (Friis, Boe & Hansen 2023 / Hansen 2019).
Dette er kontinentaleuropæisk management accounting-stil — forklarende, struktureret, propositionsdrevet.
*Ikke* den komprimerede AER/JPE-stil.

Målgruppe for engelsk version: europæiske akademikere med engelsk som 2./3. sprog.
Krav: terminologisk præcision + grammatisk korrekthed. Native feel er ikke kritisk.

Terminologisk nøgle (eksempler):
| Dansk | Engelsk (korrekt fagterm) |
|-------|--------------------------|
| Incitamentsintensitet | Incentive intensity (β) |
| Ratchet-effekt | Ratchet effect |
| Crowding out | Motivation crowding-out |
| Moral hazard | Moral hazard |
| Præstationsbaseret løn | Pay for performance |
| Selvselektionseffekt | Self-selection |
| Informationsprincippet | Holmström's informativeness principle |
| Organisatorisk retfærdighed | Organizational justice |

---

## Copyright — Hurtig Reference

| Kildetype | Brug | Kræver |
|-----------|------|--------|
| Peer-reviewed artikel | Fri citering med reference | Korrekt kildeangivelse |
| Offentliggjort working paper | Fri citering med reference | Korrekt kildeangivelse |
| HBS-cases | Kommercielt licenseret | Undgå reproduktion — skriv egne cases |
| Figurer fra bøger | Begrænset | Tilladelse ved kommerciel udgivelse |
| Teoretiske begreber | Frit | Begreber er ikke ophavsretligt beskyttede |

Working papers er offentliggjorte dokumenter — de kan og bør citeres med korrekt kildeangivelse.
Ophavsretten tilhører forfatterne (ikke institutionen) i dansk akademia.

---

## Prioriteret Tjekliste ved Projektstart

- [ ] Skriv bogens identitetsdokument (Skabelon 1)
- [ ] Opret terminologisk nøgle-regneark (Skabelon 2)
- [ ] Opret nummeringssystem-regneark (Skabelon 7)
- [ ] Skriv kapitelskabelon (Skabelon 4)
- [ ] Skriv rød tråd for alle planlagte kapitler (Skabelon 5)
- [ ] Skriv AI-politik (Skabelon 6)
- [ ] Opret MASTER_TODO.md med de tre sektioner (Skabelon 12)
- [ ] Skriv placeholder-forord (Skabelon 11)

---

## Vigtigste enkeltskabelon

**Skabelon 3 (verifikation undervejs)** er den vigtigste.
Den lader sig gøre på 15 min per kapitel — og vokser til mange timers arbejde hvis den udsættes.

**Skabelon 5 (rød tråd)** er det der adskiller en samling essays fra en bog.
