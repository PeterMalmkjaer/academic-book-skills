# Beskyttet indhold — røres aldrig, kun format tjekkes

Skillens kardinalregel. Ordlyden af alt nedenfor ændres aldrig og foreslås aldrig
ændret — heller ikke retskrivnings-/term-skift. Kun *formatet af rammen* (label,
nummerering, titellinjens tegnsætning) må flagges.

Ville en regel røre et token i beskyttet indhold, **springes ændringen over** og logges
som `tjek (beskyttet)` uden forslag.

## Beskyttet (ordlyd urørlig)
1. **Bokse** — definitioner, teoretiske bokse, perspektivbokse, casebokse,
   sammenfatningsbokse og ethvert indrammet pædagogisk element. Tjek kun: labelformat
   ("Definition 16.1: …"), nummererings­kontinuitet, titellinjens tegnsætning.
2. **Citater & epigrafer** — alt i anførselstegn eller citatmiljø, også uoversatte
   engelske epigrafer.
3. **Citationer & referencer** — "(Forfatter, år)", forfatternavne, år, DOI, sidetal,
   "Videre Læsning", bokskildeangivelser.
4. **Krydshenvisninger** — "(afsnit x.y)", "kapitel n", "figur/tabel n", "§", og selve
   numrene.
5. **Figurer & tabeller** — tekster, labels i figurer, akse-/bokstekst, tabelceller.
6. **Defineret-term-navne** — selve termen (også engelske fagtermer). Kun
   fed-ved-første-brug-*formatet* er i scope, aldrig ordlyden.
7. **Tal, data, resultater** — statistik, beløb, procenter, datoer, stikprøvestørrelser.
   Format (fx decimalkomma, interval-tankestreg) må flagges; værdien aldrig.
8. **Egennavne & navngivne rammer** — love, teorier, modelnavne, organisationsnavne.

## Detektionsheuristik (.tex)
- Boks-miljøer: `\begin{...}`…`\end{...}` med navn der matcher
  `(?i)(definition|teorem|teoretisk|perspektiv|case|sammenfatning|boks|box|citat|quote|quotation|tcolorbox|mdframed|figure|table|verbatim|lstlisting|equation)`.
- Citationskommandoer: `\cite`, `\citep`, `\citet`, `\parencite`, `\textcite`, `\autocite`.
- Krydshenvisninger: `\ref`, `\cref`, `\Cref`, `\autoref`, `\pageref`, samt literal
  "(afsnit …)", "§…", "(kapitel …)".
- Citater: `\begin{quote}`/`quotation`, `\epigraph{…}`, anførselstegn-spænd.
- Floats: `figure`/`table`, `\caption{…}`, `\label{…}`, TikZ-nodetekst.
- Verbatim/kode/matematik: `verbatim`, `lstlisting`, `$…$`, `\[ … \]`, `equation`.

## Detektionsheuristik (plaintext / PDF-udtræk)
- Linjer der starter med boks-label: `^(Definition|Teoretisk|Teoriboks|Perspektiv|Case|
  Sammenfatning|Figur|Figure|Tabel|Table|Kilde)\s*\d?`.
- Parentetisk "(... 19xx)" / "(... 20xx)" og "(afsnit \d", "§\d".
- Anførselstegn-spænd (danske eller engelske).
- "Videre Læsning" og "Diskussionsspørgsmål" (kun format).

## Reglen, gentaget
> Et forslag er gyldigt kun, hvis dets `nuværende` og `foreslået` adskiller sig i intet
> andet end et brødtekst-retskrivnings-/formattoken, OG ændringen ligger uden for hvert
> beskyttet felt ovenfor. Fase 4 bekræfter dette for hvert forslag før levering.
