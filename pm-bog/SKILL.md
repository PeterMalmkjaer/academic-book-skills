---
name: pm-bog
description: OPT-IN ONLY — Do NOT read or use this skill unless the user explicitly asks for it by name (e.g., "brug pm-bog", "use pm-bog skill", "hent pm-bog"). This skill provides chapter structure, LaTeX build instructions, box definitions, known-good baseline facts, and workflow patterns for the Performance Management textbook (PM-bogen) at CBS. Never trigger automatically based on topic detection.
---

# PM-Bog Skill — v28 Baseline (2026-03-17)

Akademisk lærebog i Performance Management for cand.merc.SAM studerende, CBS.
Forfatter: Peter Malmkjær, Department of Operations Management.

**Known-good baseline: v28 — 368 sider, 0 LaTeX-fejl, 0 advarsler, 1.6 MB (2026-03-17)**

---

## 0. Rækkefølge — typografi/cover kører SIDST (kritisk)

Denne skill dækker bl.a. **LaTeX-build, typografi, overfull/pagination og cover** —
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
typografi-pass — kør typografi + build igen. (Lært på den hårde måde: på PM-bogens EN-udgave
blev typografien kørt før grammatik/citations-passet; verifikationen var forældet, og en sen
layout-fejl (sort tom bagside) slap igennem.)

---

## 1. Bogidentitet

| Felt | Værdi |
|------|-------|
| Titel | Performance Management |
| Undertitel | Design, Dilemmaer og Løsninger i en tid med mere og mere AI |
| Forfatter | Peter Malmkjær |
| Institution | Copenhagen Business School, Department of Operations Management |
| Målgruppe | cand.merc.SAM studerende (kandidatniveau) |
| Sprog | Dansk (primært), engelsk fagterminologi i parentes ved første brug |
| LaTeX-motor | XeLaTeX (kræver TeX Gyre Pagella, TeX Gyre Heros, DejaVu Sans Mono) |
| Baseline version | v28 — 368 sider, 0 fejl (2026-03-17) |

---

## 2. Filstruktur (iCloud)

```
/Users/petermalmkjaer/Library/Mobile Documents/com~apple~CloudDocs/Claude/PM_Textbook/
├── main.tex                        # Master build-fil — inkluderer alle body-filer
├── references.bib                  # 187 poster, alle T1-verificerede
├── cover_image.png / .jpg          # Forsidebillede (skal kopieres til build-mappe)
├── kap01_body.tex … kap17_body.tex # Body-filer (bruges i build — IKKE standalone)
├── kap01_standalone.tex … kap17_standalone.tex  # Kildefiler (redigeres her)
├── appendiks_d_body.tex            # Appendiks D body
├── konceptregister_body.tex        # Konceptregister (root-kopi bruges i build)
├── 00_Front_Matter/
│   ├── titlepage.tex
│   ├── copyright.tex
│   ├── forord.tex
│   ├── kapiteloversigt.tex
│   └── tilblivelse.tex
├── 09_Back_Matter/
│   ├── konceptregister_body.tex    # Backup-kopi (root-kopien bruges i build)
│   ├── appendiks_a_matematik.tex   # [TODO — tom, MÅ IKKE inkluderes i build]
│   ├── appendiks_b_teorioversigt.tex # [TODO — tom, MÅ IKKE inkluderes i build]
│   └── appendiks_c_ordliste.tex    # Ordliste (færdig)
├── backups/
│   └── backup-2026-03-18-forord-monografi/  # v32-periode backup
└── BACKUP_2026-03-13_foer_pdf/     # Pre-PDF baseline backup
```

**KRITISK:** Body-filer genereres fra standalones. Redigér ALTID i `_standalone.tex` og regenerér `_body.tex`. Omvendt synkronisering (body → standalone) mister rettelser.

---

## 3. Bogstruktur — 17 kapitler + Appendiks D

