# 健康台灣深耕計畫 KPI / 預算 / 年度 checkpoint 整合表

狀態：提案撰寫整合表

日期：2026-05-29

目前提案包：`DEEP_CULTIVATION_APPLICATION_DRAFT_V0_7.md`

2026-06-02 後 active gate:

```text
v0.8 planning: 信義 integrated PSA 主動篩檢 + AI 智慧問診 + CRM 外包
```

目的：把每一項提案效益連到可衡量 KPI、正式提案章節、預算項目、owner、evidence artifact 與年度 checkpoint。撰寫任何預算段落前，應先查核本表。

## First Principle

```text
提案可成立的條件，是每一項被申請的資源都能改變一個可衡量的 workflow state。
```

因此：

```text
No KPI -> no core budget line.
No owner -> no operational claim.
No governance gate -> no real patient data, HIS/EMR integration, or deployment claim.
No friction reduction -> no Health Taiwan workflow value.
```

## 整合表

| 正式提案位置 | 工作包 | KPI / checkpoint | 草案目標 | 衡量路徑 | 預算項目 | 需要的 owner | evidence artifact | 年度 checkpoint |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `壹、申請單位自我檢核項目表` | official package checklist | official blanks visible | cover、self-check、COI、duplicate-funding、consent、review-response needs 均明確 | package checklist review | proposal coordination | parent proposal owner | v0.6 official package checklist | parent transfer 前 |
| `貳、計畫概要` | problem framing | staff-burden reduction thesis stated | 一段文字明確寫出 physician/nurse/staff burden | reviewer 讀摘要並檢查 burden claim | proposal coordination | proposal owner | `DEEP_CULTIVATION_APPLICATION_DRAFT_V0_6.md` | 115 prep |
| `肆、計畫規劃` | workflow slot | clinic slot confirmed | after-registration / waiting-room slot accepted or revised | hospital workflow owner review | workflow review session | clinic workflow owner | meeting record / decision note | 115 prep or 116 design |
| `肆、計畫規劃` | intended-use freeze | approved intended use and non-use | target group、output、exclusions frozen | checklist review | coordination / clinical review | clinical + proposal owner | `INTENDED_USE_FREEZE.md` | 115 prep |
| `肆、計畫規劃` | demo-scope freeze | no scope drift | current demo excludes diagnosis、treatment、final triage、queue priority、HIS/EMR writeback、real patient data | checklist review | coordination / engineering review | proposal + engineering owner | `DEMO_SCOPE_FREEZE.md` | 115 prep |
| `肆、計畫規劃` | guided intake | synthetic completion | 5-10 件 synthetic cases 可完成 intake to summary | walkthrough checklist | web/tablet prototype or internal engineering time | engineer + clinician | demo walkthrough | 115 prep / 116 design |
| `肆、計畫規劃` | question governance | first-version question set approved | LUTS / OAB-like core set approved | clinician review session | clinical review / RA coordination | urology lead | question governance table | 116 design |
| `肆、計畫規劃` | missing-field repair | missing key-field visibility | >= 90% synthetic key missing fields are surfaced，或列出 failures | synthetic output review | form logic / rules implementation | engineer + clinician | missing-field report | 116 design |
| `肆、計畫規劃` | ASR confirmation | no unconfirmed voice content used | 0 unconfirmed ASR transcript/answers enter summary | ASR confirmation test | ASR service/evaluation only if funded | engineer + clinical reviewer | ASR feasibility note | 116 design |
| `伍、效益評估` | one-page summary | clinician read time | median <= 60 秒 as design target；report actual | timed reviewer session | summary UI / summarization implementation | engineer + clinician | reviewer scorecard | 116 design |
| `伍、效益評估` | clinician usefulness | usefulness rating | median >= 4/5 or revise decision | clinician scorecard | reviewer session / RA coordination | clinical lead | scorecard | 116 design |
| `伍、效益評估` | repeated-question reduction | repeated questions reduced | baseline and after-workflow question counts defined；pilot target pending | staff/clinician walkthrough or approved pilot | workflow evaluation support | evaluator + clinical owner | before/after worksheet | 117 only if approved |
| `伍、效益評估` | staff burden | burden acceptable | no unacceptable extra clicks、duplicate entry、system switching 或 exception handling | friction log / staff walkthrough | usability / human factors review | workflow owner | `CLINICAL_FRICTION_REDUCTION_ANALYSIS.md` plus scorecard | 116 design |
| `伍、效益評估` | source labeling | source-label completeness | 100% summary lines have source category | output inspection | data model / summary schema work | engineer | audit sample | 116 design |
| `伍、效益評估` | unsafe wording | unsafe clinical wording count | safety set 中 diagnosis/treatment/final-triage/EMR-writeback claims 為 0 | safety test | safety review / test implementation | clinical + governance reviewer | safety checklist | 115 prep / 116 design |
| `伍、效益評估` | governance completion | governance owner readiness | AI、cybersecurity、data、privacy、procurement、IRB route owners named | checklist review | governance review time | hospital governance owners | `DEEP_CULTIVATION_GOVERNANCE_CHECKLIST.md` | 115 prep |
| `柒、經費規劃` | budget traceability | budget lines mapped to KPI | 100% core budget lines map to KPI、owner、checkpoint | table audit | proposal/budget coordination | budget owner | this file + `DEEP_CULTIVATION_KPI_TO_BUDGET_TABLE.md` | submission 前 |
| `柒、經費規劃` | three-year budget ceiling | NT$10,000,000 working total | parent transfer 前可見 annual split plus formal fill-out columns | budget owner review | official budget categories | parent budget owner | v0.6 budget allocation and formal fill-out table | 2026-06-02 discussion |
| `柒、經費規劃` | capital/business/personnel split | official categories satisfied | ceiling confirmed 前不做 fake itemization | budget owner review | official budget categories | budget owner | official budget table | submission 前 |
| `捌、人力配置` | role clarity | role table complete | PI、clinical lead、workflow reviewer、IT/security、AI/data governance、IRB/QI、engineer、coordinator 需具名或明確角色 | manpower table review | personnel/coordination | parent proposal owner | v0.6 owner and responsibility table | submission 前 |
| `玖、其他` | attachments | evidence packet selected | 只附 safe、proposal-relevant docs | appendix review | coordination | proposal owner | attachment list | circulation 前 |
| `拾-拾貳` | statutory forms | forms handled by institution | COI、no duplicate funding、participation consent complete | administrative review | institution admin | parent applicant | signed official forms | submission |
| `拾參、審查意見回復表` | review-response readiness | response table prepared | likely reviewer questions and response directions drafted | reviewer-readiness check | proposal coordination | proposal writer + parent owner | v0.6 review-response table | external review 前 |

