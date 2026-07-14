# 四工作包 IRB 管轄與送審路徑判定紀錄

Status: official-source check completed on 2026-07-14 / institutional written determination pending

## FIRST PRINCIPLE

- Scarce resource: 在 2026-07-31 完成可送審草案前，先把服務、QI、研究、醫療器材驗證及營運資料分流，避免用同一目的與同一同意路徑混用資料。
- Canonical home: 本檔保存四工作包的 current working determination；[使用者原始筆記](sources/irb-jurisdiction-review-path-user-note-2026-07-14.md)完整保留來源層。
- Authority: 《人體研究法》、衛福部公告、TFDA／醫療器材法規及北市聯醫當日現行表單擁有正式 authority；案件分類由北市聯醫 IRB／相關治理單位書面判定。
- Next gate: PI、IRB liaison、臨床資料 owner 以 2–3 頁 jurisdiction request 取得每一工作包的書面分類，再啟動真實資料、研究性抽血、錄音錄影或研究分析。

## 目前可採用的結論

本案採「活動目的 × 資料來源 × 是否改變照護 × 預期輸出」逐項判定。四個工作包不預設綁成同一 IRB 案；常規服務／QI／行政營運與人體研究各自擁有資料集、同意與治理路徑。

### 2026-07-14 後續團隊工作方向

`scope change`: 莊美幸主任於 LINE 指示先以「一般審查、四子計畫整合成一案」形成工作草案，整合案可共用一次審查費，Jason 只撰寫門診前候診系統責任範圍；陳美如主任隨後確認同一整合計畫配合共同線上上傳，送一個 IRB 即可，趙康邑並確認前一年度亦採單一案件。這是目前的文件協作方向，並不取代逐活動 purpose map、各子計畫 owner 覆核及北市聯醫 IRB 的正式分類。整合 [Ver1.0 working draft](sources/tpech-irb-general-review-four-workstream-integrated-application-draft-v1.0-2026-07-14.docx)已保存；送審前逐欄確認 PI、研究設計、樣本數、醫療知識、同意結構、表單版本與資料治理。

| 工作包與活動 | Current working route | Activation gate |
| --- | --- | --- |
| 門診前候診系統：合成資料開發、schema／資安／內部驗收 | 非人體研究工作層 | 僅用合成或無個人資料；不把 reviewer 表現當研究結果 |
| 門診前候診系統：真實病人或醫師可用性、工作負擔、成效研究 | 先以簡易審查候選路徑準備 | IRB 依常規病歷、行為研究、最低風險及錄音影像情形判定 |
| PSA／PHI：核准用途內的常規醫療篩檢、通知與轉介 | 醫療服務／QI 工作層 | 臨床 owner 確認試劑、設備、軟體許可與核准用途；研究目的另行分流 |
| PSA／PHI：研究性採血、檢體保存、成效比較、論文或模型研究 | 人體研究；簡易審查為低風險候選 | 採血量、檢體用途、同意、資料欄位及產品許可逐項確認；新器材／新用途或較高風險轉一般審查評估 |
| CRM：預約、提醒、個管、轉診與例行照護 | 照護／行政營運工作層 | 個資法定基礎、最小必要欄位、權限、稽核與委外契約完成 |
| CRM：病人結果、依從性、通知策略、醫事人員行為或模型研究 | 人體研究；簡易審查候選 | 研究問題、資料集、錄音／串接、同意或免同意申請明確化 |
| 碳盤查：能源、設備、耗材、採購與彙總服務量 | 組織營運資料；IRB 原則上不適用 | 維持組織／彙總層，不納入可識別個人行為研究 |
| 碳盤查延伸：員工問卷、訪談、錄影或個人行為介入 | 免審或簡易審查候選 | IRB 依匿名性、可識別性、工作關係壓力與最低風險判定 |

`非人體研究`、`免除審查`、`簡易審查`與`一般審查`是不同狀態。研究主持人可提出路徑建議，正式分類與免審證明由審查會出具。

## 官方規範核對結果

1. 《人體研究法》第 4 條將人體研究定義為取得、調查、分析或運用人體檢體，或個人生物、行為、生理、心理、遺傳、醫學等資訊的研究；第 5 條要求研究開始前完成審查；第 8 條依風險分為一般與簡易程序。現行法頁標示修正日期為 2019-01-02。
2. 衛福部現行「得簡易程序審查」公告列出：符合最低風險前提的低量成人採血、非侵入資料、常規病歷、研究錄音錄影、個人／群體特質或行為等類別。這些是候選範圍，仍由 IRB 審查是否符合。
3. 北市聯醫新案頁要求新案透過 TCHREC 線上系統；頁面仍列 `表09-03-1簡易審查案件範圍核對表_20211201`，同頁其他送審表單已有 2025-10-01 等版本。送件時以 live page 的當日版本建立 manifest，不直接把 7/14 ZIP 視為最新全集。
4. TFDA 醫用軟體指引指出並非所有醫用軟體都是醫療器材，需依功能、用途、使用方法與工作原理綜合判定；無法確認時以個案分類分級判定為準。《醫療器材管理法》第 3 條明列軟體與體外診斷試劑，第 5 條定義醫材臨床試驗，第 37 條規範核准與無顯著風險例外。
5. 《個人資料保護法》第 6 條涵蓋病歷、醫療與健康檢查資料，並列法定職務／義務、研究去識別與書面同意等法定條件。IRB 核准與個資、資安、醫療資訊存取仍是相互連接但各自成立的治理層。