| Del | Kap | Titel | Sider (ca.) |
|-----|-----|-------|-------------|
| Front Matter | — | Titelside, Copyright, Forord, TOC, Kapiteloversigt, Tilblivelse | ~10 |
| Del I: Fundamentet | 1 | Introduktion til Performance Management | ~22 |
| | 2 | Teoretiske Perspektiver (økonomi, psykologi, sociologi) | ~22 |
| Del II: Information og Måling | 3 | Design af Performance Measures | ~24 |
| | 4 | Multidimensionel Performance (BSC, frameworks) | ~20 |
| Del III: Incitamenter og Kompensation | 5 | Kompensationsprofiler | ~30 |
| | AppD | Videregående Perspektiver på Kompensationsprofiler | ~10 |
| | 6 | Incitamentsintensitet og Risikoallokering | ~28 |
| Del IV: Motivation og Adfærd | 7 | Motivation (SDT, crowding-out, Hawthorne) | ~26 |
| | 8 | Crowding og Awards | ~28 |
| Del V: Komplekse Problemer | 9 | Multitasking (Holmström-Milgrom) | ~22 |
| | 10 | Organizational Justice og Fairness | ~28 |
| Del VI: Organisation og Karriere | 11 | Social Comparison og Koordination | ~38 |
| | 12 | Karriere og Forfremmelse | ~28 |
| Del VII: Evaluering, Feedback og Implementation | 13 | Subjektiv Evaluering | ~30 |
| | 14 | Feedback og Udvikling | ~22 |
| | 15 | Design og Implementation | ~22 |
| Del VIII: AI og Performance Management | 16 | AI og Agenten | ~24 |
| | 17 | Algoritmisk Ledelse | ~36 |
| Back Matter | — | Litteratur (187 poster), Konceptregister | ~20 |

**Total v28: 368 sider**

---

## 4. main.tex — Korrekt build-struktur (v28-baseline)

```latex
\frontmatter
\input{00_Front_Matter/titlepage}    \cleardoublepage
\input{00_Front_Matter/copyright}    \cleardoublepage
\input{00_Front_Matter/forord}       \cleardoublepage
\tableofcontents                     \cleardoublepage
\input{00_Front_Matter/kapiteloversigt} \cleardoublepage
\input{00_Front_Matter/tilblivelse}  \cleardoublepage

\mainmatter
\part{Fundamentet}
\input{kap01_body}
\input{kap02_body}
\part{Information og Måling}
\input{kap03_body}
\input{kap04_body}
\part{Incitamenter og Kompensation}
\input{kap05_body}
% Appendiks D — manuel nummerering (UNDGÅ \appendix her — ødelægger kap06-17)
\renewcommand{\thechapter}{\Alph{chapter}}
\renewcommand{\chaptername}{Appendiks}
\setcounter{chapter}{3}
\input{appendiks_d_body}
\renewcommand{\thechapter}{\arabic{chapter}}
\renewcommand{\chaptername}{Kapitel}
\setcounter{chapter}{5}
\input{kap06_body}
\part{Motivation og Adfærd}
\input{kap07_body}
\input{kap08_body}
\part{Komplekse Problemer}
\input{kap09_body}
\input{kap10_body}
\part{Organisation og Karriere}
\input{kap11_body}
\input{kap12_body}
\part{Evaluering, Feedback og Implementation}
\input{kap13_body}
\input{kap14_body}
\input{kap15_body}
\part{AI og Performance Management}
\input{kap16_body}
\input{kap17_body}

\backmatter
\nocite{*}
\printbibliography[heading=bibintoc,title={Litteratur}]
\input{konceptregister_body}
```

**ADVARSEL — tre kendte fælder i main.tex:**
1. `\appendix` MÅ IKKE kaldes globalt — det ødelægger kapitelnummerering for kap06–17. Brug kun den manuelle workaround vist ovenfor.
2. Appendiks A, B, C (`09_Back_Matter/appendiks_a_matematik.tex` etc.) er TOMME (`[TODO]`) og MÅ IKKE inkluderes i build.
3. `\cleardoublepage` skal stå EFTER hvert `\input{}` i frontmatter (ikke inde i body-filerne) for at `openright`-indstillingen virker korrekt.

---

## 5. Build-kommando og forventet output

```bash
# Kør i build-mappen (ikke iCloud — for langsom)
xelatex main.tex && biber main && xelatex main.tex && xelatex main.tex
```

**Forventet output (v28-baseline):**
- Sider: 368 (stabilt over alle 3 xelatex-passes)
- Fejl: 0
- Overfull hbox: 27 (alle kendte, accepterede)
- Biber: 0 citations (korrekt — bogen bruger tekstuelle referencer, ikke `\cite{}`)
- Størrelse: ~1.6 MB

