# Jason 信義門診部深耕計畫合併版審閱資料包

Status: release packet

Prepared date: 2026-06-30

Schedule update: 2026-07-01 北市聯醫 LINE notice updates the original
2026-07-07 meeting to 2026-07-14 same time; Jason / Wu team has no time
conflict. This packet remains the active Jason / 陽明交大 preparation package
until the hospital owner requests a newer format or content package.

Audience: Jason 自用會前準備、可轉交給信義 / 忠孝深耕計畫協作窗口的工作資料包。

## 0. 一句話定位

本資料包整理目前 `信義門診部深耕計畫` 中與 Jason / 陽明交大團隊直接相關的工作：以 `泌尿科門診前問診與醫師覆核摘要支持系統` 為核心，支援 PSA 篩檢流程、問卷填答、醫師覆核摘要、KPI evidence、治理文件與智慧化流程設計；並回應美幸主任在 2026-06-26 LINE 群組提出的 `健康生活處方`、PSA 流程指標與智慧化協助需求。

## 1. 專案到目前為止的完整介紹

### 1.1 專案名稱與主軸

目前 Jason / 陽明交大工作包的穩定名稱是：

```text
泌尿科門診前問診與醫師覆核摘要支持系統
```

本工作包在信義門診部母案中的角色是智慧化支援層。它協助病人、家屬或現場人員在看診前完成低摩擦問診，將資料整理成來源清楚、缺漏可見的一頁式醫師覆核摘要，讓醫師在門診前快速掌握主訴、症狀脈絡、需要補問的欄位與流程證據。

### 1.2 目前母案架構

依 2026-06-23 會議紀錄，信義門診部深耕計畫目前以三條工作路徑整合：

| 路徑 | 會議配置 | Jason / 陽明交大角色 |
| --- | ---: | --- |
| PSA 篩檢與智慧問診 | 新臺幣 15,000,000 | 支援 AI 問診、醫師覆核摘要、KPI evidence、治理與智慧化流程 |
| CRM 系統 | 新臺幣 15,000,000 | 目前屬母案 / 其他團隊，不列入 Jason 交付範圍 |
| 信義門診部碳盤查 | 新臺幣 7,500,000 | 創新永續發展中心協助，屬 separate sustainability lane |

Jason / 陽明交大目前已完成一份 AI-only 工作稿，以每年新臺幣 10,000,000 元、三年合計新臺幣 30,000,000 元作為 AI 問診與醫師覆核摘要 package 的討論上限。這個上限不是母案總額，而是 Jason / 陽明交大可交付的 AI-only 工作包規模。

### 1.3 目前已完成的核心內容

目前 repo 內已完成並可使用的內容包括：

| 已完成項目 | 最新文件 |
| --- | --- |
| AI 問診與醫師覆核摘要完整工作稿 | `discovery/exports/nycu-wu-team-ai-previsit-health-taiwan-complete-plan-2026-06-19.md` |
| 專家審查資料包與項目定義 | `discovery/exports/nycu-ai-previsit-expert-review-packet-2026-06-19.md`、`discovery/exports/nycu-ai-previsit-proposal-item-definitions-2026-06-19.md` |
| KPI-to-budget 對照表 | `discovery/DEEP_CULTIVATION_KPI_TO_BUDGET_TABLE.md` |
| KPI / 預算 / 年度 checkpoint 整合表 | `discovery/DEEP_CULTIVATION_KPI_BUDGET_ANNUAL_INTEGRATION_TABLE.md` |
| 2026-06-23 上次會議完整紀錄 | `records/2026-06-23/taipei-city-hospital-huashan-xinyi-deep-cultivation-official-meeting-minutes.md` |
| 合併版審閱時程 | `records/2026-06-23/deep-cultivation-2026-07-07-integration-schedule.md` |
| 2026-07-01 會議改期 LINE 訊號 | `records/2026-07-01/line-tch-merged-plan-review-postponement.md` |
| 2026-06-30 美幸主任 LINE 要求完整紀錄 | `records/2026-06-30/line-xinyi-deep-cultivation-health-lifestyle-prescription-record.md` |
| 6/30 附件 repo-local source copies | `records/2026-06-30/sources/` |

