# Extraction Notes: Paper, Patent, And Product

## Status

Status: synthesized

These notes separate research, patent, and product implications from the 2026-04-23 meeting, 許醫師 LINE follow-up QA file, and 2024 TUA guideline. They do not assert patentability, clinical effectiveness, regulatory status, or hospital adoption.

## Paper Extraction

## Candidate Paper Claim

A bounded clinician-review workflow may reduce repeated urology previsit information gathering by separating patient/family intake, nurse missing-information repair, and physician-owned interpretation.

Safer current version:

> A synthetic v1 product preview can test whether role-separated previsit intake and summary generation are understandable, clinically readable, and safe enough to justify a formal pilot-readiness review.

## Evidence Captured

| Evidence | Captured? | Notes |
| --- | --- | --- |
| Current workflow map | Partly | `陽明小幫手` waiting-room mode is clearer than registration-helper mode for v1. |
| Repeated-question examples | Partly | QA/rules file gives recurring histories, medication/allergy/surgery/chronic disease, symptom forms, and 12 complaint categories. |
| Clinician usefulness statement | Partly | Positive meeting signal, but no timed line-level review yet. |
| Safety objections | Yes | No diagnosis, treatment, triage, real identifiers, live HIS, autonomous orders, or regulatory certainty. |
| Summary format preference | Partly | Existing current-platform summary concept is useful, but v1 summary order still needs physician review. |
| Patient or staff constraints | Partly | Older-adult and assisted-use assumptions remain; nurse burden needs Phase 0 review. |

## Limitation Statement

This discovery record cannot claim clinical effectiveness, measured time savings, patient outcome improvement, safety, or adoption. It can only justify a synthetic clinician/nurse review and a future pilot-readiness discussion if Phase 0 passes.

## Patent Reasoning Extraction

## Candidate System Logic

The system logic to investigate is the separation of:

1. patient/family symptom and history capture
2. answer-source labeling
3. missing-information repair
4. neutral physician-review summary
5. confirmation-only exam-prep context
6. mock export/API boundary for future HIS discussion

## Prior-Art And Rights Questions

| Question | Notes |
| --- | --- |
| Do existing intake forms already collect the same fields? | Needs prior-art and hospital form review. |
| Do existing systems separate red flags from urgency labels? | Needs vendor/current-platform comparison without copying restricted implementation. |
| Is missing-information repair ordinary form completion or a distinct workflow step? | Needs patent counsel / tech-transfer review. |
| Is assisted-use governance handled in existing systems? | Source-label design may matter, but do not assert novelty. |
| Is the one-minute clinician-review summary meaningfully different from ordinary intake notes? | Needs line-level review and comparison. |
| What has 許醫師 already filed or plans to file? | Must clarify before public disclosure or implementation claims. |
| Does 創智動能 have any vendor/IP/exclusivity constraint? | Must clarify before team-owned build promises. |

## What Not To Claim

Do not claim:

- the questionnaire itself is novel
- clinical diagnosis is automated
- triage is automated
- treatment is recommended
- exam ordering is automated
- real-world effectiveness is proven
- hospital adoption is proven
- TFDA/FDA status is settled
- the team is free to commercialize before IP/vendor/institution review

## Product Extraction

## Product Question

Would a real urology clinic adopt this because it saves time or improves readiness without adding unacceptable burden?

## Adoption Evidence

| Signal | Captured? | Notes |
| --- | --- | --- |
| Workflow slot exists | Partly | Waiting-room mode is plausible; operational owner still unknown. |
| Physician would read summary | Partly | Positive signal; line-level timed review still missing. |
| Staff burden acceptable | No | Needs nurse/staff Phase 0 review. |
| Patient or assisted completion realistic | No | Needs later usability study; Phase 0 can only test expert expectations. |
| Summary format useful | Partly | v1 exists; summary needs clinician scoring. |
| Safety boundary acceptable | Partly | Boundary is designed; reviewers must still check wording. |
| Funding path exists | No | Hospital innovation/deep-cultivation or company/hybrid funding remains open. |
| HIS path exists | No | Export/mock API only before information-office review. |

## Product Decision

Decision:

> Continue as safe-local v1 plus Phase 0 clinician/nurse review. Do not deploy.

Reason:

> The source materials justify a concrete synthetic review artifact, but unresolved nurse burden, IP/vendor, privacy/security, HIS, funding, and regulatory questions block real use.

## Smallest Next Artifact

| Field | Notes |
| --- | --- |
| Artifact | Phase 0 clinician/nurse review packet and scorecard |
| Why this artifact | It converts enthusiasm into measurable evidence without real patient data or production claims. |
| Reviewer | 許醫師, nurse/staff workflow reviewer, 吳老師 |
| Done definition | Filled scorecard, first three flows confirmed/revised, per-flow worksheet notes, unsafe/noisy wording list, and explicit continue/revise/narrow/pause/governance-review decision. |
| What not to include | Real data, HIS integration, vendor internals, diagnosis/treatment/triage/order claims, regulatory classification conclusions. |

Proposed first-three review scaffold: `頻尿或夜尿`, `小便困難或尿不出來`, and `血尿或健檢發現潛血`. Treat this as a planning default only until 許醫師 confirms, replaces, or reorders it.

The demo repo now has runnable synthetic support for the scaffold, including `synthetic-hematuria-occult-blood` for the hematuria / occult-blood flow.

The demo repo also now has a live Phase 0 capture sheet so review evidence is collected before analysis rather than reconstructed from memory.

The demo repo now has a pre-session readiness gate, `npm run phase0:check`. Latest run against `http://127.0.0.1:4176/app/v1/` passed `76/76`, so Phase 0 is ready to request reviewer time from an artifact/boundary/verification standpoint.