**Hvis sidetal svinger:** Tegn på `\appendix` kaldes forkert eller tomme appendikser inkluderes.
**Hvis 235 sider:** Fonte mangler — installer TeX Gyre Pagella, TeX Gyre Heros, DejaVu Sans Mono til `~/Library/Fonts/`.
**Hvis < 350 sider med bibliografi:** `\nocite{*}` mangler før `\printbibliography`.

---

## 6. LaTeX-boks-typer

Alle defineret i `main.tex` preamble. Syntaks: `\begin{boxtype}[Titel]...\end{boxtype}`

| Boks | Variabel | Farve | Bruges til |
|------|----------|-------|-----------|
| `theorybox` | `[Box X.Y: Titel]` | Blå (cbsblue) | Teoretiske modeller, nøglepåstande |
| `casebox` | `[Case X.Y: Titel]` | Rød (cbsred) | Virksomhedseksempler, HBS-cases |
| `definitionbox` | `[Definition X.Y: Titel]` | Grøn (cbsgreen) | Fagtermer, kernebegreber |
| `perspectivebox` | `[Titel]` | Mørk (hvid tekst) | Kritik, nuancer, tværgående pointer |
| `psychbox` | `[Titel]` | Lilla | Psykologisk perspektiv |
| `socbox` | `[Titel]` | Grøn | Sociologisk perspektiv |
| `learninggoals` | (ingen titel-arg) | Grå/blå | Læringsmål øverst i kapitel |
| `chaptersummary` | (ingen titel-arg) | Grå/blå | Sammenfatning sidst i kapitel |

**KRITISK syntaks:** Brug ALDRIG `title={...}` inde i argumentet — det giver pgfkeys-fejl.
```latex
% FORKERT:
\begin{casebox}[title={Case 9.4: Folkeskolen}]
% KORREKT:
\begin{casebox}[Case 9.4: Folkeskolen --- Når Kun Testresultater Tæller]
```
Undgå `\&` i bokstitler — brug `og` i stedet.

---

## 7. Nummerering af bokse, cases og definitioner

Hvert kapitel nummererer sine bokse selvstændigt: `Box X.Y`, `Case X.Y`, `Definition X.Y`.
Nummereringen skal matche tekstrækkefølgen (den boks der optræder først i teksten = lavest nummer).

**Verificerede numre pr. v28 (stikprøve):**
- Kap06: Definition 6.1–6.6 (Horisontproblem=6.3, Rat Race=6.4, Selektion=6.5, Ratchet=6.6)
- Kap08: Case 8.1, 8.2 (IBM), 8.3 (Gaming), 8.4 (Attendance), 8.5 (Google Peer)
- Kap13: Case 13.1, 13.2 (spring fra 13.1 → 13.2, ingen 13.3–13.4)

**Konceptregister** (`konceptregister_body.tex`) skal altid holdes synkroniseret med faktiske boksnumre i body-filerne. Efter enhver nummereringsændring: opdatér registeret.

---

## 8. Kapitelstruktur-skabelon

Hvert kapitel følger denne faste rækkefølge:

```
\begin{learninggoals}  4-6 læringsmål  \end{learninggoals}
\section{Indledning}   Motiverende case eller scenario
\section{...}          Teorisektioner med definitionbox + theorybox
\section{...}          Cases med casebox
\section*{Perspektivering: [Undertitel]}
  \addcontentsline{toc}{section}{Perspektivering: [Undertitel]}
\begin{chaptersummary} Sammenfatning \end{chaptersummary}
\section*{Diskussionsspørgsmål}
\section*{Videre Læsning}
```

---

## 9. Citationsformat og referencer

- **Inline:** `(Efternavn, Årstal)` eller `(Efternavn \& Efternavn, Årstal)`
- **3+ forfattere:** `(Første et al., Årstal)`
- **Ingen `\cite{}`-kommandoer** — alt er tekstuelle referencer direkte i brødteksten
- `references.bib` bruges kun til `\printbibliography` med `\nocite{*}`
- **187 poster, alle T1-verificerede** (95% øvre CI < 2.1% fejlrate)

