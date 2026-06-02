---
title: "泌尿科門診前問診與醫師覆核摘要支持系統"
subtitle: "正式提案篇排風格之 working discussion proposal v0.7"
author: "工作草稿"
date: "2026-06-01"
lang: zh-TW
---

\newpage

# 臺北市智慧健康城市整合發展計畫

## 子計畫：泌尿科門診前問診與醫師覆核摘要支持系統

### 正式提案篇排風格之 working discussion proposal v0.7

聚焦「門診 / 篩檢追蹤入口、低摩擦症狀蒐集、來源標記（source label）、缺漏欄位可見化、一頁式醫師覆核摘要、staff-review / CRM-ready queue、KPI 評估」之臨床 workflow 實施藍圖。

| 欄位 | 內容 |
| --- | --- |
| 主辦 / 申請單位 | 待 parent proposal owner 確認 |
| 承辦執行單位 | 待院方確認；建議以泌尿科、院外門診部、資訊 / 資安、資料治理與計畫管理角色共同組成 |
| 協辦合作單位 | 待確認；若納入篩檢追蹤、CRM follow-up 或跨單位服務，需另列合作單位與同意文件 |
| 執行期間 | 建議對齊 116-118 年三年期；正式年度由 parent proposal owner 確認 |
| 計畫總預算 | 新臺幣 1,000 萬元整；現階段為 discussion allocation |
| 類別主打 | 範疇三：導入智慧科技醫療 |
| 副支援 | 範疇一：優化醫療工作條件 |
| 目前定位 | working discussion proposal；正式送件前由 parent proposal owner 轉入最新官方 Word template 與院內簽核流程 |

\newpage

# 目錄

一、計畫背景與總體目標
二、現行門診前資訊蒐集與醫師覆核痛點分析
三、門診前問診與醫師覆核摘要支持系統之核心架構
四、低摩擦症狀蒐集與來源標記設計
五、一頁式醫師覆核摘要與缺漏欄位可見化
六、staff-review / CRM-ready queue 與追蹤支持流程
七、目標族群、服務入口與流程嵌入方式
八、AI governance、資安、資料治理、IRB/QI、採購與 FHIR/TW Core IG readiness
九、三年期分年分階段執行步驟與查核里程碑矩陣
十、專案組織架構、技術協同小組職責與跨部門人力分工
十一、臨床安全邊界、資料責任與醫師覆核規範
十二、計畫分年關鍵績效指標 KPI 管理表
十三、經費編列明細總表：新臺幣 1,000 萬元 discussion allocation

\newpage

# 一、計畫背景與總體目標

## 1.1 計畫背景

健康台灣深耕計畫將「優化醫療工作條件」與「導入智慧科技醫療」列為官方核心範疇，並把科技減少無效勞務、提升照護流程效率、資料安全與 FHIR / TW Core IG readiness 納入智慧醫療治理重點。[^policy] 北市聯醫 A2-0048 智慧醫療中心先例也採用跨院區、跨社區與 responsible-AI governance 的整體提案架構，顯示審查語境已從單點 AI 展示，推進到可治理、可維運、可被 KPI 驗收的服務流程改善。[^precedent]

在泌尿科門診情境中，常見主訴包含夜尿、頻尿、尿急、漏尿、小便困難、尿流變弱，以及篩檢後需要追蹤說明的 PSA / screening follow-up 情境。這些資訊常在看診現場才集中整理，醫師需要在有限門診時間內同步掌握主訴、症狀脈絡、持續時間、嚴重度、缺漏資訊、家屬代答內容與 red-flag observation。當資訊來源、缺漏欄位與病人不確定敘述能在門診前被清楚標記，候診時間即可轉化為 visit-readiness，重複問診與臨場補問也能轉為可量測的 workflow improvement。[^friction]

本計畫以「門診前問診與醫師覆核摘要支持」為核心，建立一套可治理的門診前資訊整理 workflow。系統專注於低摩擦症狀蒐集、來源標記（source label）、缺漏欄位與不確定資訊可見化、一頁式醫師覆核摘要，以及 staff-review / CRM-ready queue 欄位準備；診斷、治療決策、急迫性判斷與正式 HIS/EMR 記錄權責保留於院內既有臨床與治理流程。此設計把現場問診負擔轉化為可治理的資訊準備層，讓醫師於看診前快速掌握主訴與追問方向。

