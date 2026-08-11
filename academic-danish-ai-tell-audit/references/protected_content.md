# Excluded from the count — body prose only (Danish)

Measures **running body prose only**. Excluded from both word total and marker count:
- Citations, forfatternavne, år, DOI, referencelister, "Videre Læsning"
- Direkte citater og epigrafer
- Bokse: definitioner, teoretiske/perspektiv-/case-/sammenfatningsbokse
- Figur-/tabeltekster, labels, tabelceller
- Krydshenvisninger og afsnits-/kapitelnumre
- Definerede-term-navne, ligninger, kode/verbatim

## Detection heuristics
- LaTeX: box/quote/figure/table/verbatim/equation environments; \cite*, \ref*,
  \caption, \label; $…$, \[ … \].
- Plaintext/PDF: lines starting Definition/Teoretisk/Teoriboks/Perspektiv/Case/Figur/
  Figure/Tabel/Table/Kilde/Videre Læsning; quotation-mark spans; parenthetical
  (Forfatter, 19xx/20xx).
- When uncertain, treat as protected and exclude.
