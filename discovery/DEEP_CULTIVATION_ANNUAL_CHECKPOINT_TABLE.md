# Deep-Cultivation Annual Checkpoint Table

Status: proposal-prep checkpoint table

Date: 2026-05-29

Current proposal package: `DEEP_CULTIVATION_APPLICATION_DRAFT_V0_5.md`

Purpose: convert the proposal into annual checkpoints that can be monitored, reported, and tied to KPI and budget.

## Timeframe Caveat

Official public pages checked on 2026-05-20 indicate:

```text
First stage: from approved-plan date in 114 to the end of 115
Second stage: 116-118
Second-stage new solicitation: expected in 115 Q4
```

This table must be aligned with the parent proposal's actual application route.

## Checkpoint Logic

Each checkpoint should answer:

1. What artifact exists?
2. Which KPI does it support?
3. Who owns it?
4. What evidence proves completion?
5. Does it reduce clinical friction without crossing safety boundaries?

## 115 Q2-Q4: Proposal Preparation And Evidence Package

Use if the team is preparing for hospital-facing draft, continuation planning, or second-stage readiness.

| Checkpoint | Deliverable | KPI / gate | Evidence | Owner needed |
| --- | --- | --- | --- | --- |
| Applicant route clarified | applicant / mode / parent proposal relationship note | formal submission route | one-page owner note | parent proposal owner |
| Intended use frozen | intended use and non-use statement | boundary clarity | `INTENDED_USE_FREEZE.md` | clinical + proposal owner |
| Demo scope frozen | included/excluded demo scope | scope control | `DEMO_SCOPE_FREEZE.md` | proposal + engineering owner |
| Synthetic cases selected | 3-5 cases | review readiness | case list | clinician reviewer |
| Clinician summary sample | one-page summary mock | read-time KPI | sample output | engineer + clinician |
| Clinical friction plan | friction budget and measurement plan | workforce burden reduction | `CLINICAL_FRICTION_REDUCTION_ANALYSIS.md` | workflow owner |
| Governance checklist drafted | AI/data/cybersecurity checklist | Scope 3 readiness | `DEEP_CULTIVATION_GOVERNANCE_CHECKLIST.md` | governance owners |
| KPI-to-budget draft | KPI table with budget logic | budget traceability | `DEEP_CULTIVATION_KPI_TO_BUDGET_TABLE.md` | budget owner |
| Proposal draft v0.5 | 2026-06-02 discussion draft with budget and page controls | application readiness | `DEEP_CULTIVATION_APPLICATION_DRAFT_V0_5.md` | proposal writer |
| Owner table prepared | clinical, workflow, IT/security, AI/data governance, evaluation, budget and coordination roles visible | responsibility clarity | v0.5 owner and responsibility table | parent proposal owner |
| Review-response table prepared | likely reviewer questions and response direction drafted | external review readiness | v0.5 review-response table | proposal writer |
| v0.4 precedent baseline preserved | prior official-package discipline remains available as context | traceability | `DEEP_CULTIVATION_APPLICATION_DRAFT_V0_4.md` | proposal writer |
| Reference proposal analyzed | subproject-three reference PDF copied and analyzed | precedent use without scope drift | `../records/2026-05-29/xinyi-outpatient-proposal-reference/README.md` | proposal writer |

## 116: Governed Design And Pilot Preparation

Use as first full execution-year shape if the subproject becomes part of the 116-118 stage.

