# Excluded from the score — body prose only (Danish)

Scores **running body prose only**. Excluded from word/sentence totals and feature counts:
- Citations, forfatternavne, år, DOI, referencelister, "Videre Læsning"
- Direkte citater og epigrafer (de ville kunstigt hæve Human Interest)
- Bokse: definitioner, teoretiske/perspektiv-/case-/sammenfatningsbokse
- Figur-/tabeltekster, labels, tabelceller
- Krydshenvisninger og afsnits-/kapitelnumre
- Definerede-term-navne, ligninger, kode/verbatim

## Detection heuristics
- LaTeX: box/quote/figure/table/verbatim/equation-miljøer; \cite*, \ref*, \caption, \label; $…$.
- Plaintext/PDF: linjer der starter Definition/Teoretisk/Teoriboks/Perspektiv/Case/Figur/
  Figure/Tabel/Table/Kilde/Videre Læsning; anførselstegn-spænd; (Forfatter, 19xx/20xx).
- Ved tvivl: behandl som beskyttet og ekskludér.
