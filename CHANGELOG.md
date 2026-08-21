# Changelog

All notable changes to the `academic-book-skills` repo are documented here.
Format loosely follows [Keep a Changelog].

## [1.6.0] — 2026-08-21

### Fixed — `pm-konsistens-audit` 0.12.0 → 0.13.0

Fem defekter, alle af samme klasse: **et mønster læste LaTeX-kilde, som om den var ren tekst.**
De blev fundet ved at læse de passager, værktøjet udtalte sig om — og hver gang havde værktøjet
uret, ikke bogen.

- **ALVORLIG: kapitelnummeret blev læst af hele stien, ikke af filnavnet.** `load_sources`
  brugte `re.search(r'(\d+)', f)`. Kørt fra fx `/root/b36/da/kap07_body.tex` blev **hver eneste
  fil til kapitel 36**, hvorefter sektion 11 ikke fandt et matchende kapitel i spejlet, sprang
  alt over og skrev *"ingen divergens --- de to udgaver henviser ens ✓"* på en bog med **38**
  divergerende henvisninger. Samme fejlklasse som layout-skillens Check D: **"ikke målt"
  rapporteret som "målt og i orden"**. Rettet til `os.path.basename(f)`.
- **Boksenes egne titler blev talt som henvisninger.** `\begin{definitionbox}[Definition 14.1:
  Feedback]` indeholder strengen "Definition 14.1". Bogens 198 nummererede bokse blev talt som
  henvisninger til sig selv.
- **`~` og `\ ` (beskyttede mellemrum) gjorde henvisninger og citationer usynlige.**
  `Eksempel~5.1`, `afsnit~7.3`, `O'Boyle et al.\ (2012)`, `Coase, R.H.\ (1937)`. Hverken `~`
  eller `\ ` er whitespace. **15 henvisninger og 9--10 % af bogens årstalscitationer** var
  usynlige for auditten. Det er den direkte grund til, at to manglende bib-poster har kunnet stå
  i en færdig bog.
- **`\&` brød forfatterkæden.** `Paulhus \& Williams (2002)` registrerede kun *sidste*
  forfatter. I den danske udgave gælder det **280** citationer.
- **Store/små bogstaver og valgfrie tuborgklammer.** `perspektivboks 13.1` med lille p gav en
  falsk divergens; `[{Perspektivboks 12.2: ...}]` fik en boks, der FINDES, til at se manglende ud.

### Added
- **`norm_latex()`** --- ét fælles normaliseringstrin, brugt af både sektion 3 og sektion 11, så
  rettelsen ikke skal gentages hver gang et nyt mønster skrives. Maskerer boksdefinitioner og
  `\ref`-kald, normaliserer `~`/`\ `/`\,`/`\&` og kollapser whitespace.
- Sektion 11's mønstre er nu case-insensitive og sammenligner små bogstaver.
- Citationsparseren accepterer nu komma uden foranstillet mellemrum (`Coase, R.H.`) og springer
  initialer med punktum over.

### Testet --- før/efter på samme filer

| Kontrol | 0.12.0 | 0.13.0 |
|---|---|---|
| §11 kørt fra sti **med** cifre | "ingen divergens ✓" | **13 par / 38 instanser** |
| §11 kørt fra sti **uden** cifre | 12 par | **13 par / 38 instanser** |
| Rapporterne fra de to stier | forskellige | **byte-identiske** |
| §3.A ser `Coase (1937)` | nej | **ja** |
| §3.A ser `Oboyle (2012)` | nej | **ja** (og melder korrekt: efternavn findes, år 2016) |
| §3.A review-kandidater | 52 | 63 |
| **Alle øvrige sektioner (§1--§10)** | 85/1/1/1/1/1/2/8/2 | **uændret** |

**Krydsvalidering:** en uafhængig måling, skrevet uden for skillen, gav præcis samme tal ---
**13 par, 27 instanser kun i DA, 11 kun i EN**. To uafhængige implementeringer er enige.
Fire af de nyfundne divergenser er desuden verificeret ved at **læse passagen** i begge udgaver
(kap01 Teoriboks 1.2, kap09 afsnit 7.3, kap15 Case 14.2 ×2) --- alle fire er reelle.

### Kendt, ikke rettet
Den parenteserede citationsgren parrer hvert navn med *hvert* årstal i parentesen, hvilket giver
den falske `Oboyle (1997)` fra `(Kruse \& Blasi, 1997; O'Boyle, ..., 2016)`. Det kræver en anden
parsingstrategi (nærmeste årstal pr. navn) og ligger for sig.

## [1.5.0] — 2026-08-21

