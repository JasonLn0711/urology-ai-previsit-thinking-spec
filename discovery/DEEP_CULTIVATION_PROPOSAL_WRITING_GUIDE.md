# Deep-Cultivation Proposal Writing Guide

Status: working guide

## Purpose

This guide answers:

```text
深耕計畫的提案撰寫，需要寫什麼？
```

Use it when drafting the Health Taiwan deep-cultivation section for the urology previsit / visit-readiness system.

The proposal should not read like an AI model report. It should read like a healthcare workflow-improvement plan that uses AI, optional ASR, APP/tablet intake, and governance to reduce real clinical burden while preserving clinician authority. CRM follow-up is a parked future phase, not the first-version claim.

2026-05-19 expert-review update:

```text
Revise + Narrow.
```

For the first proposal-facing version, use:

```text
泌尿科門診前問診與醫師覆核摘要支持系統
```

Safe descriptive boundary:

```text
泌尿科門診前症狀蒐集與醫師覆核摘要輔助流程
```

Do not write this as an `AI medical system`. Park CRM follow-up until a future confirmed next step. Keep ASR as an optional multilingual input layer. Narrow the first version to non-acute LUTS / OAB-like outpatients: nocturia, frequency, urgency, leakage, voiding difficulty, or weak stream. Blood in urine, fever/chills, flank pain, and currently being unable to urinate are patient-reported red-flag observations, not first-version main pathways or triage judgments.

## Core Proposal Logic

The proposal must answer one practical question:

```text
Can this system truly improve a healthcare workflow in a hospital or community-care setting?
```

It should not primarily answer:

```text
Which AI model is newest?
```

For this repo, the correct story is:

```text
stable urology outpatient
-> after-registration or waiting-room QR code / tablet symptom collection
-> missing-field visibility
-> patient-reported red-flag observation display
-> one-page clinician-review outpatient summary
-> measured workflow and summary usefulness review
```

The broad system identity remains:

```text
urology previsit intake / visit-readiness / clinician-reviewed summary / future governed CRM follow-up support
```

But the first-version proposal label should be:

```text
泌尿科門診前問診與醫師覆核摘要支持系統
```

not:

```text
AI triage / autonomous risk scoring / AI diagnosis / direct EMR writeback
```

## Recommended Proposal Structure

| Section | What It Must Prove | What To Write For This Project |
| --- | --- | --- |
| 1. Policy and clinical background | The problem matters under Health Taiwan priorities | Lead with `導入智慧科技醫療`; use `優化醫療工作條件` as secondary workflow-burden support |
| 2. Clinical pain point | The current workflow has a real operational problem | Repeated urology history-taking, incomplete previsit context, and lack of a short clinician-readable intake summary |
| 3. Project objective | The project has a concrete service goal | Build a governed urology previsit intake and clinician-reviewed summary support workflow |
| 4. Service workflow | The system fits a real hospital process | Map registration, waiting-room QR/tablet intake, source-labeled answers, missing-field review, clinician summary, and physician review |
| 5. System design | The system components are understandable | Patient/family input, optional multilingual ASR, governed question engine, missing-information repair, red-flag observation display, summary draft, audit log |
| 6. AI / technical method | Technology supports the workflow | ASR, LLM-assisted summarization, governed question selection, structured summary generation, audit/version tracking |
| 7. Data and governance | Patient data, security, and responsibility are controlled | IRB, consent, privacy, de-identification, access control, logging, human-in-the-loop, security review |
| 8. KPI and evaluation | Outcomes are measurable | Synthetic flow completion, read time, missing fields, unsafe wording count, source labels, ASR confirmation, clinician usefulness, staff burden |
| 9. Implementation plan | The work is staged and executable | Year 1 design/walkthrough, Year 2 governed pilot preparation, Year 3 scale-up readiness |
| 10. Team and training | People can execute and govern it | PI/co-PI roles, hospital stakeholders, 吳老師團隊, student/engineer roles, IRB training |
| 11. Budget and procurement | Money maps to KPI | Personnel, APP/tablet intake work, ASR/cloud or server if used, security review, governance support, vendor/procurement assumptions |
| 12. Expected outcomes | The hospital receives durable value | Evaluated reduction of repeated work, better visit readiness, and governance-ready smart-healthcare workflow |
| 13. Risk and boundary | The proposal does not overclaim | No diagnosis, treatment advice, autonomous triage, production deployment, or real patient-data use without governance |

## Storyline To Use

Start from the clinic, not the model.

Recommended storyline:

1. Non-acute urology outpatient workflows repeatedly ask the same LUTS / OAB-like symptom questions.
2. A guided previsit workflow can collect repeated, previsit-safe information during the waiting-room window.
3. The system can show missing fields and patient-reported red-flag observations without making triage or diagnosis claims.
4. AI and ASR can reduce input and summary-preparation burden, but all output stays clinician-reviewed.
5. Governance, KPI, and budget mapping make the project executable rather than a demo.
6. CRM/reminder support remains a future governed phase, not the first-version scope.

