---
name: academic-book-layout-audit
description: >-
  Pre-press-/layoutaudit af en LaTeX-fagbog: måler GEOMETRI i den satte PDF og flager
  det, der bliver til trykfejl — overfull hbox klassificeret efter pt (≥50pt klippes
  i tryk), BRUDTE BOKSE hvor fortsættelsen efterfølges af tomrum (usynlig i kildeteksten),
  småhale-inventar for midt-flow-bokse, float-afstand (fremadhenvisninger >1 side),
  blanke sider, rasterbilleder under dpi-tærskel, og FOLIO-PARITET (arabertal 1 skal
  ligge på recto). Kan sammenligne mod en TIDLIGERE PDF og fortælle, om et fund er NYT
  eller præeksisterende. Læs-kun: ændrer aldrig kilder, tal, citater eller
  krydshenvisninger. Triggere: "layout-scan", "pre-press-tjek", "overfull", "brudte
  bokse", "tomme sider", "klippes teksten i tryk", "er bogen klar til tryk",
  "float-placering", "billede-dpi", "folio-paritet", "starter kapitel 1 på højreside",
  "recto/verso". OPT-IN — auto-starter ikke.
license: MIT
metadata:
  family: academic-book
  siblings: pm-konsistens-audit (numre/referencer), academic-danish-consistency og academic-english-consistency (house style)
  version: 1.1.0
---

# Academic book — layout audit (pre-press geometri)

Det manglende geometri-modul i skill-familien. De øvrige spørger *"er teksten rigtig og
konsistent?"*. Denne spørger **"renderer bogen rigtigt på papir?"**

Den arbejder på den **satte PDF**, ikke på kilden — fordi den fejlklasse, den er bygget til,
er usynlig i `.tex`-filerne. En boks, der brækker over to sider og efterlader en forældreløs
hale efterfulgt af en tom side-rest, ser fuldstændig normal ud i kildeteksten.

## Hvad den gør — og ikke gør

**Gør:** måler og flager med sidenummer og sværhedsgrad; foreslår fix.
**Gør ikke:** ændrer indhold, tal, teori, citater eller krydshenvisninger. Nummerering og
referencekonsistens hører til `pm-konsistens-audit`; retskrivning og house style til
consistency-skillene; prosakvalitet til tekstauditterne.

## Sektionerne

| Sektion | Hvad | Sværhedsgrad |
|---|---|---|
| **A** | Overfull `\hbox` fra `.log`, klassificeret: **≥50pt = klippes i tryk**, 20–50pt tydelig, <20pt kosmetisk | KRITISK ved ≥50pt |
| **Check A** | **Brudt boks, hvor fortsættelsen efterfølges af tomrum.** Boksen rører tekstbunden, samme fyldfarve starter i toppen af næste side, og der står INGEN tekst under halen | **KRITISK** |
| **Check B** | Småhale-inventar: haler under tærsklen, som EFTERFØLGES af tekst | kosmetisk — **udskyd** |
| **Check C** | Float-afstand: `Figur/Tabel X.Y`-referencer mod captions, **type-korrekt** (Figur og Tabel deler numre!). Kun fremad >1 side flages | til vurdering |
| **Check D** | **Folio-paritet:** arabertal 1 skal ligge på en ULIGE PDF-side (= recto). Plus folio-placering: venstre på verso, højre på recto | **KRITISK** |
| **E** | Blanke / næsten-blanke sider med sidenumre | papiromkostning |
| **G** | Rasterbilleder under dpi-tærskel (effektiv dpi = pixels ÷ placeret bredde) | KRITISK ved tryk |

## Hvorfor Check A og Check B skal holdes skarpt adskilt

Det er skillens vigtigste enkeltindsigt, og den er lært dyrt.

**Check A er en strukturel fejl.** I PM-bogen var 12 af 17 læringsmålsbokse brækket med en
forældreløs hale — ned til elleve ord — efterfulgt af en tom side-rest, fordi et `\newpage`
fulgte efter boksen. Fix: fjern `breakable` fra det pågældende `tcolorbox`-miljø, men **kun**
når boksen altid kan stå på én side og efterfølges af et sideskift. Tomrummet flytter da til
efter åbningsindholdet = normal kapitelåbnings-luft. Sideantal ~uændret.

