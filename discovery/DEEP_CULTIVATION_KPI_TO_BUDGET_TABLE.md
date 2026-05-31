# 健康台灣深耕計畫 KPI-To-Budget 對照表

狀態：提案準備工作表

日期：2026-05-29

目的：讓每一項預算都能追溯到 Health Taiwan KPI、工作包、owner 與 evidence artifact。

目前提案包：`DEEP_CULTIVATION_APPLICATION_DRAFT_V0_6.md`

目前預算控制：

```text
三年期。
總經費新臺幣 10,000,000 元。
每一項預算都要對應 KPI、owner、evidence artifact 與年度 checkpoint。
討論版控制在 20 頁以內。
```

## 預算規則

提案使用下列規則：

```text
No KPI, no core budget line.
No owner, no operational claim.
No governance gate, no real patient data or system integration.
```

這可避免提案變成 AI 功能清單，而是維持在可驗收的門診 workflow 改善。

## v0.6 Fill-Out Rule

正式填報前，每一項經費必須補齊：

```text
正式會計科目 / 單價 / 數量 / 年度 / KPI / owner / evidence / procurement note
```

目前的新臺幣 10,000,000 元配置是 discussion allocation。正式會計科目、單價、數量、capital/current 類別、negative-list 檢查與採購門檻，均需由 parent budget owner 或 hospital admin 確認。

## 核心 KPI-To-Budget 對照

| 工作包 | KPI / 查核項目 | 衡量路徑 | 候選預算項目 | 需要的 owner | evidence artifact |
| --- | --- | --- | --- | --- | --- |
| Intended-use freeze | intended use 與 non-use 完成內部核准 | one-page boundary review | coordinator / proposal writing time | proposal owner + clinical reviewer | `INTENDED_USE_FREEZE.md` |
| Demo scope freeze | demo 只包含已核准功能 | scope checklist | coordinator / engineering planning time | proposal owner + engineer | `DEMO_SCOPE_FREEZE.md` |
| Guided intake | synthetic completion rate | 5-10 件合成案例完成 intake -> summary | web/tablet intake development 或 internal engineering time | engineer + clinical reviewer | demo walkthrough / synthetic cases |
| Question governance | 第一版問題集完成核准 | clinician review of question bank | clinical review session / RA coordination | urology lead | question governance table |
| Missing-field repair | key missing fields 經提示後減少 | synthetic 或 pilot-approved comparison | form logic / rules implementation | engineer + clinician | missing-field report |
| One-page summary | clinician summary read time | median read time 目標 <= 60 秒 | summary UI / summarization implementation | engineer + clinician | reviewer scorecard |
| Clinician usefulness | usefulness score | 1-5 clinician rating | reviewer session / RA coordination | clinical lead | scorecard |
| Staff burden | nurse/staff burden acceptable | staff review of time、responsibility、exception handling | staff review session | nursing/outpatient reviewer | burden note |
| Clinical friction budget | 額外 clicks、system switches、training time、exception handling 維持可接受 | walkthrough friction log | usability / human factors review | workflow owner | `CLINICAL_FRICTION_REDUCTION_ANALYSIS.md` plus scorecard |
| Source labeling | 100% summary lines have source category | output inspection | data model / summary schema work | engineer | audit sample |
| Unsafe wording | diagnosis/treatment/triage/EMR-writeback terms 為 0 | safety test set | safety review / test implementation | clinical + governance reviewer | safety checklist |
| ASR confirmation | no unconfirmed ASR enters summary | ASR confirmation test | ASR service/evaluation only if used | engineer + clinical reviewer | ASR feasibility note |
| Auditability | source、question path、version、review status preserved | metadata inspection | audit-log implementation | engineer + IT/security | audit design sample |
| AI governance | AI governance checklist completed | self-check completion | governance review time | AI governance owner | governance checklist |
| Cybersecurity governance | cybersecurity checklist completed | self-check completion | security review / hardening | IT/security owner | cybersecurity checklist |
| Data governance | data governance checklist completed | self-check completion | privacy/data governance review | data/privacy owner | data governance checklist |
| Future interoperability readiness | 若主張資料交換，需有 FHIR / TW Core IG mapping | mapping review | standards mapping only if needed | IT/data owner | future readiness note |
| Future CRM readiness | 若重啟 CRM，需有 SOP owner 與 workflow | SOP review | no implementation budget unless reopened | service owner | future CRM SOP draft |
| Annual checkpoint reporting | checkpoint table maps deliverables to dates | proposal table review | coordinator / PM time | proposal owner | `DEEP_CULTIVATION_ANNUAL_CHECKPOINT_TABLE.md` |

