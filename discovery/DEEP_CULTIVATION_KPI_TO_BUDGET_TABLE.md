# 健康台灣深耕計畫 KPI-To-Budget 對照表

狀態：2026-06-19 AI 問診與醫師覆核摘要專用工作表

## Current Scope

本表只服務下列 package：

```text
泌尿科門診前問診與醫師覆核摘要支持系統
```

CRM 屬於母案 / 其他團隊 workstream。本表聚焦 Jason / 陽明交大 AI-only 工作包，將三年 NT$10M 對應到 AI 問診、醫師覆核摘要、governance、KPI evidence、年度查核點與驗收資料。

## Parent Proposal Budget Context

2026-06-02 115 年度院外門診部深耕計畫討論會議紀錄列出下列信義門診部母案配置：

| Parent workstream | Meeting allocation | Current routing |
| --- | ---: | --- |
| 攝護腺癌 (PSA) 主動篩檢 | NT$15,000,000 | 忠孝院區協助完成；PSA SOP and guideline work remain outside this table |
| AI 智慧問診，須包含 CRM 系統 | NT$15,000,000 | parent allocation reference; CRM is handled by other team |
| Jason / 陽明交大 AI-only package | NT$10,000,000 | current table scope: AI 問診、醫師覆核摘要、governance、KPI evidence |

Writing rule:

```text
可以在母案背景中說明 AI 智慧問診提報約 NT$15M 且包含 CRM；
本表只編列吳老師 / 陽明交大團隊的三年 NT$10M AI-only 工作包。
```

## Budget Decision

目前以三年新臺幣 10,000,000 元作為 AI 問診與醫師覆核摘要 package 的工作上限。

2026-06-19 專家審查後，本表的正式提案定位為：

```text
範疇三「導入智慧科技醫療」為主軸，範疇一「優化醫療工作條件」為副支援。
```

最新版 NYCU Wu-team AI previsit complete proposal draft:

```text
exports/nycu-wu-team-ai-previsit-health-taiwan-complete-plan-2026-06-19.md
```

來源分析：

```text
../records/2026-06-19/nycu-ai-previsit-expert-review-analysis.md
```

正式送件前仍需由主提單位 / budget owner 確認：

- 正式會計科目
- 單價
- 數量
- 年度
- 補助款 / 配合款
- capital / current 類別
- negative-list 檢查
- 採購與委外門檻

## Official Category Planning Amounts

| 官方科目 | 三年概算 | 編列邏輯 |
| --- | ---: | --- |
| 人事費 | NT$6,140,000 | PM/RA、KPI/evaluation RA、clinical reviewer protected time、question/schema/AI engineering、QA cycle、evaluation analyst。 |
| 業務費 | NT$3,630,000 | 外部審查、文件包、資料蒐集、workflow walkthrough、LLM/API/cloud/ASR 租金或權利使用、治理工作坊、IRB、問卷 / 訪視等。 |
| 設備費 | NT$230,000 | clinic-owned intake station readiness；若改租用則轉業務費。設備費約占總額 2.3%，低於 30% 資本門上限。 |
| 合計 | NT$10,000,000 | 100% mapped to KPI, owner and evidence；正式表仍需主提單位確認補助款 / 配合款、採購門檻、核銷科目與驗收文件。 |

## KPI And Budget Sequence

本案不應先拿金額硬湊 KPI。建議順序是：

```text
1. 先確認暫定預算上限：目前使用 NT$10,000,000。
2. 定義可交付工作：AI 問診、醫師覆核摘要、治理、評估、文件化。
3. 設計 KPI：每個 KPI 都對應 workflow value。
4. 把預算映射到 KPI-backed work packages。
5. 正式會計科目確認後，再調整金額與年度拆分。
```

## First Principle

```text
No KPI -> no core budget line.
No owner -> no operational claim.
No governance gate -> no real patient data or deployment claim.
No friction reduction -> no Health Taiwan workflow value.
```

## KPI-To-Budget Table

