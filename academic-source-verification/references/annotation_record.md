# Claim-støtte / annoterings-record — format

Output-artefakt for **tjek #3 (korrekt brug af kilde)**. Ét dokument pr. kilde (eller pr. runde),
der viser, at manuskriptet BRUGER kilden korrekt — ikke bare at metadata/DOI er rigtige.

Regel: metadata + DOI = kilden er den rigtige og korrekt beskrevet. Claim-støtte = kilden siger
faktisk det, teksten tilskriver den. Hvis en påstand IKKE er støttet → find en anden kilde
(ret aldrig bare metadata for at "redde" en forkert kilde).

## Skabelon (pr. kilde)

```
## <Forfatter(e)> (<år>), "<titel>", <journal/venue> <bind(nr)>:<sider>, DOI <...>
Kilde-PDF: <sti/filnavn>

| Manuskriptets påstand (kapitel/linje) | Understøttende passage i kilden (citat) | Verdikt |
|---|---|---|
| <påstand 1 + sted> | "<verbatim citat fra kilden>" | ✅ støttet / ◐ delvist / ❌ ikke støttet |
| <påstand 2 + sted> | "<verbatim citat>" | … |

**Verdikt for kilden:** korrekt brugt / kræver anden kilde til påstand X.
**Annotering:** <filnavn>_ANNOTATED.pdf (highlights lavet med scripts/annotate_claims.py).
```

## Felter i hovedbogen (ledger), der udfyldes efter T3
- `claim_støttet` = ja / delvist / nej / na
- `annotation_ref` = sti til `*_ANNOTATED.pdf`
- `verifikationsmetoder` += `primærbog` / `pdf_annotation`
- `kilde_evidens` += kilde-PDF + de citerede passager

## Sådan laves highlights
1. Udled de korte, distinktive fraser fra hver understøttende passage (single-line fragmenter).
2. `python scripts/annotate_claims.py --in kilde.pdf --out kilde_ANNOTATED.pdf --phrase "…" --phrase "…"`
   (eller `--manifest jobs.json` for flere kilder).
3. Scriptet rapporterer fraser, den IKKE kunne finde — en manglende frase kan betyde, at kilden
   faktisk ikke indeholder påstanden → undersøg (kandidat til "anden kilde").
