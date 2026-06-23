# 健康台灣深耕計畫年度 checkpoint 表

狀態：提案準備 checkpoint 表

日期：2026-05-29

2026-06-02 official meeting minutes + 2026-06-19 owner update + 2026-06-23
official meeting minutes:

```text
信義母案目前整合 PSA 篩檢與智慧問診 NT$15,000,000、CRM 系統
NT$15,000,000、信義門診部碳盤查 NT$7,500,000。
目前 Jason / 陽明交大提案包為 AI-only expert-review package，三年 NT$10,000,000。
本表若提到 CRM，只保留為 parent / other-team 工作，不作本案 checkpoint。
2026-07-07 09:30 是華山、信義門診部合併版計畫書審閱 gate。
```

目前提案包：`exports/nycu-ai-previsit-expert-review-packet-2026-06-19.md`

目的：把提案轉成可追蹤、可回報，且能連到 KPI 與預算的年度 checkpoint。

## 期程提醒

2026-05-20 查核過的官方公開頁面顯示：

```text
第一階段：自 114 年核定日起至 115 年底
第二階段：116-118 年
第二階段新徵件：預期 115 年第 4 季
```

本表必須依 parent proposal 的實際申請路徑調整。

## Checkpoint 邏輯

每個 checkpoint 都要回答：

1. 產出哪一個 artifact？
2. 支援哪一個 KPI？
3. 由誰擔任 owner？
4. 哪一份 evidence 能證明完成？
5. 是否降低臨床摩擦，同時維持安全邊界？

## 115 年 Q2-Q4：提案準備與 evidence package

若團隊正在準備院內討論稿、延續規劃或第二階段 readiness，使用本段。

| checkpoint | deliverable | KPI / gate | evidence | 需要的 owner |
| --- | --- | --- | --- | --- |
| 2026-07-07 合併版審閱 | 華山、信義門診部合併版計畫書，含 KPI、預算、合作單位、採購 / 資產類別與 owner | merged-plan review readiness | `../records/2026-06-23/deep-cultivation-2026-07-07-integration-schedule.md` | parent proposal owner |
| 合作單位洽談 | 友好單位、合作內容、簽約或合作文件路徑 | partner readiness | partner route note | Huashan + Xinyi teams |
| 預算 resilience | NT$37.5M annual cap、50-60% review-cut scenario、30% 硬體 / 無形資產控制 | budget review readiness | budget-resilience table | budget owner |
| 軟體租賃 / 健康艙買斷分類 | 軟體 service / license / rental 與 Health Cabin purchase category | asset-category readiness | procurement / asset-category note | IT/procurement + Health Cabin owners |
| 申請路徑釐清 | 申請單位 / 申請模式 / parent proposal 關係說明 | 正式送件路徑 | 一頁 owner note | parent proposal owner |
| Intended use 凍結 | intended use 與 non-use statement | 邊界清楚 | `INTENDED_USE_FREEZE.md` | clinical + proposal owner |
| Demo scope 凍結 | demo 納入 / 排除範圍 | scope control | `DEMO_SCOPE_FREEZE.md` | proposal + engineering owner |
| 合成案例選定 | 3-5 件合成案例 | review readiness | case list | clinician reviewer |
| 醫師摘要樣本 | 一頁式摘要 mock | read-time KPI | sample output | engineer + clinician |
| 臨床摩擦計畫 | friction budget 與衡量計畫 | 醫療人員負擔降低 | `CLINICAL_FRICTION_REDUCTION_ANALYSIS.md` | workflow owner |
| 治理 checklist 草案 | AI/data/cybersecurity checklist | 範疇三 readiness | `DEEP_CULTIVATION_GOVERNANCE_CHECKLIST.md` | governance owners |
| KPI-to-budget 草案 | 帶有預算邏輯的 KPI 表 | budget traceability | `DEEP_CULTIVATION_KPI_TO_BUDGET_TABLE.md` | budget owner |
| v0.6 提案草稿 | 2026-06-02 填報討論稿，含類別設計、子計畫三骨架轉用、KPI targets、預算填報欄位與前置治理 | application readiness | `DEEP_CULTIVATION_APPLICATION_DRAFT_V0_6.md` | proposal writer |
| owner 表準備 | clinical、workflow、IT/security、AI/data governance、IRB/QI、evaluation、budget 與 coordination 角色可見 | 責任清楚 | v0.6 owner 與責任表 | parent proposal owner |
| Review-response 表準備 | 預期審查問題與回覆方向 | external review readiness | v0.6 review-response table | proposal writer |
| v0.4 baseline 保留 | 先前正式格式紀律保留作為脈絡 | traceability | `DEEP_CULTIVATION_APPLICATION_DRAFT_V0_4.md` | proposal writer |
| 參考提案已分析 | 子計畫三 PDF 已歸檔並分析 | 借用骨架但不 scope drift | `../records/2026-05-29/xinyi-outpatient-proposal-reference/README.md` | proposal writer |