## 預算項目與成立條件

| 預算項目 | 只有在下列條件成立時可列入 | 下列情況不應列入 |
| --- | --- | --- |
| Web / tablet intake development | guided intake 與 completion KPI 是核心 | workflow slot 尚未確認 |
| ASR service or module | input burden 或 language-accessibility KPI 明確 | ASR 只是 novelty feature |
| LLM / summary generation | clinician-review summary KPI 成立 | summary 暗示診斷、治療或 EMR automation |
| Research assistant / coordinator | review sessions、KPI capture、governance documentation 需要協調 | RA 只是補 unclear ownership |
| Clinician / staff review session support | scorecards 與 workload evaluation 已規劃 | clinicians 被要求做 routine labeling work |
| Security review | APP/API/ASR/data handling 或 pilot readiness 被主張 | demo 維持 purely static and synthetic |
| Data governance support | data retention、access、de-identification 或 real-data future 被討論 | 只使用 synthetic examples 且無 future data claim |
| Vendor / outsourcing | scope、acceptance criteria、procurement path、ownership 與 KPI 都已定義 | vendor 被用來遮蔽 undefined system |
| Equipment / tablets | waiting-room tablet workflow 已確認 | patient flow 仍是推測 |
| CRM platform / reminder module | CRM phase 以 SOP、owner、consent、privacy 與 KPI 正式重啟 | CRM remains parked |
| Interoperability mapping | future FHIR / TW Core IG readiness 被要求 | proposal 未經核准即主張 current HIS/EMR integration |

## v0.6 三年經費討論配置

此配置依 2026-05-29 吳老師預算指示建立，只應由 parent budget owner 調整。

| 預算項目 | 第一年 | 第二年 | 第三年 | 合計 | 必備 KPI |
| --- | ---: | ---: | ---: | ---: | --- |
| Proposal coordination、PM、RA、KPI evidence | 900,000 | 1,050,000 | 1,050,000 | 3,000,000 | 20 頁討論稿、annual KPI evidence、checkpoint reporting |
| Intake / summary workflow 與 CRM-ready field design | 1,250,000 | 650,000 | 300,000 | 2,200,000 | summary read time、source label completeness、missing-field visibility |
| Clinician、nurse 與 outpatient workflow reviewer sessions | 400,000 | 400,000 | 300,000 | 1,100,000 | clinician usefulness、staff-friction score、workflow-slot decision |
| Security、privacy、AI/data governance、auditability | 450,000 | 300,000 | 150,000 | 900,000 | governance checklist、unsafe wording count、audit trail readiness |
| Evaluation、baseline、QI/IRB preparation、limited pilot evidence | 250,000 | 400,000 | 350,000 | 1,000,000 | baseline、approved workflow measurement、final evidence report |
| Conditional equipment / ASR / intake station support | 450,000 | 200,000 | 50,000 | 700,000 | ASR confirmation safety、workflow slot feasibility |
| Training、documentation、dissemination、review-response package | 150,000 | 100,000 | 250,000 | 500,000 | training completion、review-response readiness |
| Administration and contingency within legal accounting rules | 150,000 | 100,000 | 350,000 | 600,000 | expense-to-KPI traceability maintained |
| Total | 4,000,000 | 3,200,000 | 2,800,000 | 10,000,000 | 100% budget-to-KPI mapping |

## 正式送件前預算欄位