**Vigtige korrektioner i references.bib (må ikke overskrives):**
- `CappelliEtAl2019`: primær forfatter er Tambe, ikke Cappelli
- `Aguinis2019` 4. udgave (2019): forlaget er Chicago Business Press, IKKE Pearson
- `Drucker1973`: første udgave er 1973 (ikke 1974 som mange sekundære kilder siger)
- `MerchantVanDerStede2017`: dublet bib-entry på tværs af kap03 og kap11

---

## 10. Nøgleteorier og standardreferencer

| Teori | Reference |
|-------|-----------|
| Principal-agent | Jensen \& Meckling (1976) |
| Linear contract | Holmström \& Milgrom (1987) |
| Multi-task | Holmström \& Milgrom (1991) |
| Ratchet effect | Weitzman (1980) |
| Balanced Scorecard | Kaplan \& Norton (1992, 1996) |
| Self-determination | Deci \& Ryan (2000) |
| Goal-setting | Locke \& Latham (2002) |
| Feedback intervention | Kluger \& DeNisi (1996) |
| Organizational justice | Folger \& Cropanzano (1998) |
| Tournament theory | Lazear \& Rosen (1981) |
| Fair wage-effort | Akerlof \& Yellen (1990) |

---

## 11. Workflow: Ny session — byg PDF

1. **Læs** `PROJECT_LOG.md` og `MASTER_TODO.md` for aktuel status
2. **Kopiér** alle `_body.tex`-filer + `main.tex` + `references.bib` + `cover_image.png` + `konceptregister_body.tex` + `00_Front_Matter/` + `09_Back_Matter/appendiks_c_ordliste.tex` + `appendiks_d_body.tex` til build-mappe
3. **UNDLAD** at kopiere `appendiks_a_matematik.tex` og `appendiks_b_teorioversigt.tex` (tomme)
4. **Kør** `xelatex main.tex && biber main && xelatex main.tex && xelatex main.tex`
5. **Verificér** sidetal = 368 ± 5 (variation fra bibliografi-rendering acceptabel)
6. **Gem** PDF som `PM_bog_komplet_vXX_YYYY-MM-DD.pdf`

---

## 12. Workflow: Ret en _standalone.tex og synkronisér til build

```bash
# 1. Ret kildefilen (standalone) i iCloud
# 2. Generér body-fil (strip preamble og \begin/end{document})
python3 -c "
import re
with open('kap01_standalone.tex') as f:
    content = f.read()
# Find alt efter \begin{document}
match = re.search(r'\\\\begin\{document\}(.*)\\\\end\{document\}', content, re.DOTALL)
body = match.group(1).strip() if match else content
# Fjern \maketitle hvis den er der
body = re.sub(r'\\\\maketitle\s*', '', body)
with open('kap01_body.tex', 'w') as f:
    f.write(body)
"
# 3. Gem body-fil til iCloud-rod og build-mappe
```

---

## 13. Kendte kompileringsfejl og løsninger

| Fejl | Årsag | Løsning |
|------|-------|---------|
| pgfkeys-fejl i boks | `title={...}` syntaks eller `\&` i titel | Fjern `title={}`, brug `-{}-{}` i stedet for `\&` |
| Sidetal svinger | `\appendix` kald eller tomme appendikser | Se main.tex-struktur i afsnit 4 |
| 235 sider (komprimeret) | Fonte mangler | Installer til `~/Library/Fonts/` |
| Biber: 0 citations | Korrekt — ingen `\cite{}` bruges | Acceptér |
| `anchor of a bookmark` | tcolorbox + colorbox i titlepage | Acceptér — harmløs |
| 26 label-dubletter | `sec:summary` etc. bruges ikke med `\ref{}` | Acceptér |
| iCloud-sti med mellemrum fejler i bash | Mellemrum i `Mobile Documents` | Brug Python `shutil.copy2()` eller Filesystem MCP |

---

## 14. Projektlog-stier

| Fil | Indhold |
|-----|---------|
| `PROJECT_LOG.md` | Komplet sessionshistorik v1–v28+ |
| `MASTER_TODO.md` | Åbne og lukkede opgaver |
| `KORREKTUR_LOG.md` | Specifikke tekstrettelser |
| `KILDEVERIFICERING_LOG.txt` | Log fra v33-session (Cowork, 2026-03-23) |
| `backups/backup-2026-03-18-*/` | v32-periode backup |
| `BACKUP_2026-03-13_foer_pdf/` | Pre-PDF baseline |
