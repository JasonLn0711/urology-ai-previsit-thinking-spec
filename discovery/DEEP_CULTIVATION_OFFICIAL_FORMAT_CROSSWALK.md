# 健康台灣深耕計畫正式格式對照表

狀態：提案撰寫控制文件

日期：2026-05-20

2026-06-02 official meeting minutes + 2026-06-19 owner update:

```text
Current writing target is AI-only: 泌尿科門診前問診與醫師覆核摘要支持系統.
Use `exports/nycu-ai-previsit-proposal-item-definitions-2026-06-19.md` for
current official-section definitions. The parent 信義 AI 智慧問診 allocation is
about NT$15M and includes CRM; this crosswalk maps the Jason / 陽明交大
AI-only package at three-year NT$10M.
```

目的：將目前泌尿科門診前問診 deep-cultivation 草稿包對應到 Health Taiwan 正式提案格式，讓下一版可以寫成可申請經費的醫院 workflow 提案，而不是研究 memo 或 AI demo 說明。

## 來源依據

本 repo 內已歸檔的正式格式來源：

- `../records/2026-07-01/sources/health-taiwan-stage2-application-guidance-116-118-ai-agent-readable.md`
- `../records/2026-05-19/policy-documents/application/health-taiwan-phase1-proposal-format-114-115-0909.docx`
- `../records/2026-05-19/policy-documents/application/health-taiwan-phase1-application-guidelines.pdf`
- `../records/2026-05-19/policy-documents/execution/category3-smart-healthcare-governance-lazy-guide-1140702.pdf`
- `../records/2026-05-19/policy-documents/budget/budget-preparation-notes-lazy-guide-1140701.pdf`
- `../records/2026-05-19/policy-documents/budget/`
- `../records/2026-05-19/policy-documents/qa/`

重要提醒：

```text
本對照表使用本地 114-115 官方歸檔作為撰寫骨架。
2026-07-01 保存的 116-118 申請說明 source 應作為第二階段申請模式、
經費上限、KPI / 查核點 / 預算串接、負面表列與 governance 檢核的
目前 planning reference。
正式院內流通或送件前，parent proposal owner 必須確認最新 live template、申請階段、院內指引與行政流程。
```

## 正式提案順序

已歸檔的正式提案格式使用下列順序：

1. Cover page
2. Table of contents
3. `壹、申請單位自我檢核項目表`
4. `貳、計畫概要`
5. `參、申請單位簡介`
6. `肆、計畫規劃`
7. `伍、效益評估`
8. `陸、出國計畫書`
9. `柒、經費規劃`
10. `捌、人力配置表`
11. `玖、其他`
12. `拾、公職人員利益衝突迴避自主檢核表`
13. `拾壹、未有重複申請計畫之聲明切結書`
14. `拾貳、參與計畫同意書`
15. `拾參、審查意見回復表`

## 對照表