## 116 年：Governed design 與 pilot 準備

若本子計畫進入 116-118 年期，使用本段作為第一個完整執行年度形狀。

| checkpoint | deliverable | KPI / gate | evidence | 需要的 owner |
| --- | --- | --- | --- | --- |
| Workflow slot 確認 | 報到 / 候診 / 覆核流程確認 | adoption feasibility | workflow map 與會議紀錄 | clinic workflow owner |
| 題庫核准 | 第一版問題集 | 臨床適切性 | clinician-signed 或 recorded review | urology lead |
| Summary schema v1 | 一頁式摘要與 source label | read-time 與 source-label KPI | summary template | engineer + clinician |
| Safety wording test | unsafe wording count = 0 in test set | safety boundary | safety test report | clinical + governance reviewer |
| Synthetic walkthrough 完成 | 5-10 件合成案例 | demo evidence | walkthrough report | engineer |
| Staff burden review | nurse/staff review | burden acceptability | scorecard / meeting note | nursing/outpatient reviewer |
| Governance owner assignment | AI/security/data owners named | governance readiness | owner table | hospital administration |
| IRB/QI determination route | research vs QI/service decision pathway | real-data readiness | governance note | IRB/governance support |
| 預算定稿 | budget maps to KPI | budget traceability | budget table | budget owner |

## 117 年：通過治理後的 limited workflow evaluation

僅在治理核准與院內 ownership 成立後使用。

| checkpoint | deliverable | KPI / gate | evidence | 需要的 owner |
| --- | --- | --- | --- | --- |
| Pilot protocol 核准 | governed pilot 或 QI workflow | legal/ethical gate | approved document | hospital owner |
| Access and data controls 啟用 | role-based access、retention、deletion | data/security readiness | security review record | IT/security owner |
| Baseline workflow captured | current repeated-question / burden baseline | comparison readiness | baseline report | evaluator |
| Limited workflow test | 已核准的非急性門診流程 | completion and burden KPI | pilot log 或 walkthrough log | clinic owner |
| Clinician review measured | read time、usefulness、edit/reject status | summary usefulness | scorecard / audit log | clinician reviewer |
| Nurse burden measured | staff intervention time and burden | friction budget | staff log / scorecard | nursing reviewer |
| Safety monitoring completed | unsafe wording、confusion、incidents | safety KPI | safety monitoring report | governance owner |
| Revise/narrow/continue decision | 書面決策 | stage gate | decision record | PI / proposal owner |

## 118 年：Scale-up 或 integration-readiness 決策

僅在前期 evidence 支持延續時使用。

| checkpoint | deliverable | KPI / gate | evidence | 需要的 owner |
| --- | --- | --- | --- | --- |
| Evidence review | workflow value 與 burden reduction review | continuation decision | evaluation report | PI + hospital owner |
| Scope expansion decision | 同科擴大或跨科 readiness | no scope drift | decision record | governance committee |
| CRM decision | reopen 或 keep parked | service continuity | SOP 與 owner decision | service owner |
| Interoperability decision | 若需要，完成 FHIR / TW Core IG mapping | integration readiness | mapping note | IT/data owner |
| Procurement decision | internal / outsourced / hybrid path | sustainability | procurement plan | admin/procurement |
| Maintenance plan | post-project owner 與更新週期 | sustainability | operations plan | hospital owner |
| Final safety/governance review | 無未解責任缺口 | closeout readiness | governance report | AI/data/security owners |

## 年度 KPI 摘要

| 年度 / 階段 | 主要 KPI focus | 不應宣稱 |
| --- | --- | --- |
| 115 prep | boundary、evidence package、proposal format、governance preflight、owner table、review-response readiness | clinical effectiveness |
| 116 design | workflow fit、synthetic review、staff burden、summary readability | real-world outcome improvement |
| 117 limited evaluation | approved workflow value、friction reduction、safety monitoring | broad scalability before evidence |
| 118 scale readiness | sustainability、integration readiness、maintenance ownership | production integration without governance |

## Checkpoint 回報寫法

使用具體寫法：

```text
完成 5 件合成案例 walkthrough，所有輸出均保留來源標記，未出現診斷、治療、自動分流或 EMR 寫入語句。
```

避免模糊寫法：

```text
AI 系統已提升效率。
```

## 待確認事項

| 項目 | 最終提案前需要 |
| --- | --- |
| 實際申請階段 | parent proposal owner |
| 正式年度標籤 | parent proposal owner |
| 新臺幣 10,000,000 元工作上限的正式會計科目與年度拆分 | hospital admin / parent budget owner |
| 目標 reviewer 人數 | clinical owner |
| 是否允許 real pilot | IRB/governance owner |
| 是否納入 CRM / future interoperability | service + IT owner |