| Checkpoint | Deliverable | KPI / gate | Evidence | Owner needed |
| --- | --- | --- | --- | --- |
| Workflow slot confirmed | registration / waiting-room / review flow confirmed | adoption feasibility | workflow map and meeting record | clinic workflow owner |
| Question bank approved | first-version question set | clinical appropriateness | clinician-signed or recorded review | urology lead |
| Summary schema v1 | one-page summary and source labels | read-time and source-label KPI | summary template | engineer + clinician |
| Safety wording test | unsafe wording count = 0 in test set | safety boundary | safety test report | clinical + governance reviewer |
| Synthetic walkthrough completed | 5-10 synthetic cases | demo evidence | walkthrough report | engineer |
| Staff burden review | nurse/staff review | burden acceptability | scorecard / meeting note | nursing/outpatient reviewer |
| Governance owner assignment | AI/security/data owners named | governance readiness | owner table | hospital administration |
| IRB/QI determination route | research vs QI/service decision pathway | real-data readiness | governance note | IRB/governance support |
| Budget finalization | budget maps to KPI | budget traceability | budget table | budget owner |

## 117: Limited Workflow Evaluation If Approved

Use only if governance approval and hospital ownership exist.

| Checkpoint | Deliverable | KPI / gate | Evidence | Owner needed |
| --- | --- | --- | --- | --- |
| Pilot protocol approved | governed pilot or QI workflow | legal/ethical gate | approved document | hospital owner |
| Access and data controls active | role-based access, retention, deletion | data/security readiness | security review record | IT/security owner |
| Baseline workflow captured | current repeated-question / burden baseline | comparison readiness | baseline report | evaluator |
| Limited workflow test | approved non-acute outpatient workflow | completion and burden KPI | pilot log or walkthrough log | clinic owner |
| Clinician review measured | read time, usefulness, edit/reject status | summary usefulness | scorecard / audit log | clinician reviewer |
| Nurse burden measured | staff intervention time and burden | friction budget | staff log / scorecard | nursing reviewer |
| Safety monitoring completed | unsafe wording, confusion, incidents | safety KPI | safety monitoring report | governance owner |
| Revise/narrow/continue decision | written decision | stage gate | decision record | PI / proposal owner |

## 118: Scale-Up Or Integration-Readiness Decision

Use only if earlier evidence supports continuation.

| Checkpoint | Deliverable | KPI / gate | Evidence | Owner needed |
| --- | --- | --- | --- | --- |
| Evidence review | workflow value and burden reduction reviewed | continuation decision | evaluation report | PI + hospital owner |
| Scope expansion decision | same department expansion or cross-department readiness | no scope drift | decision record | governance committee |
| CRM decision | reopen or keep parked | service continuity | SOP and owner decision | service owner |
| Interoperability decision | FHIR / TW Core IG mapping if needed | integration readiness | mapping note | IT/data owner |
| Procurement decision | internal / outsourced / hybrid path | sustainability | procurement plan | admin/procurement |
| Maintenance plan | post-project owner and update cycle | sustainability | operations plan | hospital owner |
| Final safety/governance review | no unresolved responsibility gap | closeout readiness | governance report | AI/data/security owners |

## Annual KPI Summary

| Year / stage | Primary KPI focus | Must not claim |
| --- | --- | --- |
| 115 prep | boundary, evidence package, proposal format, governance preflight, owner table, review-response readiness | clinical effectiveness |
| 116 design | workflow fit, synthetic review, staff burden, summary readability | real-world outcome improvement |
| 117 limited evaluation | approved workflow value, friction reduction, safety monitoring | broad scalability before evidence |
| 118 scale readiness | sustainability, integration readiness, maintenance ownership | production integration without governance |

## Checkpoint Reporting Style

Use concrete wording:

```text
完成 5 件合成案例 walkthrough，所有輸出均保留來源標記，未出現診斷、治療、自動分流或 EMR 寫入語句。
```

Avoid vague wording:

```text
AI 系統已提升效率。
```

## Open Items

| Item | Needed before final proposal |
| --- | --- |
| actual application stage | parent proposal owner |
| official year labels | parent proposal owner |
| official accounting categories and annual split for NT$10,000,000 working ceiling | hospital admin / parent budget owner |
| target reviewer count | clinical owner |
| whether real pilot is allowed | IRB/governance owner |
| whether CRM/future interoperability is included | service + IT owner |