本計畫類別主打「範疇三：導入智慧科技醫療」，因為主要工作是建立 governed digital intake、clinician-review summary、audit/version control、AI governance、資安治理與資料治理機制。副支援「範疇一：優化醫療工作條件」，因為此 workflow 直接指向降低重複問診、缺漏補問、摘要整理與 staff follow-up 摩擦。

## 1.2 計畫總體目標

本計畫總體目標是建立一套可由院方治理、可被醫師覆核、可被 KPI 驗收的泌尿科門診前問診與摘要支持 workflow。

| 目標 | 說明 | 驗收方向 |
| --- | --- | --- |
| 建立低摩擦症狀蒐集流程 | 讓病人、家屬或工作人員協助於門診前或候診中完成症狀脈絡填答 | synthetic walkthrough 與 workflow-slot review |
| 產出一頁式醫師覆核摘要 | 將主訴、症狀時間軸、缺漏欄位、來源標記與不確定資訊整理成醫師可快速閱讀的摘要 | summary read time <= 60 秒 |
| 保留來源標記與缺漏欄位 | 每個摘要重點需能標示來源與是否缺漏 | source label 100%；missing-field visibility >= 90% |
| 建立 staff-review / CRM-ready queue | 在治理核准後，支援 care-team review 與 CRM-ready follow-up fields | owner、consent、privacy、procurement、security gates named |
| 建立治理與責任邊界 | 使 AI governance、資安治理、資料治理、IRB/QI、採購治理與 FHIR/TW Core IG readiness 成為計畫主體 | governance owner named |

\newpage

# 二、現行門診前資訊蒐集與醫師覆核痛點分析

## 2.1 現行 workflow 的結構性瓶頸

目前門診前資訊蒐集的核心挑戰，是病人敘述、家屬協助、工作人員補充與追問缺漏在進入醫師覆核前需要更清楚的結構化、來源標記與缺漏可見化。

| 痛點 | 臨床 / workflow 影響 | 本計畫處理方式 |
| --- | --- | --- |
| 重複問診 | 醫師需在短時間內重問主訴、時間軸與症狀嚴重度 | 門診前低摩擦症狀蒐集，將既有等待時間轉成 visit-readiness |
| 來源不明 | 家屬代答、病人自述、工作人員協助內容混在一起 | 來源標記（source label）保留病人、家屬、工作人員協助、ASR-confirmed 等類別 |
| 缺漏欄位不可見 | 醫師需臨場辨識哪些資訊尚未填 | 缺漏欄位集中顯示，並保留 exception log |
| 摘要閱讀負擔 | 長表單與完整問卷需要轉譯為醫師可快速掌握的門診摘要 | 一頁式醫師覆核摘要，驗收摘要閱讀時間 <= 60 秒 |
| staff follow-up 斷點 | 需追蹤或補件的病人資訊需要形成可治理 queue | staff-review / CRM-ready queue 於治理 owner 與 gates 命名後啟用 |
| AI claim 對齊 | AI 工作範圍需和目前 evidence、KPI 與治理責任一致 | 明確定位為 clinician-review support，臨床決策保留於醫師與院內流程 |

## 2.2 提案回應方式

本計畫以可被院方治理的門診 workflow improvement 作為主軸，並將 AI、ASR、CRM、預算與人力支出綁回 workflow、KPI、owner、governance。此設計使計畫能同時回應智慧醫療導入能力與醫療工作條件改善。

\newpage

# 三、門診前問診與醫師覆核摘要支持系統之核心架構

## 3.1 系統核心架構

本系統採三層式 workflow-support 架構，目標是把門診前可蒐集、可整理、可標記的資料提前準備好，讓醫師在既有臨床權責下取得更完整的覆核素材。

