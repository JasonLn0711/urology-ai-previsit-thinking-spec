# Decision Record: Deep-Cultivation Proposal Package v0.5

Status: synthesized

## Decision Identity

| Field | Notes |
| --- | --- |
| Decision record ID | DR-2026-05-29-001 |
| Date | 2026-05-29 |
| Source meeting | Prof. Wu 2026-05-29 follow-up |
| Related capture | `prof-wu-xinyi-proposal-meeting-capture.md` |
| Related reference analysis | `xinyi-outpatient-proposal-reference/README.md` |
| Supersedes for active drafting | v0.4 package as the current discussion base |

## Decision

Promote the urology deep-cultivation proposal package to v0.5 as a 2026-06-02 discussion draft.

The active drafting constraints are:

```text
三年期
總經費新臺幣 1,000 萬元整
每一項經費均需對應 KPI
整份討論版控制在 20 頁以內
```

## Rationale

The 2026-05-29 meeting clarified the parent-proposal operating constraint. The previous v0.4 package already had the correct governance posture and official-format discipline, but it still kept the budget ceiling pending. v0.5 turns the budget and page limit into active drafting controls.

## What v0.5 Adds

- A fixed NT$10,000,000 three-year working budget.
- Page-budget discipline for a 20-page discussion version.
- A budget allocation table that maps every budget bucket to KPI, evidence, owner, and checkpoint.
- A second precedent analysis from the attached subproject-three reference PDF.
- A 2026-06-02 readiness checklist.

## What v0.5 Preserves

- Urology previsit / clinician-review summary as the current system role.
- Non-acute LUTS / OAB-like outpatient scope as the safest first slice.
- Clinical-friction reduction as the Health Taiwan value claim.
- Source-labeled, missing-field-visible, clinician-reviewed output.
- No diagnosis, treatment advice, autonomous triage, queue priority, or automatic EMR writeback.
- No real patient data without separate IRB/QI, privacy, data, cybersecurity, procurement, and hospital-governance approval.

## Reference Proposal Learning

Adopt these patterns from the attached subproject-three PDF:

- clear cover identity
- three-year total budget visible from page one
- section order from problem to technology, implementation, organization, governance, KPI, and budget
- year-by-year milestones
- role-based organization table
- KPI and budget tables with numerical targets

Modify or reject these patterns:

- over-broad clinical claims
- direct HIS and FHIR integration as an early promise
- automatic red/yellow/green clinical routing language
- forced appointment or urgent routing wording
- page-number and section-number inconsistencies
- generated math/text artifacts
- budget items without enough KPI or owner clarity

## Immediate Next Actions

| Action | Done definition |
| --- | --- |
| Create v0.5 proposal draft | `discovery/DEEP_CULTIVATION_APPLICATION_DRAFT_V0_5.md` exists and states budget/page/KPI constraints. |
| Update KPI budget files | Current package points to v0.5 and includes NT$10,000,000 allocation. |
| Update annual checkpoints | The 115/116/117/118 checkpoint logic reflects 2026-06-02 discussion readiness and three-year execution. |
| Update README / NEXT_STEP | The repo index points to v0.5 and the 2026-05-29 records. |
| Mirror planning status | Planning project tracker and day note point to the canonical urology files. |

## 2026-06-02 Discussion Questions

- Does the parent proposal want this as a standalone subproject, a work package inside the outpatient-department proposal, or an appendix?
- Are the three-year annual allocations acceptable: 4.0M, 3.2M, 2.8M, or should the parent budget owner require a different profile?
- Which budget categories must be hospital personnel, outsourcing, equipment, security/governance, training, or administrative expense?
- Who owns clinical, outpatient workflow, IT/security, AI/data governance, evaluation, procurement, and proposal coordination?
- Is ASR a funded KPI-backed module or only a demo capability?
- Is CRM reopened as a funded phase, or kept as future readiness language?
- Is real patient-data evaluation intended in year two or three, and under which IRB/QI route?

## Review Boundary

v0.5 is proposal-prep material. It is not a signed institutional application, procurement specification, IRB protocol, clinical deployment plan, or production integration approval.
