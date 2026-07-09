# 信義門診部深耕計畫 7/14 彙整前專家請益與任務拆解資料包

Status: working packet

Prepared date: 2026-07-02

Audience: Jason 會前自用、廖醫師 / 美幸主任 / proposal coordinator
請益、後續任務拆解。

## 一句話定位

7/14 前的工作主軸是先把美幸主任提出的 `健康生活處方`、PSA 流程指標與
智慧化支援方向整理成可確認的細項，再請信義院區泌尿科廖醫師確認臨床
流程與可行指標。確認後，再把內容放回信義門診部深耕計畫合併版。

本資料包不是正式送件稿；它是彙整前的任務包與專家請益包。

## Source Stack

| Source | Repo path | Use |
| --- | --- | --- |
| 廖醫師 6/18 交付 | `records/2026-06-18/liao-wesley-line-deep-cultivation-integration-record.md` | 確認 Jason 需協助統整，並以 6/18 Word 為格式來源。 |
| 6/19 AI-only 專家審查 | `records/2026-06-19/nycu-ai-previsit-expert-review-analysis.md` | 保持 AI 問診、醫師覆核摘要、治理、KPI、NT$10M 邊界。 |
| 6/22 三期預算 | `records/2026-06-22/xinyi-previsit-nt10m-three-phase-budget-record.md` | 2026-07-02 已校正為每年 NT$10M、三年合計 NT$30M；正式科目與細目需 budget owner 確認。 |
| 6/23 官方會議 | `records/2026-06-23/taipei-city-hospital-huashan-xinyi-deep-cultivation-official-meeting-minutes.md` | 確認母案三路徑、KPI、預算刪減、30% 資產控制與合併版 gate。 |
| 6/30 美幸主任 LINE | `records/2026-06-30/line-xinyi-deep-cultivation-health-lifestyle-prescription-record.md` | 直接建立健康生活處方、PSA 指標與智慧化支援任務。 |
| PSA workflow | `records/2026-06-30/sources/psa-screening-workflow-2026-06-30.md` | 3000 人、IPSS、健康生活處方、通知、追蹤、報表與核銷流程來源。 |
| 7/1 改期通知 | `records/2026-07-01/README.md` | 會議由 2026-07-07 改至 2026-07-14 同時段。 |
| 116-118 申請說明 | `records/2026-07-01/health-taiwan-stage2-application-guidance-record.md` | 確認第二階段申請需串接 workflow、KPI、checkpoint、budget、治理。 |
| 7/9 資本門 source gate | `records/2026-07-09/xinyi-capital-budget-liao-subproject-integration-checklist.md` | 合併廖醫師子計畫時確認美幸主任 email 與 `資本門` 附件是否已納入，或由 budget owner 另案決策。 |
| 既有會議包 | `records/2026-06-30/jason-2026-07-07-complete-meeting-packet.md` | 作為可重用的會前總覽；本檔只更新 7/14 前任務拆解。 |

## Current Decision Frame

### 已穩定的方向

| Item | Current working decision |
| --- | --- |
| Project label | `泌尿科門診前問診與醫師覆核摘要支持系統` |
| Safe descriptive boundary | `泌尿科門診前症狀蒐集與醫師覆核摘要輔助流程` |
| Jason / 陽明交大 scope | AI 問診、醫師覆核摘要、KPI evidence、治理、budget mapping。 |
| Mother proposal context | 信義母案包含 PSA 篩檢與智慧問診、CRM、碳盤查。 |
| Current AI-only ceiling | 每年新臺幣 10,000,000 元，三年合計新臺幣 30,000,000 元；正式會計科目、補助款 / 配合款與年度細目仍待主提案 / budget owner 確認。 |
| CRM | 母案 / 其他團隊 workstream，不列入 Jason / 陽明交大交付。 |
| HIS/EMR / real data / procurement | 由院內 owner、QI/IRB、資安、資料治理與採購路徑另案啟動。 |
| 7/14 gate | 審閱華山與信義門診部深耕計畫合併版本。 |

### Budget Working Amount

目前最新工作口徑為：

```text
NYCU / 陽明交大 AI-only 工作包是每年新臺幣 10,000,000 元，三年合計
新臺幣 30,000,000 元。
```

需要在正式彙整前向主提案 / budget owner 確認正式會計科目、補助款 /
配合款、年度細目與可核銷項目。若遇到舊稿仍使用舊版錯誤口徑，一律以本次校正口徑為準。