| 架構分層 | 核心功能 | 交付價值 |
| --- | --- | --- |
| 病人 / 家屬 / 工作人員協助輸入層 | 低摩擦症狀蒐集、選項式填答、必要時 ASR-assisted input | 降低病人輸入負擔，讓候診時間轉為資訊整理時間 |
| governed intake 與摘要生成層 | 問題路由、source label、缺漏欄位、不確定資訊、summary drafting | 形成可被醫師覆核的一頁式摘要，診斷與治療決策保留於醫師端 |
| clinician / staff review 層 | 醫師確認、修改、忽略或退回；staff-review / CRM-ready queue | 保留臨床權責與 follow-up governance |

## 3.2 服務流程

```text
門診 / 篩檢追蹤入口
-> 低摩擦症狀蒐集
-> 來源標記（source label）/ 缺漏欄位
-> 一頁式醫師覆核摘要
-> staff-review / CRM-ready queue
-> KPI 評估
```

| 流程節點 | 工作內容 | owner / gate |
| --- | --- | --- |
| 門診 / 篩檢追蹤入口 | 報到後、候診中、QR code / tablet 或核准的篩檢追蹤流程 | outpatient workflow owner |
| 低摩擦症狀蒐集 | LUTS / OAB-like 問題、PSA follow-up optional、red-flag observation | urology clinical lead |
| 來源標記（source label）/ 缺漏欄位 | 標示病人、家屬、工作人員協助、ASR-confirmed；顯示未填欄位 | engineering owner + clinical reviewer |
| 一頁式醫師覆核摘要 | 醫師於 60 秒內掌握主訴、脈絡、缺漏、追問方向 | clinician reviewer |
| staff-review / CRM-ready queue | 治理核准後才啟用追蹤欄位與 staff review | service owner + governance owner |
| KPI 評估 | 以 scorecard、audit sample、safety checklist 驗證 | evaluation owner |

\newpage

# 四、低摩擦症狀蒐集與來源標記設計

## 4.1 第一版症狀範圍

第一版以非急性成人泌尿科門診或經核准的篩檢後追蹤流程為主，優先處理下列症狀群：

1. 夜尿、頻尿、尿急、漏尿。
2. 小便困難、尿流變弱。
3. PSA / screening follow-up，於 parent proposal 擁有該服務 route 時納入。
4. patient-reported red-flag observations，供臨床人員依既有 SOP 評估。

## 4.2 來源標記（source label）

每一項可進入摘要的資訊都需保留來源標記（source label），讓病人自述、家屬代答、工作人員協助與 ASR-confirmed transcript 維持清楚層級。

| source label 類別 | 定義 | 摘要呈現方式 |
| --- | --- | --- |
| 病人自述 | 病人本人填答或確認 | 可進入主摘要 |
| 家屬協助 | 家屬代答或協助補充 | 標示為 family-assisted，供醫師覆核 |
| 工作人員協助 | 門診或照護團隊協助輸入 | 標示 staff-assisted，需保留協助脈絡 |
| ASR-confirmed | 語音轉文字後經人確認 | 完成人員確認後進入摘要 |
| 不確定資訊 | 病人不確定、時間不清或描述矛盾 | 顯示為不確定資訊，供醫師追問 |

## 4.3 低摩擦設計原則

低摩擦設計的重點，是讓病人完成核心資訊，並讓醫師快速判斷追問方向。第一版將護理或櫃台工作量控制在例外處理與必要協助，讓 routine labeling 與欄位整理由系統 workflow 承擔。

\newpage

# 五、一頁式醫師覆核摘要與缺漏欄位可見化

## 5.1 一頁式摘要內容

一頁式醫師覆核摘要以門診閱讀為設計核心，保留足夠脈絡，並維持 focused previsit workflow layer 的定位；正式病歷與 EMR 記錄仍由院內既有流程處理。