## v0.8 信義整合 KPI / Budget Architecture

This section supersedes the old `CRM parked` interpretation for the 信義
proposal lane. CRM outsourcing is now an explicit proposal-writing scope after
the 2026-06-02 responsibility clarification. Procurement, data route, security,
privacy, patient messaging, and maintenance remain governance gates.

| Component | KPI / checkpoint | Draft target | Budget meaning | Required owner | Evidence artifact | Stop rule |
| --- | --- | --- | --- | --- | --- | --- |
| PSA active screening | annual screening volume | `3,500-5,000` men per year | PSA screening operations and coordination, about NT$15,000,000 signal | 忠孝院區 urology / clinical SOP owner | PSA SOP, guideline-compliance note, screening-count workbook | Do not write clinical SOP as Jason-owned |
| PSA follow-up | abnormal-case return / tracking completion | `>= 70%` | follow-up coordination and CRM-linked tracking | clinical owner + CRM workflow owner | abnormal-case tracking report | Do not claim cancer-outcome improvement |
| AI 智慧問診 | one-page physician-reference summary | generated / readable within `60` seconds | AI 問診 / summary workflow, part of about NT$15,000,000 AI/CRM signal | 智慧健康醫療中心 + clinical reviewer | timed reviewer scorecard | Do not claim diagnosis, treatment, triage, or queue priority |
| Information quality | source label and missing-field visibility | source label `100%`; missing-field visibility `>= 90%` | summary schema, data model, auditability | engineering + clinical reviewer | audit sample, missing-field report | Do not hide uncertainty or unsupported inference |
| Safety wording | unsafe wording count | `0` diagnosis / treatment / autonomous triage / automatic EMR phrases | safety review and prompt/rule governance | clinical + governance reviewer | unsafe-wording checklist | Do not soften this gate |
| CRM outsourcing | follow-up queue / contact-management readiness | CRM workflow fields reviewed; owner and procurement path named | CRM outsourced service / system scope | CRM owner + procurement + IT/security | CRM field map, vendor-scope note, procurement note | No real patient messaging or production CRM claim before privacy/security/procurement approval |
| CRM-to-PSA KPI mapping | abnormal follow-up evidence route | every abnormal case has status field and next-action owner | CRM supports `>= 70%` KPI evidence | clinical owner + CRM workflow owner + evaluation owner | follow-up dashboard spec, evidence workbook | Do not treat CRM as decorative software line |
| Governance | owner readiness | AI/data/cybersecurity/IRB-QI/procurement/maintenance owners named or pending explicitly | governance review time and documentation | parent proposal owner | governance checklist | No real-data or deployment claim without owner route |
| Capital / equipment cap | capital expenditure review | capital items below legal `30%` cap | equipment / device procurement only if workflow and accounting allow | budget + procurement owner | official budget table | Do not invent equipment lines without accounting review |

## v0.8 Budget Transition