| 工作包 | KPI / 查核項目 | 草案目標 | 預算意義 | 需要 owner | evidence artifact |
| --- | --- | --- | --- | --- | --- |
| Proposal coordination / PM / RA | 20 頁內提案草稿、KPI workbook、review-response table | proposal package complete | 支援格式化、彙整、專家回饋、年度證據整理 | proposal coordinator | proposal draft、review table |
| Clinical workflow review | workflow slot confirmed or revised | 報到後 / 候診中 / QR / tablet / staff-assisted 路徑擇一 | 防止系統增加門診負擔 | clinical workflow owner | workflow decision note |
| Question governance | 第一版問題集完成 review | LUTS / OAB-like 與門診前必要資訊欄位完成核對 | 支援安全且精簡的問診題組 | urology clinical reviewer | question governance table |
| AI 問診 / intake flow | minimum required fields completed or visibly missing | >= 90% in synthetic / approved review set | 支援低摩擦資料蒐集 | engineering owner | synthetic walkthrough |
| Missing-field visibility | key missing fields surfaced | >= 90% or exception log | 讓醫師知道哪些資訊仍需補問 | engineering + clinical reviewer | missing-field report |
| Source labeling | source label completeness | 100% summary lines / fields labeled | 保留資訊來源與責任邊界 | AI/data owner | audit sample |
| One-page physician-review summary | summary read time | <= 60 秒 design target, report actual | 驗證醫師是否願意讀且讀得完 | clinical reviewer | timed reviewer scorecard |
| Clinician usefulness | usefulness score | median >= 4/5 or revise | 驗證摘要是否真的有用 | clinical reviewer | scorecard |
| Staff-friction review | hidden workload identified | no unacceptable duplicate entry / clicks / training / exception load | 防止把工作轉嫁護理或櫃台 | outpatient workflow owner | staff-friction worksheet |
| Unsafe wording control | unsafe wording count | 0 diagnosis / treatment / autonomous triage / queue priority / EMR writeback phrases | 維持醫師覆核與臨床權責 | clinical + governance reviewer | safety checklist |
| ASR optional review | no unconfirmed ASR enters summary | 0 unconfirmed content | 只有在 input burden / accessibility KPI 成立時納入 | engineering + clinical reviewer | ASR confirmation test |
| AI/data/security governance | governance checklist completion | owners / gates named before real-data claim | 支援範疇三可信度 | AI/data/security owner | governance checklist |
| Evaluation and annual checkpoint | yearly evidence complete | output, KPI, issue, correction, next checkpoint visible | 支援年度查核與專家評估 | evaluation owner | annual evidence packet |

## Three-Year NT$10,000,000 Discussion Allocation

| 預算項目 | 第一年 | 第二年 | 第三年 | 合計 | KPI |
| --- | ---: | ---: | ---: | ---: | --- |
| Proposal coordination、PM、RA、KPI evidence | 900,000 | 900,000 | 700,000 | 2,500,000 | proposal package、KPI workbook、annual evidence |
| Clinical workflow review and reviewer sessions | 450,000 | 450,000 | 300,000 | 1,200,000 | clinician usefulness、summary read time、staff-friction review |
| Question governance、intake flow、summary schema | 1,000,000 | 600,000 | 300,000 | 1,900,000 | question set、completion、missing-field visibility |
| AI 問診與摘要 prototype / implementation evidence | 900,000 | 700,000 | 300,000 | 1,900,000 | source label、summary generation、audit sample |
| AI/data/security/privacy governance | 400,000 | 350,000 | 250,000 | 1,000,000 | governance checklist、unsafe wording = 0 |
| Evaluation、baseline、QI/IRB preparation | 250,000 | 400,000 | 350,000 | 1,000,000 | baseline、approved workflow measurement、final report |
| Optional ASR / intake station readiness | 350,000 | 150,000 | 0 | 500,000 | ASR confirmation safety、workflow feasibility |
| 總計 | 4,250,000 | 3,550,000 | 2,200,000 | 10,000,000 | 100% KPI-to-budget mapping |

## Formal Budget Columns Still Needed

| 項目 | 定義 |
| --- | --- |
| 正式會計科目 | 由主提單位 / budget owner 依官方經費標準分類 |
| 單價 | 每一人月、場次、設備、服務或文件工作的計算基礎 |
| 數量 | 人月、場次、件數、設備數、服務期間 |
| 年度 | 第一年、第二年、第三年拆分 |
| KPI | 該項支出要改善或產出的可驗收指標 |
| owner | 對該項工作與證據負責的角色 |
| evidence | 審查或年度查核可看到的文件 / scorecard / report |
| procurement note | 是否涉及採購、委外、資安或正式會計限制 |

## Do Not Budget

- CRM
- CRM-ready handoff
- CRM 欄位 / dashboard / follow-up queue
- patient messaging / LINE / SMS reminder
- HIS / EMR writeback
- autonomous diagnosis / treatment / triage
- unsupported chronic-disease outcome claims
- foreign travel as a core AI-package item
- personal phones, personal tablets, or routine administrative devices