### 1.4 工作邊界

Jason / 陽明交大目前可主動負責：

- 門診前問診流程設計。
- 一頁式醫師覆核摘要設計。
- source label、missing-field visibility、unsafe wording control。
- KPI evidence、年度 checkpoint、KPI-to-budget traceability。
- PSA 流程中的智慧化支援建議。
- `健康生活處方` 候選項目與可累計指標設計。

Jason / 陽明交大目前不直接承諾：

- PSA 臨床 SOP 最終定稿。
- PSA 數值臨床解讀、診斷、治療決策。
- CRM 系統採購、維運、推播與長期追蹤。
- 碳盤查。
- HIS/EMR 正式寫回。
- 真實病患資料使用，除非院內 QI / IRB / data governance route 已確認。

## 2. 美幸主任對 Jason 的要求

### 2.1 LINE 原始要求

2026-06-26 至 2026-06-30，LINE `信義門診部 深耕計畫` 群組中，美幸主任提出三個直接要求：

1. 泌尿科需要一起想 `健康生活處方` 可以寫什麼。
2. PSA 篩檢流程應參考藍色標示處，加入幾個可衡量指標。
3. 智慧化的部分請 Jason 幫忙想。

美幸主任特別強調：

```text
這種本錢低的，才能有實質幫助醫院營運。多寫一點。

或是真的可以幫我們提高效率的也可以。

如果光是寫來給其他廠商的，好像只是在幫別人而已。
```

### 2.2 對 Jason 的實際任務解讀

Jason 要準備的不是一個大型新系統，而是一組可放進合併版計畫討論的低成本、高可驗收、能支持院內流程的智慧化建議：

- 把泌尿科 `健康生活處方` 寫成可累計、可查核、可由現場人員執行的服務項目。
- 把 PSA 流程拆成幾個可量化指標，讓計畫能呈現範疇四與範疇三的 evidence。
- 把 AI / 智慧化放在現場效率、問卷填答、結果通知、追蹤紀錄、報表產出與醫師覆核摘要，而不是只寫成廠商服務。
- 保留醫療責任邊界：系統支援資料整理與流程提醒，臨床判斷與處置由醫師與院內流程負責。

## 3. 上次會議完整會議紀錄

上次會議以 2026-06-23 `115 年度華山、信義門診部深耕計畫討論會議紀錄` 為正式 source。完整會議紀錄已放入本資料包：

```text
02_last_meeting_complete_minutes_2026-06-23.md
```

會議重點如下：

| 主題 | 會議結論 |
| --- | --- |
| 下次會議 | 2026-07-14 同時段，審閱華山與信義門診部深耕計畫合併版本 |
| 信義母案 | PSA 篩檢與智慧問診、CRM 系統、碳盤查三條路徑 |
| 華山母案 | 無紙化與步態分析 / 健康艙兩條路徑 |
| 預算控制 | 各專案每年總經費上限約新臺幣 37,500,000；審查可能刪至 50-60% |
| KPI | KPI 服務量能不能因預算刪減而任意縮減，需 claim-evidence aligned |
| 資產限制 | 硬體與無形資產各自遵守 30% 控制；軟體優先以租賃 / service framing |
| 合作單位 | 需確認友好合作單位、簽約路徑、合作內容與 evidence |

## 4. 合併版審閱會議準備內容

### 4.1 Jason 的會議目標

Jason 在合併版審閱會議應帶去三件事：

1. AI-only 工作包目前已經有完整工作稿、KPI、預算與治理邊界。
2. 美幸主任新增的 `健康生活處方` 可以用低成本、可累計、可查核方式接到 PSA workflow。
3. PSA 流程指標與智慧化支援可以服務現場人員、醫師覆核與年度 evidence，不需要把範圍擴張成 CRM 或大型採購。