### Changed
- **ÉN version pr. skill, i BEGGE filer, holdt identiske.** Repoet havde to konkurrerende
  konventioner, og ingen af dem blev håndhævet: seks skills havde et tal i `SKILL.md`
  (`metadata.version`) og et andet i `plugin.json`, otte havde slet ingen version i SKILL.md,
  og kun `academic-book-layout-audit` havde de to i overensstemmelse.
  **Reglen, der er anvendt:** det VEDLIGEHOLDTE tal vinder, og intet tal er opfundet.
  Git-historikken afgjorde hvilket: `plugin.json`-værdien `1.0` blev sat identisk på seks
  skills i ét bulk-commit (e18e4d9) og aldrig rørt siden --- en placeholder --- mens
  `SKILL.md`s tal (0.1.0 / 0.1.2 / 0.1.3) er forskellige pr. skill og faktisk bumpet med
  feature-commits. `pm-konsistens-audit` er den omvendte: dens `plugin.json` ER blevet passet
  (0.7.4 → 0.8.0 → 0.9.0 → 0.9.2), mens SKILL.md aldrig har haft en version.

| Skill | før (SKILL.md / plugin.json) | nu |
|---|---|---|
| `academic-book` | — / 0.5.0 | **0.5.0** |
| `academic-book-layout-audit` | 1.1.0 / 1.1.0 | 1.1.0 (uændret) |
| `academic-danish-ai-tell-audit` | 0.1.2 / 1.0 | **0.1.2** |
| `academic-danish-consistency` | 0.1.0 / 1.0 | **0.1.0** |
| `academic-danish-engagement-audit` | 0.1.0 / 1.0 | **0.1.0** |
| `academic-danish-klarsprog` | 0.1.0 / 1.0 | **0.1.0** |
| `academic-english-ai-tell-audit` | 0.1.2 / 1.0 | **0.1.2** |
| `academic-english-engagement-audit` | 0.1.0 / 1.0 | **0.1.0** |
| `academic-english-text-audit` | — / 1.5 | **1.5** |
| `academic-source-verification` | 0.1.3 / 0.6.1 | **0.1.3** |
| `academic-translation-da-en` | — / 0.2 | **0.2** |
| `akademisk-tekstaudit` | — / 1.5 | **1.5** |
| `faglig-bog` | — / 0.5.0 | **0.5.0** |
| `pm-bog` | — / 0.1.0 | **0.1.0** |
| `pm-konsistens-audit` | — / 0.9.2 | **0.12.0** |

- **`pm-konsistens-audit`s manifest bragt ajour: 0.9.2 → 0.12.0.** Den var tre udgivelser
  bagud --- 0.10.0 (sektion 9, epigrafer) og 0.12.0 (sektion 11, krydsreference-spejl) bumpede
  aldrig manifestet.

### Fixed
- **`version: 1.5` uden anførselstegn er ikke en streng i YAML --- det er tallet 1.5.**
  Fanget af den skærpede preflight: `academic-english-text-audit`, `academic-translation-da-en`
  og `akademisk-tekstaudit` havde tocifrede versioner, som YAML læste som **float**, så de
  aldrig kunne sammenlignes med `plugin.json`s streng. Nu sat i anførselstegn.
  Trecifrede versioner (`0.1.0`) rammes ikke --- de er ikke gyldige tal og parses som strenge.
  Fælden er derfor tavs, indtil nogen skriver en tocifret version.

### Tooling
- **`push.sh`** --- genbrugeligt commit-/push-script for repoet. Rydder de `.git/index.lock`-rester,
  Cowork-VM'en efterlader (den må ikke slette filer, så git kan ikke rydde sine egne låse);
  kører preflight; viser hvad der ville blive committet; kræver `JA`; og **verificerer til sidst
  lokal `HEAD` mod `git ls-remote`**, så et push, der siger "done" uden at være landet, fanges.
  Committer aldrig `_to_delete/`, `*.skill` eller `push*.sh`. Tørkørsel er default.
- **Preflight skærpet:** versionsdrift, manglende version i ét af de to felter, og ikke-streng
  YAML-version er nu **FEJL**, ikke noter. Den kunne have fanget hele oprydningen ovenfor, før
  den nåede at blive publiceret.

## [1.4.0] — 2026-08-21

### Added
- **`pm-konsistens-audit` → 0.12.0: sektion 11 — krydshenvisninger på tværs af udgaver**
  (`--mirror`). En henvisning kan pege på et afsnit, der **findes**, og alligevel være den
  forkerte; sektion 2 og 6 verificerer eksistens, ikke korrekthed, og er blinde over for den
  fejl. I et spejlet tosproget værk skal de to udgaver derimod henvise til de samme numre ---
  kapitelstrukturen er den samme --- så enhver divergens er en fejl i præcis én af dem.
  Sektion 11 sammenligner fordelingen af afsnits-, float- og boks-henvisninger kapitel for
  kapitel og siger, hvor de ikke stemmer. Den dømmer ikke mening; hvilken udgave der har ret,
  afgør mennesket (normalt facit-udgaven).
  Anledningen var ti forkerte kapitel-14-henvisninger i PM-bogens engelske kap17, som den
  eksisterende audit meldte som "0 dangling" --- fordi de alle pegede på afsnit, der fandtes.
