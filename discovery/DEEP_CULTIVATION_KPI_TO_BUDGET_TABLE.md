# Deep-Cultivation KPI-To-Budget Table

Status: proposal-prep working table

Date: 2026-05-20

Purpose: make every proposed budget line traceable to a Health Taiwan KPI, work package, owner, and evidence artifact.

## Budget Rule

Use this rule for the proposal:

```text
No KPI, no core budget line.
No owner, no operational claim.
No governance gate, no real patient data or system integration.
```

This prevents the proposal from becoming a list of interesting AI features.

## Core KPI-To-Budget Map

| Work package | KPI / check item | Measurement route | Candidate budget item | Owner needed | Evidence artifact |
| --- | --- | --- | --- | --- | --- |
| Intended-use freeze | Intended use and non-use approved internally | one-page boundary review | coordinator / proposal writing time | proposal owner + clinical reviewer | `INTENDED_USE_FREEZE.md` |
| Demo scope freeze | Demo includes only approved features | scope checklist | coordinator / engineering planning time | proposal owner + engineer | `DEMO_SCOPE_FREEZE.md` |
| Guided intake | synthetic completion rate | 5-10 synthetic cases complete intake -> summary | web/tablet intake development or internal engineering time | engineer + clinical reviewer | demo walkthrough / synthetic cases |
| Question governance | approved first-version question set | clinician review of question bank | clinical review session / RA coordination | urology lead | question governance table |
| Missing-field repair | fewer missing key fields after prompts | synthetic or pilot-approved comparison | form logic / rules implementation | engineer + clinician | missing-field report |
| One-page summary | clinician summary read time | median read time, target <=60 seconds | summary UI / summarization implementation | engineer + clinician | reviewer scorecard |
| Clinician usefulness | usefulness score | 1-5 clinician rating | reviewer session / RA coordination | clinical lead | scorecard |
| Staff burden | nurse/staff burden acceptable | staff review of time, responsibility, exception handling | staff review session | nursing/outpatient reviewer | burden note |
| Clinical friction budget | extra clicks, system switches, training time, exception handling remain acceptable | walkthrough friction log | usability / human factors review | workflow owner | `CLINICAL_FRICTION_REDUCTION_ANALYSIS.md` plus scorecard |
| Source labeling | 100% summary lines have source category | output inspection | data model / summary schema work | engineer | audit sample |
| Unsafe wording | zero diagnosis/treatment/triage/EMR-writeback terms | safety test set | safety review / test implementation | clinical + governance reviewer | safety checklist |
| ASR confirmation | no unconfirmed ASR enters summary | ASR confirmation test | ASR service/evaluation only if used | engineer + clinical reviewer | ASR feasibility note |
| Auditability | source, question path, version, review status preserved | metadata inspection | audit-log implementation | engineer + IT/security | audit design sample |
| AI governance | AI governance checklist completed | self-check completion | governance review time | AI governance owner | governance checklist |
| Cybersecurity governance | cybersecurity checklist completed | self-check completion | security review / hardening | IT/security owner | cybersecurity checklist |
| Data governance | data governance checklist completed | self-check completion | privacy/data governance review | data/privacy owner | data governance checklist |
| Future interoperability readiness | FHIR / TW Core IG mapping exists if data exchange is claimed | mapping review | standards mapping only if needed | IT/data owner | future readiness note |
| Future CRM readiness | SOP owner and workflow defined if reopened | SOP review | no implementation budget unless reopened | service owner | future CRM SOP draft |
| Annual checkpoint reporting | checkpoint table maps deliverables to dates | proposal table review | coordinator / PM time | proposal owner | `DEEP_CULTIVATION_ANNUAL_CHECKPOINT_TABLE.md` |

## Budget Buckets And Conditions