| 預算項目 | 正式會計科目 | 單價 | 數量 | 年度 | KPI | owner | evidence | procurement note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Proposal coordination、PM、RA、KPI evidence | 待正式會計科目確認 | 待確認 | 待確認 | 第 1-3 年 | 20 頁討論稿、annual KPI evidence、checkpoint reporting | proposal coordinator / evaluation owner | proposal file、KPI workbook、checkpoint report | confirm personnel / service category |
| Intake / summary workflow 與 CRM-ready field design | 待正式會計科目確認 | 待確認 | 待確認 | 第 1-3 年 | summary read time、source label completeness、missing-field visibility | engineering owner | summary schema、walkthrough、audit sample | confirm internal / vendor / hybrid route |
| Clinician、nurse 與 outpatient workflow reviewer sessions | 待正式會計科目確認 | 待確認 | 待確認 | 第 1-3 年 | clinician usefulness、staff-friction review、workflow-slot decision | clinical / workflow owners | reviewer scorecards、meeting records | confirm whether reviewer support can be budgeted |
| Security、privacy、AI/data governance、auditability | 待正式會計科目確認 | 待確認 | 待確認 | 第 1-3 年 | governance owner named、unsafe wording count、audit trail readiness | IT/security、AI/data governance | governance checklist、security review note | vendor security required if outsourced |
| Evaluation、baseline、IRB/QI preparation、limited pilot evidence | 待正式會計科目確認 | 待確認 | 待確認 | 第 1-3 年 | baseline、approved workflow measurement、final evidence report | evaluation、IRB/QI owners | baseline worksheet、protocol / QI note、evaluation report | real patient-data route pending |
| Conditional equipment / ASR / intake station support | 待正式會計科目確認 | 待確認 | 待確認 | 第 1-3 年 | ASR confirmation safety、workflow slot feasibility | budget / workflow owners | ASR confirmation test、site-readiness note | tablets、microphones 或 ASR service 需通過 procurement 與 security review |
| Training、documentation、dissemination、review-response package | 待正式會計科目確認 | 待確認 | 待確認 | 第 1-3 年 | training completion、review-response readiness | proposal owner | training record、review-response table | only if parent owner funds training / dissemination |
| Administration and contingency within legal accounting rules | 待正式會計科目確認 | 待確認 | 待確認 | 第 1-3 年 | expense-to-KPI traceability maintained | budget owner | budget traceability audit | negative-list and accounting-category check required |

## KPI 細項表

| KPI | baseline / 目前狀態 | 草案目標 | 衡量方法 | 目前 evidence 層級 |
| --- | --- | --- | --- | --- |
| Summary read time | 尚未量測 | <= 60 秒 design target；回報 actual | synthetic reviewer timing | draft artifact |
| Clinician usefulness | 尚未量測 | median >= 4/5 or revise decision | 3-5 clinician scorecards | draft artifact |
| Nurse/staff burden | 尚未量測 | acceptable burden threshold documented | staff walkthrough | draft artifact |
| Clinical friction budget | 尚未量測 | no unacceptable extra clicks/logins/training/exception handling | friction log | draft artifact |
| Synthetic flow completion | 尚未正式計數 | 完成 5-10 件 synthetic cases | demo run and checklist | draft artifact |
| Missing-field flagging | 尚未量測 | >= 90% on synthetic review 或列出 failures | manual review | draft artifact |
| Source-label completeness | partial design | 100% in synthetic outputs | output inspection | draft artifact |
| Unsafe wording count | target zero | 0 in safety test set | safety test | draft artifact |
| ASR confirmation | 尚未量測 | 0 unconfirmed ASR content enters summary | ASR confirmation test | optional |
| Governance checklist completion | draft only | AI/data/cybersecurity owners and gates listed | checklist review | draft artifact |
| KPI-to-budget traceability | 尚未完成 | 100% core budget lines mapped to KPI | table audit | draft artifact |

## 預算敘述模板

提案使用下列句型：

```text
因本子計畫需驗證門診前問診流程是否能降低重複問診與臨床工作摩擦，故編列[工作項目]支援[系統/流程/評估]。該項經費對應 KPI 為[指標]，衡量方式為[方法]，由[負責角色]於[年度查核點]提供[證據文件]。
```

範例：

```text
因本子計畫需驗證醫師是否能於 60 秒內閱讀一頁式覆核摘要，故編列系統摘要畫面與 reviewer session 相關工作。該項經費對應 KPI 為「醫師摘要可讀時間」與「醫師 useful rating」，衡量方式為合成案例 reviewer scorecard，由泌尿科臨床團隊與計畫協調人於第一年度查核點提供評估紀錄。
```

## Red flags

下列情況不應申請預算項目：

- 沒有 KPI
- 沒有 owner
- 在治理前就需要 real patient data
- 暗示 autonomous clinical decision-making
- 把工作轉給護理端，卻未量測 burden
- 新增臨床人員必須使用的系統，但沒有 workflow proof
- 主要是 AI novelty，而不是 clinical friction reduction

## 目前待確認事項

| 待確認項目 | 需要來源 |
| --- | --- |
| 工作預算上限 | v0.6 先設定為新臺幣 10,000,000 元；parent proposal owner 可調整正式會計科目與年度拆分 |
| 人事類別與可支用費率 | official funding documents / hospital admin |
| tablets/equipment 是否允許且有用 | hospital workflow owner |
| ASR 是否有 funded KPI | clinical + proposal owner |
| vendor work 是否允許 | procurement owner |
| CRM 是否重啟 | service owner + governance owner |
| 本子計畫是否需要 FHIR / TW Core IG mapping | IT/data governance owner |
