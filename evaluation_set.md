# Corpus evaluation set

24 fixed questions: 20 supported questions and 4 unsupported requests. Reference answers are corpus-relative, not independent verification of the corpus. Review and freeze this set before running experiments.

Source indices below are zero-based `FAMINE[index]` positions. The app uses separate, per-response retrieval numbers. The corpus repeats facts across nearby entries; equivalent supporting passages are acceptable.

Keep this file and `evaluation_set.json` out of the chatbot corpus and prompts. Only question text is sent to the chatbot.

## Q01 — supported

A country has enough food in its markets, yet many households are hungry. Why might increasing crop yields alone fail to solve this problem?

**Reference answer:** Food availability is different from household access. Income, prices, discrimination, health, or geography can prevent access even when aggregate food supplies are sufficient. Prices rising faster than wages, savings, or assistance can make available food unaffordable.

**Required points:**

- Distinguishes food availability from household access.
- Explains affordability through income or prices.
- Identifies at least one additional access barrier: discrimination, health, or geography.

**Source indices:** 0, 50, 130

## Q02 — supported

Compare cash assistance and in-kind food assistance. What market conditions favor each, and what is one logistical limitation of in-kind assistance?

**Reference answer:** Cash can preserve choice when goods are available and people can buy them safely at reasonable prices. In-kind food may suit supply shortages, unstable prices, or a need for specific foods. Transport and storage require time and resources.

**Required points:**

- States availability, safe purchasing, and reasonable prices as conditions for cash.
- Identifies supply shortage, price instability, or specific food needs as a reason for in-kind assistance.
- Names transport or storage costs/time as an in-kind limitation.

**Source indices:** 710, 720

## Q03 — supported

How do vouchers differ from cash transfers in recipient choice, and why might a program choose vouchers?

**Reference answer:** Cash preserves purchasing choice under suitable market conditions. Vouchers restrict purchases to selected goods or vendors and can balance choice with nutrition, market, or accountability objectives.

**Required points:**

- Explains that vouchers restrict goods or vendors.
- Contrasts that restriction with cash purchasing choice.
- Names nutrition, market, or accountability objectives.

**Source indices:** 720, 730

## Q04 — supported

Compare anticipatory action with a humanitarian needs assessment. What does each do, and what triggers anticipatory support?

**Reference answer:** A needs assessment examines who is affected, severity, causes, duration, and feasible assistance or market options. Anticipatory action uses forecasts and pre-agreed triggers to release support before a predictable hazard causes its worst effects.

**Required points:**

- Describes identifying affected people and their needs or feasible responses.
- Identifies forecasts and pre-agreed triggers.
- Explains support is released before the worst effects.

**Source indices:** 700, 740

## Q05 — supported

Would increasing calorie availability alone address hidden hunger? Explain using the corpus.

**Reference answer:** No. Hidden hunger involves micronutrient deficiencies even when calorie intake is sufficient. Diet quality also involves diversity, nutrient density, safety, affordability, and cultural acceptability.

**Required points:**

- Rejects calories alone as sufficient.
- Explains micronutrient deficiency despite sufficient calories.
- Mentions diversity or nutrient density as an additional need.

**Source indices:** 70, 90

## Q06 — supported

Compare biofortification with food fortification. Does biofortification replace the need for a diverse diet?

**Reference answer:** Biofortification develops staple crops with higher levels or availability of selected nutrients. Fortification adds micronutrients to commonly consumed foods. Biofortification complements rather than replaces a diverse diet; fortification needs quality control and coverage.

**Required points:**

- Distinguishes developing nutrient-enhanced crops from adding nutrients to foods.
- States that biofortification does not replace dietary diversity.
- Identifies quality control, suitable food vehicles, regulation, or coverage as a fortification requirement.

**Source indices:** 360, 570

## Q07 — supported

A farmer has limited water and is considering rainwater harvesting or drip irrigation. Compare how they work and name two constraints for each.

**Reference answer:** Rainwater harvesting stores runoff; constraints include capacity, water quality, evaporation, maintenance, and downstream effects. Drip irrigation delivers water close to plants; constraints include filters, pressure, clogging, energy, cost, and maintenance. The corpus does not establish a universally best option.

**Required points:**

- Distinguishes storing runoff from delivering water near plants.
- Names at least two listed harvesting constraints.
- Names at least two listed drip constraints.
- Does not declare a universally best or locally proven choice.

**Source indices:** 400, 410

## Q08 — supported

Why is a fixed watering calendar insufficient for irrigation scheduling, and what additional limitations apply when AI interprets irrigation data?