| Budget bucket | Allowed only if | Not allowed if |
| --- | --- | --- |
| Web / tablet intake development | guided intake and completion KPI are core | no workflow slot is confirmed |
| ASR service or module | input burden or language-accessibility KPI is explicit | ASR is just a novelty feature |
| LLM / summary generation | clinician-review summary KPI exists | summary implies diagnosis, treatment, or EMR automation |
| Research assistant / coordinator | review sessions, KPI capture, governance documentation need coordination | RA is only used to compensate for unclear ownership |
| Clinician / staff review session support | scorecards and workload evaluation are planned | clinicians are asked for routine labeling work |
| Security review | APP/API/ASR/data handling or pilot readiness is claimed | demo remains purely static and synthetic |
| Data governance support | data retention, access, de-identification, or real-data future is discussed | no data beyond synthetic examples is used and no future data claim is made |
| Vendor / outsourcing | scope, acceptance criteria, procurement path, ownership, and KPI are defined | vendor is used to hide an undefined system |
| Equipment / tablets | waiting-room tablet workflow is confirmed | patient flow is only speculative |
| CRM platform / reminder module | CRM phase is officially reopened with SOP, owner, consent, privacy, and KPI | CRM remains parked |
| Interoperability mapping | future FHIR / TW Core IG readiness is requested | proposal claims current HIS/EMR integration without approval |

## KPI Detail Table

| KPI | Baseline / current status | Draft target | Measurement method | Evidence level now |
| --- | --- | --- | --- | --- |
| Summary read time | not yet measured | <=60 seconds design target; report actual | synthetic reviewer timing | draft artifact |
| Clinician usefulness | not yet measured | median >=4/5 or revise decision | 3-5 clinician scorecards | draft artifact |
| Nurse/staff burden | not yet measured | acceptable burden threshold documented | staff walkthrough | draft artifact |
| Clinical friction budget | not yet measured | no unacceptable extra clicks/logins/training/exception handling | friction log | draft artifact |
| Synthetic flow completion | not formally counted | 5-10 synthetic cases completed | demo run and checklist | draft artifact |
| Missing-field flagging | not measured | >=90% on synthetic review or failures listed | manual review | draft artifact |
| Source-label completeness | partial design | 100% in synthetic outputs | output inspection | draft artifact |
| Unsafe wording count | target zero | 0 in safety test set | safety test | draft artifact |
| ASR confirmation | not measured | 0 unconfirmed ASR content enters summary | ASR confirmation test | optional |
| Governance checklist completion | draft only | AI/data/cybersecurity owners and gates listed | checklist review | draft artifact |
| KPI-to-budget traceability | not complete | 100% core budget lines mapped to KPI | table audit | draft artifact |

## Budget Narrative Template

Use this pattern in the proposal:

```text
因本子計畫需驗證門診前問診流程是否能降低重複問診與臨床工作摩擦，故編列[工作項目]支援[系統/流程/評估]。該項經費對應 KPI 為[指標]，衡量方式為[方法]，由[負責角色]於[年度查核點]提供[證據文件]。
```

Example:

```text
因本子計畫需驗證醫師是否能於 60 秒內閱讀一頁式覆核摘要，故編列系統摘要畫面與 reviewer session 相關工作。該項經費對應 KPI 為「醫師摘要可讀時間」與「醫師 useful rating」，衡量方式為合成案例 reviewer scorecard，由泌尿科臨床團隊與計畫協調人於第一年度查核點提供評估紀錄。
```

## Red Flags

Do not request a budget item if:

- it has no KPI
- it has no owner
- it requires real patient data before governance
- it implies autonomous clinical decision-making
- it shifts work to nurses without measuring burden
- it creates a new system clinicians must use without workflow proof
- it is mainly for AI novelty rather than clinical friction reduction

## Current Open Items

| Open item | Needed from |
| --- | --- |
| Budget ceiling | parent proposal owner |
| Personnel categories and allowed rates | official funding documents / hospital admin |
| Whether tablets/equipment are allowed and useful | hospital workflow owner |
| Whether ASR has a funded KPI | clinical + proposal owner |
| Whether vendor work is allowed | procurement owner |
| Whether CRM is reopened | service owner + governance owner |
| Whether FHIR / TW Core IG mapping is required in this subproject | IT/data governance owner |
