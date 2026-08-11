# Danish marker lexicon (versioned) — v0.1.0  [informed adaptation — calibrate]

LLM-overused Danish style markers (informed adaptation; not yet corpus-validated — see
research_basis.md). These are legitimate Danish words in moderation — score *density*,
never presence.

## Adjectives / adverbs
afgørende, central, centralt, centrale, nuanceret, robust, banebrydende, sømløs, alsidig,
mangefacetteret, uvurderlig, essentiel, markant, betydelig, dybdegående, omfattende,
innovativ, holistisk, ydermere, endvidere, desuden, derudover

## Verbs / abstractions
udnytte, muliggøre, understøtte, fremhæve, belyse, forankre, sammenvæve, potentiale,
indsigt(er), landskab [abstrakt], synergi, hjørnesten, samspil

## Fixed phrases
"en bred vifte af"; "spiller en central rolle"; "spiller en afgørende rolle"; "det er
værd at bemærke"; "det er vigtigt at bemærke"; "kaster lys over"; "baner vejen for"; "i
takt med"; "i en verden hvor"; "i sidste ende"; "i stigende grad"

## Structural tells (detected by the script)
- **Rule-of-three**: "x, y og z" strings of parallel adjectives/nouns.
- **Negative parallelism**: "ikke kun ... men også", "ikke blot ... men".
- **Boilerplate emphasis**: "det er værd at bemærke", "det er vigtigt at bemærke".
- **Connective openers**: sentences starting "Derudover", "Desuden", "Endvidere",
  "Ydermere", "Ikke desto mindre".
- **Formulaic closers**: "Afslutningsvis", "Sammenfattende".
- **Em-dash density**: high em-dash counts.

> Calibrate against a Danish baseline before treating the numbers as authoritative.