| 正式章節 | 正式格式期待內容 | 目前材料 | 缺口 | 下一步撰寫動作 |
| --- | --- | --- | --- | --- |
| Cover page | project name、county/city、application mode、categories、applicant/co-applicant institutions、institution codes、budget、execution period、PI、contact | `DEEP_CULTIVATION_APPLICATION_DRAFT_V0_6.md` cover/package fields and 2026-06-02 official minutes | applicant、mode、institution codes、parent proposal name 尚未確認；類別設計為主打 `範疇三`、副支援 `範疇一`；parent AI 智慧問診 allocation 約 NT$15M 含 CRM；Jason / 陽明交大 AI-only working budget 為每年 NT$10,000,000，三年合計 NT$30,000,000 | 保留 placeholder；Word transfer 前詢問 hospital owner，並明確分開 parent CRM allocation 與 AI-only package |
| TOC | official auto-generated section order | Markdown 不需另維護 | final Word/PDF step | 本 repo 不手動維護 |
| `壹、自我檢核` | eligibility、official format、COI forms、no duplicate funding、participation consent、only one application mode | v0.2 preflight、MOHW compliance rubric | legal/administrative facts pending | 加入 applicant-owner checklist，institutional blanks 留白 |
| `貳、計畫概要` | 簡明計畫摘要與問題 framing | v0.6 one-page positioning、clinical friction analysis、system positioning | summary still needs parent-owner approval | 使用 v0.6 摘要，聚焦範疇三 smart-healthcare workflow 與範疇一 staff-burden reduction |
| `參、申請單位簡介` | applicant/co-applicant institutional background | role table only | institutional text pending | 提供 role-specific placeholder，不捏造 institution prose |
| `肆、計畫規劃` | 四大範疇計畫內容、workflow、工作項目、deliverables | 2026-06-19 expert-review packet、proposal item definitions、proposal writing guide、intended-use freeze、demo-scope freeze | workflow slot 與 owner 仍需 hospital confirmation | 結構寫成：門診前 / 候診中低摩擦症狀蒐集 -> 來源標記（source label）/ 缺漏欄位 -> 一頁式醫師覆核摘要 -> 醫師 accept / edit / ignore / return -> KPI 評估 |
| `伍、效益評估` | KPI table by category、baseline/current data、target、annual checkpoints | v0.6 KPI table、KPI-to-budget table、annual checkpoint table | baselines still draft | 使用可驗收 targets：summary read time <= 60 秒、source label 100%、unsafe wording = 0、missing-field visibility >= 90%、clinician usefulness >= 4/5、governance owner named |
| `陸、出國計畫書` | 只有在 scope 2 training-related overseas activity 編列時使用 | not applicable | 必須明確標示不適用 | 除非新增 overseas training plan，否則寫 N/A |
| `柒、經費規劃` | 分年經費總表、budget category details、scope allocation、capital/personnel/business categories | v0.6 budget table, KPI-to-budget table, 2026-06-02 official minutes | NT$10,000,000 AI-only discussion allocation 已設定；parent NT$15M AI/CRM relation、formal accounting category、unit price、quantity、procurement note 仍需確認 | 每列補齊 formal accounting category / unit price / quantity / year / KPI / owner / evidence / procurement note；CRM 經費另列 parent / other-team workstream |
| `捌、人力配置表` | subsidized-unit personnel、current post、work role | role table | named personnel pending | 保留 role-based table，姓名標示 pending |
| `玖、其他` | attachments、quotations、cooperation materials、figure/table list | repo inclusion recommendation、governance checklist、demo/reviewer artifacts | attachment packet 尚未選定 | 列出 recommended appendices 與 do-not-attach items |
| `拾、利衝自主檢核` | official signed form | none | 必須由 institution owner 處理 | 標示 parent owner action |
| `拾壹、未重複補助切結` | signed statement | none | 必須由 institution owner 處理 | 標示 parent owner action |
| `拾貳、參與計畫同意書` | partner consent forms | MOU/partner questions in meeting notes | partner list pending | 建立 partner decision question，不捏造 partner commitment |
| `拾參、審查意見回復` | reviewer comments、response、revision location | scoring rubric and review response style | review 後才需要 | 先準備 empty response table |

## 目前草稿包路由

正式格式撰寫時使用下列文件：

- Current 2026-06-19 expert-review packet：`exports/nycu-ai-previsit-expert-review-packet-2026-06-19.md`
- Current proposal item definitions：`exports/nycu-ai-previsit-proposal-item-definitions-2026-06-19.md`
- Historical v0.7 discussion draft：`DEEP_CULTIVATION_APPLICATION_DRAFT_V0_7.md`
- Historical v0.6 fill-out discussion draft：`DEEP_CULTIVATION_APPLICATION_DRAFT_V0_6.md`
- Prior v0.5 discussion draft：`DEEP_CULTIVATION_APPLICATION_DRAFT_V0_5.md`
- Precedent-integrated baseline：`DEEP_CULTIVATION_APPLICATION_DRAFT_V0_4.md`
- Official-format crosswalk：`DEEP_CULTIVATION_OFFICIAL_FORMAT_CROSSWALK.md`
- KPI / budget / annual checkpoint integration: `DEEP_CULTIVATION_KPI_BUDGET_ANNUAL_INTEGRATION_TABLE.md`
- Intended-use freeze: `INTENDED_USE_FREEZE.md`
- Demo-scope freeze: `DEMO_SCOPE_FREEZE.md`
- Clinical friction reduction analysis: `CLINICAL_FRICTION_REDUCTION_ANALYSIS.md`
- Governance checklist: `DEEP_CULTIVATION_GOVERNANCE_CHECKLIST.md`
- Scoring rubric: `DEEP_CULTIVATION_SCORING_RUBRIC.md`
- MOHW compliance rubric: `DEEP_CULTIVATION_MOHW_COMPLIANCE_RUBRIC.md`