| 摘要區塊 | 內容 | 安全邊界 |
| --- | --- | --- |
| 主訴與主要症狀 | 夜尿、頻尿、尿急、漏尿、小便困難、尿流變弱等 | 供醫師判讀 |
| 症狀時間軸 | 開始時間、持續時間、變化趨勢 | 供醫師確認治療脈絡 |
| 嚴重度與 bother | 病人感受、影響睡眠或日常活動程度 | 供醫師綜合評估 |
| 來源標記（source label） | 病人、家屬、工作人員協助、ASR-confirmed | 保留資訊責任 |
| 缺漏欄位 | 未填、矛盾或不確定資訊 | 顯示追問方向 |
| patient-reported red-flag observations | 血尿、發燒、腰痛、尿不出等病人觀察 | 供臨床人員依既有 SOP 評估 |
| 醫師覆核動作 | 確認、修改、忽略、退回 | 醫師保留臨床判斷權 |

## 5.2 摘要驗收指標

一頁式摘要的核心驗收，是能否支援醫師快速覆核、精準追問與安全掌握缺漏欄位。

| KPI | 草案目標 | evidence |
| --- | --- | --- |
| summary read time <= 60 秒 | synthetic clinician review 中位數 <= 60 秒，並回報 actual | timed reviewer scorecard |
| clinician usefulness >= 4/5 | clinician reviewer median >= 4/5，未達標則 revise | clinician scorecard |
| missing-field visibility >= 90% | synthetic key missing fields 顯示率 >= 90%，或列出 exception log | missing-field report |
| unsafe wording = 0 | test set 中診斷、治療、自動分流、EMR writeback 語句為 0 | safety checklist |

\newpage

# 六、staff-review / CRM-ready queue 與追蹤支持流程

## 6.1 設計定位

staff-review / CRM-ready queue 是本計畫的延伸支持流程，第一版定位為可治理欄位與流程設計。它把「需要補問、需要追蹤、需要回診或篩檢後追蹤」的資訊整理成可治理 queue，供院方在 owner、consent、privacy、procurement、security gates 命名後使用。

## 6.2 Queue 欄位設計

| 欄位 | 用途 | 啟用條件 |
| --- | --- | --- |
| 病人識別方式 | 連回院內核准流程 | privacy / data governance owner named |
| follow-up reason | 顯示需補問、需回診提醒或篩檢後追蹤原因 | clinical owner confirmed |
| source label | 保留資訊來源與協助型態 | source label completeness 100% |
| missing-field list | 顯示未完成欄位與追問方向 | missing-field visibility >= 90% |
| staff review status | pending、reviewed、returned、closed | staff workflow owner named |
| CRM-ready export | 未來可能轉入 CRM / PRM / follow-up system | procurement、security、consent gates passed |

## 6.3 第一版 claim alignment

第一版 claim 聚焦 CRM-ready field design、staff review 欄位、來源標記、缺漏欄位與醫師覆核摘要。CRM reminders、messaging、queue priority、HIS/EMR 寫入與 production follow-up deployment 進入後續治理階段，需 owner、consent、privacy、procurement、security gates 命名後啟用。

\newpage

# 七、目標族群、服務入口與流程嵌入方式

## 7.1 目標族群

| 目標族群 | 納入理由 | 第一版處理方式 |
| --- | --- | --- |
| 非急性成人泌尿科門診病人 | 症狀資訊可在門診前先整理，降低重複問診 | 報到後或候診中完成低摩擦問診 |
| LUTS / OAB-like 症狀病人 | 症狀脈絡常需多項追問 | 以 governed question routing 整理主訴與缺漏 |
| PSA / screening follow-up 病人 | 若 parent proposal 擁有此服務 route，可形成追蹤入口 | optional；owner 確認後進入核心 claim |
| 需要家屬協助填答者 | 老年或資訊負擔較高者常由家屬協助 | 保留 family-assisted source label |

## 7.2 服務入口

本計畫建議先以三種入口作為院內討論選項：

1. 報到後 QR code / tablet 填答。
2. 候診中由病人或家屬完成短問診。
3. 經核准之篩檢後追蹤入口。

正式導入前，需由 outpatient workflow owner 確認入口設計能保護護理、櫃台與行政端工作量，並將必要協助集中於例外處理。

\newpage

# 八、AI governance、資安、資料治理、IRB/QI、採購與 FHIR/TW Core IG readiness

## 8.1 治理作為核心章節

