# 陽明交大泌尿科 AI 問診與醫師覆核摘要支持系統：專家評估資料包

狀態：2026-06-19 expert-review packet

用途：供專家評估後撰寫正式深耕計畫內容。

## 1. Current Decision

本案目前只處理：

```text
泌尿科門診前問診與醫師覆核摘要支持系統
```

陽明交大 / Jason 負責範圍：

- AI 問診 / guided intake。
- 醫師覆核用一頁式摘要。
- source label、缺漏欄位、unsafe wording control。
- 合成案例或核准流程下的 reviewer evidence。
- AI/data/security/privacy governance 準備。
- KPI-to-budget traceability。
- 三年新臺幣 10,000,000 元討論額度之設計與拆分。

CRM 完全 out of scope：

- 不規劃 CRM。
- 不與 CRM 團隊討論。
- 不做 CRM-ready handoff。
- 不列 CRM KPI。
- 不列 CRM 預算。
- 不處理 CRM 採購、維運、病人追蹤、訊息通知或 dashboard。

PSA 主動篩檢可作為臨床背景或母計畫 sibling content，但 PSA SOP、臨床 guideline、異常值追蹤與回診管理不由陽明交大本案承擔。

## 2. Source Evidence

| 類型 | 檔案 | 用途 |
| --- | --- | --- |
| 5/19 會議紀錄 | `records/2026-05-19/deep-cultivation-meeting-capture.md` | 證明會議方向是 service workflow、智慧醫療、KPI、治理，不是 pure AI model。 |
| Jason 工作範圍整理 | `records/2026-05-19/jason-work-scope-from-deep-cultivation-meeting.md` | 證明陽明交大任務是把智慧醫療 / AI 問診整理成可提報子計畫。 |
| 6/12 CRM 排除紀錄 | `records/2026-06-12/wu-yuelin-line-crm-888-record.md` | 證明 CRM 已由其他團隊處理，目前不屬於本案。 |
| 6/12 美如主任截圖 | `records/2026-06-12/sources/chen-meiru-crm-other-team-line-2026-06-12.png` | 原始證據：CRM 由忠孝岳霖主任找其他團隊處理。 |
| 6/18 廖醫師交付紀錄 | `records/2026-06-18/liao-wesley-line-deep-cultivation-integration-record.md` | 證明廖醫師提供 Word 格式範本，請 Jason 協助統整。 |
| 廖醫師 PSA 範本 | `records/2026-06-18/sources/tch-zhongxiao-xinyi-deep-cultivation-plan-revised-2026-06-18.docx` | 作為正式章節、欄位、經費與效益評估格式參考。 |
| AI-only KPI / budget | `discovery/DEEP_CULTIVATION_KPI_TO_BUDGET_TABLE.md` | 本案 1000 萬預算與 KPI 對照。 |
| AI-only checkpoint | `discovery/DEEP_CULTIVATION_KPI_BUDGET_ANNUAL_INTEGRATION_TABLE.md` | 本案章節、KPI、年度 checkpoint 對照。 |
| 套版稿 | `discovery/exports/nycu-urology-previsit-deep-cultivation-plan-in-tch-template-2026-06-18.md` | 已套入廖醫師格式的 AI-only 工作稿。 |

## 3. Proposal Thesis

本計畫以泌尿科門診前資訊摩擦為主要問題：病人在看診前常有主訴分散、症狀時間軸不清、重要欄位缺漏、醫師需要重複問診、護理或櫃台難以承接額外整理工作的情境。

本計畫建立一套 AI 問診與醫師覆核摘要支持流程，讓病人於門診前或候診時完成低摩擦症狀蒐集，系統保留資訊來源標記、缺漏欄位、不確定資訊與安全邊界，並產出一頁式醫師覆核摘要。醫師保留臨床解讀、診斷、治療與處置責任；AI 僅支援資料整理、缺漏提示、摘要草擬與 reviewer evidence。

## 4. Scope Control

### In Scope

| 項目 | 定義 |
| --- | --- |
| AI 問診 | 以泌尿科常見非急性症狀為起點，收集主訴、時間軸、嚴重度、相關症狀、既往資訊與需補問欄位。 |
| 醫師覆核摘要 | 一頁式摘要，供醫師快速掌握病人陳述與缺漏資訊。 |
| Source label | 標示資訊來自病人、家屬、工作人員協助、或 ASR-confirmed。 |
| Missing-field visibility | 讓醫師清楚看到未填、矛盾、不確定或需要補問的欄位。 |
| Safety wording | 避免診斷、治療建議、自動分流、queue priority、EMR writeback。 |
| Reviewer evidence | 用合成案例或核准流程測試 summary read time、usefulness、staff friction。 |
| Governance | AI/data/security/privacy/IRB-QI/procurement gates before real data or deployment claim。 |
| Budget/KPI mapping | 每一筆經費都對應 KPI、owner、evidence、checkpoint。 |