### 7/14 前的實際策略

先完成三個可被確認的工作包：

1. `健康生活處方`：泌尿科版本的處方候選、適用條件、欄位與累計方式。
2. `PSA 流程指標`：從 PSA workflow 抽出可衡量、可報表化、可核銷佐證的指標。
3. `智慧化支援`：以現場人員、問卷填答、缺漏提醒、結果通知紀錄、追蹤狀態與醫師覆核摘要為主，不擴張成 CRM。

## 美幸主任方向整理

美幸主任在 2026-06-26 至 2026-06-30 LINE 對話中給出的方向可以整理為
四個設計原則：

| Direction | Working interpretation |
| --- | --- |
| 泌尿科要提出健康生活處方 | 將 IPSS、排尿日誌、夜尿 / 頻尿生活提醒、PSA 結果追蹤配合等項目寫成可累計服務。 |
| 本錢低、實質幫助醫院營運 | 優先採用問卷、QR Code、衛教單、追蹤表、報表欄位等低採購負擔工具。 |
| 能提高效率 | 把資格確認、問卷上傳、結果通知、回診安排、外院三個月追蹤與報表產出標準化。 |
| 智慧化不要只幫廠商 | 智慧化要服務院內 evidence、現場流程、醫師覆核與年度查核，不以 vendor feature 為中心。 |

## 廖醫師確認包

先問廖醫師的問題應該短、可圈選、能直接改稿。

### A. 健康生活處方

| Question | Options to confirm | Why it matters |
| --- | --- | --- |
| 健康生活處方是每位符合資格者都產出，還是依 IPSS / 症狀觸發？ | 全員產出 / 條件觸發 / 先試辦條件觸發 | 決定 KPI 分母、工作量與報表欄位。 |
| 第一版處方要包含哪些項目？ | IPSS 後衛教、排尿日誌、夜尿頻尿生活提醒、PSA 結果追蹤配合、泌尿健康資源單 | 決定正式計畫可寫入的服務項目。 |
| 處方是否需由醫師核准文字？ | 醫師核准模板 / 現場人員發放標準單 / 先以候選文字審閱 | 控制醫療責任與現場效率。 |
| 健康生活處方 evidence 怎麼算？ | 開立數、發放數、QR 掃描、問卷完成、回收日誌、追蹤完成 | 決定年度 KPI 與核銷佐證。 |

### B. PSA workflow

| Question | Options to confirm | Why it matters |
| --- | --- | --- |
| 3000 人是目標收案數、預估篩檢量，還是計畫上限？ | 目標 / 預估 / 上限 | 影響 KPI 量能與 budget resilience。 |
| IPSS 電子表單是否已有固定欄位？ | 已有 / 可修改 / 需新建 | 影響 AI 問診與資料欄位設計。 |
| PSA 結果由哪個系統或人員回填？ | LIS/HIS 匯出 / 助理手動 / 其他 | 影響資料品質與權限設計。 |
| PSA >= 4 通知是否已有標準話術？ | 已有 / 需新增 / 由泌尿科審閱 | 影響安全 wording 與訓練材料。 |
| 外院三個月追蹤要記錄哪些欄位？ | 是否就醫、院所、檢查、診斷、處置、未就醫原因 | 影響 follow-up 表與研究資料邊界。 |
| 報表格式由誰決定？ | 衛生局 / 醫院 / 計畫辦公室 / 泌尿科 | 影響月報、年報、結案報告欄位。 |

### C. AI / 智慧化支援

| Question | Options to confirm | Why it matters |
| --- | --- | --- |
| 第一版填答場景放在哪裡？ | 報到後、候診中、QR Code、平板站、現場人員協助 | 決定流程摩擦與設備需求。 |
| 醫師覆核摘要要顯示哪些五個欄位？ | 主訴、IPSS、PSA 狀態、缺漏欄位、追蹤狀態等 | 決定摘要版型與 KPI。 |
| 醫師是否願意看 60 秒內一頁摘要？ | 願意 / 需更短 / 只看特定欄位 | 決定 summary read-time KPI。 |
| AI 要先做什麼？ | 問卷缺漏提醒、摘要、報表彙整、追蹤狀態表 | 決定 7/14 可寫入的最小智慧化範圍。 |
| ASR 是否需要進第一版？ | 不需要 / demo-only / 特定族群輔助 | 避免不必要的採購與安全負擔。 |

