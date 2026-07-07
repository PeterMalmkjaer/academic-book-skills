# Hovedbog — layout & præsentationskonvention

Hovedbogen (regnearket) er ikke kun data — det er et revisionsspor, forlag og læsere
kan blive bedt om at se. Derfor skal det emitterede regneark være **pænt og
overskueligt**, ikke bare korrekt. Konventionen nedenfor er obligatorisk og anvendes
deterministisk af `scripts/ledger_format.py`.

## Fane-rækkefølge
1. **Læsevejledning** (forrest, grøn fane) — indhold + fuld legende.
2. **Oversigt** — status-resume.
3. **Datafaner** — hovedtabel + delmængder (fx `Alle Referencer`, `T1`, `T2`, `Afventer`).
4. **Fejl fundet & rettet** (bagerst, rød fane) — rapport + fejltabel.

## Læsevejledning (forrest)
Skal indeholde, i denne rækkefølge:
- **Om filen** + `v8` (fryst master, rør ikke) vs `v9` (arbejdskopi).
- **Indhold** — én linje pr. fane, hvad den er.
- **Kolonner** — hver kolonne forklaret i klart sprog.
- **Koder** — alle `verifikationsmetoder`-koder udfoldet (`crossref/doi`, `scite`,
  `pdf_annotation`, …).
- **Værdier** — vokabularer for `retraktionsstatus`, `claim_støttet`, `in_text_match`.
- **Bemærk** — `ikke tjekket` er et *ærligt* signal (ikke udfyldt endnu, ikke "tjekket");
  provenans-kolonnerne (7–16) er selve revisionssporet.

**Regel om forkortelser:** ingen forkortelse uden forklaring. Brug forkortelser, en læser
forstår; udfold dem alle i Læsevejledning.

## Datafaner — formatering
- Overskriftsrække: mørk fyld (navy `#1F4E79`), hvid fed, centreret, kant.
- `freeze_panes` sat, så overskrift + de første identifikations­kolonner står fast.
- Autofilter på hele tabellen.
- Kolonnebredder tilpasset indhold; tekstombrydning på de lange felter
  (`Verificeringskommentar`, `verifikationsmetoder`, `kilde_evidens`, `værktøj_version`).
- Let stribning (lys `#EAF1F8`) på hver anden datarække.

## Fejl fundet & rettet (bagerst)
- Kort **rapporttekst** øverst: mønsteret bag fejlene + at v8 er urørt.
- Tabel med kolonner: `# · Type · Kilde/sted · Kapitel · Hvad var forkert · Rettelse ·
  Verificeret via · Konfidens · Delt m. DA? · DA-pendant · RUN · Status`.
- Én række pr. fund; stribning + autofilter som datafanerne.

## Farver
navy `#1F4E79` (overskrifter) · lys `#EAF1F8` (stribe) · grøn `#2E7D32` (Læsevejledning-fane)
· rød `#C0392B` (Fejl-fane) · guld `#E0A654` (accent, valgfri).

## Script
`python scripts/ledger_format.py --in ledger.xlsx --out ledger_pretty.xlsx [--errors errors.json]`
anvender hele konventionen (styling + Læsevejledning + fejl-frame). Skriver aldrig til
master; producér altid en versioneret kopi.
