# Rapportskabelon

Brug PRÆCIS denne struktur. Fast format er det, der gør kørsler sammenlignelige på tværs af
kapitler og over tid. Sprog: dansk, akademisk register, ingen rosende fyld.

---

# Tekstaudit: [tekstens titel/kapitel]

## Sådan læses denne rapport

> Denne audit er lavet af en sprogmodel (LLM) med en forankret vurderingsrubrik. En
> sprogmodel har begrænsninger: den kan overse, fejlvægte og fejllæse. Rapporten er derfor
> et **dialogværktøj** — et struktureret input til forfatterens og redaktørens videre
> arbejde — og må **aldrig stå alene** som endelig dom over teksten.
>
> **Om tallene:** Skalaen følger ikke skoleskalaen. 50 % svarer til standarden i den
> valgte målestok (her: [baseline]); 75–89 % er markant over standarden og den realistiske
> sigtezone; 90 % og derover er eksemplar-niveau, som pr. design er sjældent og ikke er
> arbejdsmålet; 100 % er et teoretisk maksimum. Et højt tal gør ikke i sig selv teksten
> klar til udgivelse — det afgøres af, om listen over bindende begrænsninger nederst er tom.

## Kalibrering
| Parameter | Valg |
|---|---|
| Genreprofil | [profil] |
| Niveau-baseline | [(a)/(b)/(c) + navn] |
| Aktive dimensioner | [fx S, H, T, M (F udgår: ingen figurer)] |
| Dimensionsvægte (renormaliserede) | [S 0,xx; H 0,xx; …] |
| Scoringsmateriale | [ca. X ord brødtekst; Y tabeller; Z figurer; ekskluderet: …] |

## Argumentrekonstruktion
**Hovedtese:** [én sætning]
**Bærende påstande:** [nummereret liste, 3–8, med afhængigheder]
**Betydningsniveauer:** [fx empirisk / teoretisk / normativt / ontologisk — og om skiftene markeres]
**Afvigelse fra tekstens selvbeskrivelse:** [fx "indledningen lover 4 kritikpunkter; teksten leverer 6 delpåstande" — eller "ingen"]

## Scoreoversigt
| Dimension | Score | Bånd | Konfidens | Svageste kriterium |
|---|---|---|---|---|
| S Semantisk | xx % | ±x pp | … | Sx |
| … | | | | |
| **Samlet (vægtet)** | **xx %** | | | |

**Fortolkning:** [Placér samlet score og hver dimension i fortolkningsskalaen fra
kalibrering.md — fx "86 % = stærk tekst, markant over baseline (b)-standarden; sigtezone
nået. 50 % svarer til baseline-standarden; 90+ er eksemplar-zone, ikke arbejdsmålet."]

[Halo-alarm her, hvis alle dimensioner ligger inden for 10 pp.]
[Stabilitetsresultat her, hvis to gennemløb er kørt: |ΔD_j| pr. dimension.]

## Kriterievurderinger

### S1 Definitionspraksis — score x/4 (konfidens: …)
**Belæg:** "[ordret citat]" (afsnit N). "[ordret citat]" (afsnit M).
**Analyse:** [hvad belægget viser i forhold til forankringerne — hvorfor x og ikke x±1]

[… gentag for alle aktive kriterier, i rækkefølgen S→H→T→M→F …]

**Under S4 — påstandstabel:**
| Påstand | Formuleringsstyrke | Belægsstyrke | Kalibreret? |
|---|---|---|---|
| [påstand 1, kort] | afdæmpet/kalibreret/absolut | svag/moderat/stærk | ja/nej + flag |

**Under M — metafor-inventar (én række pr. bærende metafor):**
| Metafor | Funktion (M1) | Afbildning (M2) | Konsistens (M3) | Framing (M4) | Belæg |
|---|---|---|---|---|---|
| [fx "organisationen som X"] | 0–4 | 0–4 | 0–4 | 0–4 | [sted] |

M-kriteriescorerne aggregeres fra inventaret; svageste BÆRENDE metafor vægter tungest.

## Tværgående fund
[Mønstre på tværs af kriterier — fx samme begrebsglidning bag både S2- og T2-fund.
Kun observationer, der har belæg i kriterievurderingerne ovenfor.]

## Produktionsfund (ikke-scoret)
[Produktionsrester, orddelings-/parsing-artefakter, tomme sider, tabel-/figurformatering,
dangling numre. Indgår ikke i scoren; rapporteres altid. Bogdækkende nummerkontrol →
pm-konsistens-audit.]

## Prioriterede flag
1. **[Kriterium, sted]:** [fundet + hvorfor det er vigtigst]. *Henvis til omskrivning via
   academic-danish-klarsprog / relevant skill — foreslå ALDRIG selv ny ordlyd.*
2. …
[5–10 flag, ordnet efter forventet effekt på tekstens kvalitet, ikke efter rækkefølge i teksten.]

## Bindende begrænsninger
[Pr. dimension: hvilke flag holder aktuelt scoren nede. Fx: "S: løses flag 1 (S2-glidning),
er næste begrænsning S1-definitionen i afsnit 3." Ingen 'parathedsprocent' — udpeg
begrænsningerne i stedet.]

[Valgfrit: **"Hvad teksten ikke påstår"-anbefaling** — foreslå (uden at skrive den) en
eksplicit afgrænsning, hvis teksten er polemisk udsat.]

## Handoff-pakke
[Omskrivningsbriefs til relevante skills — pr. brief: passage(r), problem, retning.
INGEN færdig ordlyd. Fx: "klarsprog: afsnit 12–14, absolut modalitet på moderat belæg
(jf. påstandstabel), retning: kalibrér uden at svække konklusionen."]

## Metodeboks
- Denne audit er en struktureret second opinion fra en sprogmodel-bedømmer med forankret
  rubrik — ikke et psykometrisk valideret måleinstrument. Den er et dialogværktøj til
  videre menneskelig bearbejdning og står aldrig alene; beslutninger om teksten er
  forfatterens og redaktørens.
- Scores gælder KUN mod den valgte kalibrering ([profil] + baseline [x]); de kan ikke
  sammenlignes med kørsler under anden kalibrering.
- Konfidensbånd er konventioner (±3/±6/±10 pp efter kriteriekonfidens), ikke statistiske intervaller.
- Kriterier scoret som "skøn" (uden belæg): [liste eller "ingen"].
- H1/H2 er pr. design højst middel-konfidens (fortolkningsdybde er disciplineret skøn).
- Evidensgrundlag for kriterierne: se skill'ens referenceliste (Jonsson & Svingby 2007;
  Suddaby 2010; Tracy 2010; m.fl.).
