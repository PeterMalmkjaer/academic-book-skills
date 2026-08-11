# Beskyttet indhold & meningstroskab — academic-danish-klarsprog

Denne skill **omskriver brødtekst**, så dens troskabsregel er strengere end et
formattjek: den skal ændre *tekstur* og bevare *mening og hver reference nøjagtigt*.

## Den absolutte regel

En omskrivning er gyldig kun hvis BEGGE holder:
1. **Propositionelt indhold er identisk** — ingen påstand tilføjet, fjernet, styrket,
   svækket eller om-afgrænset. Omskrivning må ændre ord og struktur; den må aldrig
   ændre, hvad der hævdes, inkl. forbeholdets styrke (et "kan" forbliver et "kan").
2. **Alle referencer er byte-identiske** — hver citation, forfatter, år, DOI,
   `(afsnit x.y)` / `kapitel n` / `figur/tabel n`, hvert tal/statistik/beløb og hvert
   **defineret-term-navn** står ordret i omskrivningen.

## Aldrig omskrevet (ordlyd urørlig)

Kun den *omkringliggende* brødtekst er i scope. Følgende står nøjagtigt som skrevet
(en omskrivning må ikke trænge ind):
- Definitioner, Teoretiske/Perspektiv-/Case-/Sammenfatningsbokse og ethvert indrammet
  pædagogisk element
- Direkte citater og epigrafer (også uoversatte engelske citater)
- Figur-/tabeltekster, labels i figurer, tabelceller
- "Videre Læsning", referencelister, citationsstrenge
- Ligninger, kode/verbatim, matematik

## Defineret terminologi (dansk/engelsk)

*Navnet* på et defineret begreb — også de bevidst engelske fagtermer (*moral hazard,
ratchet effect, career concerns, asset specificity, crowding-out*) — er fast. En
omskrivning må forbedre sætningen omkring termen, men skal gengive termen ordret og må
ikke om-definere, gloss-skifte eller fordanske selve termen. (Hvorvidt en term *bør*
fordanskes er en konsistens-/oversættelsesbeslutning — ikke en klarsprogsbeslutning.)
Koordinér med termbasen i `academic-danish-consistency`, hvis den findes.

## Detektionsheuristik (.tex / .docx / plaintext)

- Boks-miljøer: `\begin{...}`…`\end{...}` der matcher
  `(?i)(definition|teorem|teoretisk|perspektiv|case|sammenfatning|boks|box|citat|tcolorbox|mdframed|figure|table)`.
- Citationskommandoer: `\cite`, `\citep`, `\citet`, `\parencite`, `\textcite` m.fl.
- Krydshenvisninger: `\ref`, `\cref`, `\autoref`, samt literal `(afsnit …)`, `§…`,
  `(kapitel …)`, `(figur …)`.
- Citater: `\begin{quote}`/`quotation`, `\epigraph{…}`, anførselstegn-spænd.
- Floats: `figure`/`table`-miljøer, `\caption{…}`, `\label{…}`, TikZ-nodetekst.
- Verbatim/kode/matematik: `verbatim`, `lstlisting`, `$…$`, `\[ … \]`, `equation`.
- Ved tvivl: **behandl som beskyttet og omskriv ikke.**

## Fase 3 menings-troskabstjek (bekræftes før levering)

For hver foreslået omskrivning:
- [ ] samme påstande, samme epistemiske styrke
- [ ] citationer / forfattere / år / DOI byte-identiske
- [ ] afsnit- & figurhenvisninger byte-identiske
- [ ] tal, statistik, beløb byte-identiske
- [ ] defineret-term-navne byte-identiske (også engelske fagtermer)
- [ ] intet beskyttet felt rørt

Enhver fejl → drop omskrivningen, gendan originalen, log årsagen. Lever linjen:
`Troskabstjek bestået: N omskrivninger, 0 påstande ændret, 0 beskyttede tokens rørt.`