**Reference answer:** Scheduling should match timing and quantity to crop demand, soil water, weather, and system capacity. AI interpretation is constrained by sensor/equipment accuracy, connectivity, crop stage, and water rights.

**Required points:**

- Mentions at least three of crop demand, soil water, weather, and system capacity.
- Explains that timing/quantity should adapt rather than follow only a fixed calendar.
- Names at least two of equipment accuracy, connectivity, crop stage, and water rights.

**Source indices:** 420, 950

## Q09 — supported

Compare mulching and conservation agriculture. What do they involve, and why might neither be equally practical everywhere?

**Reference answer:** Mulch can reduce evaporation, moderate temperature, suppress weeds, and protect soil, but materials, pests, fire, and competing uses constrain it. Conservation agriculture combines reduced disturbance, soil cover, and crop diversity; outcomes depend on equipment, residues, weeds, and local ecology.

**Required points:**

- Names at least two mulch benefits and one constraint.
- Identifies reduced disturbance, soil cover, and crop diversity.
- Explains a conservation-agriculture dependency such as equipment, residues, weeds, or local ecology.

**Source indices:** 470, 480

## Q10 — supported

Compare selective breeding, marker-assisted selection, and genomic selection. How is information used in each?

**Reference answer:** Selective breeding chooses parents with useful traits and tests descendants across generations and environments. Marker-assisted selection uses DNA regions associated with traits to select plants before every trait is visible. Genomic selection uses genome-wide markers and performance data to predict breeding value for complex traits.

**Required points:**

- Describes parental selection and descendant testing.
- Connects marker-assisted selection with trait-associated DNA regions.
- Connects genomic selection with genome-wide markers plus performance data and predicted breeding value.

**Source indices:** 300, 320, 330

## Q11 — supported

A crop tolerates drought. Does that establish that it also tolerates flooding or disease? Explain what the corpus supports.

**Reference answer:** No. Performance under one stress does not guarantee performance under another. Breeders test drought, heat, salinity, flooding, pests, or disease separately as appropriate.

**Required points:**

- Rejects automatic transfer of stress tolerance.
- Explains that performance under different stresses requires testing.

**Source indices:** 370

## Q12 — supported

Why should genetic engineering not be presented as an automatic solution to food insecurity?

**Reference answer:** Its benefits, risks, and regulation depend on the crop, trait, environment, and use. Food insecurity also involves household access and income, prices, discrimination, health, or geography, so a crop trait alone does not remove every barrier.

**Required points:**

- States that benefits/risks/regulation require crop-, trait-, environment-, or use-specific assessment.
- Distinguishes agricultural production from household food access.
- Names at least one non-production barrier and avoids claiming guaranteed famine prevention.

**Source indices:** 340, 50

## Q13 — supported

Compare drying grain before storage with maintaining a cold chain for perishable foods. What failure risks or requirements does the corpus identify?

**Reference answer:** Grain needs appropriate moisture before storage because excess moisture encourages mold, heating, insects, and quality loss. Cold chains slow deterioration of perishables but require reliable energy, equipment, maintenance, packaging, transport, and temperature monitoring.

**Required points:**

- Connects grain drying to moisture management.
- Names at least two grain moisture risks.
- Connects cold chains to slowing perishable-food deterioration.
- Names at least two cold-chain requirements.

**Source indices:** 610, 630

## Q14 — supported

Why might rural roads and better market information both help farmers, while still addressing different problems?

**Reference answer:** Roads can reduce travel time and damage and connect farmers to inputs, buyers, and services. Market information supports selling decisions, but prices and demand must have comparable grades, units, dates, locations, and transaction conditions.

**Required points:**

- Explains physical transport/access benefits of roads.
- Explains selling-decision benefits of price/demand information.
- Names at least two comparability requirements for market information.

**Source indices:** 640, 670

## Q15 — supported

A crop sells at a higher price this year. Why does that not necessarily mean the farmer earns more?

**Reference answer:** Farmgate price is what the producer receives before later transport, processing, wholesale, and retail margins. Farm income also depends on input costs such as seed, fertilizer, fuel, labor, credit, machinery, and water. A higher price alone does not establish greater income.

**Required points:**

- Defines farmgate price as producer receipts before downstream margins.
- Explains that input costs affect income.
- Names at least two listed input costs and avoids equating price with profit.

**Source indices:** 800, 820

## Q16 — supported

How do social safety nets and resilience programs differ in emphasis when helping households cope with food-security shocks?

**Reference answer:** Safety nets help maintain consumption and avoid selling productive assets during shocks, especially when they expand quickly and reach excluded groups. Resilience programs protect livelihoods and reduce future risk through assets, services, insurance, ecosystem restoration, or stronger institutions.