### Out Of Scope

| 項目 | 原因 |
| --- | --- |
| CRM | 2026-06-19 owner update 已排除。 |
| CRM-ready handoff | 不需要與 CRM 團隊連結或討論。 |
| Patient messaging | 屬 CRM / 院方追蹤，不屬本案。 |
| HIS / EMR writeback | 需後續院內治理與系統 owner；本案不主張。 |
| Diagnosis / treatment | 臨床權責保留於醫師。 |
| Autonomous triage / queue priority | 不符合本案 intended use。 |
| PSA SOP ownership | 可作背景，不由本案承擔。 |
| 慢病 / 三高改善成效 | 可作政策背景，不作本案成效 claim。 |

## 5. Budget And KPI Answer

目前建議以三年新臺幣 10,000,000 元作為 AI 問診與醫師覆核摘要 package 的討論額度。

是否要先確認預算再規劃 KPI？

答案是：

```text
先確認暫定預算上限，但不要等正式預算定案才設 KPI。
```

實作順序：

```text
NT$10M working ceiling
-> define deliverables
-> define KPI from workflow value
-> map budget to KPI-backed work packages
-> revise after official accounting review
```

原因：

- 沒有暫定預算，設計會失去尺度。
- 沒有 KPI，預算會變成功能清單。
- 正式會計科目、單價、數量、補助款 / 配合款、capital cap，需要主提單位確認後才能定稿。
- 專家評估階段最需要的是：每一筆錢為什麼存在、改善哪個 workflow state、誰驗收、看什麼 evidence。

## 6. Three-Year Budget Draft

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

## 7. KPI Draft

| KPI | 草案目標 | Evidence |
| --- | --- | --- |
| Summary read time | <= 60 秒 design target, report actual | timed reviewer scorecard |
| Clinician usefulness | median >= 4/5 or revise | clinician scorecard |
| AI 問診 completion | >= 90% minimum fields completed or flagged | synthetic / approved walkthrough |
| Missing-field visibility | >= 90% key missing fields surfaced | missing-field report |
| Source-label completeness | 100% summary fields labeled | audit sample |
| Unsafe wording count | 0 diagnosis / treatment / triage / queue-priority / EMR phrases | safety checklist |
| Staff-friction review | no unacceptable duplicate entry / clicks / exception load | staff-friction worksheet |
| Governance checklist | AI/data/security/IRB-QI gates named before real-data claim | governance checklist |
| KPI-to-budget traceability | 100% core budget lines mapped | budget table audit |

## 8. Fast Planning Path

建議下一步不要直接寫長版全文，先做四件事：

1. **確認 NT$10M 是否為本案正式討論上限。**
   - 若是，直接用本資料包的 budget architecture。
   - 若不是，只調整金額，不重寫 scope。

2. **確認第一版臨床入口。**
   - 報到後 / 候診中 / QR code / tablet / staff-assisted selected cases。

3. **確認摘要最上方五個欄位。**
   - 建議候選：主訴、症狀時間軸、嚴重度 / 影響、重要伴隨症狀、缺漏 / 不確定資訊。

4. **用 3-5 個合成案例做專家評估。**
   - 讓專家評 summary read time、usefulness、unsafe wording、missing fields、staff friction。

## 9. Expert Review Questions

請專家優先回答：

1. 這個計畫名稱是否清楚：`泌尿科門診前問診與醫師覆核摘要支持系統`？
2. 本案是否應以三年 NT$10,000,000 作為討論額度？
3. 第一版病人入口應放在哪個 workflow slot？
4. 醫師一頁摘要最上方五個欄位應該是什麼？
5. KPI 是否足以支撐 NT$10M 經費？
6. 哪些經費項目需要改成正式會計科目或刪除？
7. 是否需要 ASR？若需要，是 funded item 還是 optional evaluation？
8. 若未來涉及真實病患資料，本案應走 QI/service improvement、IRB research，或 mixed route？
9. 哪些詞會讓醫師誤以為這是診斷、治療建議或自動病歷？
10. 本案是否足以獨立成為子計畫，或應作為母計畫中的智慧醫療 work package？
