# Deep-Cultivation Governance Checklist

Status: proposal-prep governance checklist

Date: 2026-05-20

2026-06-02 official meeting minutes + 2026-06-19 owner update:

```text
The parent 信義 AI 智慧問診 allocation is about NT$15,000,000 and includes CRM.
CRM is handled by parent / other-team scope. This checklist governs Jason /
陽明交大 AI 問診、醫師覆核摘要、AI/data/security governance, and KPI evidence
only. CRM outsourcing, CRM-ready handoff, CRM KPI, CRM budget, patient
messaging, dashboard, vendor CRM, and CRM maintenance are governed by the
parent proposal / other-team workstream.
```

Purpose: prepare AI, cybersecurity, data, privacy, and clinical-responsibility governance before any Health Taiwan proposal claims pilot readiness, patient-data use, or smart-healthcare deployment.

## Governance Principle

```text
Governance is not an appendix.
For Scope 3 smart healthcare, governance is part of the core proposal value.
```

## Gate Summary

| Gate | Current status | Required before |
| --- | --- | --- |
| Intended-use freeze | Created | proposal v0.2 circulation |
| Demo-scope freeze | Created | reviewer demo |
| Clinical boundary | Existing in `../core/SAFETY_BOUNDARY.md` | proposal wording |
| AI governance owner | Pending | any AI-governance claim |
| Cybersecurity owner | Pending | APP/API/ASR/pilot claim |
| Data governance owner | Pending | data retention or real-data claim |
| IRB / QI determination | Pending | any real patient workflow |
| Procurement owner | Pending | vendor or outsourced work |
| Hospital workflow owner | Pending | pilot or deployment planning |
| FHIR / TW Core IG owner | Pending | interoperability-readiness claim |
| PSA clinical SOP owner | Pending | any PSA clinical-procedure or guideline-compliance claim |

## Clinical Governance

| Item | Required statement / artifact | Status |
| --- | --- | --- |
| No diagnosis | System does not diagnose or infer disease | drafted |
| No treatment advice | System does not recommend medication, procedures, or actions | drafted |
| No autonomous triage | System does not assign urgency, risk, or queue priority | drafted |
| Clinician final authority | Clinician owns interpretation and formal documentation | drafted |
| Red-flag observations | Patient-reported observations only; local human review | drafted |
| Override path | accept / edit / ignore / reject status | needs prototype evidence |
| Unsafe wording test | zero diagnosis/treatment/triage terms | needs test artifact |
| Clinical friction check | no hidden nurse/physician burden | needs reviewer evidence |

## AI Governance

| Item | Required for proposal | Status |
| --- | --- | --- |
| AI role statement | AI assists structuring, missing-field detection, and summary drafting only | drafted |
| Model/prompt/rule versioning | version fields listed before pilot | draft needed |
| Human-in-the-loop | every output is clinician-reviewable | drafted |
| Transparency | summary shows source labels and uncertainty/missing fields | drafted |
| Failure behavior | low confidence / contradiction / incomplete answers have fallback | partially drafted |
| Bias/fairness note | accessibility and language support considered without overclaim | draft needed |
| Monitoring plan | future pilot would monitor errors, unsafe wording, correction rate | draft needed |
| Retraining policy | no automatic learning from clinician edits without governance | drafted |
| AI lifecycle owner | named owner required | pending |

## Cybersecurity Governance

| Item | Required before pilot claim | Status |
| --- | --- | --- |
| System boundary | local demo / prototype / pilot / production clearly separated | drafted |
| Authentication | define if staff-facing view exists | pending |
| Role-based access | patient, staff, clinician, admin roles separated | draft needed |
| Logging | access and output review logs defined | draft needed |
| Network exposure | no production endpoint without review | drafted |
| Secrets management | no tokens or credentials in repo/docs | standing rule |
| Vendor security | required if outsourced platform/ASR/cloud service is used | pending |
| Incident response | define reporting route for pilot | pending |
| Security owner | hospital IT/security contact named | pending |

## Data Governance

| Item | Required before real data | Status |
| --- | --- | --- |
| Data classification | synthetic / patient-reported / staff-supplemented / clinical-record data separated | drafted |
| Consent model | required before real patient use | pending |
| Retention period | required before real patient use | pending |
| Deletion process | required before real patient use | pending |
| De-identification | required for any research dataset | pending |
| Access control | role and purpose-based access | pending |
| Data minimization | minimum useful context, not maximum capture | drafted |
| ASR data handling | audio/transcript storage decision | pending |
| Export rules | no EMR writeback without approval | drafted |
| Data owner | hospital data/privacy owner named | pending |