**Check B er kosmetik.** Midt-flow-haler efterfølges af tekst — der er intet tomrum, og det er
normal `breakable`-adfærd. Hale-polering er **sidste-pagineringsarbejde**: enhver senere
tekstændring re-flower dem alligevel. Ret dem efter prøvetryk, ikke før.

Blander man de to, retter man tolv kosmetiske ting og re-flower dem væk ved næste build.

## Check D: folio-paritet — den fejl, der rammer hele bogen på én gang

Alle de øvrige checks finder lokale fejl: én boks, én float, ét billede. Check D finder den
ene fejl, der gør **hele bogen** forkert, og som ingen ser i kildeteksten.

**Reglen:** PDF-side 1 er recto. Derfor skal den første arabisk nummererede side — folio "1" —
ligge på en ULIGE PDF-side. Gør den ikke det, er hvert eneste opslag i bogen spejlvendt:
kapitler åbner på venstresider, marginfolioer vender indad, og et prøvetryk afslører det først,
når papiret er købt.

**Hvornår den brydes:** når frontmatteret vokser eller skrumper med et **ULIGE** antal sider.
En tilføjet dedikation, en fjernet blank side, en forord-side mere. Ændringer i bagmatteren —
en ny litteraturlistepost, et udvidet register — kan aldrig bryde pariteten, og det er værd at
vide, når man skal afgøre, om en rettelse overhovedet kræver et nyt paritetstjek.

```bash
python3 scripts/check_d.py main.pdf            # exit 0 / 1 / 2
```

Tre udfald, med hver sin exitkode, så scriptet kan bruges som gate i en rettelsesrunde:
`ULIGE ✓` (0) · `LIGE ✗ — PARITETSFEJL` (1, også ved forkert placerede folioer) ·
`INKONKLUSIV ⚠` (2, arabertal-1 blev ikke fundet).

### Fælden, som enhver implementering falder i

Arabertal 1 falder **altid** på en kapitelåbningsside, og kapitelåbninger bruger `plain`
pagestyle med **centreret** folio. Den første, ad hoc-skrevne udgave af denne kontrol sprang
centrerede folioer over med `continue` — *før* den registrerede tallet — og meldte derfor
"arabertal-1 ikke fundet → paritetsfejl" på en bog med fuldstændig korrekt paritet, hver eneste
gang. I PM-bogen ligger folioen 5,7 pt (DA) og 7,1 pt (EN) fra sidemidten, altså langt inden
for centrerings-toleransen.

To principper er bygget ind i `check_d.py` som følge:

1. **Mål først, klassificér bagefter.** Registrér observationen, før du beslutter, om siden
   hører til den kategori, du er ved at måle.
2. **"Ikke målt" er ikke "målt og fejlet".** De to udfald har hver sin tilstand og hver sin
   exitkode. Ellers råber værktøjet ulv, og operatøren lærer at ignorere det.

Kontrollen er verificeret både positivt (PM-bogen DA s. 31 / EN s. 27, begge ulige, 0 forkert
placerede folioer) og **negativt**: en kopi af PDF'en med én frontmatter-side fjernet giver
`PARITETSFEJL` og exit 1, og en PDF uden folioer giver `INKONKLUSIV` og exit 2. Et
paritetstjek, der aldrig har set en paritetsfejl, er ikke afprøvet.

## `--compare`: er fundet nyt?

Det spørgsmål, en operatør altid stiller efter en rettelsesrunde, er *"har jeg lige ødelagt
noget?"*. Med `--compare tidligere.pdf` kører skillen samme scan mod en ældre PDF og
rapporterer pr. fundklasse, om tallet er steget.

I PM-bogen viste den, at seks blanke sider og én fremad-float fandtes i **alle** builds fra
samme dag — altså præeksisterende, ikke indført af dagens rettelser. Uden den kontrol ligner
seks blanke sider set for første gang en regression.

## Bokstyper

`--preamble main.tex` udleder farve→miljø-kortet fra `\definecolor` + `\newtcolorbox{...}{...
colback=...}`, så rapporten siger `theorybox` frem for `(240,248,255)`. **Flere miljøer kan
dele farve** — i PM-bogen deler `learninggoals` og `chaptersummary` samme lysegrå, og
rapporten skriver dem derfor som `learninggoals / chaptersummary`. Uden `--preamble` vises RGB.