Do not lead with:

- LLM novelty
- model benchmark scores
- broad AI transformation slogans
- autonomous triage
- direct hospital-system integration claims

## Proposal-Safe System Architecture

```mermaid
flowchart TD
    A[Non-acute scheduled urology outpatient] --> B[Registration completed]
    B --> C[Waiting-room QR code or tablet intake]
    C --> D[Patient / family structured answers]
    D --> E[Optional multilingual ASR, confirmed before use]
    E --> F[Governed LUTS / OAB-like question set]
    F --> G[Missing fields and red-flag observations]
    G --> H[Nursing review only when needed]
    H --> I[One-page clinician-review summary]
    I --> J[Physician confirms, edits, ignores, or rejects]
```

This diagram is intentionally not an AI triage diagram. It does not include queue prioritization, autonomous urgency labels, or direct EMR writeback.

## Technical Section Guidance

The technical method should be written after the workflow section.

Use this order:

1. Patient-facing guided intake
2. Optional multilingual ASR as an input layer
3. Governed urology question bank
4. Dynamic question selection within approved boundaries
5. Missing-information detection
6. Structured clinician-review summary
7. SOAP-structured reference summary, only for clinician review
8. Patient-reported red-flag observation display
9. Audit logging and version tracking
10. Future interoperability readiness, if governance permits
11. Future CRM follow-up readiness only if the parked phase is reopened

Allowed technical wording:

- `clinician-review summary`
- `SOAP-structured clinician-review reference summary`
- `human-in-the-loop`
- `governed question selection`
- `future FHIR/TW Core IG readiness`
- `future governed CRM follow-up readiness`
- `auditability and traceability`

Avoid technical wording:

- `AI doctor`
- `AI triage`
- `risk score`
- `automatic diagnosis`
- `automatic treatment recommendation`
- `direct HIS/EMR integration in the current demo`
- `clinical effectiveness proven`

## Clinical Workflow Integration

The proposal must show how the system enters the real workflow.

Write the before/after clearly:

| Current workflow problem | Proposed workflow change |
| --- | --- |
| Patient symptoms are collected late or repeatedly | Collect repeated, previsit-safe information before clinician-led interpretation |
| Physicians spend time reconstructing basic history | Provide a short clinician-review summary |
| Missing context appears during the visit | Surface missing information before handoff |
| Red-flag patient reports can be mistaken for AI triage if worded poorly | Display them only as patient-reported observations for human review |
| AI demo value is unclear | Tie AI to measurable workflow burden reduction |

The proposal should explicitly name who acts at each step:

- patient or helper completes intake
- nurse or staff handles only missing, conflicting, or red-flag-observation cases when needed
- clinician reviews and owns interpretation
- CRM owner or service SOP handles follow-up only if a future governed phase is reopened

## KPI And Evaluation Design

Use measurable KPI. Avoid generic phrases like `提升效率` without a metric.

Candidate KPI:

| KPI Category | Candidate Indicator | Why It Matters |
| --- | --- | --- |
| Visit readiness | Clinician can review summary in under one minute | Prevents long-transcript burden |
| Repeated work | Repeated history questions reduced in walkthrough or pilot | Tests actual workflow value |
| Missing information | Missing key previsit fields reduced after repair prompts | Tests readiness improvement |
| Completion feasibility | Patient/helper/staff-assisted completion rate reaches agreed target | Tests adoption reality |
| Clinician usefulness | Clinician usefulness rating reaches agreed threshold | Tests whether physicians would read it |
| Staff burden | Nurse/staff burden remains acceptable | Prevents hidden workload transfer |
| ASR confirmation | ASR-derived text or structured answer is confirmed before entering summary | Prevents speech errors becoming fact |
| Unsafe wording | Diagnosis, treatment, triage, exam-order, and EMR-writeback terms remain absent | Preserves clinical boundary |
| Future CRM continuity | Return-visit, lab-draw, or follow-up SOP is defined only if future phase is reopened | Keeps parked scope clear |
| Governance | IRB/privacy/security/procurement gates have owners | Tests execution readiness |
| Safety boundary | Zero diagnosis, treatment, or autonomous triage claims | Preserves clinical responsibility |
| Auditability | Output source and review status are traceable | Supports responsible AI |

Each KPI should have:

- baseline or current-process assumption
- target or draft target
- measurement method
- owner
- matching budget line, if money is requested

## Budget Logic

The budget must follow the KPI.

Write the logic as:

```text
Because the project must achieve KPI X,
we need work package Y,
therefore the budget includes Z.
```

Examples:

| If The Proposal Claims | Then Budget May Include | Required Justification |
| --- | --- | --- |
| guided previsit completion | APP / web intake work, usability review | completion KPI and patient/helper workflow |
| reduced summary burden | ASR or summary-generation work | review-time and clinician-usefulness KPI |
| future CRM follow-up continuity | CRM platform/customization or vendor work | only if the parked phase is reopened with reminder/follow-up KPI and SOP owner |
| governed pilot readiness | security review, audit logging, RA/coordinator | IRB/privacy/security/procurement gates |
| cross-domain training | training time or student/RA support | talent-training plan and role definition |

Do not include a budget line only because it is technically interesting.

## Governance Section Checklist

The governance section should include:

- IRB training and approval path
- patient-data boundary
- consent model before real patient data
- data retention and deletion rules
- role-based access control
- audit logging
- model / prompt / rule versioning
- clinician review and override
- error reporting
- security-governance review for APP, API, ASR, future CRM, or platform work
- procurement review for outsourced work
- MOU or written collaboration record for cross-unit partners

The proposal should say that discovery and demo materials use synthetic or non-real data unless a separate governance decision approves otherwise.

## Three-Year Writing Frame

## Year 1: Design, Governance, And Workflow Validation

Write:

- finalize after-registration / waiting-room workflow for non-acute urology visit-readiness
- define governed urology question bank
- build or refine clinician-review summary format
- run synthetic walkthrough and stakeholder review
- define red-flag observation wording and manual-review boundary
- keep CRM follow-up parked unless hospital stakeholders explicitly reopen it
- list IRB, privacy, security, MOU, and procurement gates
- collect clinician/staff feedback on readability and burden

## Year 2: Governed Pilot Preparation And Optional Future CRM Specification

Write:

- refine patient/helper/staff-assisted workflow
- prepare audit log and review-status requirements
- define CRM reminder, lab-draw, return-visit, or case-management prototype only if the parked phase is reopened
- decide internal, outsourced, or hybrid ownership
- complete required governance before any real patient-data workflow
- prepare interoperability-readiness mapping only if hospital stakeholders request it

## Year 3: Evidence-Based Scale-Up Readiness

Write:

- evaluate whether workflow burden and visit-readiness improved
- decide whether the system should extend beyond non-acute urology LUTS / OAB-like workflows
- decide whether CRM follow-up becomes a sustained service module
- prepare integration discussion only after evidence, governance, and ownership are clear
- keep diagnosis, treatment, and autonomous triage outside scope unless separately approved

## One-Page Proposal Skeleton

Use this as the first draft skeleton:

```text
Title:
泌尿科門診前問診與醫師覆核摘要支持系統

Problem:
Non-acute urology outpatient workflows repeatedly collect LUTS / OAB-like symptom history and often lack a short, source-labeled previsit summary before physician review.

Objective:
Build a governed urology previsit intake and clinician-reviewed summary support workflow that evaluates whether repeated information capture can be reduced while preserving clinician authority.

Workflow:
Registration -> waiting-room QR/tablet guided intake -> missing-information and red-flag observation display -> clinician-review summary -> physician confirms, edits, ignores, or rejects.

Technology:
Optional multilingual ASR, governed question selection, structured summary generation, audit/version logging, and future interoperability readiness.

Governance:
Human-in-the-loop, no diagnosis, no treatment advice, no autonomous triage, no automatic EMR writeback, no real patient-data workflow without IRB/privacy/security approval.

KPI:
Synthetic flow completion, review time, missing-field marking, unsafe wording count, source-label completeness, ASR confirmation, clinician usefulness, staff burden, auditability, and governance gates.

Budget:
Personnel, intake/APP/tablet work, optional ASR or summary module, security/governance, and vendor/procurement items only when tied to KPI. CRM/API readiness belongs only to a reopened future phase.

Expected impact:
Evaluated reduction of repeated work, improved visit readiness, responsible AI governance, and Health Taiwan smart-healthcare alignment.
```

## Common Failure Modes

Avoid these:

- writing the proposal as `LLM + RAG + ASR` before explaining clinical pain
- claiming hospital integration before governance and ownership exist
- promising AI triage when the current scope is previsit readiness
- adding vital-sign/kiosk/smart-pharmacy components without explaining the workflow slot
- listing KPI without data source, owner, or measurement method
- listing budget without a matching KPI
- treating Aging Clock as core before its data source, aging definition, intervention, and IRB path are defined
- citing external examples as if this project already has their validation status

## Minimum June 2 Draft Package

Before the June 2 follow-up, prepare:

1. One-page 子計畫二 narrative.
2. Workflow diagram.
3. Three-year milestone table.
4. KPI table with measurement method.
5. KPI-to-budget mapping.
6. Governance gate checklist.
7. Scope boundary paragraph.
8. Open decision list: exact workflow slot, first patient group, clinician summary length, red-flag observation handling, vendor/internal split, IRB timing, MOU partners, and whether optional CRM/kiosk/smart-pharmacy ideas remain parked.