本計畫主打範疇三，因此治理即是智慧科技醫療導入能力本身。第一版即納入 AI governance、資安治理、資料治理、IRB/QI、採購治理與 FHIR/TW Core IG readiness。

| governance layer | 設計要求 | 目前填法 |
| --- | --- | --- |
| AI governance | AI 支援結構化、缺漏提示、summary drafting、versioning、human-in-the-loop、錯誤處理與 monitoring | 第一版設計要求；owner 待確認 |
| 資安治理 | role-based access、audit log、network exposure、vendor security、incident response | APP / API / ASR / CRM 進入預算前需 IT/security owner |
| 資料治理 | data classification、data minimization、consent、retention、deletion、de-identification、access control | 真實病患資料 route 確認前，採 synthetic / reviewer evidence |
| IRB/QI | 判定 research、QI、service improvement 或 mixed route | real-patient pilot claim 由 IRB/QI route 確認後書寫 |
| 採購治理 | vendor scope、acceptance criteria、資料處理、維護責任、procurement threshold | 正式預算前由 budget / procurement owner 確認 |
| FHIR/TW Core IG readiness | 有資料交換 claim 時才寫 mapping；第一版可寫 future readiness | current HIS/EMR production integration 進入後續治理與串接確認 |

## 8.2 安全邊界

本計畫的安全邊界採取權責保留與治理閘門設計：診斷與治療決策保留於醫師端，急迫性判斷與處置依院內既有 SOP，queue priority、CRM follow-up、HIS/EMR 串接、臨床導入與真實病患資料使用，均由院內治理、資安、資料治理、IRB/QI、採購與臨床責任確認後進入。

\newpage

# 九、三年期分年分階段執行步驟與查核里程碑矩陣

| 年度 / 階段 | 核心目標 | 主要工作 | checkpoint | claim alignment |
| --- | --- | --- | --- | --- |
| 115 prep / 2026-06-02 discussion | 完成 working discussion proposal | v0.7 草稿、正式提案篇排 docx、KPI-budget table、governance owner questions | parent owner discussion | working discussion proposal |
| 116 phase 1 | governed design 與 reviewer evidence | intended use、question set、summary schema、source label、synthetic walkthrough | real-patient route follows approval | reviewer evidence |
| 116 phase 2 | workflow fit 與 staff burden review | workflow slot、staff-friction scorecard、safety wording test | unsafe wording = 0 | clinician-review support |
| 117 phase 3 | limited workflow evaluation if approved | approved pilot/QI route、baseline、clinician scorecards | IRB/QI、privacy、security、procurement gates | approved workflow evidence |
| 117 phase 4 | CRM-ready / ASR readiness review | ASR confirmation、CRM field map、staff-review queue feasibility | 0 unconfirmed ASR content enters summary | CRM-ready design |
| 118 phase 5-6 | 完成三年成果彙整、維運移轉與下一階段擴充準備 | final KPI report、maintenance owner、training record、CRM-ready field package、next-stage governance brief | evidence package、維運責任與下一階段 owner 完成確認 | governed continuation planning |

\newpage

# 十、專案組織架構、技術協同小組職責與跨部門人力分工

## 10.1 組織分工原則

本計畫採 role-based owner 表示，正式姓名、單位與職稱由 parent proposal owner 確認。這樣可維持責任結構的可填報性，同時保留正式填報所需欄位。

| 工作小組 | 主要責任 | 需要 owner |
| --- | --- | --- |
| 臨床與題庫治理小組 | 目標族群、問題集、red-flag observation wording、summary acceptance | Subproject PI / urology clinical lead |
| workflow 與 staff burden 小組 | 報到、候診、staff assist、exception handling、staff-friction review | outpatient workflow owner、nursing / care-team reviewer |
| 工程與 summary schema 小組 | intake、source label、missing-field visibility、一頁式摘要、audit trail | engineering owner |
| AI/data/security governance 小組 | AI governance、資料治理、資安、versioning、retention、access control | IT/security owner、AI/data governance owner |
| IRB/QI 與 evaluation 小組 | research vs QI/service route、baseline、scorecards、annual report | IRB/QI owner、evaluation owner |
| 預算與採購小組 | 正式會計科目、單價、數量、年度、procurement note | budget owner、procurement owner |

