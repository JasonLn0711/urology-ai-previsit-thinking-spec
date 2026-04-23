# V1 Phase 0 Priority Flow Selection

Date: 2026-04-23
Status: proposed default until 許醫師 confirms, replaces, or reorders it
Depends on: `V1_PHASE0_CLINICIAN_REVIEW_PROTOCOL.md`

## Purpose

Phase 0 should not ask reviewers to approve all 12 complaint categories at once.

The first review should choose a small set of complaint flows that can test the product pattern deeply:

- patient/family intake wording
- nurse missing-information repair
- physician summary order
- confirmation-only exam-prep reminders
- unsafe wording detection
- decision to continue, revise, narrow, pause, or send to governance review

## First-Principles Selection Rule

Choose flows that maximize decision value while minimizing safety and scope drift.

A good first flow should:

- represent a common urology outpatient problem
- test a distinct symptom domain rather than repeating the same logic
- map to 許醫師's QA / training materials or TUA guideline concepts
- be reviewable with synthetic data only
- expose wording that could accidentally sound like diagnosis, triage, treatment, or exam ordering
- produce clear feedback for the next artifact

## Proposed First Three

| Priority | Flow | Why first | What the reviewer must judge |
| ---: | --- | --- | --- |
| 1 | 頻尿或夜尿 | Tests storage/nocturia collection, diary-language boundaries, and symptom-score reminder wording. | Which history fields are useful, whether diary/IPSS language is feasible, and whether any wording implies diagnosis. |
| 2 | 小便困難或尿不出來 | Tests voiding/retention language, nurse repair boundaries, and PVR/uroflow/IPSS confirmation-only wording. | How to handle "cannot urinate" without triage claims, and which information belongs to nurse vs physician review. |
| 3 | 血尿或健檢發現潛血 | Tests hematuria wording, avoids cancer inference, and checks urine/blood/imaging reminder boundaries. | Whether visible blood, clots, and occult blood should be separated, and which words imply cancer risk or false reassurance. |

These are planning defaults, not clinical priority claims.

The shortlist becomes accepted only if 許醫師 explicitly confirms or revises it.

## Runnable Synthetic Support

Each proposed first-three flow now has a runnable synthetic case in the demo repo:

| Flow | Demo synthetic case |
| --- | --- |
| `頻尿或夜尿` | `synthetic-frequency-older-adult` |
| `小便困難或尿不出來` | `synthetic-emptying-difficulty` |
| `血尿或健檢發現潛血` | `synthetic-hematuria-occult-blood` |

The hematuria case is still synthetic-only and review-only. It is included to test wording and workflow fit, not to test diagnosis, cancer-risk scoring, reassurance, or exam ordering.

## Backup Substitution Order

| Substitute | Use when | Why |
| --- | --- | --- |
| 抽血發現 PSA 升高 | 許醫師 wants a prostate-focused first review. | High urology-specific value; must avoid cancer-risk inference. |
| 尿失禁 | Nurse/staff workflow and sensitive disclosure are the main questions. | Tests pad/continence wording, source labels, and embarrassment-sensitive intake. |
| 突發腰痛 | Clinic wants flank-pain readiness first. | Tests pain and imaging language; requires stricter triage-boundary review. |

## Review Questions Per Flow

For each selected flow, capture:

1. What should the patient/family be asked before physician entry?
2. What should nurse/staff repair or confirm?
3. What should appear first in the physician summary?
4. Which exam-prep reminders are acceptable before physician confirmation?
5. Which words sound like diagnosis, triage, treatment, or automatic exam ordering?
6. What must remain hidden until nurse/physician review?
7. Should the flow continue, revise, narrow, pause, or go to governance review?

## Decision Standard

Accept the first three only if:

- 許醫師 confirms or revises the shortlist
- at least one clinician can identify useful and unsafe lines per flow
- confirmation-only exam-prep wording is possible for each flow
- no flow requires real patient data, live HIS behavior, autonomous triage, treatment advice, or exam ordering
- the next artifact is smaller than "build all 12 flows"

If the review cannot choose three flows, narrow to one flow and repeat the review.

## Repository Update Rule

If 許醫師 changes the shortlist, update:

- this file
- `V1_PHASE0_EXECUTION_AND_ANALYSIS_PLAN.md`
- `../core/EVALUATION.md`
- demo repo `docs/research/v1-priority-flow-shortlist.md`
- demo repo `docs/research/v1-priority-flow-review-worksheet.md`
- planning repo v1 Phase 0 research plan

Do not change production scope from the shortlist alone.

## Stop Conditions

Stop and route to governance review if priority-flow discussion requires:

- real patient identifiers or real visit records
- HIS, EMR, EHR, registration, messaging, or live queue integration
- diagnosis, triage, treatment advice, risk/probability output, or autonomous exam ordering
- regulatory classification claims
- vendor/IP ownership commitments
- hospital pilot promises