- **`academic-book-layout-audit` 1.0.0 → 1.1.0: Check D — folio-paritet** (`scripts/check_d.py`).
  Kontrollen har eksisteret som ad hoc-script siden PM-bogens §CCXXI, men aldrig i skillen ---
  og derfor blev den skrevet forfra i hver session. Nu er den en del af familien.
  **Reglen:** PDF-side 1 er recto, så den første arabisk nummererede side (folio "1") skal ligge
  på en ULIGE PDF-side. Ellers er hvert opslag i bogen spejlvendt. Fejlen opstår kun, når
  frontmatteret ændres med et ULIGE antal sider; brødtekst og bagmatter kan ikke bryde den.
  Scriptet tjekker samtidig folio-placering (venstre på verso, højre på recto) og skelner
  `plain`-sidernes centrerede folioer fra fejl.

### Fixed
- **`pm-konsistens-audit`: float-mønstrene dækkede kun den danske udgave.** `check_refs` matchede
  `Figur`/`Tabel` og aldrig `Figure`/`Table` eller registerets forkortede `Fig N.M`. Den engelske
  udgaves float-henvisninger blev altså **aldrig kontrolleret**. Nu dækker mønstrene begge
  udgaver og den forkortede form.
- **`pm-konsistens-audit`: konceptregister og appendiks blev kun set af sektion 5.** De er
  selvstændige henvisningsflader --- registeret peger på figurer, tabeller og afsnit præcis som
  brødteksten --- men `check_refs` scannede kun kapitelfilerne. De fodres nu ind på lige fod via
  `extra_files`. Konkret fund i PM-bogen: registerposter, der pegede på Figur 14.1 og §14.3/§14.4
  efter en omnummerering, blev ikke fanget af nogen sektion.
- **ALVORLIG i den ad hoc-udgave, Check D afløser: paritetstjekket meldte fejl på en korrekt bog,
  hver eneste gang.** Arabertal 1 falder ALTID på en kapitelåbning, og kapitelåbninger bruger
  `plain` pagestyle med CENTRERET folio. Koden sprang centrerede folioer over med `continue` ---
  FØR den registrerede tallet --- så `arabic1` forblev `None`. I PM-bogen ligger folioen 5,7 pt
  (DA) og 7,1 pt (EN) fra sidemidten, altså langt inden for toleransen.
  To principper er nu bygget ind og dokumenteret i SKILL.md: **(1) mål først, klassificér
  bagefter**; **(2) "ikke målt" er ikke "målt og fejlet"** --- de to udfald har hver sin
  tilstand og hver sin exitkode (0 / 1 / 2), så scriptet kan bruges som gate uden at råbe ulv.
- Kandidatvalget tog den SIDSTE matchende span i bundbåndet, hvilket er vilkårligt, hvis båndet
  indeholder andet end folioen. Nu vælges den nederste span, ved uafgjort den yderste.

### Documentation
- SKILL.md: nyt afsnit om Check D med fælden, reglen og hvornår tjekket skal køres; Check D
  tilføjet til sektionstabellen og til triggerne ("folio-paritet", "starter kapitel 1 på
  højreside", "recto/verso"); to nye grænser noteret (folio antages i det nederste 65pt-bånd;
  frontmatter antages romertalsnummereret).
- SKILL.md, Forudsætning: opskrift på **offline-installation af PyMuPDF** fra et lokalt hjul,
  for miljøer hvor `pip3 install` afvises af en egress-proxy (403) --- plus påmindelsen om at
  kontrollere, HVOR pakken landede, da en `--user`-installation i et sessionshjem forsvinder.

### Testet
Positivt mod PM-bogens to udgaver (DA 627 s., EN 433 s., Linux-build): arabertal-1 på s. 31 og
s. 27, begge ULIGE ✓, 0 forkert placerede folioer (DA 589 korrekte, EN 385), exit 0. Alle tal
identiske med den gamle implementerings --- kun detektionen er ændret, ikke placeringskontrollen.
**Negativt:** en kopi af DA-PDF'en med én frontmatter-side fjernet giver `PARITETSFEJL` + 587
forkert placerede folioer, exit 1; en PDF uden folioer giver `INKONKLUSIV`, exit 2. Et
paritetstjek, der aldrig har set en paritetsfejl, er ikke afprøvet.

## [1.3.0] — 2026-08-19

### Added
- **NY SKILL: `academic-book-layout-audit` 1.0.0** --- familiens manglende geometri-modul.
  De øvrige skills spørger "er teksten rigtig og konsistent?"; denne spørger "renderer bogen
  rigtigt på papir?". Arbejder på den SATTE PDF, fordi fejlklassen er usynlig i `.tex`.
  Sektioner: **A** overfull `\hbox` klassificeret efter pt (≥50 = klippes i tryk);
  **Check A** brudt boks hvor fortsættelsen efterfølges af TOMRUM (kritisk --- 12 af 17
  læringsmålsbokse i PM-bogen, forældreløs hale ned til 11 ord); **Check B** småhale-inventar
  (kosmetisk, skal UDSKYDES til sidste paginering); **Check C** float-afstand, type-korrekt
  (Figur og Tabel deler numre); **E** blanke sider; **G** billede-dpi.
