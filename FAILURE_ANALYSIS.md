# Failure Analysis

## Purpose

Failure analysis exists to make risk visible before the system is mistaken for a clinical product.

## Patient-Level Failure Modes

| Failure | Cause | Signal | Response |
| --- | --- | --- | --- |
| Patient misunderstands question | jargon or unclear wording | inconsistent answer | simplify wording |
| Patient skips key information | fatigue or uncertainty | missing fields | prompt before summary |
| Older adult cannot use system | visual, motor, or phone difficulty | abandonment | nurse-assisted path |
| Language mismatch | Mandarin, Taiwanese, mixed language | wrong or vague answers | language preference field |
| Patient believes system gives advice | unsafe trust | patient asks what to do | strengthen safety copy |

## Clinician-Level Failure Modes

| Failure | Cause | Signal | Response |
| --- | --- | --- | --- |
| Summary too long | over-collection | clinician does not read | shorten output |
| Summary not useful | wrong information captured | clinician ignores it | revise question tree |
| Summary sounds diagnostic | unsafe wording | clinician distrust | neutralize language |
| Missing important field | incomplete question design | repeated follow-up needed | add only high-value fields |

## Workflow-Level Failure Modes

| Failure | Cause | Signal | Response |
| --- | --- | --- | --- |
| No place in clinic flow | operational mismatch | staff cannot identify when to use it | map workflow first |
| Adds staff burden | extra supervision required | nurse workload increases | use assisted mode only when needed |
| Duplicate documentation | summary not reusable | same information re-entered | clarify output destination |
| Privacy confusion | data flow unclear | stakeholders hesitate | keep MVP synthetic |

## Governance Failure Modes

- scope expands into diagnosis
- real patient data enters before approval
- integration is promised too early
- patient-facing claims overstate benefit
- red flags are framed as decisions
- summary is treated as clinically complete

## Failure Principle

A failed MVP is still useful if it identifies the wrong workflow, wrong output, or wrong boundary before costly implementation.
