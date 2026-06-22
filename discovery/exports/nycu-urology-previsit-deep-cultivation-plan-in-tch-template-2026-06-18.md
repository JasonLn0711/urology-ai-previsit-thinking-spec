# 「健康台灣深耕計畫」－泌尿科門診前問診與醫師覆核摘要支持系統

狀態：陽明交大團隊內容套入忠孝 / 信義深耕計畫格式之工作稿

日期：2026-06-18

格式來源：`records/2026-06-18/sources/tch-zhongxiao-xinyi-deep-cultivation-plan-revised-2026-06-18.docx`

2026-06-02 official meeting context: 信義母案將「PSA 主動篩檢 + AI 智慧問診」整合提報；AI 智慧問診母案額度約新臺幣 15,000,000 元且包含 CRM。依後續 owner split，本工作稿只承接吳老師 / 陽明交大團隊 AI 問診與醫師覆核摘要工作包，三年新臺幣 10,000,000 元；CRM 由母案 / 其他團隊規劃。

## 封面填報建議

| 欄位 | 建議填法 |
| --- | --- |
| 計畫名稱 | 泌尿科門診前問診與醫師覆核摘要支持系統 |
| 縣市別 | 臺北市 |
| 申請模式 | 建議由主提機構確認；本稿先依忠孝 / 信義範本保留 A / A1 路徑 |
| 計畫範疇 | 主打：導入智慧科技醫療；副支援：優化醫療工作條件 |
| 主提機構 | 待主提單位確認 |
| 合作機構 | 國立陽明交通大學團隊；臺北市立聯合醫院相關院區 / 門診部依主提案確認 |
| 申請經費 | 信義母案 AI 智慧問診約 NT$15M 且包含 CRM；本稿只列吳老師 / 陽明交大 AI-only package，三年新臺幣 10,000,000 元整。正式會計科目待主提單位與 budget owner 確認。 |
| 執行期程 | 待主提案年度定案；本稿先以三年期設計年度工作與 KPI |
| 計畫主持人 | 待主提單位確認 |
| 聯絡人 | 待主提單位確認 |

## 壹、申請單位自我檢核項目表

本工作稿支援主提單位完成格式、範疇、KPI、預算、治理與合作單位內容整合。正式送件前，主提單位需完成資格證明、公職人員利益衝突迴避自主檢核、未重複申請聲明、參與計畫同意書、醫事機構代碼、簽章與函送程序。

陽明交大團隊可提供智慧醫療 workflow 設計、AI/data governance、KPI evidence、問診摘要 schema、prototype / reviewer evidence 與技術文件；正式醫療場域、個資、資安、IRB/QI、採購、委外與病人資料使用由主提單位指定 owner 後啟動。CRM 保留於信義母案 / 其他團隊 workstream，本稿僅呈現本團隊 AI-only 工作包。

## 貳、計畫概要

本子計畫建立泌尿科門診前低摩擦症狀蒐集與醫師覆核摘要支持流程。系統以病人或工作人員協助填答、來源標記、缺漏欄位可見化、一頁式醫師覆核摘要與治理紀錄為核心，協助臨床團隊在看診前掌握主訴、症狀脈絡、追問方向與需補問資訊。

本計畫的主要貢獻是把 AI / APP / ASR / API readiness 放在可治理的門診前資訊整理流程中：AI 支援結構化、缺漏提示、摘要草擬、版本紀錄與人機協作；醫師保留臨床解讀與處置責任；真實病患資料、HIS/EMR 連接、IRB/QI、資安與採購流程，依院內治理與主提單位決策啟用。CRM 由信義母案 / 其他團隊承接，本稿的預算、KPI 與交付範圍聚焦 AI 問診與醫師覆核摘要。

若主提案採用忠孝 / 信義 PSA 社區篩檢路徑，本子計畫可作為「回院或門診前 visit readiness」支援層：病人在看診前完成 guided intake，醫師取得一頁式覆核摘要。PSA SOP、回診追蹤與 CRM 均由臨床或其他團隊處理，本案提供可銜接該母案的門診前資訊準備能力。

## 參、申請單位簡介

陽明交大團隊在本案中擔任智慧醫療工作流、AI 輔助問診、資料治理、KPI evidence 與技術轉譯角色。團隊重點是把泌尿科門診前資訊蒐集與醫師覆核摘要整理成可審查、可驗收、可治理的服務系統，並讓 CRM 等母案追蹤工作可由對應 owner 另行承接。