v0.7 used NT$10,000,000 as a discussion allocation for the AI 智慧問診 slice.
The 2026-06-02 meeting signal changes the budget architecture:

```text
PSA 主動篩檢: about NT$15,000,000
AI 智慧問診 including CRM: about NT$15,000,000
信義碳盤查: about NT$7,500,000, parallel parent-proposal workstream
```

The v0.8 draft should keep budget discipline:

```text
No KPI -> no core budget line.
No owner -> no operational claim.
No procurement/data/security route -> no CRM production claim.
No clinical SOP owner -> no PSA clinical-procedure claim.
```

## v0.8 NT$15M AI / CRM Fine-Grained KPI Support

The AI 智慧問診 / CRM allocation is about NT$15,000,000. This amount needs a
reviewable KPI stack. A small set of headline KPIs is not enough for主管單位 or
審查機關.

Use this rule:

```text
Every budgetable work package must have at least one sub-KPI, one owner, one
evidence artifact, and one annual checkpoint.
```

Draft fine-grained KPI stack:

| Budget-support area | Sub-KPI | Draft target | Evidence artifact | Owner needed |
| --- | --- | --- | --- | --- |
| Proposal integration | integrated PSA / AI / CRM proposal package completeness | one integrated v0.8 skeleton plus owner-question table | v0.8 skeleton, review-response table | proposal coordinator |
| PSA handoff | PSA abnormal case has CRM-ready status field | 100% of designed abnormal cases have status / next-action fields in schema | CRM field map | clinical SOP owner + CRM owner |
| PSA follow-up evidence | abnormal follow-up tracking reportability | report can calculate denominator, numerator, pending, unreachable, completed | KPI workbook / dashboard spec | evaluation owner |
| AI intake completion | minimum required previsit fields collected or flagged | >= 90% key fields completed or visibly marked missing in test set | missing-field report | AI workflow owner |
| One-page summary | physician-reference summary timing | <= 60 seconds review target, with actual timed evidence | timed reviewer scorecard | clinical reviewer |
| Source labels | source-label completeness | 100% summary lines or fields show patient / family / staff / ASR-confirmed source | audit sample | data / AI owner |
| Unsafe wording | unsafe clinical wording count | 0 diagnosis, treatment, autonomous triage, queue-priority, automatic EMR phrases | safety checklist | clinical + governance reviewer |
| CRM outsourcing scope | vendor deliverables mapped to acceptance criteria | 100% vendor deliverables map to KPI or governance requirement | vendor-scope table | procurement owner |
| CRM follow-up queue | follow-up queue completeness | all abnormal / follow-up candidates have owner, status, due date, and next action in design | CRM workflow spec | CRM workflow owner |
| CRM contact evidence | contact-attempt traceability | contact attempt, channel, result, and timestamp fields defined before real use | CRM data dictionary | privacy + CRM owner |
| Staff burden | no hidden staff overload | staff workflow review records clicks, duplicate entry, exception load, and training burden | staff-friction worksheet | outpatient workflow owner |
| Training readiness | role-based training material completeness | training checklist for clinician / staff / admin / CRM operator roles | training checklist | training owner |
| Data governance | retention / deletion / access rules named | data route table completed before real-data claim | data governance note | data/privacy owner |
| Cybersecurity | access and audit controls defined | authentication, role access, audit log, incident route fields named | security review note | IT/security owner |
| Procurement / maintenance | post-project maintenance route | maintenance owner, exportability, transition, SLA / support expectation named | procurement / maintenance note | procurement + maintenance owner |
| Annual reporting | checkpoint evidence completeness | yearly report can show output, KPI, issue, correction, next checkpoint | annual evidence packet | evaluation owner |

Budget explanation sentence:

```text
本案 AI 智慧問診與 CRM 經費以細項 KPI 支撐，涵蓋 proposal integration、PSA 異常個案銜接、AI 問診摘要、CRM 外包追蹤、資料品質、staff burden、資安/資料/AI governance、採購驗收與年度 evidence package。每一項支出均對應可查核 KPI、負責 owner、evidence artifact 與年度 checkpoint，使 NT$15,000,000 經費可向主管單位與審查機關清楚說明。
```

## 提案 KPI 建議分組

除非 hospital owner 調整，v0.6 KPI 表建議使用下列列項：

