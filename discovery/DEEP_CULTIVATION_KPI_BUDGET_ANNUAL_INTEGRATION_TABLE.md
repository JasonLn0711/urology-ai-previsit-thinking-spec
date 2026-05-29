# Deep-Cultivation KPI / Budget / Annual Checkpoint Integration Table

Status: proposal-writing integration table

Date: 2026-05-29

Current proposal package: `DEEP_CULTIVATION_APPLICATION_DRAFT_V0_5.md`

Purpose: connect each proposed benefit to a measurable KPI, official proposal section, budget bucket, owner, evidence artifact, and annual checkpoint. This file should be used before writing any budget paragraph.

## First Principle

```text
The proposal is fundable only if every requested resource changes a measurable workflow state.
```

Therefore:

```text
No KPI -> no core budget line.
No owner -> no operational claim.
No governance gate -> no real patient data, HIS/EMR integration, or deployment claim.
No friction reduction -> no Health Taiwan workflow value.
```

## Integrated Table

| Official proposal location | Work package | KPI / checkpoint | Draft target | Measurement route | Budget bucket | Owner needed | Evidence artifact | Annual checkpoint |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `壹、申請單位自我檢核項目表` | official package checklist | official blanks visible | cover, self-check, COI, duplicate-funding, consent, review-response needs are explicit | package checklist review | proposal coordination | parent proposal owner | v0.5 official package checklist | before parent transfer |
| `貳、計畫概要` | problem framing | staff-burden reduction thesis stated | one paragraph explicitly names physician/nurse/staff burden | reviewer reads abstract and checks burden claim | proposal coordination | proposal owner | `DEEP_CULTIVATION_APPLICATION_DRAFT_V0_4.md` | 115 prep |
| `肆、計畫規劃` | workflow slot | clinic slot confirmed | after-registration / waiting-room slot accepted or revised | hospital workflow owner review | workflow review session | clinic workflow owner | meeting record / decision note | 115 prep or 116 design |
| `肆、計畫規劃` | intended-use freeze | approved intended use and non-use | target group, output, exclusions frozen | checklist review | coordination / clinical review | clinical + proposal owner | `INTENDED_USE_FREEZE.md` | 115 prep |
| `肆、計畫規劃` | demo-scope freeze | no scope drift | current demo excludes diagnosis, treatment, final triage, queue priority, HIS/EMR writeback, real patient data | checklist review | coordination / engineering review | proposal + engineering owner | `DEMO_SCOPE_FREEZE.md` | 115 prep |
| `肆、計畫規劃` | guided intake | synthetic completion | 5-10 synthetic cases can complete intake to summary | walkthrough checklist | web/tablet prototype or internal engineering time | engineer + clinician | demo walkthrough | 115 prep / 116 design |
| `肆、計畫規劃` | question governance | first-version question set approved | LUTS / OAB-like core set approved | clinician review session | clinical review / RA coordination | urology lead | question governance table | 116 design |
| `肆、計畫規劃` | missing-field repair | missing key-field visibility | >=90% synthetic key missing fields are surfaced, or failures listed | synthetic output review | form logic / rules implementation | engineer + clinician | missing-field report | 116 design |
| `肆、計畫規劃` | ASR confirmation | no unconfirmed voice content used | 0 unconfirmed ASR transcript/answers enter summary | ASR confirmation test | ASR service/evaluation only if funded | engineer + clinical reviewer | ASR feasibility note | 116 design |
| `伍、效益評估` | one-page summary | clinician read time | median <=60 seconds as design target; report actual | timed reviewer session | summary UI / summarization implementation | engineer + clinician | reviewer scorecard | 116 design |
| `伍、效益評估` | clinician usefulness | usefulness rating | median >=4/5 or revise decision | clinician scorecard | reviewer session / RA coordination | clinical lead | scorecard | 116 design |
| `伍、效益評估` | repeated-question reduction | repeated questions reduced | baseline and after-workflow question counts defined; target pending pilot | staff/clinician walkthrough or approved pilot | workflow evaluation support | evaluator + clinical owner | before/after worksheet | 117 only if approved |
| `伍、效益評估` | staff burden | burden acceptable | no unacceptable extra clicks, duplicate entry, system switching, or exception handling | friction log / staff walkthrough | usability / human factors review | workflow owner | `CLINICAL_FRICTION_REDUCTION_ANALYSIS.md` plus scorecard | 116 design |
| `伍、效益評估` | source labeling | source-label completeness | 100% summary lines have source category | output inspection | data model / summary schema work | engineer | audit sample | 116 design |
| `伍、效益評估` | unsafe wording | unsafe clinical wording count | 0 diagnosis/treatment/final-triage/EMR-writeback claims in safety set | safety test | safety review / test implementation | clinical + governance reviewer | safety checklist | 115 prep / 116 design |
| `伍、效益評估` | governance completion | governance owner readiness | AI, cybersecurity, data, privacy, procurement, IRB route owners named | checklist review | governance review time | hospital governance owners | `DEEP_CULTIVATION_GOVERNANCE_CHECKLIST.md` | 115 prep |
| `柒、經費規劃` | budget traceability | budget lines mapped to KPI | 100% core budget lines map to KPI, owner, and checkpoint | table audit | proposal/budget coordination | budget owner | this file + `DEEP_CULTIVATION_KPI_TO_BUDGET_TABLE.md` | before submission |
| `柒、經費規劃` | three-year budget ceiling | NT$10,000,000 working total | annual split and accounting categories visible before parent transfer | budget owner review | official budget categories | parent budget owner | v0.5 budget allocation | 2026-06-02 discussion |
| `柒、經費規劃` | capital/business/personnel split | official categories satisfied | no fake itemization until ceiling is confirmed | budget owner review | official budget categories | budget owner | official budget table | before submission |
| `捌、人力配置` | role clarity | role table complete | named people or roles for PI, clinical lead, workflow reviewer, IT/security, AI/data governance, engineer, coordinator | manpower table review | personnel/coordination | parent proposal owner | v0.5 owner and responsibility table | before submission |
| `玖、其他` | attachments | evidence packet selected | attach only safe, proposal-relevant docs | appendix review | coordination | proposal owner | attachment list | before circulation |
| `拾-拾貳` | statutory forms | forms handled by institution | COI, no duplicate funding, participation consent complete | administrative review | institution admin | parent applicant | signed official forms | submission |
| `拾參、審查意見回復表` | review-response readiness | response table prepared | likely reviewer questions and response directions drafted | reviewer-readiness check | proposal coordination | proposal writer + parent owner | v0.5 review-response table | before external review |