主提醫療機構提供臨床場域、病人流程、門診工作流、資安與個資治理、IRB/QI 判定、採購與行政送件路徑。正式合作單位、醫事機構代碼、負責人、計畫主持人、聯絡人與簽章文件由主提案 owner 補齊。

## 肆、計畫規劃

### 一、範疇一：優化醫療工作條件

本子計畫透過門診前 guided intake 與一頁式醫師覆核摘要，降低重複問診、臨場補問、缺欄補資料、病人敘述分散與 follow-up 整理負擔。工作流設計聚焦於醫師、護理與櫃台可實際承接的流程，並以 reviewer scorecard 測量摘要可讀性、缺漏欄位可見性與 staff-friction。

### 二、範疇二：規劃多元人才培育

本工作稿可支援 training / documentation / governance readiness。若主提案指定訓練 owner 與預算，可納入臨床 reviewer 教育、AI governance 說明、資料最小化原則、IRB/QI 進場條件、資安與採購注意事項。若未指定 owner，本範疇先保留為支援項，不作核心經費 claim。

### 三、範疇三：導入智慧科技醫療

本計畫主打範疇三。核心建置包括：

- 低摩擦問診入口：病人、家屬或工作人員協助填答。
- ASR optional confirmation：語音輸入僅作為可確認輸入，未確認 transcript 不進入摘要。
- Clinical question governance：以 LUTS / OAB-like 與 PSA follow-up 所需資訊為第一版問題集。
- Source label：標示資訊來源為病人、家屬、工作人員協助或 ASR-confirmed。
- Missing-field visibility：讓醫師看見重要缺漏與不確定資訊。
- 一頁式醫師覆核摘要：提供看診前快速閱讀與修改。
- AI / data / cybersecurity governance：保留版本、錯誤處理、audit trail 與 reviewer evidence。

### 四、範疇四：社會責任醫療永續

本子計畫可支援範疇四的前提，是母計畫另行擁有社區或篩檢服務路徑；本案的貢獻是讓回到泌尿科門診的個案在看診前完成症狀整理，提升醫師覆核效率與資訊完整性，並把社區追蹤、CRM 或病人管理成效留給母案對應 owner 評估。

## 伍、效益評估

### 一、績效指標

| 範疇 | 績效指標 | 衡量或量化基準定義 | 現況數據 | 第一階段達成值 |
| --- | --- | --- | --- | --- |
| 優化醫療工作條件 | 醫師摘要閱讀時間 | 一頁式摘要由 reviewer 計時閱讀 | 待 baseline | synthetic review <= 60 秒，並回報 actual |
| 優化醫療工作條件 | 缺漏欄位可見率 | 重要缺漏欄位被標示數 / 應標示缺漏欄位數 | 待測 | >= 90% |
| 導入智慧科技醫療 | source label 完整率 | 摘要每一項資訊是否有來源標記 | partial design | 100% synthetic summary lines have source label |
| 導入智慧科技醫療 | safety wording | 測試集中診斷、治療建議、自動分流、EMR writeback 等未核准語句 | target zero | 0 unresolved unsafe wording |
| 導入智慧科技醫療 | governance owner named | AI/data/security/IRB/procurement owner 是否命名或 pending 欄位清楚 | owner table pending | owner named or pending fields explicit |
| 導入智慧科技醫療 | AI 問診完成率 | 合成或核准流程中完成最低必要欄位之比例 | 待測 | >= 90% 或列出未完成原因 |

### 二、年度查核點說明

| 階段 | 工作內容 | 查核點 | 累計預定進度 | 查核點說明 |
| --- | --- | --- | ---: | --- |
| 第一年 setup | 建立 intended use、問題集、摘要 schema、source label、synthetic walkthrough | reviewer evidence 完成 | 35% | 不碰真實病患資料前先完成治理設計與測試案例 |
| 第一年 setup | 完成 AI/data/security/IRB/procurement owner table | governance route 可查核 | 45% | 每個資料與技術 claim 有 owner 或 pending 欄位 |
| 第二年 evaluation | 若院內治理核准，進行 limited workflow evidence | clinician usefulness、missing-field visibility、staff-friction review | 75% | 以核准流程評估工作流，不擴張成自動診斷 |
| 第三年 handoff | 完成 KPI evidence、維運責任、訓練紀錄與下一階段治理 brief | final report / maintenance owner | 100% | 形成可交接的 AI 問診與摘要流程 |