## 建議送審架構

### 1. 非研究／QI 管轄判定包

以一份 2–3 頁 jurisdiction request 分列：常規 PSA 服務、候診系統合成資料開發、CRM 例行個管、碳盤查。每列寫明目的、對象、資料、是否額外介入、輸出用途及是否發表，請院方出具書面判定。

### 2. PSA 篩檢與追蹤研究案

當確定要研究 PSA／PHI、IPSS、病歷、回診或篩檢結果時，建立獨立 protocol。低風險設計先依簡易審查範圍準備；研究用採血、剩餘檢體、未核准試劑／用途或介入風險另行啟動一般審查與 TFDA 判定路徑。

### 3. 門診前系統與 CRM 導入評估案

真實病人／醫師的使用資料、摘要完整性、閱讀時間、工作負擔、接受度、操作紀錄及錄音影像需要獨立可辨識的 protocol section。若整合成一案，仍以分章、分資料集、分同意選項與分 owner 維持同等清楚；若 IRB 認定目的或風險不宜合併，再拆成獨立案件。

### 4. 一般審查／醫材路徑

當 intended use 擴及診斷、治療、急迫分級、自動臨床決策，或研究未核准檢驗／醫材的安全性或效能時，啟動醫療器材分類、一般審查與可能的 TFDA 臨床試驗核准評估。現行 [Intended Use Freeze](../../discovery/INTENDED_USE_FREEZE.md) 將第一版維持在病人自述整理、缺漏提示與醫師覆核摘要，支持目前的低風險工作定位。

## 本週執行清單

| ID | Action | Owner | Due / evidence |
| --- | --- | --- | --- |
| IRB-J01 | 建立 KPI purpose map，每一 KPI 標示 service／QI／research | PI + evaluation owner | 2026-07-31 / signed map |
| IRB-J02 | 建立資料分類與資料流圖：合成、可識別、編碼、去連結、彙總 | data owner + security owner | 2026-07-31 / field manifest + DFD |
| IRB-J03 | 查核 PSA、Free PSA、p2PSA、PHI 的試劑、儀器與軟體許可、用途與限制 | PSA clinical owner | before protocol freeze / license matrix |
| IRB-J04 | 完成四工作包 jurisdiction request 並取得書面判定 | PI + IRB liaison | immediate / written determination |
| IRB-J05 | 依 live TPECH page 建立送件當日表單與版本 manifest | IRB liaison | draft 2026-07-31; submit target 2026-08-05 |
| IRB-J06 | 在書面判定／核准前維持 synthetic-only 與治理設計路徑 | all workstream owners | continuous / access and release log |

## Strong Connections

- [原始筆記](sources/irb-jurisdiction-review-path-user-note-2026-07-14.md)：完整保留使用者提供的問題、推論、分類與參考連結。
- [IRB 表單與 7/14 會議紀錄](line-xinyi-irb-checklists-and-deep-cultivation-meeting-record.md)：連接 7/31 草案、8/5 送審、四子計畫及院內協作時程。
- [source manifest](sources/README.md)：連接三份核對清單、簡易範圍 ODT、26 表單 ZIP 與會議 evidence。
- [Governance Checklist](../../discovery/DEEP_CULTIVATION_GOVERNANCE_CHECKLIST.md)：承接 activation gate、owner、資料與資安治理。
- [Intended Use Freeze](../../discovery/INTENDED_USE_FREEZE.md)與[Safety Boundary](../../core/SAFETY_BOUNDARY.md)：控制候診系統不進入診斷、治療、分流或自主臨床決策。
- [Open Questions](../../meta/open_questions.md)：保留 PI、IRB liaison、資料用途、表單版本與核准證據的未決欄位。

## Current Official References

- [人體研究法（全國法規資料庫）](https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=L0020176)
- [倫理審查委員會得簡易程序審查之人體研究案件範圍（衛福部）](https://www.mohw.gov.tw/dl-16069-71ed79fe-8929-4a85-91b2-56cbafefeb0a.html)
- [臺北市立聯合醫院：新案審查](https://tpech.gov.taipei/News_Content.aspx?n=C219D4DEF1A9AB4F&s=F9375857D3314BB9&sms=018D05F1FE46A114)
- [醫用軟體分類分級參考指引（TFDA）](https://www.fda.gov.tw/tc/includes/GetFile.ashx?id=f637443989833238169)
- [醫療器材管理法（全國法規資料庫）](https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=L0030106)
- [個人資料保護法第 6 條（全國法規資料庫）](https://law.moj.gov.tw/LawClass/LawSingle.aspx?flno=6&pcode=I0050021)

## Evidence Boundary

本檔是 2026-07-14 的工作判定與送審準備依據，提供可執行分類與證據路徑。正式案件類別、免審資格、醫材屬性、臨床試驗核准需求及院內資料使用權限，以北市聯醫 IRB、相關治理單位與 TFDA 的書面結果為準。