仍有參考價值但已被取代的舊草稿：

- `DEEP_CULTIVATION_APPLICATION_DRAFT_V0_3.md`
- `DEEP_CULTIVATION_APPLICATION_DRAFT_V0_2.md`
- `DEEP_CULTIVATION_SUBPROJECT_UROLOGY_PREVISIT_V0_1.md`

## Writing Principles For v0.6

### 1. Write as a hospital workflow proposal

Use:

```text
門診前問診與醫師覆核摘要支持
降低重複問診與文書準備負擔
低摩擦導入既有門診流程
```

Avoid:

```text
AI triage
AI diagnosis
自動風險分級
自動寫入 EMR
全院 chatbot
```

### 2. Make staff burden the central benefit

Every major paragraph should answer:

```text
這會減少哪一類醫療人員負擔？
醫師、護理師、櫃台或行政人員需要多做什麼？
新增負擔是否小於被移除的舊負擔？
```

### 3. Keep technology subordinate to workflow

Correct order:

```text
clinical workflow problem
-> low-friction process insertion
-> clinician-reviewable artifact
-> measurable KPI
-> governance and budget
-> AI / ASR / implementation method
```

Wrong order:

```text
AI model
-> possible use cases
-> later find a hospital process
```

### 4. Mark administrative unknowns explicitly

Do not invent:

- applicant identity
- application mode
- official accounting category split for the NT$10,000,000 working ceiling
- matching-fund ratio
- exact execution period
- institution codes
- signatories
- procurement route
- real-patient pilot approval

院方確認前，使用 `Pending parent proposal owner` 標示。

## Immediate Questions For Hospital / PI Owner

| Question | Why it matters |
| --- | --- |
| Is this a continuation, internal supplement, or future second-stage / new proposal package? | determines template, period, and section wording |
| Who is the formal applicant and PI? | required cover page and self-check |
| What is the official parent proposal name? | determines whether this is 子計畫二 or an appendix |
| Is the first workflow slot `報到後 / 候診中 / QR code or tablet` acceptable? | determines plan feasibility |
| Are staff allowed to help patients complete intake? | determines staffing and burden KPI |
| v0.6 討論稿是否現在轉入 Word template？ | 決定下一個 artifact format |
| Does the NT$10,000,000 working ceiling need a different annual or accounting-category split? | prevents fake budget lines |
| Who owns AI, cybersecurity, data governance, and privacy sign-off? | required for Scope 3 credibility |
| Is CRM follow-up reopened or parked? | prevents scope drift |
| Does `醫師覆核用 SOAP 架構參考摘要` sound safe? | avoids EMR automation overclaim |

## Ready / Not Ready Gate

符合下列條件時，提案可進入 internal clinical/admin review：

- v0.6 discussion draft exists
- official-format crosswalk exists
- KPI-budget-checkpoint integration table exists
- intended use and demo scope are frozen
- governance checklist names required owners
- open administrative fields are visible
- all unsafe claims are removed

在下列事項完成前，提案還不適合 external 或 formal submission：

- latest official template is confirmed
- institutional applicant and mode are confirmed
- budget is itemized by official category
- COI / duplicate funding / consent forms are handled by the institution
- governance self-checks have owner review
- parent proposal owner confirms wording and attachments
