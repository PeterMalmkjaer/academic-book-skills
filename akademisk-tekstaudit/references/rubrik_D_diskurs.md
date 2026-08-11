# Dimension D — Diskurs- og magtrefleksivitet (v1.1-tillæg)

## Status og sikkerhedsventiler (læs FØR brug)

Dimension D adskiller sig principielt fra S/H/T/M/F: den vurderer tekstens *refleksivitet om
magt, position og framing* — ikke tekstens holdninger. Fordi netop denne skelnen er svær for
en LLM-bedømmer (risiko: at score politik i stedet for kvalitet), gælder fire hårde ventiler:

1. **OPT-IN pr. kørsel.** D køres kun, når brugeren eksplicit beder om det. Default er FRA,
   og rapporten noterer altid, om D var til- eller fravalgt.
2. **FLAG-tilstand er default.** D rapporteres som strukturerede fund UDEN score. Scoret
   tilstand (0–4 pr. kriterium) kræver brugerens eksplicitte anmodning og indgår da med
   vægt højst 0,05 (renormalisér øvrige vægte).
3. **Konfidens-loft: middel** — som H1/H2. Diskursfund er disciplineret skøn, ikke måling.
4. **Positionsneutralitet:** En tekst kan indtage ENHVER position og opnå topniveau, hvis
   positionen deklareres, alternativer anerkendes, og framingen er markeret. Bedømmeren må
   ALDRIG belønne/straffe selve positionen. Fund formuleres som "teksten markerer ikke X" —
   aldrig som "teksten burde mene Y".

**Begrundelse for optagelsen (dokumenteret designhistorik):** Dimensionen manglede i v1.0,
selvom diskurs/magt var det mest produktive fund i det kryds-model-review, skillen blev
formaliseret fra (laveste score, udløste væsentlig værkudvikling). Udeladelsen var
udokumenteret. v1.1 optager dimensionen med ovenstående ventiler frem for at lade instrumentet
være blindt for sin egen mest værdiskabende fundklasse. Evidensforbehold: D-kriterierne har
svagere psykometrisk forankring end S/T-kriterierne (kritisk diskursanalyse er en
fortolkningstradition, ikke en målestandard — Fairclough 1992; framing-evidens:
Thibodeau & Boroditsky 2013; Entman 1993); det skal stå i metodeboksen ved hver D-kørsel.

## Kriterier (observerbare forankringer — scor kun det, du kan pege på)

**D1 Deklareret ståsted**
- 0: Teksten fremsætter omstridte vurderinger uden nogen markering af eget ståsted eller interesse.
- 2: Ståstedet markeres stedvist (fx i metode- eller forbeholdsafsnit), men ikke dér, hvor de
  omstridte vurderinger faktisk fremsættes.
- 4: Ved hver omstridt vurdering er tekstens position og evt. egeninteresse deklareret i eller
  nær passagen; læseren kan altid se, hvem der taler, og hvad talerens interesse er.

**D2 Definitionsmagt**
- 0: Tekstens bærende kategorier ("kvalitet", "redelighed", "parathed" el.lign.) behandles som
  givne; hvem der har defineret dem, tematiseres ikke.
- 2: Enkelte kategoriers ophav angives; andre centrale kategorier står umarkerede.
- 4: Teksten angiver, hvem der definerer de bærende kategorier, og markerer, hvor definitionsmagten
  er omstridt eller ligger hos teksten selv.

**D3 Stemme og fravær**
- 0: Parter, der berøres af tekstens argument, optræder hverken med stemme eller som markeret fravær.
- 2: De vigtigste parter er repræsenteret eller nævnt, men mindst én berørt part er fraværende
  uden markering.
- 4: Berørte parter er repræsenteret, ELLER deres fravær er eksplicit markeret med begrundelse
  ("X's perspektiv indgår ikke, fordi …").

**D4 Framing af omstridte forhold** *(udvidelse af M4 ud over metaforer)*
- 0: Værdiladede ordvalg (ikke kun metaforer) framer omstridte forhold uden markering, og teksten
  veksler ikke perspektiv.
- 2: Framingen er rimelig for genren, men ureflekteret; enkelte umarkerede ladede valg.
- 4: Ved omstridte forhold viser teksten framing-bevidsthed: vælger, markerer eller modbalancerer
  sine ordvalg, evt. med eksplicit perspektivskifte.

## Rapportering (flag-tilstand, default)

Pr. kriterium: 1–3 ordrette belæg med sted, én analyse (hvad er markeret/umarkeret), og et
eventuelt flag formuleret som *observation + spørgsmål til forfatteren* — aldrig som anvisning
af holdning. D-fund indgår i "Prioriterede flag" på lige fod, men mærkes [D] og tæller ikke i
scoren. I metodeboksen tilføjes: "Dimension D kørt i flag-tilstand (uscoret); D-kriterier har
svagere evidensforankring end S/T; konfidens-loft middel; positionsneutralitet påkrævet."
