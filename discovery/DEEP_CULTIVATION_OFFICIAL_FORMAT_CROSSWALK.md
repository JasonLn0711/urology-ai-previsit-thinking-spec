# 健康台灣深耕計畫正式格式對照表

狀態：提案撰寫控制文件

日期：2026-05-20；current formal-format source update：2026-07-14

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

- `../records/2026-07-14/sources/health-taiwan-phase2-application-instructions-116-118-ai-agent-readable-verified-2026-07-07.md`
- `../records/2026-07-14/sources/health-taiwan-phase2-application-template-and-attachments-116-118-ai-agent-readable-verified-2026-07-13.md`
- `../records/2026-07-01/sources/health-taiwan-stage2-application-guidance-116-118-ai-agent-readable.md`
- `../records/2026-07-13/sources/health-taiwan-phase2-solicitation-briefing-116-118-verified-2026-07-13.md`
- `../records/2026-05-19/policy-documents/application/health-taiwan-phase1-proposal-format-114-115-0909.docx`
- `../records/2026-05-19/policy-documents/application/health-taiwan-phase1-application-guidelines.pdf`
- `../records/2026-05-19/policy-documents/execution/category3-smart-healthcare-governance-lazy-guide-1140702.pdf`
- `../records/2026-05-19/policy-documents/budget/budget-preparation-notes-lazy-guide-1140701.pdf`
- `../records/2026-05-19/policy-documents/budget/`
- `../records/2026-05-19/policy-documents/qa/`

重要提醒：

```text
2026-07-14 保存的 attach1／attach2 verified copies 是目前 116-118 第二階段
formal instructions + live template working layer。2026-07-13 verified 說明會
source 提供 briefing interpretation；114-115 官方歸檔提供歷史 traceability。
正式院內流通與送件由 parent proposal owner 進一步確認 live platform、院內
指引、簽章流程與任何 7/16 後續修正。
```

## 正式提案順序

已歸檔的正式提案格式使用下列順序：

1. Cover page
2. `計畫摘要`（500 字內）
3. `第一階段具體成效`（延續型計畫適用）
4. `計畫概要`
5. `申請單位簡介`
6. `計畫規劃`
7. `效益評估`
8. `出國計畫書`（範疇二適用）
9. `經費規劃`
10. `人力配置表`
11. `其他`
12. `公職人員利益衝突迴避自主檢核表`
13. `計畫申請聲明暨未重複補助切結書`
14. `參與計畫同意書`
15. `智慧醫療整體執行情形聲明書`（範疇三適用）
16. `B2 類社區醫療群申請確認切結書`（條件式）

## 對照表

| 正式章節 | 正式格式期待內容 | 目前材料 | 缺口 | 下一步撰寫動作 |
| --- | --- | --- | --- | --- |
| Cover page | project name、county/city、application mode、categories、applicant/co-applicant institutions、institution codes、budget、execution period、PI、contact | `DEEP_CULTIVATION_APPLICATION_DRAFT_V0_6.md` cover/package fields and 2026-06-02 official minutes | applicant、mode、institution codes、parent proposal name 尚未確認；類別設計為主打 `範疇三`、副支援 `範疇一`；parent AI 智慧問診 allocation 約 NT$15M 含 CRM；Jason / 陽明交大 AI-only working budget 為每年 NT$10,000,000，三年合計 NT$30,000,000 | 保留 placeholder；Word transfer 前詢問 hospital owner，並明確分開 parent CRM allocation 與 AI-only package |
| `計畫摘要` | 必要性、核心作法、關鍵效益，500 字內 | v0.6 one-page positioning、clinical friction analysis、system positioning | summary needs parent-owner approval and 500-character check | 聚焦範疇三 workflow、範疇一 staff-burden outcome 與可驗證效益 |
| `第一階段具體成效` | 延續型填寫質化／量化成果、1-2 項圖文亮點、問題與精進 | historical evidence records | continuation/new-project classification pending | 先確認類型；延續型由 parent owner 提供 first-stage verified evidence |
| `計畫概要` | 辦理依據、現況及問題分析 | v0.6 positioning + policy records | parent narrative approval pending | 以實際門診工作流與 evidence-backed burden baseline 建立問題鏈 |
| `申請單位簡介` | applicant/co-applicant institutional background | role table only | institutional text pending | 由 institution owner 提供正式文字與機構事實 |
| `計畫規劃` | 依範疇列出 116-118 分年目標、策略、方法與成效 | expert-review packet、item definitions、writing guide、scope freezes | workflow slot 與 owner 仍需 hospital confirmation | 結構寫成低摩擦症狀蒐集 -> source label / missing fields -> clinician-review summary -> human review -> KPI evidence |
| `效益評估` | 範疇、KPI、基準定義、115 現況、116／117／118 達成值 | KPI-to-budget table、annual checkpoint table | baselines still draft | 鎖定公式、資料源、frequency、owner 與公開／去識別審核 |
| `出國計畫書` | 僅範疇二填列，並受 20% 經費控制 | current AI-only package has no owned overseas-training work | scope applicability confirmation | 由 parent owner 確認適用性；範例日期／地點／匯率保持 EXAMPLE |
| `經費規劃` | 分年經費、各範疇配置、科目、單價、數量、KPI linkage | v0.6 budget + KPI-to-budget table | working ceiling and official itemization need budget-owner confirmation | 每列補齊 category / unit / quantity / year / KPI / owner / evidence / procurement note；capital ratio <= 30% |
| `人力配置表` | 補助單位人員、現職與工作角色 | role table | named personnel pending | 保留 role-based fields，交由 institution owner 填入核實姓名／職稱 |
| `其他` | quotations、cooperation materials、supporting artifacts | repo inclusion recommendation、governance checklist | attachment packet pending | 建立正式 attachment manifest 與 page/file-size check |
| `利衝自主檢核` | official form and conditional identity disclosure | owner gate | applicant identity review pending | institutional admin 依身分與法規完成 |
| `申請聲明暨未重複補助切結` | signed application, no-duplicate-funding and result obligations | funding-separation notes | signature pending | parent owner 完成 work-package/cost dedup matrix 後簽署 |
| `參與計畫同意書` | each partner institution consent | partner route notes | partner list pending | named partner owner 完成正式同意與簽章 |
| `智慧醫療整體執行情形聲明` | 範疇三 conditional attachment | governance checklist | AI/data/security/FHIR evidence owner review pending | 完成 governance evidence manifest 與 responsible-owner sign-off |
| `B2 切結書` | 診所／衛生所主提 B2 時適用 | application-mode question | mode pending | 由 parent owner 確認 application mode 後 activation |

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

目前已完成的 format-source gate：

- 116-118 formal application instructions copied and verified
- 116-118 live proposal template and attachments copied and verified
- formal-format crosswalk updated to current fields

符合下列條件時，提案可進入 internal clinical/admin review：

- v0.6 discussion draft exists
- official-format crosswalk exists
- KPI-budget-checkpoint integration table exists
- intended use and demo scope are frozen
- governance checklist names required owners
- open administrative fields are visible
- all unsafe claims are removed

External / formal submission readiness 由下列 owner gates共同建立：

- current attach2 fields are transferred into the parent working DOCX
- institutional applicant and mode are confirmed
- budget is itemized by official category
- COI / duplicate funding / consent forms are handled by the institution
- governance self-checks have owner review
- parent proposal owner confirms wording and attachments