### 4.2 建議會議發言稿

```text
目前陽明交大這邊可以先把工作定位在「門診前問診、醫師覆核摘要、PSA 流程指標與健康生活處方紀錄」四個部分。這樣可以接到信義 PSA 篩檢流程，也能回應美幸主任提到的範疇四健康生活處方。

我們建議先做低成本、可累計、可查核的項目：問卷完成率、健康生活處方開立數、PSA 結果通知紀錄、需要回診個案的門診安排紀錄、外院就醫三個月追蹤紀錄、以及一頁式醫師覆核摘要。這些指標可以支持年度報表、核銷資料與計畫成效，不會把臨床判斷交給系統。

智慧化部分我們會以現場人員好用為主，協助問卷填答、缺漏欄位提醒、來源標記、報表彙整與醫師覆核摘要。CRM、HIS/EMR 寫回、真實資料使用與正式採購，等院內 owner 和治理路徑確認後再另案啟動。
```

### 4.3 泌尿科健康生活處方候選表

以下為會議候選項目，需由廖醫師 / 美幸主任確認後才進正式計畫：

| 候選處方 | 適用位置 | 可累計 evidence | 智慧化支援 |
| --- | --- | --- | --- |
| IPSS 後衛教處方 | PSA 抽血前問卷後 | 完成 IPSS + 完成健康生活處方件數 | 平板問卷、處方簽紀錄、缺漏提醒 |
| 排尿日誌 / 症狀自我觀察處方 | 有下泌尿道症狀者 | 發出日誌份數、回收份數、門診帶回率 | QR Code 表單、回診前摘要 |
| 飲水 / 咖啡因 / 夜尿生活型態提醒 | 夜尿或頻尿主訴者 | 發出提醒件數、病人確認閱讀或填答件數 | 問卷條件觸發、衛教單自動帶出 |
| PSA 結果追蹤配合處方 | PSA >= 4 或需回診者 | 通知完成、門診安排、三個月外院追蹤完成 | 通知紀錄、追蹤狀態、報表彙整 |
| 泌尿健康促進資源單 | 一般篩檢民眾 | 發放件數、QR Code 掃描或問卷完成件數 | QR Code、健康資訊中心資源連結 |

### 4.4 PSA 流程指標候選表

以下指標可接到 `PSA 篩檢流程.md` 現有步驟：

| 指標 | 流程位置 | 衡量方式 |
| --- | --- | --- |
| 篩檢資格確認完成率 | 報到 / 篩檢前 | 已確認資格人數 / 報到人數 |
| IPSS 問卷完成率 | 抽血前問卷 | 完成 IPSS 人數 / 符合資格人數 |
| 健康生活處方完成率 | 抽血前問卷 | 完成處方紀錄人數 / 符合資格人數 |
| 問卷上傳成功率 | 平板填答後 | 上傳成功件數 / 問卷完成件數 |
| PSA 結果回填完成率 | 檢驗結果後 | PSA 值已回填人數 / 已抽血人數 |
| PSA >= 4 通知完成率 | 結果通知 | 完成電話 / 簡訊通知人數 / PSA >= 4 人數 |
| 回忠孝泌尿科門診安排率 | 異常結果追蹤 | 已約定門診人數 / PSA >= 4 人數 |
| 外院就醫三個月追蹤完成率 | 外院追蹤 | 三個月追蹤完成件數 / 選擇外院人數 |
| 月報 / 年報 / 結案報告完成率 | 報表與核銷 | 已完成報表數 / 應完成報表數 |
| 醫師覆核摘要可用率 | AI 問診支援 | reviewer scorecard median >= 4/5 或需改版 |

### 4.5 會議需要確認的決策

