# Decision Record: 2026-05-19 Deep-Cultivation Meeting

Status: synthesized

2026-06-19 supersession note:

```text
This decision record remains the historical 2026-05-19 interpretation. The
active Jason / 陽明交大 package was later narrowed to AI 問診與醫師覆核摘要 only;
CRM is out of scope and should not be treated as Jason's current responsibility.
```

## Decision Identity

| Field | Notes |
| --- | --- |
| Decision record ID | DR-2026-05-19-001 |
| Date | 2026-05-19 |
| Decision owner | Jason |
| Review context | 北市聯醫 deep-cultivation planning discussion with 吳老師、美如主任, 泌尿科團隊, and related collaborators |
| Related capture note | `deep-cultivation-meeting-capture.md` |
| Related transcript | `taipei-city-hospital-deep-cultivation-meeting-transcript.md` |

## Decision

Continue the urology smart-previsit work, but revise its near-term framing.

The next framing should be:

```text
clinician-reviewed visit-readiness and patient-management support inside a PSA / community-screening / CRM service workflow
```

It should not be framed as:

```text
AI model research by itself
```

## Rationale

The meeting repeatedly emphasized service landing, patient management, SOP, CRM, reminders, follow-up, KPI, budget, procurement, IRB, and security governance.

This means the thinking repo should treat AI, APP, ASR, adaptive questioning, and kiosk-style interaction as enabling tools inside a governed service workflow. The practical claim is improved readiness and follow-up, not diagnosis, treatment, autonomous triage, or model novelty.

## Evidence Summary

| Evidence | Strength | Implication |
| --- | --- | --- |
|美如主任 emphasized CRM and patient management as a hospital weakness. | Strong | CRM should become a central planning axis. |
| PSA screening was repeatedly tied to SOP, return flow, and case management. | Strong | 子計畫一 should not be just screening; it needs follow-up workflow. |
| KPI and budget linkage was emphasized. | Strong | Future drafts need KPI-first budgeting. |
| IRB training and privacy governance were repeatedly flagged. | Strong | No real patient-data work without governance. |
| Procurement / tender requirements were discussed for outsourced systems. | Medium | CRM/APP/API planning must include procurement assumptions. |
| Aging Clock was challenged as research-like and under-defined. | Strong | Keep it bounded until data source, definition, and service fit are clarified. |

## Scope Result

## Continue

Continue:

- guided previsit / adaptive-questioning concept
- clinician-review summary
- missing-information repair
- ASR as optional input layer
- CRM-adjacent patient management framing
- PSA/community screening support framing

## Revise

Revise:

- AI-first language
- demo-only framing
- any claim that smart healthcare value comes mainly from model novelty
- Aging Clock inclusion unless it is attached to a clear service and governance model

## Still Out Of Scope

Still out of scope:

- diagnosis
- treatment advice
- autonomous triage
- urgency or risk scoring
- real patient data during discovery
- HIS / EMR / EHR / registration integration
- production clinical-use claims

## Next Small Artifact

| Field | Notes |
| --- | --- |
| Artifact | Smart-healthcare / AI / CRM subproject draft outline plus `../../core/DEEP_CULTIVATION_SYSTEM_POSITIONING.md` |
| Purpose | Prepare the June 2 follow-up discussion with a fundable service-flow frame |
| Reviewer | 吳老師, 美如主任, 泌尿科 / 北市聯醫 planning stakeholders |
| Done definition | A draft that maps workflow, KPI, budget categories, outsourcing choices, IRB/security gates, and expected outputs |
| Explicit non-goals | No real patient data; no diagnostic claims; no final procurement spec; no aging-clock claim without definition |

## Jason Work Package

Jason's actionable work package is detailed in `jason-work-scope-from-deep-cultivation-meeting.md`.

Operationally, Jason owns preparing or coordinating the 子計畫二 draft content for 吳老師團隊:

- smart-healthcare / AI / CRM service workflow
- KPI and budget mapping
- first-year, second-year, and third-year KPI structure
- internal vs outsourced work questions
- IRB, MOU, security, and procurement gates
- nine-hour IRB training requirement if Jason enters research-data or patient-data work
- alignment with 子計畫一 PSA/community screening follow-up
- assessment of kiosk / chronic-disease-system adaptation and smart-pharmacy ideas as core, optional, or out-of-scope
- bounded handling of Aging Clock as research-adjacent unless defined further

## Paper Implication

The stronger paper framing is not "AI asks medical questions."

The safer framing is:

```text
A governed previsit and patient-management workflow can support visit readiness, follow-up, and clinician review while preserving clinical authority.
```

Evidence still missing:

- clinician usefulness judgment on the actual summary
- staff burden estimate
- workflow slot confirmation
- patient completion / assisted-use feasibility

## Product / Grant Implication

The strongest grant/product frame is:

```text
PSA/community screening + CRM + reminders + guided intake + clinician-review summary + governed follow-up
```

The proposal should treat APP, AI, ASR, kiosk, API, and analytics as infrastructure supporting service flow.

## Research Boundary

Aging Clock should be tracked as a possible research appendix or later sub-study, not a core claim, until the team defines:

- target population
- data source
- aging definition
- biomarker list
- intervention plan
- follow-up interval
- service workflow fit
- IRB and data governance path

## Review Date

Next discussion is tentatively 2026-06-02 10:00.