## Task Breakdown

### P0：7/14 前必須完成

| Task | Owner to ask | Output | Source |
| --- | --- | --- | --- |
| 確認健康生活處方採全員或條件觸發 | 廖醫師 / 美幸主任 | 一句決策 + KPI 分母 | 6/30 LINE, PSA workflow |
| 圈選第一版健康生活處方 3-5 項 | 廖醫師 | 候選表定稿 | 6/30 LINE |
| 確認 PSA 流程指標 6-10 項 | 廖醫師 / proposal coordinator | KPI candidate table | PSA workflow |
| 確認 3000 人量能的性質 | 廖醫師 / proposal coordinator | 目標量能說明 | PSA workflow |
| 確認 AI-only 預算正式科目、補助款 / 配合款、年度細目與可核銷項目 | 主提案 / budget owner | budget boundary confirmation note | 6/19, 6/22, 2026-07-02 user correction |
| 合併廖醫師子計畫時核對美幸主任 email 與 `資本門` 附件是否已納入 | 廖醫師 / proposal coordinator / budget owner | capital-budget inclusion or separate-work-package decision | 7/9 copied source gate |
| 確認 CRM、HIS/EMR、真實資料暫列 activation gate | parent proposal owner | scope-control paragraph | 6/19, 6/23, 7/1 |
| 把確認後內容更新到合併版彙整稿 | Jason | revised merged draft section | 6/30 packet |

### P1：若 7/14 前有餘裕

| Task | Owner to ask | Output |
| --- | --- | --- |
| 製作一頁式醫師覆核摘要欄位草稿 | 廖醫師 | summary mockup fields |
| 產出 PSA 月報 / 年報欄位草稿 | proposal coordinator | report field table |
| 對照 116-118 申請說明做 governance checklist | Jason / governance owner | pre-submission checklist |
| 將健康生活處方對應範疇四 3.1 / 3.2 | Jason | proposal paragraph |
| 將 AI 問診對應範疇三與範疇一 | Jason | proposal paragraph |

### P2：7/14 後再啟動

| Task | Activation gate |
| --- | --- |
| 真實資料使用、QI / IRB、研究分析 | 院內資料治理與 IRB/QI route 確認後。 |
| HIS / EMR / LIS / FHIR 串接 | 資訊、資安、採購、臨床 owner 確認後。 |
| CRM、簡訊推播、長期病人管理 | parent proposal owner 或其他團隊確認後。 |
| 正式採購、vendor quote、維運 SLA | budget / procurement owner 確認後。 |
| TFDA / SaMD / 醫材法規定位 | 系統從 review-support 走向臨床決策或醫材路徑時。 |

## Candidate Tables For Expert Review

### 健康生活處方候選表

| Candidate | Suggested trigger | Evidence field | Smart support |
| --- | --- | --- | --- |
| IPSS 後衛教處方 | 完成 IPSS 後 | `ipss_completed`, `prescription_issued` | 平板填答完成後自動帶出標準衛教單。 |
| 排尿日誌 / 症狀自我觀察 | 下泌尿道症狀、夜尿、頻尿、解尿困難 | `diary_issued`, `diary_returned` | QR Code 表單與回診摘要。 |
| 飲水 / 咖啡因 / 夜尿生活提醒 | 夜尿或頻尿主訴 | `lifestyle_tip_issued`, `patient_acknowledged` | 條件觸發衛教單與閱讀確認。 |
| PSA 結果追蹤配合處方 | PSA >= 4 或需回診者 | `notified`, `appointment_scheduled`, `follow_up_status` | 通知紀錄、回診安排與狀態追蹤。 |
| 泌尿健康資源單 | 一般篩檢民眾 | `resource_sheet_issued`, `qr_scan_count` | QR Code 連到健康資訊中心或院內資源。 |

### PSA KPI 候選表