## 陸、出國計畫書

本子計畫第一版不以出國研習作為核心工作。若主提案以範疇二納入訓練或國外觀摩，需由 training owner 另列目的、行程、人數、天數、經費與補助比例，並對應人才培育 KPI。

## 柒、經費規劃

本稿以三年新臺幣 10,000,000 元作吳老師 / 陽明交大 AI-only 工作包討論配置。2026-06-02 會議紀錄中的信義 AI 智慧問診母案約新臺幣 15,000,000 元且包含 CRM；CRM 由母案 / 其他團隊承接，不併入下表。正式送件前，主提單位需依健康台灣深耕計畫經費支用標準，轉成正式會計科目、單價、數量、年度、補助款 / 配合款、採購註記與支用說明。

| 預算項目 | 第一年 | 第二年 | 第三年 | 合計 | KPI / evidence | 採購與治理註記 |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| Proposal coordination、PM、RA、KPI evidence | 900,000 | 900,000 | 700,000 | 2,500,000 | proposal package、KPI workbook、annual evidence | 正式前拆成可支用人事 / 業務類別 |
| Clinical workflow review and reviewer sessions | 450,000 | 450,000 | 300,000 | 1,200,000 | clinician usefulness、summary read time、staff-friction review | 確認不增加門診負擔 |
| Question governance、intake flow、summary schema | 1,000,000 | 600,000 | 300,000 | 1,900,000 | question set、completion、missing-field visibility | 不含 CRM |
| AI prototype、summary generation、review evidence | 900,000 | 700,000 | 300,000 | 1,900,000 | prototype evidence、reviewer scorecard | 不承諾 production deployment |
| AI/data/security/privacy governance | 400,000 | 350,000 | 250,000 | 1,000,000 | governance checklist、unsafe wording = 0 | real-data route pending |
| Evaluation、baseline、IRB/QI preparation、limited pilot evidence | 250,000 | 400,000 | 350,000 | 1,000,000 | baseline worksheet、protocol / QI note、evaluation report | real patient-data route pending |
| Optional ASR / intake station readiness | 350,000 | 150,000 | 0 | 500,000 | ASR confirmation safety、workflow feasibility | 僅在 input-burden / accessibility KPI 成立時啟用 |
| 總計 | 4,250,000 | 3,550,000 | 2,200,000 | 10,000,000 | 100% mapped | official accounting categories pending |

## 捌、人力配置表

| 類別 | 姓名 | 現職 | 在本計畫內擔任之具體工作性質、項目及範圍 |
| --- | --- | --- | --- |
| Parent proposal owner | 待確認 | 待確認 | 正式提報 route、Word/PDF、簽核、合作單位 |
| Subproject clinical owner | 待確認 | 泌尿科 / 門診 owner 待確認 | 目標族群、問題集、summary acceptance、clinical boundary |
| Proposal coordinator | 待確認 | 待確認 | 格式整合、版本控管、KPI-to-budget traceability |
| Engineering owner | 待確認 | 陽明交大團隊 | intake、summary schema、versioned implementation evidence |
| AI/data governance owner | 待確認 | 待確認 | prompt / rule versioning、data minimization、auditability |
| IT/security owner | 待確認 | 待確認 | access control、device/API/security review、audit log |
| Evaluation owner | 待確認 | 待確認 | baseline、scorecards、KPI evidence、annual report |
| Budget / procurement owner | 待確認 | 待確認 | AI 問診正式會計科目、年度拆分、採購與委外驗收；不含 CRM |

## 玖、其他

本工作稿保留與忠孝 / 信義 PSA 計畫的銜接能力，也保留陽明交大智慧醫療子計畫的治理邊界。正式送件前需要主提單位確認：

1. 本稿是 standalone subproject、work package，或 parent proposal appendix。
2. 主提機構、合作機構、醫事機構代碼、計畫主持人、聯絡人與簽核流程。
3. 範疇設計是否採「範疇三主打、範疇一副支援、範疇四條件式支援」。
4. 三年 NT$10,000,000 是否維持為 AI 問診與醫師覆核摘要 package 討論額度。
5. ASR、APP/API、intake station 是 funded item、demo-only，或後續採購。
6. 真實病患資料 route 為 no data、QI/service、IRB research，或 mixed route。
7. 採購 threshold、正式會計科目、單價、數量、配合款與 negative-list 檢查。