## Recommended KPI Grouping For Proposal Table

Use these as the v0.5 KPI rows unless the hospital owner changes them:

| Category | KPI | Current baseline | Draft target | Why it fits Health Taiwan |
| --- | --- | --- | --- | --- |
| Workflow burden | Summary read time | not yet measured | <=60 seconds in synthetic reviewer session | directly tests whether the summary saves attention |
| Workflow burden | Repeated-question reduction feasibility | not yet measured | define baseline and after-workflow count; pilot target pending | links to staff/physician workload reduction |
| Information quality | Missing key-field visibility | not yet measured | >=90% synthetic key missing fields flagged, or failures listed | improves visit readiness without diagnosis |
| Information quality | Source-label completeness | partial design | 100% in synthetic summary outputs | preserves auditability and responsibility |
| Safety | Unsafe wording count | target zero | 0 in test set | prevents AI triage / diagnosis overclaim |
| Staff burden | Clinical friction budget | not yet measured | no unacceptable extra clicks/logins/training/exception load | prevents making staff work harder |
| Input burden | ASR confirmation safety | optional | 0 unconfirmed ASR content enters summary | makes voice input safe if used |
| Governance | AI/data/cybersecurity checklist completion | draft only | owners and gates named before pilot claim | required for Scope 3 smart-healthcare credibility |
| Budget discipline | KPI-to-budget traceability | not complete | 100% core budget lines mapped | prevents budget without deliverable |

## Budget Buckets By Evidence Strength

| Budget bucket | Current status | Recommendation |
| --- | --- | --- |
| Project coordination / RA | justified by reviewer sessions, KPI capture, governance documents and review-response tracking | v0.5 allocates NT$3,000,000 discussion total, subject to parent budget owner |
| Clinician/staff review sessions | justified by summary usefulness and friction-budget KPI | include as evaluation/support activity, not routine labeling |
| Web/tablet intake prototype | justified if waiting-room QR/tablet slot is accepted | include only after workflow slot confirmation |
| Summary-generation implementation | justified by read-time and source-label KPI | include as workflow artifact development |
| ASR module/service | optional | include only if input-burden or multilingual-accessibility KPI is explicit |
| Security/data/AI governance review | required for Scope 3 readiness | include or assign internal owner |
| FHIR / TW Core IG mapping | future readiness only | include mapping only if proposal claims future interoperability |
| CRM/reminder platform | parked | do not budget unless CRM phase is reopened with SOP, consent, owner, and KPI |
| Tablets/equipment | conditional | do not budget until site workflow and procurement allow it |
| HIS/EMR integration | excluded from current scope | do not budget in v0.5 |

## Annual Checkpoint Integration

| Stage | Main goal | Checkpoints | Evidence |
| --- | --- | --- | --- |
| 115 prep | prepare fundable, safe, format-compliant package | intended use, scope freeze, v0.5 discussion draft, KPI-budget table, governance owner questions, review-response table | v0.5 package and review log |
| 116 design | validate workflow fit before real deployment | workflow slot, question set, summary schema, synthetic walkthrough, staff burden review | clinician/staff scorecards, safety tests |
| 117 limited evaluation | only if governance and hospital ownership exist | approved pilot/QI route, baseline and after-workflow measurement, safety monitoring | approved protocol or QI plan, audit logs |
| 118 scale decision | decide whether to scale, integrate, or stop | evidence review, maintenance plan, CRM/interoperability decision, procurement route | final decision record and operations plan |

## Proposal Narrative Snippet

Use this wording when connecting budget to KPI:

```text
本子計畫之經費編列不以 AI 功能數量為核心，而以可驗收之門診流程改善工作為核心。各工作項目均需對應明確 KPI、年度查核點與負責角色；若無法對應降低重複問診、提升門診前資訊完整性、縮短醫師摘要閱讀時間、降低護理/行政額外負擔或完成資安/資料/AI治理要求，則不列為本階段核心經費。
```

## Do Not Write These As KPI

- AI diagnosis accuracy
- final triage accuracy
- treatment recommendation quality
- automatic EMR completion rate
- mortality or cancer detection improvement
- broad all-department scalability
- current HIS/EMR integration success
- current CRM retention effect

These are outside the current intended use.

## Next Owner Questions

| Question | Required before |
| --- | --- |
| Does the NT$10,000,000 working ceiling fit the parent proposal's official accounting categories and annual split? | official budget table |
| Are tablets/equipment allowed and desired? | any capital item |
| Is ASR worth funding as a KPI-backed input-burden reduction tool? | ASR budget |
| Who signs off cybersecurity/data/AI governance? | Scope 3 self-check wording |
| Is this a QI/service improvement path or research/IRB path? | any real-patient pilot claim |
| Is CRM still parked? | any follow-up/reminder budget |
| Is FHIR/TW Core IG mapping required now or future-state only? | interoperability budget |
