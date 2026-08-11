# Stilprofiler — stemmeprofiler og deres dial-indstillinger

En profil er et navngivet bundt af indstillinger på målbare **dials**. Dialerne er
forankret i `forskningsgrundlag.md`. Niveauer er vejledende bånd, ikke hårde grænser;
`maal.py` rapporterer, hvor teksten ligger, så diagnosen er evidensbaseret, ikke
subjektiv.

## Dialerne

1. **Nominal/verbalstil** — andel af verbalsubstantiver/nominaliseringer (NyS;
   `maal.py` suffiks-proxy). Lavere = mere verbal/dynamisk. *Strip ikke til nul* —
   nominalisering er også fag- og kohæsionsredskab.
2. **LIX (rådgivende)** — Björnsson-tal. **Aldrig auto-handlet.** Sigtebånd pr. profil;
   læseværdighed > læsbarhed.
3. **Sætningsrytme/variation** — spredning i sætningslængde + variation i ordstilling
   (undgå monoton ligefrem ordstilling; Rask).
4. **Anglicisme-tæthed** — klodsede hybrider ("crowde … ud", "processere", "applicere",
   "redesigne"). Fordansk hybrider; behold bevidste engelske fagtermer (termbase).
5. **Kohæsion/forbindere** — tydelig rød tråd, jf.-apparat (Rienecker & Stray Jørgensen).
6. **Læser-tiltale** — du/vi/man; metatekst og signposting (Pontoppidan).
7. **Konkretisering/motivation** — eksempler, "menneskeligt ansigt", relevans,
   velplaceret overraskelse (Hidi & Renninger; Guthrie et al.). Skal være *relevant*
   (undgå seductive details).

Skala: **ML / L / M / H / MH** (meget lav … meget høj).

---

## Profil: `laerebog-klarsprog`  *(default)*
Mål: klar, levende universitetslærebogs-dansk. Den sikre default for brødtekst.

| Dial | Indstilling |
|---|---|
| Nominal/verbalstil | L–M (reducér, strip ikke) |
| LIX (sigtebånd) | ~45–52 (fagbånd; rådgivende) |
| Sætningsrytme | H (varieret; vekslende ordstilling) |
| Anglicisme-tæthed | L (fordansk hybrider; behold fagtermer) |
| Kohæsion | M–H |
| Læser-tiltale | M (du/vi hvor genren tillader) |
| Konkretisering/motivation | M |

## Profil: `formidlende-engagerende`
Mål: introkapitler, cases, forord. Varmere, mere motiverende.

| Dial | Indstilling |
|---|---|
| Nominal/verbalstil | L |
| LIX (sigtebånd) | ~40–48 |
| Sætningsrytme | H |
| Anglicisme-tæthed | L |
| Kohæsion | H (mere signposting) |
| Læser-tiltale | H |
| Konkretisering/motivation | H (eksempler, menneskeligt ansigt — relevant) |

## Profil: `stram-faglig`
Mål: tætte teori-/metodeafsnit, specialistmonografi. Præcis og konventionel.

| Dial | Indstilling |
|---|---|
| Nominal/verbalstil | M (tolereret) |
| LIX (sigtebånd) | ~50–56 (specialistlæser tåler højere) |
| Sætningsrytme | M |
| Anglicisme-tæthed | L–M |
| Kohæsion | M–H |
| Læser-tiltale | L |
| Konkretisering/motivation | L–M |

---

## Anvendelsesregler

- **Én default-profil pr. bog.** Element-type-overstyringer (fx cases →
  `formidlende-engagerende`, teoriafsnit → `stram-faglig`, bokse urørte) er tilladt,
  men skal **erklæres og logges**, så bogen læses som ét værk.
- **Bokse, definitioner, citater, figurer omskrives aldrig** uanset profil
  (`beskyttet_indhold.md`) — kun den omkringliggende brødtekst er i scope.
- **Præcision overstyrer profilen.** Ville en dial sløre en påstand, bevares den
  præcise original; log det.
- **LIX auto-handles aldrig.** Tallet er et symptom; en omskrivning må aldrig laves
  alene for at flytte LIX (Björnsson).
- **Sekvens med søsteren.** Kør klarsprog først, derefter `academic-danish-consistency`
  for at rydde stave-/formatdrift, en omskrivning kan have genindført.