- **`--compare tidligere.pdf`** --- rapporterer pr. fundklasse om et fund er NYT eller
  præeksisterende. Besvarer det spørgsmål en operatør altid har efter en rettelsesrunde:
  "har jeg lige ødelagt noget?" I PM-bogen viste den, at 6 blanke sider og 1 fremad-float
  fandtes i alle builds fra samme dag --- altså ikke indført af dagens rettelser.
- **`--preamble main.tex`** --- udleder farve→bokstype-kortet fra `\definecolor` +
  `\newtcolorbox`, så rapporten siger `theorybox` frem for RGB. Håndterer at flere miljøer
  deler farve (PM-bogen: `learninggoals / chaptersummary`).

### Testet
Mod PM-bogens danske udgave (619 s., Mac-build): 0 kritiske overfull, 0 boks-tomrum,
12 småhaler, 1 fremad-float, 6 blanke sider --- og regressionskontrollen bekræftede, at
ingen af dem var nye.

## [1.2.0] — 2026-08-19

### Added
- **`pm-konsistens-audit` 0.11.0 — sektion 10: epigrafer PAA TVAERS af udgaver (`--mirror`).**
  §9 ser kun én udgave, så en fejl hvor DA og EN har FORSKELLIGE epigrafer var usynlig for begge
  kørsler. Fire sammenligninger pr. kapitelpar: 10A tilstedeværelse, 10B citat-status (den ene
  i citationstegn, den anden ikke), 10C årstal (med `\citeyear`-nøgler slået op i `--bib`, så
  `\citeyear{Deming1982}` og `(1982)` sammenlignes som årstal), 10D tal i epigrafteksten.
  **Regressionstestet mod den faktiske fejl:** mod EN-kilden FØR rettelsen udløses 10B og 10D
  på kap02; mod den rettede tilstand 0 afvigelser; 10C udløses korrekt ikke.
  Der er bevidst kun ÉN implementation — den engelske søsterskill henviser hertil.
- **§9: `--epigraph-head N`** gør de hidtil hårdkodede 25 linjer konfigurerbare.
- **§9E: filer uden epigraf** rapporteres nu. Før blev de sprunget lydløst over, så en glemt
  epigraf var usynlig (i PM-bogen: kap04, kap13, kap14 — bevidst, men det kunne man ikke se).

### Unchanged
- §1-§8 og §9A-§9D er byte-identiske med 0.10.0 på samme input.

## [1.1.0] — 2026-08-19

### Added
- **`pm-konsistens-audit` 0.10.0 — sektion 9: epigraf-tjek.** Kapitelåbningens citat står i
  `\begin{quote}` før brødteksten og bærer aldrig `\cite`; den var derfor usynlig for både
  §3 (prosa↔bib) og enhver citations-scanning. Fire kontroller: **9A** ordret citat uden
  kildeår (hardt), **9B** kildeår uden matchende bib-post (hardt), **9C** attributions-format
  ikke ensartet (review), **9D** citationstegns-konvention ikke ensartet (review). Markeret
  parafrase (`Frit efter …`) og selv-attribution (`Forfatteren`) er undtaget — bevidst, så
  ærlig omskrivning ikke straffes; det, der rammes, er en omskrivning, der udgiver sig for at
  være ordret.
  **Baggrund:** i PM-bogen var tre af fjorten epigrafer forkerte (parafrase i citationstegn;
  forkert årstal både i epigraf og i `references.bib`; citat helt uden kilde), og fire stod som
  ordrette citater uden år. Hverken kildeverificering, korrektur eller nogen tidligere
  audit-kørsel havde set dem. Fejlklassen er den dyreste i en fagbog — en anmelder slår netop
  epigrafen efter.
  **Regression:** hele rapporten før §9 er byte-identisk med 0.9.2 på samme input.

## [1.0.0] — 2026-08-11

### Added
- **The article's full editing/audit skill chain (11 skills)** as a publication snapshot, per
  the Data and tool availability statement of *Writing a Scholarly Book with AI*:
  `akademisk-tekstaudit` (1.2), `academic-english-text-audit` (1.2),
  `academic-translation-da-en` (0.1), `academic-danish-klarsprog`,
  `academic-danish-consistency`, `academic-english-narrative`,
  `academic-english-consistency`, `academic-danish-ai-tell-audit`,
  `academic-english-ai-tell-audit`, `academic-danish-engagement-audit`,
  `academic-english-engagement-audit`. All registered in the plugin marketplace.
  Development homes remain the companion repos; the copies here are the cited versions.

