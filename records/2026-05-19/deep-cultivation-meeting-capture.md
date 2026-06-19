# Meeting Capture: 北市聯醫深耕計畫討論

Status: captured

2026-06-19 supersession note:

```text
This file preserves the 2026-05-19 meeting signal. CRM was later removed from
Jason / 陽明交大 current package by the 2026-06-19 owner update. Current work is
AI 問診、醫師覆核摘要、governance、KPI evidence, and NT$10,000,000 AI-only
budget mapping.
```

## Meeting Identity

| Field | Notes |
| --- | --- |
| Date | 2026-05-19 |
| Time | 上午，錄音約 10:42 開始 |
| Location | 北市聯醫 |
| Participants | 美如主任、吳老師、泌尿科團隊、陽明交大團隊、冠宇等 |
| Source transcript | `taipei-city-hospital-deep-cultivation-meeting-transcript.md` |
| Source archive | `sources/` |
| Primary question | How should the deep-cultivation proposal be structured so it is fundable, executable, and governed? |

## 1. Core Meeting Signal

The meeting did not validate a pure AI-model project. It pushed the project toward a practical healthcare service system:

- PSA and community screening can be the visible clinical entry point.
- SOP, return-to-hospital flow, case management, and CRM are the service backbone.
- APP, AI, ASR, kiosk, API, and reminders are useful only if they support the service flow.
- Aging Clock is a plausible research-adjacent direction, but it needs clearer data source, aging definition, biomarker scope, intervention logic, and service packaging before it belongs in the deep-cultivation plan.

## 2. Proposed Three-Subproject Structure

| Subproject | Main focus | Meeting interpretation |
| --- | --- | --- |
| 子計畫一 | PSA, community screening, SOP, follow-up, CRM | The most concrete service anchor. Screening must lead to a managed return and follow-up process, not end at the screening event. |
| 子計畫二 | Smart healthcare, APP, AI, CRM, API, patient management | The likely home for the urology previsit / adaptive-questioning / reminder-system work. AI should be framed as a workflow tool. |
| 子計畫三 | ESG, carbon accounting, new-site management | Policy and completeness layer, likely additive rather than the clinical mainline. |

## 3. Confirmed Planning Constraints

| Constraint | Capture |
| --- | --- |
| IRB training | Anyone entering the project to handle research, papers, human-subject content, or patient data needs IRB training, repeatedly described as nine hours. |
| MOU | Cross-unit cooperation should be documented through MOUs where relevant, including community, clinics, hospital units, university teams, and possibly government units. |
| Patient privacy | If PSA data, medical records, biomarkers, or other private patient information are collected, the research team must be governed through IRB and privacy controls. |
| KPI-budget linkage | Budget lines must map to written plan content and KPI. Money cannot appear without a corresponding project objective and KPI. |
| Procurement | CRM, APP, platform, questionnaire, API, or other outsourced work may trigger procurement / tender requirements. Exact threshold needs confirmation. |
| Security governance | APP, AI, CRM, API, platform, and patient-data flows require security-governance review and documentation. |

## 4. CRM And Service Workflow Signal

The strongest operational point in the meeting was that the hospital's immediate weakness is not necessarily model intelligence, but patient management.

Captured service idea:

```text
screening / intake -> reminder -> lab draw if needed -> visit reminder -> return visit -> case management -> CRM tracking -> clinician review
```

Potential features mentioned:

- visit reminders
- blood-draw reminders
- medication reminders
- LINE / APP notifications
- kiosk or front-end intake
- API connection between front end and CRM
- back-end patient follow-up and status tracking
- possible pharmacy / medication-packaging integration

Governance interpretation:

- CRM is now a central product and grant-writing concept.
- The previsit system should be positioned as a governed input and readiness layer inside CRM, not as a standalone chatbot.

## 5. Aging Clock Research Capture

冠宇 proposed an Aging Clock / Biological Age research direction.

Core idea:

- avoid relying only on expensive DNA methylation clocks
- build a Taiwanese / Asian-population biological-age model from more accessible biomarkers
- use baseline biomarkers, targeted intervention, and follow-up testing to observe whether biological age or aging speed improves

Candidate data and biomarkers:

- CBC / DBC
- general biochemistry
- kidney function
- liver function
- metabolism markers
- inflammation markers
- CRP
- oxidative stress
- ROS
- SOD
- MDA
- hormone-related markers
- functional or chronic-disease context where available

Open design issues raised by 美如主任:

- Is the data source National Health Insurance data, community cohort data, or data collected through the PSA/community workflow?
- What exactly is the definition of aging?
- How many biomarkers are required?
- What is the intervention?
- Is this a research project, or can it be packaged as a real service workflow?
- Should this be in the deep-cultivation proposal at this stage?

## 6. Decision Signals

| Signal | Evidence | Implication |
| --- | --- | --- |
| Continue service-flow thinking | PSA, CRM, SOP, reminders, and follow-up were repeatedly emphasized. | Keep developing the governed previsit / CRM-adjacent workflow. |
| Revise AI framing | AI was treated as a tool, not the proposal's core justification. | Do not lead with model novelty. Lead with service workflow and clinical operations. |
| Narrow Aging Clock claim |美如主任 treated it as research-like and under-defined. | Keep it research-adjacent until data source, definition, and service fit are clarified. |
| Add procurement and security gates | Outsourcing, APP, CRM, API, and patient data were all discussed. | Next plan must include vendor/procurement/security assumptions. |
| Prepare for 2026-06-02 | Next meeting tentatively set for June 2 at 10:00. | Draft subproject pages and questions before then. |

## 7. Same-Day Summary

The meeting supports a practical proposal structure:

```text
子計畫一: PSA + community screening + SOP + case management + CRM
子計畫二: smart healthcare + AI/APP + guided intake + reminders + CRM/API integration
子計畫三: ESG + carbon accounting + new-site sustainability
```

The urology previsit system's strongest fit is inside 子計畫二 and as a support layer for 子計畫一. It should be described as a clinician-reviewed visit-readiness and patient-management aid, not as autonomous diagnosis, triage, or treatment recommendation.

## 8. Immediate Follow-Up

- Prepare a 20-23 page draft scope for the smart-healthcare / AI / CRM subproject.
- Decide whether CRM and APP work will be outsourced, internally staffed, or hybrid.
- Estimate budget lines only after each KPI is named.
- Clarify IRB training and governance requirements for all participants who may touch patient data.
- Clarify whether Aging Clock is excluded, included as a small research appendix, or reframed as a biomarker follow-up service workflow.
- Prepare questions for the 2026-06-02 follow-up meeting.

## 9. Jason-Specific Work Interpretation

See `jason-work-scope-from-deep-cultivation-meeting.md`.

The concise interpretation is:

```text
Jason should help turn 子計畫二 into a concrete smart-healthcare / AI / CRM proposal draft, tied to PSA/community screening, KPI, budget, outsourcing, IRB, security governance, and clinician-reviewed workflow boundaries.
```

This interpretation is bounded: the recording assigns the work mainly to 吳老師團隊 / students rather than always naming Jason directly. Aging Clock is treated as 冠宇-led research-adjacent content unless reassigned.