## Forudsætning

Skillen kræver **PyMuPDF**, som ikke følger med en standard-Python:

```bash
pip3 install pymupdf          # eller: pip3 install pymupdf --break-system-packages
```

Begge scripts fejler med en klar besked, hvis pakken mangler --- ikke en traceback. Bemærk at
Python-installationen betyder noget: PyMuPDF kan være til stede for `/usr/local/bin/python3`
og mangle for en anden `python3` på samme maskine. Kør skillen med den Python, der HAR pakken.

**Uden netadgang** (afskærmet arbejdsmiljø, sandkasse med egress-proxy) fejler `pip3 install`
med `403 Forbidden` fra pakkeindekset. Så hent hjulet ét sted med netadgang og installér det
lokalt --- husk at matche platform, Python-version og arkitektur:

```bash
# på en maskine med net:
pip download pymupdf --only-binary=:all: \
    --platform manylinux2014_aarch64 --python-version 310 --implementation cp --abi cp310 -d .
# på målmaskinen:
pip3 install --no-index --no-deps --break-system-packages pymupdf-*.whl
python3 -c "import pymupdf; print(pymupdf.__version__)"
```

Kontrollér også **hvor** pakken landede: en `--user`-installation i et sessionshjem forsvinder,
når sessionen slutter. `python3 -c "import pymupdf; print(pymupdf.__file__)"` afslører det.
Ligger hjulet gemt i projektmappen, tager geninstallationen få sekunder og kræver ikke net.

## Kørsel

```bash
python3 scripts/layout_audit.py --pdf main.pdf --log main.log \
    --preamble main.tex --lang da --out LAYOUT_SCAN.md \
    --compare forrige_build.pdf
```

Parametre: `--tail-cm` (Check B-tærskel, default 2,5), `--dpi` (default 250 — Saxo kræver
≥250 i indmad, ≥300 på omslag), `--lang da|en` (styrer `Figur/Tabel` mod `Figure/Table`).

Check D kører separat, fordi den er en gate og ikke en rapport --- den skal kunne stoppe en
rettelsesrunde på sin exitkode:

```bash
python3 scripts/check_d.py main.pdf main_EN.pdf
```

**Kør Check D efter enhver ændring i frontmatteret.** Ændringer i brødtekst og bagmatter kan
ikke bryde pariteten; frontmatteret kan.

**PDF'en skal være bygget på den maskine, der ejer trykfilen.** Samme kilde bygget under en
anden TeX Live-version pagineres anderledes — i PM-bogen 619 sider på forfatterens Mac mod
624–625 i en Linux-container. Et layout-scan af den forkerte PDF måler den forkerte bog.

## Grænser, værd at kende

- Check A/B hviler på fyldte rektangler bredere end 250pt. Bokse uden fyldfarve ses ikke.
- Check C matcher kun `Type X.Y`-mønstret; henvisninger i prosa uden nummer fanges ikke.
- Blank-side-testen er "under 40 tegn og ingen tegninger" — en side med kun et sidehoved
  tælles ikke som blank.
- Widow/orphan er ikke med. Det er svært at måle robust, og falske positiver ville drukne
  de fund, der betyder noget.
- Omslagsgeometri (bleed, ryg, stregkodezone) er ikke med i v1.1.
- Check D antager, at folioen står i det nederste 65pt-bånd, og at centrerede folioer betyder
  `plain` pagestyle. En bog med folio i sidehovedet eller i marginen på siden måles ikke
  korrekt --- den vil rapportere `INKONKLUSIV` eller mange falske "uden folio", hvilket er den
  rigtige opførsel: hellere sige "jeg kunne ikke måle" end at gætte.
- Check D finder arabertal-1 som den første folio, der er cifferet "1". En bog, hvis frontmatter
  bruger arabertal frem for romertal, kan derfor ikke måles med den her.

## Rør-ikke

Skillen skriver kun sin egen rapport. Foreslåede fixes udføres af operatøren med backup,
assertion og byte-diff — som i resten af familien.