### Fixed
- `pm-konsistens-audit/.claude-plugin/plugin.json` version bumped 0.9.0 → 0.9.2 (the 0.9.1 and
  0.9.2 code changes were already committed on 22 July but the plugin manifest was not bumped).

## [0.9.2] — 2026-07-22

### Changed
- `pm-konsistens-audit`: **§3.A review candidates are now surfaced in full** so a "0 flags"
  summary cannot hide cited-but-missing references — the A2 year-mismatch list is written out
  (in the PM case this exposed Bol 2011 and Buckingham & Goodall 2019, which had been hidden
  behind an aggregated count). (Commit 3305f87.)

## [0.9.1] — 2026-07-22

### Fixed
- `pm-konsistens-audit`: §3 A-list false-positive reduction. (Commit f519b3e.)

## [0.9.0] — 2026-07-22

### Added
- `pm-konsistens-audit` (`audit_all.py`): **section 7 — unnumbered `\chapter*` header-mark
  (`\markboth`) + TOC hygiene.** Catches a *silent* class of error the compiler and general
  linters (ChkTeX/lacheck) both miss: an unnumbered `\chapter*` does **not** call
  `\chaptermark`, so with `fancyhdr` the running header keeps showing the *previous numbered
  chapter's* name (e.g. an Afterword displaying "Chapter 17"). Section 7 flags every author
  `\chapter*{Title}` that is not followed (within a short window) by `\markboth` (HARD flag →
  stale running header) and, as a REVIEW note, any missing `\addcontentsline{toc}` (heading
  absent from the TOC). `\section*` is intentionally out of scope (end-matter such as
  "Discussion Questions" legitimately uses `\section*`; the chapter's `\leftmark` stays
  correct). Package-generated chapters (`\tableofcontents`, biblatex `\printbibliography`) are
  not author `\chapter*` and are naturally skipped.
- New `--structure` argument: comma-separated globs of front/back-matter `.tex` (the
  unnumbered headings live outside `kap*_body.tex`), scanned by section 7 alongside `--src`.
- **Motivation / worked example:** the PM textbook had this exact bug in 7 headings across
  both editions (EN Afterword, Foreword, Chapter Overview, The Making of This Book; DA Forord,
  Kapiteloversigt, Bogens Tilblivelse). Verified: the detector flags all of them *before* the
  `\markboth` fix and reports **0** after; it does **not** flag the numbered appendices,
  References, Concept Register or the TOC (the known-good cases). Sections 1–6 unchanged.

## [0.8.0] — 2026-07-13

### Added
- `pm-konsistens-audit` (`audit_all.py`): **section 6 — hardcoded section/chapter prose references.**
  The PM textbook cross-references sections in prose ("Section 12.7" / Danish "afsnit 12.7" /
  "Chapter 5" / "Kapitel 5") rather than with `\ref`, so LaTeX never validates them and they can go
  stale silently on renumbering. Section 6 validates that every such reference **exists** (chapter X
  must have at least Y numbered `\section`s; chapter N must be within the book). Dangling = HARD flag.
  Case-insensitive so it covers both editions (EN "Section", capitalised; Danish "afsnit"/"kapitel",
  usually lower-case — 254× vs 14× in the DA book). Verified on the live book: EN **425** and DA **413**
  prose references, **0 dangling** in both. Motivation: the AI chapters (kap16–17) carry the most such
  references (161/130), but the convention is book-wide — section 6 holds every chapter to the same
  standard and catches future breakage automatically. Limitation: ranges ("Sections 7.2--7.3") are
  checked on the first endpoint only.

## [0.7.5] — 2026-07-13

### Packaging
- The repo is now installable as a **Cowork/Claude Code plugin marketplace**. Added
  `.claude-plugin/marketplace.json` at the root (lists the five skills as plugins) and a
  `.claude-plugin/plugin.json` in each skill directory (`academic-book`, `faglig-bog`,
  `pm-konsistens-audit`, `academic-source-verification`, `pm-bog`). No files moved — each skill's
  root `SKILL.md` is auto-discovered as its plugin's skill, so direct script paths (e.g.
  `pm-konsistens-audit/scripts/audit_all.py`) are unchanged. Enables
  `claude plugin marketplace add PeterMalmkjaer/academic-book-skills` and install via Cowork →
  Customize → Plugins → Add marketplace. Plugin versions seeded from this CHANGELOG
  (academic-book 0.5.0, faglig-bog 0.5.0, pm-konsistens-audit 0.7.4,
  academic-source-verification 0.6.1, pm-bog 0.1.0).

## [0.7.4] — 2026-07-11