| 類別 | KPI | 目前 baseline | 草案目標 | 為何符合 Health Taiwan |
| --- | --- | --- | --- | --- |
| Workflow burden | Summary read time | measurement scheduled | synthetic reviewer session 中 <= 60 秒 | 直接測試摘要是否節省醫師注意力 |
| Workflow burden | Repeated-question reduction feasibility | measurement scheduled | 定義 baseline and after-workflow count；pilot target pending | 連到 staff/physician workload reduction |
| Information quality | Missing key-field visibility | measurement scheduled | >= 90% synthetic key missing fields flagged with exception log | 改善 visit readiness，同時保留 clinician-owned decision making |
| Information quality | Source-label completeness | partial design | synthetic summary outputs 中 100% | 保留 auditability 與 responsibility |
| Safety | Unsafe wording count | target zero | test set 中 0 | 避免 AI triage / diagnosis overclaim |
| Staff burden | Clinical friction budget | measurement scheduled | approved workflow 符合 click、login、training、exception-load budget | 保護 staff attention，維持 workflow 輕量 |
| Input burden | ASR confirmation safety | optional | 0 unconfirmed ASR content enters summary | 若使用 voice input，確保其可治理 |
| Governance | AI/data/cybersecurity checklist completion | draft only | pilot claim 前 owners and gates named | 範疇三 smart-healthcare credibility 必備 |
| Budget discipline | KPI-to-budget traceability | completion gate active | 100% core budget lines mapped | 每一項預算都連到 deliverable |

## 依 evidence 強度分層的預算項目

| 預算項目 | 目前狀態 | 建議 |
| --- | --- | --- |
| Project coordination / RA | reviewer sessions、KPI capture、governance documents、review-response tracking 可支持 | v0.6 討論配置新臺幣 3,000,000 元，仍需 parent budget owner 確認 |
| Clinician/staff review sessions | summary usefulness 與 friction-budget KPI 可支持 | 作為 evaluation/support activity 納入，並保護 clinician time |
| Web/tablet intake prototype | waiting-room QR/tablet slot 接受後可支持 | workflow slot confirmed 後才納入 |
| Summary-generation implementation | read-time 與 source-label KPI 可支持 | 作為 workflow artifact development 納入 |
| ASR module/service | optional | 僅在 input-burden 或 multilingual-accessibility KPI 明確時納入 |
| Security/data/AI governance review | 範疇三 readiness 必備 | 納入或指定 internal owner |
| FHIR / TW Core IG mapping | future readiness only | 只有 proposal 主張 future interoperability 時才納入 mapping |
| CRM/reminder platform | 2026-06-02 responsibility clarification makes CRM outsourcing active proposal scope for 信義 | 編列前需 SOP、consent / data route、owner、KPI、procurement、security、maintenance path |
| Tablets/equipment | site-readiness gate | site workflow 與 procurement path confirmed 後才編預算 |
| HIS/EMR integration | future integration path | 放在 later governed integration phase |

## 年度 checkpoint 整合

| 階段 | 主要目標 | checkpoints | evidence |
| --- | --- | --- | --- |
| 115 prep | 準備 fundable、safe、format-compliant package | intended use、scope freeze、v0.6 discussion draft、KPI-budget table、governance owner questions、review-response table | v0.6 package and review log |
| 116 design | real deployment 前驗證 workflow fit | workflow slot、question set、summary schema、synthetic walkthrough、staff burden review | clinician/staff scorecards、safety tests |
| 117 limited evaluation | 僅在 governance 與 hospital ownership 成立時 | approved pilot/QI route、baseline and after-workflow measurement、safety monitoring | approved protocol or QI plan、audit logs |
| 118 scale decision | 決定 scale、integrate 或 stop | evidence review、maintenance plan、CRM/interoperability decision、procurement route | final decision record and operations plan |

## 提案敘述片段

預算連到 KPI 時可使用下列文字：

```text
本子計畫之經費編列以可驗收之門診流程改善工作為核心。各工作項目均對應明確 KPI、年度查核點與負責角色；本階段核心經費集中投入降低重複問診、提升門診前資訊完整性、縮短醫師摘要閱讀時間、降低護理/行政額外負擔，以及完成資安、資料與 AI 治理要求的工作。
```

## 不應寫成 KPI 的項目

- AI diagnosis accuracy
- final triage accuracy
- treatment recommendation quality
- automatic EMR completion rate
- mortality or cancer detection improvement
- broad all-department scalability
- current HIS/EMR integration success
- current CRM retention effect

這些超出 current intended use。

## 下一輪 owner 問題

| 問題 | 需要在何時確認 |
| --- | --- |
| 新臺幣 10,000,000 元工作上限是否符合 parent proposal 的正式會計科目與年度拆分？ | official budget table |
| tablets/equipment 是否允許且需要？ | any capital item |
| ASR 是否值得作為 KPI-backed input-burden reduction tool 編列？ | ASR budget |
| cybersecurity/data/AI governance 由誰簽核？ | Scope 3 self-check wording |
| 本案屬於 QI/service improvement path 或 research/IRB path？ | any real-patient pilot claim |
| CRM 外包如何列成 funded service / system scope, and which parts remain activation gates? | v0.8 skeleton and any follow-up/reminder budget |
| FHIR/TW Core IG mapping 現在需要，還是只寫 future-state？ | interoperability budget |
