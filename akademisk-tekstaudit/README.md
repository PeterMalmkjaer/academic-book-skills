# akademisk-tekstaudit

Evidensbaseret kvalitetsaudit af danske akademiske tekster (kapitler, efterskrifter, monografier,
artikeludkast) på fem dimensioner — semantisk indhold, hermeneutisk indhold, teknisk opbygning,
metaforbrug samt tabeller/figurer — plus en valgfri sjette flag-dimension for diskurs- og
magtrefleksivitet (v1.1). Forankret 0–4-rubrik, to-parameter-kalibrering (genreprofil +
niveau-baseline), vægtet aggregering, konfidensbånd og ordret tekstbelæg pr. score.

**Måler og flager — omskriver aldrig.** Omskrivning henvises til `academic-danish-klarsprog`.
OPT-IN: kør kun ved eksplicit anmodning. Søster-skill: `academic-english-text-audit` (engelsk).

## Struktur

- `SKILL.md` — workflow (kalibrering → argumentrekonstruktion → analyse-før-scoring → rapport)
- `references/kalibrering.md` — genreprofiler, baselines, fortolkningsskala
- `references/rubrikker.md` — 19 kriterier med forankringer
- `references/rubrik_D_diskurs.md` — valgfri D-dimension (v1.1) med sikkerhedsventiler
- `references/rapportskabelon.md` — fast rapportformat
- `references/referencer.md` — evidensgrundlag (APA, DOI-verificeret)

Se `CHANGELOG.md` for versionshistorik og `SKILL.md` § Designhistorik for begrundede dimensionsvalg.