### Added
- `pm-konsistens-audit` (`audit_all.py`): new **section 5 — typeless box-pointers**. Flags any bare
  `Box N.N` (an anglicism; Danish labels are `Teoriboks`/`Perspektivboks`) and **escalates to a HARD
  FLAG** when `N.N` is ambiguous — i.e. exists as *both* a Teoriboks and a Perspektivboks (the book uses
  separate counters per box type per chapter, so collision numbers are genuinely ambiguous to the reader).
  Other typeless pointers are listed as REVIEW. The type-map is derived from the *actual* box titles in
  the source (never from a handover/table — numbers drift). `Theory Box`/`Perspective Box` (English typed
  forms) are excluded via lookbehind.
- `audit_all.py`: wired in real `--register` (default `konceptregister_body.tex`) and `--appendix`
  (default `09_Back_Matter/appendiks_b_teorioversigt.tex`) arguments so the concept register/appendix are
  actually scanned. Previously the usage example referenced these flags but `main()` never defined them,
  so the register was only audited if manually folded into `--src`.

### Rationale
- Surfaced by the PM-bog concept register: 52 bare `Box N.N` pointers, of which 14 register lines
  (13 collision numbers, 16.1 twice) were truly ambiguous. Fixed manually 2026-07-11; regression test
  confirms section 5 catches the pre-fix state (14 hard flags) and reports the post-fix master clean.

## [0.7.3] — 2026-07-11

### Documented
- `pm-konsistens-audit` (`audit_all.py`): added an inline rationale above `LABELMAP` recording WHY
  `Case`, `Example` and `Eksempel` all map to one `Case/Eksempel` category. **Case = a real-world
  situation; Example/Eksempel = a constructed/hypothetical illustration** — two deliberate labels that
  deliberately share one casebox counter per chapter. They must NOT be merged in the manuscript or
  concept register (the naming carries meaning), but for numbering they are one continuous series. This
  prevents a future maintainer from "simplifying" the dual labels or the shared-counter mapping. No code
  behaviour change.

## [0.7.2] — 2026-07-10

### Fixed
- `pm-konsistens-audit` (`audit_all.py`): the numbering audit now covers **two-word box labels** —
  "Theory Box X.Y" and "Perspective Box X.Y". The box regex previously captured only a single word
  before the number, so English two-word labels were read as "Box", mapped to nothing, and the Theory
  Box and Perspective Box series were silently NOT validated (only Definition and Case/Example were).
  Widened the label capture to an optional second word and mapped `'Theory Box'→Teoriboks`,
  `'Perspective Box'→Perspektivboks` (plus their cross-reference patterns). Verified on the live EN
  textbook: all six categories (Definition, Theory Box, Perspective Box, Case/Example, Figure, Table)
  are now validated and consecutive; audit clean. Independent manual check confirmed both series run
  1..n in every chapter.

## [0.7.1] — 2026-07-10

### Fixed
- `pm-konsistens-audit` (`audit_all.py`): the Case numbering series now recognises the **English label
  "Example"** (previously only Danish `Case`/`Eksempel` were mapped). Books that use one shared casebox
  series with mixed "Case X.Y" and "Example X.Y" titles were false-flagged as having numbering gaps —
  e.g. a chapter with Example 5.1 + Case 5.2–5.4 was read as Case [2,3,4] and reported as "missing 1".
  Added `'Example'` to `LABELMAP` and to the Case cross-reference pattern. Verified on the live EN
  textbook: **4 false-positive numbering flags → 0** (audit now fully clean). No manuscript change — the
  book's numbering was already correct; renumbering would have broken the valid sequence.

## [0.7.0] — 2026-07-10