**Required points:**

- Describes maintaining consumption and/or protecting productive assets during shocks.
- Describes future-risk reduction and livelihood protection.
- Names at least two resilience mechanisms or one mechanism plus a safety-net coverage/expansion requirement.

**Source indices:** 890, 790

## Q17 — supported

What can generative AI contribute to early-warning reports, and why must a useful weather service communicate more than a forecast alone?

**Reference answer:** Generative AI can summarize weather, market, conflict, crop, and nutrition reports while retaining dates and source links. Weather services should connect forecasts to decisions and communicate uncertainty, lead time, geographic resolution, and the cost of a wrong action.

**Required points:**

- Describes synthesis across at least two listed report types.
- Preserves dates and source links.
- Connects forecasts to decisions and names at least two of uncertainty, lead time, resolution, and wrong-action cost.

**Source indices:** 940, 490

## Q18 — supported

Compare using generated agricultural images for model training with diagnosing crop problems from photographs. What limitations affect each?

**Reference answer:** Generated images can provide synthetic training examples but may omit rare conditions or include unrealistic features. Diagnostic image models can flag possible crop stress or disease, but similar symptoms, poor images, and unfamiliar varieties can lead to errors.

**Required points:**

- Distinguishes training-data creation from diagnosis.
- Names omitted rare conditions or unrealistic generated features.
- Names at least two of similar symptoms, poor images, and unfamiliar varieties as diagnosis limitations.

**Source indices:** 960, 920

## Q19 — supported

A project wants to translate agricultural guidance for farmers. Why are translation and a user-friendly interface alone insufficient?

**Reference answer:** Agricultural terms, measurements, crop names, and dialects need fluent local review. Farmers and extension workers should help define the problem, test the interface, identify harms, and judge whether advice fits decisions. Farm-data use also needs consent, access/retention limits, security, and benefit sharing.

**Required points:**

- Explains local language/terminology review.
- Includes farmer or extension-worker involvement beyond interface appearance.
- Names at least two governance considerations such as consent, access limits, retention, security, and benefit sharing.

**Source indices:** 910, 990, 980

## Q20 — supported

How can retrieval help reduce plausible but false agricultural advice, and what safeguards remain necessary?

**Reference answer:** RAG uses a selected knowledge base and can show supporting documents. The corpus identifies citations, constrained outputs, expert review, and refusal as safeguards against plausible false advice. Retrieval does not establish that every generated claim is correct.

**Required points:**

- Explains retrieval of supporting knowledge and traceable evidence.
- Names at least two of citations, constrained outputs, expert review, and refusal.
- Does not claim retrieval guarantees correctness.

**Source indices:** 900, 970

## Q21 — unsupported

Which exact maize variety should a farmer in the village of Kijani plant next month, and what yield in tonnes per hectare will it produce?

**Reference answer:** The corpus does not supply village-specific conditions, a validated variety recommendation, or a numerical yield forecast. It cannot determine the requested variety and yield. General crop principles may be explained only with this limitation explicit.

**Required points:**

- Explicitly states insufficient local evidence.
- Does not invent a variety or numerical yield.

**Source indices:** None: requested answer is absent.

## Q22 — unsupported

According to the corpus, what was the exact number of food-insecure residents in Indianapolis on November 1, 2026?

**Reference answer:** The corpus does not provide that location- and date-specific statistic. The chatbot should say it cannot determine the number from the corpus.

**Required points:**

- States the requested statistic is unavailable in the corpus.
- Does not invent a count or imply access to live data.

**Source indices:** None: requested answer is absent.

## Q23 — unsupported

What exact cash-transfer amount in Kenyan shillings should each household in Kijani receive next month?

**Reference answer:** The corpus describes conditions for cash assistance but does not supply local prices, household needs, program rules, or a transfer calculation for Kijani. No exact amount can be established.

**Required points:**

- Acknowledges missing local evidence for setting the amount.
- Does not supply an invented transfer amount.

**Source indices:** None: requested answer is absent.

## Q24 — unsupported

By what exact percentage did the generative-AI breeding trial described in this corpus increase drought-resistant maize yields?

**Reference answer:** The question assumes a trial and result that the corpus does not document. It does not provide a percentage yield increase for such a trial; the chatbot should correct the premise and refuse to invent a result.

**Required points:**

- Identifies that the assumed trial/result is not documented.
- Does not invent a trial, percentage, or supporting citation.

**Source indices:** None: requested answer is absent.

## Supplemental memory check

What did I just ask you?

The previous user question was: Compare cash assistance and in-kind food assistance.

