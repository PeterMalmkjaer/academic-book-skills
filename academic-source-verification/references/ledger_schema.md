# Hovedbog / ledger — kolonneskema (v9)

Hovedbogen er reference-audit-regnearket. v9 = v8-skemaet + 10 provenans-kolonner.
Én række pr. citeret kilde (bib-nøgle). Regnearket er **revisionssporet**: ingen kilde
markeres verificeret uden en provenans-fyldt række.

## Eksisterende kolonner (v8 — bevares uændret)

| Kolonne | Betydning |
|---|---|
| `Kapitel` | hvor kilden citeres (fx `kap07`, `appendiks_b`) |
| `Bib-nøgle` | nøgle i `references.bib` (fx `MellstromJohannesson2008`) |
| `Reference (forkortet)` | kort form (fx `Johannesson (2008)`) |
| `Tier` | verifikationsniveau: `T1` (fuldt verificeret) / `T2` (metadata) |
| `p_correct` | sandsynlighed for korrekt (0–100); i json også `p_wrong`, `p_unknown` |
| `Verificeringskommentar` | fritekst-noten (json: `full_context`, `llm_comment`) |

## Nye kolonner (v9 — provenans / revisionsspor)

| # | Kolonne | Type / tilladte værdier | Udfyldningsregel |
|---|---|---|---|
| 1 | `verifikationsmetoder` | flervalg, semikolon-separeret: `bog_læst`, `primærbog`, `scite`, `referencer`, `elicit`, `web`, `crossref/doi`, `retraction_watch`, `pdf_annotation` | ALLE metoder faktisk brugt for denne kilde |
| 2 | `antal_kilder` | heltal ≥1 | antal uafhængige, verificerbare kilder konsulteret |
| 3 | `kilde_evidens` | fritekst: DOI'er / URL'er / bog-sted (side) | de konkrete beviser, så *kilden er tydelig* |
| 4 | `annotation_ref` | fritekst / sti | peger på highlight/annotation lavet i artiklen (cbs-libsearch); ellers tom |
| 5 | `retraktionsstatus` | `none` / `retracted` / `corrected` / `erratum` / `EoC` / `ikke tjekket` | tjek 2-resultat (Retraction Watch / Crossmark / scite) |
| 6 | `claim_støttet` | `ja` / `delvist` / `nej` / `na` / `ikke tjekket` | tjek 3: siger kilden det, teksten påstår? |
| 7 | `in_text_match` | `match` / `drift-rettet` / `na` / `ikke tjekket` | matcher inline/tabel-gengivelse bib'en (resultat fra `pm-konsistens-audit`) |
| 8 | `verificeret_af` | initialer + `(AI: ja/nej)` | menneskelig sign-off + om AI assisterede |
| 9 | `verifikationsdato` | ISO-dato `YYYY-MM-DD` | dato for (seneste) verifikation |
| 10 | `værktøj_version` | fritekst: værktøj + version | til AI-deklarationen (fx `Claude (Cowork) + Exa + Scite`) |

## Defaults for eksisterende v8-rækker

v8 registrerede ikke provenans struktureret. For ærlighed sættes v9-defaults for de
rækker, der ikke er nyverificeret:

- `verifikationsmetoder` = `` (tom) · `antal_kilder` = `` · `kilde_evidens` = `(se Verificeringskommentar — ikke struktureret i v8)`
- `retraktionsstatus` = `ikke tjekket` · `claim_støttet` = `ikke tjekket` · `in_text_match` = `ikke tjekket`
- `verificeret_af` = `` · `verifikationsdato` = `` · `værktøj_version` = ``

Disse fylder skillen efterhånden ud, kilde for kilde. En blank provenans er et *ærligt*
signal om, at kilden endnu ikke har fået det fulde spor — ikke en påstand om, at den har.

## Udfyldte eksempler (nyverificeret 2026-07-07)

**MellstromJohannesson2008** (kap07) — inline-journal rettet AER → JEEA:
- `verifikationsmetoder`: `referencer; crossref/doi; web; scite`
- `antal_kilder`: `6`
- `kilde_evidens`: `DOI 10.1162/JEEA.2008.6.4.845; Wiley; IDEAS/RePEc; EconPapers; references.bib; main_EN.bbl`
- `retraktionsstatus`: `none` · `claim_støttet`: `ja` · `in_text_match`: `drift-rettet`
- `verificeret_af`: `PM (AI: ja)` · `verifikationsdato`: `2026-07-07` · `værktøj_version`: `Claude (Cowork) + Exa + Scite`

**PosthumaCampion2008** (kap15/appendiks_b) — tabel-år rettet 2009 → 2008:
- `verifikationsmetoder`: `referencer; web`
- `antal_kilder`: `2`
- `kilde_evidens`: `Sage (Compensation & Benefits Review 40:47-55, 2008); Semantic Scholar; references.bib`
- `retraktionsstatus`: `none` · `claim_støttet`: `ja` · `in_text_match`: `drift-rettet`
- `verificeret_af`: `PM (AI: ja)` · `verifikationsdato`: `2026-07-07` · `værktøj_version`: `Claude (Cowork) + Exa`