### Added
- `pm-konsistens-audit`: **kapitel-skabelon-konsistens-tjek (sektion 4)** i `audit_all.py`. Udleder den
  MODALE åbningsstruktur fra flertallet af kapitler (`\chapter` → `\chaprule` → epigraf → "Hvad dette
  kapitel handler om"-boks → læringsmål → første `\section`) og **flager kapitler der bryder rækkefølgen**
  (relativ rækkefølge, ikke linjenumre → epigraf-eller-ej giver ikke falske positiver), **manglende
  påkrævede landemærker** (H/L påkrævet hvis ≥50 % har dem), og **afvigende læringsmål-indledning**
  (modal frase udledes; review). Harde flag = rækkefølge + manglende. Baggrund: PM-bogen — en læser fandt
  at kap16/17 åbnede med læringsmål FØR "Hvad dette kapitel handler om" (de 15 øvrige omvendt) + brugte en
  anden indlednings-frase; sektion 4 reproducerer begge fund deterministisk (bevist mod før/efter-versioner).
  Numre-/reference-tjek ser ikke denne fejlklasse.

## [0.6.1] — 2026-07-10

### Fixed
- `academic-source-verification`: **`ledger_build.py`s in-text-scanner var svag** — den fangede kun den
  parentetiske form `(Forfatter, år)`, ikke den narrative `Forfatter (år)` (den dominerende i
  tekstuelle-reference-bøger). På PM-bogen betød det 22 fundne citationer og 196 "forældreløse" (falsk).
  Porteret `pm-konsistens-audit/audit_all.py`s robuste logik: begge citationsformer, deaccent (ö→o, é→e),
  genitiv-'s-fjernelse, og matchning mod ALLE forfatter-efternavne (ikke kun første). Resultat på PM-bogen:
  311 citationer, 32 reelle forældreløse. Phantom-detektion opdelt i **"efternavn slet ikke i bib" (høj
  signal)** vs **"år-mismatch" (co-forf.-støj)** — så de to søster-skills nu er enige om citations-modellen.

## [0.6.0] — 2026-07-10

### Added
- `pm-konsistens-audit`: **reference-integritets-tjek (prosa ↔ references.bib)** — implementerer
  det hidtil dokumenterede-men-manglende "fantom-/forældreløs"-kontraktpunkt som
  `academic-source-verification` allerede henviste til. `scripts/audit_all.py` får en `--bib`-parameter
  og en ny **sektion 3** med fire kategorier: **A** prosa-citation uden matchende bib-nøgle (delt i
  "efternavn slet ikke i bib" = høj signal vs. "år-mismatch" = co-forf.-støj), **B** orphan-nøgler,
  **C** dublet-poster (samme DOI, eller samme titel + samme år — forskellige udgaver springes over),
  **D** nøglenavn-år ≠ `year`-felt. Kun **C+D tæller som harde flag**; A+B er review-kandidater der ikke
  fælder "RENT ✓". Prosaen deaccentes (ö→o, é→e) + genitiv-'s fjernes før navne-udtræk for at dæmpe
  falske positiver. Gælder bøger med **tekstuelle** referencer + `\nocite{*}` (ikke `\cite`), hvor en
  numre-/float-audit pr. konstruktion ikke kan fange en citation der peger på en ikke-eksisterende nøgle.
  SKILL.md får en "Reference-integritet"-sektion med **P1/P2/P3-triage** (læser-synlige fejl → integritet →
  kosmetisk) og forbehold. Baggrund: PM-bogen (2026-07) — fandt 12 manglende referencer, 4 dublet-poster
  og flere skjulte prosa/år-fejl som de øvrige tjek ikke så.

### Fixed
- `pm-konsistens-audit`: SKILL.md "Filer" listede forkerte parametre (`--register`, `--appendix` findes ikke
  i `audit_all.py`); rettet til de faktiske: `--src`, `--aux`, `--bib`, `--out`.

### Changed
- `academic-source-verification`: krydsreference til søster-skillen præciseret — fantom-/forældreløs-detektionen
  er nu faktisk implementeret (`audit_all.py --bib`, sektion 3) og dækker desuden dublet + nøgle/år.

## [0.5.0] — 2026-07-08

### Added
- `faglig-bog` (Danish sibling of `academic-book`): **mirrored the two 0.4.0 layout additions into
  Danish** so the sibling skills do not drift apart. SKILL.md gains a Danish "Tabel-kolonnejustering
  — foretræk ragged-right" section (same ragged-right rule + the honest note that it fixes in-column
  overflow but does NOT zero a book's overfull count), and a new `faglig-bog/references/
  prepress_pdf_checklist.md` (Danish pre-press checklist: trim, ≥300 dpi, font embedding, PDF/X
  [ISO 15930] / PDF/A [ISO 19005] / PDF/UA [ISO 14289], CMYK, bleed, tagging), with a pointer from
  Skabelon 9. Principle recorded: language-agnostic learnings (layout, pre-press, build) go into
  BOTH `academic-book` and `faglig-bog`.

## [0.4.0] — 2026-07-08

### Added
- `academic-book`: **table column-alignment rule** + **pre-press/PDF-format checklist**.
  SKILL.md gains a "Table column alignment — prefer ragged-right" note (narrow/multi-column
  `p{}`/`X` tables must use `>{\raggedright\arraybackslash}`: justification in narrow columns
  causes rivers, hyphenation, in-column overflow, and makes the last word of a column hug the next
  column so they read as "merged"; fixes the column-level bunching with no content change, but
  note it does NOT zero a book's overfull count — remaining overfull boxes usually sit in wide
  figures/tables/math elsewhere). New `references/prepress_pdf_checklist.md` — a reusable
  pre-press checklist (trim size, image ≥300 dpi, font embedding+subsetting, PDF/X [ISO 15930]
  vs PDF/A [ISO 19005] vs PDF/UA [ISO 14289], CMYK for offset, bleed + crop marks, tagging,
  metadata), with the ordering rule that trim/geometry must be settled BEFORE the final
  typography pass (a trim change reflows the book). Pointer added from Template 9 (print quality).
  Both distilled from a live DA→EN textbook production pass.

## [0.3.0] — 2026-07-08

### Added
- `academic-book`: **term-gloss / parenthetical house-style convention**. New
  `references/gloss_and_parenthesis_convention.md` — a five-category decision tree for the common
  situation where a term is followed by another term in parentheses (frequent as a leftover
  translation artifact): redundant self-gloss → delete; genuine synonym → keep + italicise (gloss
  once, at first use); false calque (source-language equivalent that is not an established
  target-language term, e.g. "the Pawl Effect" for *the ratchet effect*) → delete; missing
  synonym/abbreviation → add; true non-gloss parentheticals → leave. Encodes two error-preventing
  rules: **never invent a synonym** (verify every alternative name via Elicit/Scite/Exa/CrossRef),
  and **precision over label** (keep related-but-distinct terms distinct — *target ratcheting* the
  practice vs *the ratchet effect* the consequence; a rational effect is not a cognitive bias).
  Style basis: APA/Chicago/Turabian (italicise a term at first use) + Farkas (1983). Pointer added
  from SKILL.md (Template 2). Distilled from a live DA→EN textbook pass.

## [0.2.3] — 2026-07-08

### Added
- `academic-source-verification`: **operationalised tjek #3 (claim-support / correct use of source)**.
  Added `scripts/annotate_claims.py` (highlights the claim-supporting passages in a source PDF →
  `*_ANNOTATED.pdf`; reports phrases it cannot find = candidates for "wrong source"),
  `references/annotation_record.md` (the claim → quote → verdict record format), and a "Claim-støtte
  / korrekt brug — arbejdsgang" section in SKILL.md. Encodes the lesson: metadata/DOI being correct
  does NOT prove the manuscript uses the source correctly; if a claim is unsupported, find another
  source — never just fix metadata to "rescue" a wrong source. Skill bumped to 0.1.3.

## [0.2.2] — 2026-07-08

### Added
- `academic-source-verification`: a **reference-integrity module** — three read-only CrossRef
  scripts bundled under `scripts/`: `check_dois.py` (DOI resolution + title match),
  `find_dois.py` (propose the correct DOI for bad ones), and `metadata_check.py` (field-by-field
  verification of author/journal/volume/pages/year). Battle-tested on a live 206-entry
  bibliography: caught 27 bad DOIs (dead/wrong-target) and, after removing a false-positive class,
  2 genuine metadata errors — including entries with fabricated titles/journals and wrong
  volume/pages that a bib-only or title-only check missed. Key lesson encoded: `metadata_check.py`
  must NOT field-compare against a low-confidence title match (DOI-less books/cases), or it emits
  false positives. Skill bumped to 0.1.2.

## [0.2.1] — 2026-07-07

### Added
- `academic-source-verification`: a **presentation convention** for the emitted ledger so the
  regneark is readable, not just correct — front `Læsevejledning` legend sheet (tab index + full
  column/abbreviation legend), styled/frozen/filtered data sheets with tuned widths + wrapping +
  banding, and a back `Fejl fundet & rettet` report sheet. New `references/regneark_layout.md`
  (the spec) and `scripts/ledger_format.py` (deterministic formatter; writes a versioned copy,
  never the master). Added a "Præsentation" section to SKILL.md; skill bumped to 0.1.1.

## [0.2.0] — 2026-07-07

### Added
- New skill **`academic-source-verification`** (DA) — source & citation verification (external
  truth) plus a transparent, reproducible **audit ledger** used as an accountability instrument
  toward publisher and reader. Three checks: (1) reference correctness (CrossRef/DOI/OpenAlex/
  Semantic Scholar), (2) retraction/reliability (Retraction Watch/Crossmark/scite), (3) claim–
  source fidelity (primary source/Elicit/scite/cbs-libsearch annotations). Produces/maintains the
  reference-audit ledger with per-source provenance (methods, evidence, n-sources, retraction
  status, claim support, human sign-off, tool+version, date) and derives the in-book AI/source
  declaration. Includes `references/ledger_schema.md`, `references/declaration_templates.md`, and
  a read-only `scripts/ledger_build.py` (seeds the ledger, extracts in-text cites, flags phantom/
  orphan). Runs at the text-freeze boundary; companion to `pm-konsistens-audit` (internal
  consistency). Prompted by three citation errors that a bib-only audit could not catch (an inline
  journal misattribution, an appendix table year, and a phantom citation with no bib entry).

## [0.1.0] — 2026-07-07

### Added
- Initial repository. Brought four previously local-only, unpublished skills under version
  control: `academic-book`, `faglig-bog`, `pm-bog`, `pm-konsistens-audit`
  (incl. `pm-konsistens-audit/scripts/audit_all.py`).
- Added a **"Pipeline ordering"** note to every skill: these are form-phase skills
  (typography / overfull / pagination / cover, or numbering/float audit) and must run
  **after the text is frozen** — never before content, register and consistency are locked.
  A later word-count change invalidates a prior typography pass (re-run typography + build).
  Prompted by a live textbook where typography was run before the grammar/citation pass and
  the verification went stale (a late all-black blank back-cover page slipped through).