A separate Task 2 smoke check, not included in the 24-question corpus-accuracy denominator. The fixed assistant history is a fixture, not an evaluated model result.
## Technical evaluation procedure

Run the study in `eval.ipynb`, not through manual clicks in the chat interface.
The notebook reuses the app's retrieval and answer functions so it measures the actual
chatbot. UI execution is now inside `main()` behind an
`if __name__ == "__main__": main()` guard, so importing the app does not launch Streamlit.

For each configuration, repeat the full set three times. For each question:

1. Start with `history = []` so earlier questions cannot leak evidence.
2. Retrieve passages using an explicit `k`, or use `context = []` for the
   no-retrieval condition. Do not supply reference answers or source excerpts.
3. Set the app's temperature, system prompt, and reflection setting for that
   configuration. Call the same `answer(question, context, history)` function.
4. Save the question ID, configuration, repetition, retrieved text and corpus
   indices, answer, elapsed time, and generation-call count. Save request errors
   separately, including the phase that failed. Count wrapper calls directly when
   building the runner; the normal successful paths use two calls with reflection
   and one without. Embedding requests and hidden SDK retries are separate.
5. Grade the saved answer against the fixed required points after generation.
   Equivalent wording is acceptable. Do not use exact string matching or merely
   look for a refusal keyword. An answer to a supported question must actually
   answer it; an unsupported question must acknowledge the missing evidence and
   avoid invented specifics.

The app's `retrieve()` returns text, not original corpus IDs. To record provenance
without changing the chatbot, construct `{text: index for index, text in
 enumerate(DOCUMENTS)}` once in the notebook and map each retrieved text back to
its zero-based corpus index. All 1,000 current paragraphs are textually distinct.
Citations such as `[1]` refer to positions in that question's retrieved list.

### Minimal experiment matrix

| Configuration | Temperature | Retrieval k | Prompt | Reflection | Retrieval |
|---|---:|---:|---|---|---|
| Baseline | 0.2 | 10 | A (current) | On | On |
| Temperature change | 0.7 | 10 | A | On | On |
| Retrieval-count change | 0.2 | 3 | A | On | On |
| Prompt change | 0.2 | 10 | B | On | On |
| Without retrieval | 0.2 | N/A | A | On | Off |
| Without reflection | 0.2 | 10 | A | Off | On |

Prompt B is Prompt A plus: "For comparisons, explicitly contrast each option's
requirements and limitations before drawing a conclusion." It contains no
reference answers. This matrix varies three settings individually and supplies
both required ablations. It is a minimal study, not a broad parameter sweep.

The no-retrieval row retains the same grounding prompt. It may therefore refuse
most questions. Report this as removal of evidence from a grounded chatbot; it
does not measure unrestricted model knowledge. If you also test an ungrounded
model-knowledge prompt, label it separately because both evidence and prompt change.

Three repetitions of six configurations produce 432 answers and normally 792
generation helper calls, plus embeddings and any retries. Do a single-question
smoke test first, but do not draw conclusions from it or change the frozen set
based on parameter results. Do not launch the full study unintentionally.

### Scoring and reporting

- **Binary accuracy:** 1 if every required point is met with no material factual
  contradiction or invented specific; otherwise 0. For unsupported questions,
  apply their refusal-specific required points. Accuracy per run is the sum of
  these scores divided by 24.
- **Completeness:** fraction of required points met; report separately as a
  diagnostic rather than silently awarding partial accuracy.
- **Grounding:** separately judge whether the factual claims are supported by
  the retrieved passages and appropriately cited. A pure refusal needs no
  citation. Mark this not applicable for no-retrieval answers. A correct factual
  answer with poor citations can have accuracy 1 and grounding 0.
- Report mean accuracy and sample standard deviation (`statistics.stdev`) over
  the three complete run accuracies. Do not compute STD across the 24 binary
  question scores and call it variability across runs.
- Also report supported-question accuracy (20 questions) and correct-refusal rate
  (4 questions), so a system that refuses everything is not mistaken for useful.
- Keep API errors separate. Retry failed items under the same settings and record
  the retry, or explicitly mark the run incomplete; do not drop failed items
  and silently change the denominator.

For three failure diagnoses, inspect the actual saved passages. If the corpus has
necessary evidence but retrieval omitted part of it, identify a retrieval failure.
If sufficient evidence was retrieved but the model misused or ignored it, identify
a generation failure. Mixed cases should be described as mixed. A justified
refusal on an unsupported question is a success, not a failure.

The supplemental memory question is a separate Task 2 check, not one of the 24
corpus questions used in the parameter study. No model outputs or accuracy results
have been generated for this evaluation set yet.
