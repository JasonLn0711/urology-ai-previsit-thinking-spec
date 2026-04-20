# Failure Analysis

## Purpose

Failure analysis exists to make risk visible before the concept is mistaken for a clinical product.

The goal is not to avoid all failure. The goal is to fail early, visibly, and safely if the workflow, summary, or boundary is wrong.

## Patient-Level Failure Modes

| Failure | Likely Cause | Signal | Response |
| --- | --- | --- | --- |
| Patient misunderstands a question | medical wording or unclear phrasing | inconsistent or uncertain answer | simplify wording and add review |
| Patient skips key information | fatigue, embarrassment, or uncertainty | missing fields | ask only high-value follow-up questions |
| Older adult cannot complete the flow | visual, motor, or phone-use difficulty | abandonment or staff takeover | strengthen assisted mode |
| Language mismatch | Mandarin, Taiwanese, mixed language, or unclear terms | vague answers | record language preference and simplify choices |
| Patient believes the system gives advice | role confusion | patient asks what to do medically | strengthen safety wording and clinician-review framing |

## Clinician-Level Failure Modes

| Failure | Likely Cause | Signal | Response |
| --- | --- | --- | --- |
| Summary too long | over-collection | clinician does not read it | shorten and group fields |
| Summary not useful | wrong information captured | clinician ignores it | revise question tree |
| Summary sounds diagnostic | unsafe wording | clinician distrust | rewrite as neutral observations |
| Important field missing | incomplete workflow understanding | repeated follow-up remains necessary | add only if high value |
| Output feels like extra work | poor fit with visit rhythm | staff or physician resistance | change workflow slot or pause |

## Workflow-Level Failure Modes

| Failure | Likely Cause | Signal | Response |
| --- | --- | --- | --- |
| No place in clinic flow | imagined workflow | staff cannot say when it would be used | map real workflow first |
| Staff burden increases | assistance need underestimated | nurses spend more time than saved | narrow use case or pause |
| Duplicate documentation | output has no practical destination | same information is re-entered | clarify whether summary is only discussion aid |
| Privacy confusion | unclear data boundary | stakeholders hesitate | keep discovery synthetic and document governance needs |
| Summary ignored | clinician does not trust or need it | no use during visit | treat as evidence and revise or stop |

## Governance Failure Modes

Governance fails if:

- scope expands into diagnosis
- real patient data enters before explicit approval
- automated urgency labels appear without review
- integration is promised before workflow value is proven
- patient-facing claims overstate benefit
- safety concerns are converted into feature requests too quickly
- the summary is treated as complete clinical truth

## Failure Signals That Should Stop Expansion

Pause expansion if:

- clinicians cannot identify useful previsit information
- patients repeatedly misunderstand core questions
- staff burden increases
- privacy questions cannot be answered
- the summary requires more than one minute to read
- safety wording repeatedly drifts into medical conclusions

## Failure Principle

A failed discovery version is still useful if it reveals the wrong workflow, wrong output, wrong user model, or wrong boundary before larger investment.