| KPI | Denominator | Numerator | Evidence |
| --- | --- | --- | --- |
| 篩檢資格確認完成率 | 報到或接觸人數 | 已完成資格確認人數 | roster / eligibility log |
| IPSS 問卷完成率 | 符合資格人數 | 完成 IPSS 人數 | questionnaire log |
| 健康生活處方完成率 | 符合資格或觸發條件人數 | 完成處方紀錄人數 | prescription log |
| 問卷上傳成功率 | 問卷完成件數 | 上傳成功件數 | upload log |
| PSA 結果回填完成率 | 已抽血人數 | PSA 值已回填人數 | result log |
| PSA >= 4 通知完成率 | PSA >= 4 人數 | 完成電話 / 簡訊通知人數 | notification log |
| 回忠孝泌尿科門診安排率 | PSA >= 4 人數 | 已約定門診人數 | appointment log |
| 外院三個月追蹤完成率 | 選擇外院人數 | 三個月追蹤完成件數 | follow-up log |
| 月報 / 年報完成率 | 應完成報表數 | 已完成報表數 | report archive |
| 醫師覆核摘要可用率 | review cases | median >= 4/5 or revised | clinician scorecard |

## Expert Consultation Script

可以直接用以下訊息請教廖醫師：

```text
廖醫師您好，我先把 7/14 合併版彙整前需要確認的泌尿科項目整理成三類：

1. 健康生活處方：想請您先圈選第一版要放進計畫的 3-5 項，例如 IPSS 後衛教、排尿日誌、夜尿/頻尿生活提醒、PSA 結果追蹤配合、泌尿健康資源單。也想確認這是每位符合資格者都產出，還是依 IPSS/症狀條件觸發。

2. PSA 流程指標：我先從 PSA workflow 抽出資格確認、IPSS 完成、健康生活處方完成、問卷上傳、PSA 結果回填、PSA>=4 通知、回診安排、外院三個月追蹤、月報/年報完成等指標。想請您確認哪些適合放正式 KPI，哪些只放年度報表 evidence。

3. 智慧化支援：我建議先寫成協助現場人員完成問卷填答、缺漏提醒、結果通知紀錄、追蹤狀態、報表彙整與一頁式醫師覆核摘要，不先承諾 CRM、HIS/EMR 寫回或真實資料研究使用。這樣是否符合泌尿科流程與 7/14 彙整方向？

我會依您的確認，把內容更新到正式彙整稿。
```

## 7/14 前 Execution Plan

| Date | Action | Done when |
| --- | --- | --- |
| 2026-07-02 | 完成本資料包並整理廖醫師請益問題 | task packet exists in repo |
| 2026-07-03 至 2026-07-05 | 請廖醫師圈選健康生活處方與 PSA 指標 | decision notes captured |
| 2026-07-06 至 2026-07-08 | 對齊美幸主任方向與 proposal coordinator 需要的 KPI / 報表格式 | revised tables ready |
| 2026-07-09 至 2026-07-11 | 更新合併版信義章節、KPI、budget boundary、scope controls | draft section updated |
| 2026-07-12 至 2026-07-13 | 做 release read-through：正向語氣、owner、evidence、activation gate | clean pre-read |
| 2026-07-14 | 帶著確認後版本進合併版審閱 | meeting-ready packet |

## Update Targets After Confirmation

確認後優先更新下列檔案：

| Target | Update |
| --- | --- |
| `records/2026-06-30/jason-2026-07-07-complete-meeting-packet.md` | 若仍作為會前總包，更新 7/14 狀態與已確認內容。 |
| `discovery/DEEP_CULTIVATION_KPI_TO_BUDGET_TABLE.md` | 加入已確認 PSA / 健康生活處方 KPI 與 owner / evidence。 |
| `discovery/DEEP_CULTIVATION_KPI_BUDGET_ANNUAL_INTEGRATION_TABLE.md` | 把年度 checkpoint 接到 116-118 planning。 |
| `discovery/exports/nycu-wu-team-ai-previsit-health-taiwan-complete-plan-2026-06-19.md` | 需要正式彙整稿時，再更新提案正文。 |
| `meta/open_questions.md` | 將廖醫師已確認問題標為 resolved / accepted decision。 |

## Scope Controls For The Formal Draft

正式彙整稿應保留以下正向邊界：

- 系統支援 `問卷填答、缺漏提醒、來源標示、追蹤紀錄、報表彙整、醫師覆核摘要`。
- 健康生活處方是 `低成本、可累計、可查核` 的範疇四服務項目。
- PSA 流程指標支援 `年度 evidence、核銷附件、計畫成效與現場效率`。
- 醫療判斷、PSA 臨床解讀、診斷、治療與回診處置由醫師與院內流程負責。
- CRM、HIS/EMR 正式寫回、真實病患資料、採購、維運與研究使用由院內 owner 另案啟動。