## 10.2 目前 owner 狀態

| 角色 | 責任 | 目前狀態 |
| --- | --- | --- |
| Parent proposal owner | 正式提報 route、Word/PDF、簽核、合作單位 | 待確認 |
| Budget owner | 正式會計科目、年度拆分、採購 route | 待確認 |
| Urology clinical lead | 目標族群、問題集、summary acceptance | 待確認 |
| Outpatient workflow owner | 報到、候診、staff assist、exception handling | 待確認 |
| IT/security owner | access control、device/API/security review、audit log | 待確認 |
| AI/data governance owner | model/prompt/rule versioning、retention、transparency | 待確認 |
| IRB/QI owner | research vs QI/service route、real patient-data approval | 待確認 |
| Evaluation owner | baseline、scorecards、KPI evidence、annual report | 待確認 |

\newpage

# 十一、臨床安全邊界、資料責任與醫師覆核規範

## 11.1 醫師覆核責任

本系統產出醫師覆核用 workflow evidence，定位為門診前資訊整理與摘要支持層。SOAP 病歷、正式病歷與 EMR 記錄由醫師與院內既有流程完成；醫師可以確認、修改、忽略或退回摘要內容，系統應保留版本、來源、問題路徑與 review status。

## 11.2 第一版 claim alignment checklist

1. 診斷與治療決策保留於醫師端。
2. 急迫性判斷、分流與處置依院內既有 SOP。
3. Queue priority、CRM reminders 與 messaging 由 owner、consent、privacy、procurement、security gates 命名後啟用。
4. 檢查、藥物與處置開立維持於醫師與院內流程。
5. Production clinical-use approval 由院內治理程序確認。
6. Citywide scale-up 由 site ownership、maintenance plan 與 evidence package 支撐。
7. CRM-ready design 先建立欄位、責任與治理條件，後續再決定 production deployment。
8. 第二版再納入 HIS / EMR / EHR writeback 的系統串接、權限、資料治理與臨床責任確認。

## 11.3 資料責任

| 資料類型 | 第一版處理方式 | 責任邊界 |
| --- | --- | --- |
| synthetic data | 可用於 walkthrough、scorecard、safety wording test | 作為治理核准前的 reviewer evidence |
| patient-reported content | 需完成治理與同意後才可進入真實流程 | clinician review required |
| staff-assisted content | 必須保留 source label | routine labeling work 由系統 workflow 承擔 |
| ASR transcript | 完成人員確認後進入摘要 | 0 unconfirmed ASR content enters summary |
| CRM-ready fields | 需 owner、consent、privacy、procurement、security gates | production deployment follows governance gates |

\newpage

# 十二、計畫分年關鍵績效指標 KPI 管理表

## 12.1 核心 KPI

本計畫核心可驗收 KPI 包含：summary read time <= 60 秒、source label 100%、unsafe wording = 0、missing-field visibility >= 90%、clinician usefulness >= 4/5、governance owner named、KPI-to-budget traceability 100%。

| KPI | baseline / 目前狀態 | 第一年目標 | 第二年目標 | 第三年目標 | evidence |
| --- | --- | --- | --- | --- | --- |
| summary read time <= 60 秒 | 尚未量測 | synthetic clinician review 中 <= 60 秒，並回報 actual | approved workflow if allowed | maintain or improve | timed reviewer scorecard |
| source label 100% | partial design | synthetic summary lines 100% have source label | approved workflow samples 100% if allowed | final evidence sample 100% | audit sample |
| unsafe wording = 0 | target zero | test set 中 diagnosis / treatment / final triage / EMR writeback phrases 為 0 | 0 unresolved safety wording incidents | 0 unresolved safety wording incidents | safety checklist |
| missing-field visibility >= 90% | 尚未量測 | synthetic key missing fields surfaced >= 90%，或列出 exception log | approved workflow measurement if allowed | final exception-aware report | missing-field report |
| clinician usefulness >= 4/5 | 尚未量測 | median >= 4/5 or revise | approved workflow measurement if allowed | final usefulness report | clinician scorecard |
| governance owner named | owner table pending | AI/data/cybersecurity/IRB/procurement owners named 或 pending fields explicit | approvals completed before real-data pilot | maintenance owner named | governance checklist |
| KPI-to-budget traceability 100% | completion gate active | core budget lines 100% map to KPI、owner、evidence、checkpoint | updated during execution | final expense-to-KPI report | KPI-budget table |