## FHIR / TW Core IG Readiness

| Item | Safe first-version wording | Status |
| --- | --- | --- |
| Interoperability posture | future governed interoperability readiness | drafted |
| Current integration | no current HIS/EMR integration claim | drafted |
| Mapping target | future mapping of summary fields if hospital requests | pending |
| SMART on FHIR | mention only if actual route is planned | not current scope |
| Owner | IT/data governance owner required | pending |

## IRB / Research Governance

| Question | Required answer before next phase |
| --- | --- |
| Is the activity research, QI, service improvement, or mixed? | pending IRB/governance review |
| Will real patient data be collected? | not in current discovery/demo |
| Will patient audio be recorded? | not in current proposal-prep scope |
| Will clinician edits be analyzed? | only after governance approval |
| Will data leave the hospital? | not allowed without explicit approval |
| Will outputs affect clinical care? | not before pilot governance |

## Procurement And Vendor Governance

| Item | Required if applicable |
| --- | --- |
| Vendor scope | exact deliverables and acceptance criteria |
| Data handling | storage, transfer, retention, deletion, breach response |
| Security review | hospital security owner approval |
| Ownership | who maintains the system after the project |
| Lock-in risk | exportability and transition plan |
| Budget trace | each vendor line maps to KPI |
| ASR / cloud | no procurement without workflow owner and governance owner |

## Out-of-Scope CRM Note

CRM is handled outside Jason / 陽明交大 current package. If another hospital team
needs CRM governance, it should be documented in that team's plan, not in this
AI 問診與醫師覆核摘要 package.

## PSA Clinical-Governance Interface

The PSA screening plan is integrated into the proposal architecture, but the
clinical SOP remains clinically owned.

| Item | Required answer |
| --- | --- |
| Clinical owner | Which 忠孝院區 / urology lead owns PSA SOP? |
| Guideline boundary | Which Taiwan Urological Association guidance must be cited or followed? |
| Eligibility | How are men `50+` and `45+` with family history identified? |
| Follow-up trigger | What counts as abnormal or requiring follow-up? |
| Follow-up responsibility | Who contacts, schedules, or tracks the patient? |
| AI intake relation | Which PSA / urology visit context, if any, should inform the AI question set? |
| Research/QI route | Is AI 問診與摘要 evidence used for service improvement, research, or both? |
| Evidence owner | Who signs off on screening count and follow-up completion evidence? |

## Audit Fields For Pilot-Ready Design

Minimum fields:

- case id or synthetic id
- data source category
- answer source: patient / family / staff-assisted / ASR-confirmed
- question set version
- rule / prompt / model version if used
- summary schema version
- missing-field list
- red-flag observation wording version
- generated summary
- clinician review status
- clinician edit / rejection reason if captured
- timestamp
- responsible role

## Governance Completion Table

| Artifact | Current status | Next action |
| --- | --- | --- |
| Intended use | created | ask clinical/proposal owner to confirm |
| Demo scope | created | use before demo update |
| Clinical boundary | existing | align wording with proposal v0.2 |
| AI governance checklist | this file | map to official self-check form |
| Cybersecurity checklist | this file | get hospital IT/security owner |
| Data governance checklist | this file | get data/privacy owner |
| KPI-to-budget table | created | fill budget amounts after ceiling known |
| Annual checkpoint table | created | align with parent proposal period |
| Official self-check forms | local archive exists | transfer answers into official forms when requested |

## Pilot-Readiness Claim Requirements

A pilot-readiness claim requires:

- named clinical workflow owner
- named AI/data/security governance owner
- real patient-data governance approval before any real patient data use
- output wording that preserves diagnosis, treatment, and triage authority for clinicians
- clinician review that does not become routine AI labeling labor
- nursing workflow that does not become the hidden default operating layer
- budget requests mapped to KPI
- clear vendor/system responsibility

## Proposal-Safe Governance Sentence

```text
本子計畫於第一版即納入 AI 治理、資安治理與資料治理設計，包含人機協作邊界、資料最小化、來源標記、版本紀錄、醫師覆核、錯誤處理、未來互通標準準備與實際導入前之 IRB/個資/資安/採購審查。真實病患資料、HIS/EMR 連接、診斷、治療與自動分流權限均保留於完成治理審查後的院內流程與臨床責任架構。
```