| 決策問題 | 需要誰確認 |
| --- | --- |
| Jason / 陽明交大 AI-only 工作包是否仍以 NT$10M 作討論上限？ | 主提案 / budget owner |
| `健康生活處方` 要作為 PSA 流程中的必填欄位，還是依問卷條件觸發？ | 廖醫師 / 美幸主任 |
| 健康生活處方是否每位符合資格民眾都產出？ | 廖醫師 / 美幸主任 |
| PSA 指標要進正式 KPI 表，還是先放在流程 evidence / 年度報表？ | proposal coordinator |
| 系統是否只做問卷、摘要、紀錄與報表，CRM 另由其他團隊承接？ | parent proposal owner |
| 真實資料使用 route 是 no-data demo、QI/service improvement、IRB research，還是 mixed？ | clinical + IRB/QI + data governance owner |
| 軟體費用以租賃 / service / subscription 寫入，還是自建無形資產？ | budget + procurement owner |

## 5. 目前做好的項目與最新文件

### 5.1 最新可交付文件

本資料包已複製下列最新文件：

| Packet file | 原始 repo 位置 |
| --- | --- |
| `01_project_intro_and_july7_prep.md` | 本檔 |
| `02_last_meeting_complete_minutes_2026-06-23.md` | `records/2026-06-23/taipei-city-hospital-huashan-xinyi-deep-cultivation-official-meeting-minutes.md` |
| `03_integration_schedule.md` | `records/2026-06-23/deep-cultivation-2026-07-07-integration-schedule.md` |
| `05_meeting_postponement_line_2026-07-01.md` | `records/2026-07-01/line-tch-merged-plan-review-postponement.md` |
| `04_miyuki_line_request_complete_record_2026-06-30.md` | `records/2026-06-30/line-xinyi-deep-cultivation-health-lifestyle-prescription-record.md` |
| `latest-documents/nycu-wu-team-ai-previsit-health-taiwan-complete-plan-2026-06-19.md` | `discovery/exports/nycu-wu-team-ai-previsit-health-taiwan-complete-plan-2026-06-19.md` |
| `latest-documents/deep-cultivation-kpi-to-budget-table.md` | `discovery/DEEP_CULTIVATION_KPI_TO_BUDGET_TABLE.md` |
| `latest-documents/deep-cultivation-kpi-budget-annual-integration-table.md` | `discovery/DEEP_CULTIVATION_KPI_BUDGET_ANNUAL_INTEGRATION_TABLE.md` |
| `sources/health-taiwan-stage1-application-guidelines-114-115-2026-06-30.md` | `records/2026-06-30/sources/health-taiwan-stage1-application-guidelines-114-115-2026-06-30.md` |
| `sources/psa-screening-workflow-2026-06-30.md` | `records/2026-06-30/sources/psa-screening-workflow-2026-06-30.md` |

### 5.2 目前狀態

| 工作 | 狀態 |
| --- | --- |
| 6/30 LINE 對話保存 | source preserved |
| 6/30 附件保存 | source preserved |
| AI 問診完整工作稿 | completed working draft |
| KPI-to-budget 表 | completed working draft |
| 6/23 官方會議紀錄 | captured |
| 合併版審閱時程 | captured |
| 7/1 會議改期 LINE 訊號 | source preserved |
| 健康生活處方候選表 | prepared for confirmation |
| PSA 流程指標候選表 | prepared for confirmation |
| 正式提案改寫 | pending owner confirmation |
| 真實資料 / IRB / QI / HIS/EMR / CRM | activation-gated |

## 6. Jason 會前最小行動清單

1. 先確認合併版審閱會議是否要 Jason 以 AI-only 工作包代表陽明交大發言。
2. 帶著 `健康生活處方候選表` 與 `PSA 流程指標候選表` 請廖醫師 / 美幸主任圈選。
3. 問清楚 `健康生活處方` 是每位篩檢民眾都產出，還是依 IPSS / 症狀結果觸發。
4. 問清楚 PSA 指標要寫入正式 KPI，還是先作為年度報表 evidence。
5. 重申 CRM、HIS/EMR、真實資料使用與採購屬 activation gate，不在會中直接承諾。
6. 會後把確認結果更新到 KPI-to-budget table 與正式提案稿。