## 12.2 KPI 使用原則

KPI 用來支撐審查、執行與年度查核。每一項 KPI 都需有 measurement route、owner、evidence artifact 與年度 checkpoint；技術與預算項目需能連到 KPI，才列為核心預算。

\newpage

# 十三、經費編列明細總表：新臺幣 1,000 萬元 discussion allocation

## 13.1 三年討論配置

| 預算項目 | 第一年 | 第二年 | 第三年 | 合計 | KPI | owner | evidence | procurement note |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| Proposal coordination、PM、RA、KPI evidence | 900,000 | 1,050,000 | 1,050,000 | 3,000,000 | 20 頁討論稿、annual KPI evidence、checkpoint reporting | proposal coordinator / evaluation owner | proposal file、KPI workbook、checkpoint report | 正式前拆成 allowed personnel / service category |
| Intake / summary workflow 與 CRM-ready field design | 1,250,000 | 650,000 | 300,000 | 2,200,000 | summary read time、source label、missing-field visibility | engineering owner | summary schema、synthetic walkthrough、audit sample | vendor / internal / hybrid route pending |
| Clinician、nurse、outpatient workflow reviewer sessions | 400,000 | 400,000 | 300,000 | 1,100,000 | clinician usefulness、staff-friction review、workflow-slot decision | clinical / workflow owners | reviewer scorecards、meeting records | 確認 reviewer support 是否可列支 |
| Security、privacy、AI/data governance、auditability | 450,000 | 300,000 | 150,000 | 900,000 | governance owner named、unsafe wording = 0、audit trail readiness | IT/security、AI/data governance | governance checklist、security review note | 若委外需 vendor security requirement |
| Evaluation、baseline、IRB/QI preparation、limited pilot evidence | 250,000 | 400,000 | 350,000 | 1,000,000 | baseline、approved workflow measurement、final evidence report | evaluation、IRB/QI owners | baseline worksheet、protocol / QI note、evaluation report | real patient-data route pending |
| Conditional equipment / ASR / intake station support | 450,000 | 200,000 | 50,000 | 700,000 | 0 unconfirmed ASR content enters summary、workflow slot feasibility | budget / workflow owners | ASR confirmation test、site-readiness note | tablets、microphones、ASR service must pass procurement and security review |
| Training、documentation、dissemination、review-response package | 150,000 | 100,000 | 250,000 | 500,000 | training completion、review-response readiness | proposal owner | training record、review-response table | only if parent owner funds training / dissemination |
| Administration and contingency within legal accounting rules | 150,000 | 100,000 | 350,000 | 600,000 | expense-to-KPI traceability maintained | budget owner | budget traceability audit | negative-list and accounting-category check required |
| 總計 | 4,000,000 | 3,200,000 | 2,800,000 | 10,000,000 | 100% mapped | parent budget owner | KPI-budget table | official accounting categories pending |

## 13.2 正式預算表必補欄位

正式預算表必須包含：正式會計科目 / 單價 / 數量 / 年度 / KPI / owner / evidence / procurement note。

正式送件前，每一列均需補齊下列欄位。現階段若尚未確認，使用「待正式會計科目確認」與「待確認」，不捏造。

