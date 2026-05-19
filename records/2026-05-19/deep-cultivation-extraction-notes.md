# Extraction Notes: Deep-Cultivation Meeting

Status: synthesized

## Source

- Transcript: `taipei-city-hospital-deep-cultivation-meeting-transcript.md`
- Capture: `deep-cultivation-meeting-capture.md`
- Decision record: `deep-cultivation-decision-record.md`
- Policy reference: `health-taiwan-deep-cultivation-policy-reference.md`
- Related examples: `health-taiwan-related-examples.md`
- Evergreen positioning: `../../core/DEEP_CULTIVATION_SYSTEM_POSITIONING.md`

## Paper Extraction

## Candidate Claim

A bounded urology previsit workflow may be more useful when embedded in a patient-management / CRM service pathway than when presented as a standalone AI interviewer.

## Evidence From Meeting

| Evidence | Captured? | Notes |
| --- | --- | --- |
| CRM identified as current operational weakness | Yes | The meeting repeatedly described patient management as weaker than AI capability. |
| PSA screening requires follow-up | Yes | Screening was tied to SOP, return-to-hospital flow, case management, and CRM. |
| AI treated as tool | Yes | APP, AI, ASR, kiosk, and API were discussed as support layers. |
| Clinician authority preserved | Yes | No meeting signal authorized diagnosis, treatment, or autonomous triage. |
| Governance and procurement matter | Yes | IRB, MOU, security governance, KPI, budget, and tendering were all raised. |

## Limitation Statement

This meeting does not prove clinical effectiveness, adoption, time savings, or safety. It supports a clearer workflow and grant-framing hypothesis.

## Product / Grant Extraction

## Strategic Label

```text
AI Systems Engineering for Healthcare Deployment
```

This label fits the meeting better than `AI model research`.

It means the proposal should emphasize CRM, SOP, reminders, patient-management workflow, governed intake, clinician review, and deployment governance. AI is a component in the service system, not the standalone contribution.

## Policy Alignment Extraction

The official `健康台灣深耕計畫(114-118年)` frame strengthens this repo's current direction.

Recommended mapping:

| Proposal element | Policy category |
| --- | --- |
| AI-assisted guided intake, ASR, adaptive questioning, APP, CRM/API | 導入智慧科技醫療 |
| reduced repeated work, reminders, visit-readiness summary | 優化醫療工作條件 |
| 吳老師團隊 / student cross-domain work and IRB readiness | 規劃多元人才培訓, if explicitly designed |
| PSA community screening, clinic/community MOU, follow-up pathway | 社會責任醫療永續 |
| ESG / carbon accounting | 社會責任醫療永續 |

This mapping supports the `AI Systems Engineering for Healthcare Deployment` label.

## Related-Examples Extraction

The online examples reinforce the same proposal pattern:

- MOHW outcome examples: nursing voice AI assistant, e-paper bedside card, smart medication cabinet.
- Official plan guidance: AI/RPA/report-generation style workload reduction, clinical note / handoff documentation support, smart workflow, data sharing/security, SMART on FHIR.
- Tainan Municipal Hospital case: ALL-IN-ONE mobile medical service vehicle, clinical AI, cross-hospital data exchange, telecare, chronic-disease management, community care, AI voice records.
- Jen-Ai / Mercy Hospital case: AI lung imaging assistance, integrated HIS, health-management app, and green-hospital metrics.
- AI Center guidance: cybersecurity governance, data governance, AI governance, FHIR and TW Core IG.

Implication:

```text
子計畫二 should read like intelligent clinical intake and visit-readiness infrastructure, not an LLM demo.
```

## Recommended Grant Frame

```text
子計畫一: PSA / community screening / SOP / case management / CRM
子計畫二: smart healthcare / guided previsit / AI-APP / reminders / API-CRM integration
子計畫三: ESG / carbon accounting / new-site sustainability
```

## Subproject Two Scope

The urology smart-previsit system belongs most naturally in 子計畫二, with direct links back to 子計畫一.

Recommended wording:

- governed previsit intake
- patient-reported information capture
- missing-information repair
- patient or family review
- clinician-review summary
- visit and lab reminders
- CRM follow-up support
- optional ASR as input layer
- API-ready architecture for later governed integration

Avoid wording:

- diagnosis engine
- autonomous triage
- AI doctor
- risk score
- automatic treatment recommendation
- direct HIS integration as current scope

## KPI Extraction

Candidate KPI categories to draft, not final commitments:

- number of PSA/community participants reached
- percentage of screened participants with completed follow-up workflow
- number of SOPs established
- reminder delivery / response rate
- return-visit completion rate
- CRM enrollment or tracking completeness
- clinician-review summary completion rate
- missing-information reduction before visit
- patient/staff usability feedback
- security / IRB / procurement gates completed

## Budget Extraction

Budget lines must map to KPI. Candidate categories:

- research assistant / project coordinator
- CRM platform or platform customization
- APP / guided-intake development
- API or messaging integration
- kiosk or front-end device if justified
- security review / governance documentation
- procurement / outsourcing cost
- biomarker testing only if Aging Clock is included with defined scope

## Aging Clock Extraction

## Current Status

Research-adjacent, not yet proposal-core.

## Why It Is Not Yet Core

美如主任's questions show that the direction still lacks:

- data-source decision
- aging definition
- biomarker boundary
- intervention design
- field workflow
- service relevance to the deep-cultivation plan

## Possible Future Packaging

If kept, it should be packaged as:

```text
PSA/community blood draw -> optional biomarker panel -> baseline biological-age estimate -> targeted lifestyle/nutrition intervention -> three-month follow-up -> clinician/research review
```

That packaging requires separate IRB and data-governance review.

## Patent / System-Logic Extraction

Do not claim novelty from ordinary questionnaire, CRM, or reminders alone.

Potential system-logic angle, if later supported:

- screening-triggered guided intake
- governed missing-information repair
- source-labeled patient/family/nurse input
- neutral clinician-review summary
- CRM-based follow-up loop
- optional ASR as an input layer with correction/review

Claims not supported yet:

- clinical effectiveness
- triage accuracy
- diagnostic performance
- biomarker-aging intervention effectiveness
- production integration readiness