| 預算項目 | 討論配置金額 | 正式會計科目 | 單價 | 數量 | 年度 | KPI | owner | evidence | procurement note |
| --- | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| Proposal coordination、PM、RA、KPI evidence | 3,000,000 | 待正式會計科目確認 | 待確認 | 待確認 | 第 1-3 年 | 20 頁討論稿、annual KPI evidence、checkpoint reporting | proposal coordinator / evaluation owner | proposal file、KPI workbook、checkpoint report | 正式前拆成 allowed personnel / service category |
| Intake / summary workflow 與 CRM-ready field design | 2,200,000 | 待正式會計科目確認 | 待確認 | 待確認 | 第 1-3 年 | summary read time <= 60 秒、source label 100%、missing-field visibility >= 90% | engineering owner | summary schema、synthetic walkthrough、audit sample | vendor / internal / hybrid route pending |
| Clinician、nurse、outpatient workflow reviewer sessions | 1,100,000 | 待正式會計科目確認 | 待確認 | 待確認 | 第 1-3 年 | clinician usefulness >= 4/5、staff-friction review、workflow-slot decision | clinical / workflow owners | reviewer scorecards、meeting records | 確認 reviewer support 是否可列支 |
| Security、privacy、AI/data governance、auditability | 900,000 | 待正式會計科目確認 | 待確認 | 待確認 | 第 1-3 年 | governance owner named、unsafe wording = 0、audit trail readiness | IT/security、AI/data governance | governance checklist、security review note | 若委外需 vendor security requirement |
| Evaluation、baseline、IRB/QI preparation、limited pilot evidence | 1,000,000 | 待正式會計科目確認 | 待確認 | 待確認 | 第 1-3 年 | baseline、approved workflow measurement、final evidence report | evaluation、IRB/QI owners | baseline worksheet、protocol / QI note、evaluation report | real patient-data route pending |
| Conditional equipment / ASR / intake station support | 700,000 | 待正式會計科目確認 | 待確認 | 待確認 | 第 1-3 年 | 0 unconfirmed ASR content enters summary、workflow slot feasibility | budget / workflow owners | ASR confirmation test、site-readiness note | tablets、microphones、ASR service must pass procurement and security review |
| Training、documentation、dissemination、review-response package | 500,000 | 待正式會計科目確認 | 待確認 | 待確認 | 第 1-3 年 | training completion、review-response readiness | proposal owner | training record、review-response table | only if parent owner funds training / dissemination |
| Administration and contingency within legal accounting rules | 600,000 | 待正式會計科目確認 | 待確認 | 待確認 | 第 1-3 年 | expense-to-KPI traceability maintained | budget owner | budget traceability audit | negative-list and accounting-category check required |

## 13.3 仍待院方確認

1. 正式申請單位、PI、共同 / 協同單位、機構代碼與簽核欄位。
2. 是否為 standalone subproject、work package 或 parent proposal appendix。
3. 正式會計科目、單價、數量、年度與採購 threshold。
4. AI governance、資安治理、資料治理、IRB/QI、採購治理 owner。
5. ASR 採 funded item 或 demo-only。
6. CRM 採 CRM-ready only 或 funded follow-up work。
7. real patient-data route 採 no data、QI/service、IRB research 或 mixed route。

\newpage

# 附註：本 working proposal 的使用邊界與參考依據

本文件是正式提案篇排風格之 working discussion proposal。正式送件前需轉入最新官方 Word template，並由 parent proposal owner 確認申請路徑、院內行政欄位、正式會計科目、治理 self-check、附件與簽核程序。

[^policy]: `records/2026-05-19/health-taiwan-deep-cultivation-policy-reference.md`；該檔彙整衛生福利部科技發展組、健康台灣深耕計畫網站與臺灣智慧醫療三大中心公開來源，並記錄「範疇一：優化醫療工作條件」與「範疇三：導入智慧科技醫療」的官方 framing。
[^precedent]: `records/2026-05-21/a2-0048-smart-healthcare-center-precedent/README.md`；該檔保存北市聯醫 A2-0048 智慧醫療中心提案之格式、四大範疇、KPI、governance 與跨單位架構分析。
[^friction]: `discovery/CLINICAL_FRICTION_REDUCTION_ANALYSIS.md`、`discovery/DEEP_CULTIVATION_APPLICATION_DRAFT_V0_6.md`、`discovery/DEEP_CULTIVATION_KPI_BUDGET_ANNUAL_INTEGRATION_TABLE.md`；本工作稿依據這些 repo 內 evidence records 將臨床摩擦、KPI、預算與治理 owner 連結成可填報章節。
