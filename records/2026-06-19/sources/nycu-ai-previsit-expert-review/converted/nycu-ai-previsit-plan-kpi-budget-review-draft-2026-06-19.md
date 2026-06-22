泌尿科門診前問診與醫師覆核摘要支持系統

健康台灣深耕計畫｜計畫內容填寫、KPI 與三年 NT$10,000,000 經費規劃審查版

版本：2026-06-19｜依 package 內容與官方資料核實後整理

## 一、結論與審查策略

建議採「範疇三：導入智慧科技醫療」為主軸，「範疇一：優化醫療工作條件」為副支援。理由很簡單：官方健康台灣深耕計畫明列智慧科技醫療包含 AI 協助臨床、優化醫療照護流程和效率、醫療數據共享和安全；衛福部專區也鼓勵醫療機構提出創新績效指標與具體可行的衡量方式。這使本案以 guided intake、source label、missing-field visibility、一頁式醫師覆核摘要與 AI/data/security governance 作為核心，是合理且可審查的設計。

經費建議維持三年 NT$10,000,000 作為 AI-only 工作額度，不納入 CRM、病人追蹤、HIS/EMR 正式寫回、AI 診斷/治療/分流或國外旅費。這不是保守，而是把評審最容易攻擊的 scope creep 先切掉，集中火力證明：門診前資訊蒐集與醫師覆核摘要可以被治理、被驗收、被量化、被交接。

正式表格應把本稿工作包轉成官方科目：人事費、業務費、設備費，並依「健康台灣深耕計畫經費支用標準」逐項列細目、單價、數量、年度、採購註記與驗收證據。資本門本案規劃約 NT$230,000，占總額 2.3%，低於 30% 上限；其餘以人事、流程治理、資料治理、評估與可租用資訊服務為主。

## 二、封面與基本欄位填寫建議

| 欄位 | 建議填寫 | 審查說服點 / 注意事項 |
| --- | --- | --- |
| 計畫名稱 | 泌尿科門診前問診與醫師覆核摘要支持系統 | 名稱直接扣住門診前問診、醫師覆核與摘要支持，不寫 CRM 或 AI 診斷。 |
| 縣市別 | 臺北市 | 依 package 與忠孝 / 信義母計畫脈絡。 |
| 申請模式 | 由主提單位確認；本稿先保留 A / A1 路徑 | 此欄涉及主提資格與行政路徑，不能由 NYCU 單方定案。 |
| 計畫範疇 | 主：範疇三「導入智慧科技醫療」；副：範疇一「優化醫療工作條件」 | 範疇三支撐 AI、流程效率、資料安全；範疇一支撐降低重複問診與資訊整理負擔。 |
| 主提機構 / PI / 聯絡人 | 待主提單位確認 | 這些是行政責任欄位；正式送件前必須補齊簽章、醫事機構代碼、利益衝突與參與同意文件。 |
| 合作機構 | 國立陽明交通大學團隊；臺北市立聯合醫院相關院區 / 門診部依主提案確認 | NYCU 擔任 AI workflow、資料治理、KPI evidence、schema 與 prototype 支援角色。 |
| 申請經費 | 三年 NT$10,000,000 | AI 問診與醫師覆核摘要 package 額度；正式科目與配合款由 budget owner 轉表。 |
| 執行期程 | 三年期；Y1 setup、Y2 evaluation、Y3 handoff | 配合年度查核點與管考資料。 |

## 三、可直接套入計畫書的內容

## 3.1 計畫概要

本子計畫建立泌尿科門診前低摩擦症狀蒐集與醫師覆核摘要支持流程。系統以病人、家屬或工作人員協助填答、來源標記、缺漏欄位可見化、一頁式醫師覆核摘要與治理紀錄為核心，協助臨床團隊在看診前掌握主訴、症狀脈絡、追問方向與需補問資訊。

本計畫的主要貢獻是把 AI / APP / ASR / API readiness 放在可治理的門診前資訊整理流程中。AI 支援結構化、缺漏提示、摘要草擬、版本紀錄與人機協作；醫師保留臨床解讀、診斷與處置責任；真實病患資料、HIS/EMR 連接、IRB/QI、資安與採購流程，依院內治理與主提單位決策啟用。

若母計畫採用 PSA 社區篩檢或回院路徑，本子計畫可作為 visit readiness 支援層：病人在看診前完成 guided intake，醫師取得一頁式覆核摘要。PSA SOP、CRM、病人追蹤、訊息推播與回診管理，不列入本案承諾。

## 3.2 申請單位簡介與分工

陽明交大團隊在本案中擔任智慧醫療工作流、AI 輔助問診、資料治理、KPI evidence 與技術轉譯角色。團隊重點不是建立自動診斷系統，也不是主責 CRM 建置，而是把泌尿科門診前資訊蒐集與醫師覆核摘要整理成可審查、可驗收、可治理的服務系統。

主提醫療機構提供臨床場域、病人流程、門診工作流、資安與個資治理、IRB/QI 判定、採購與行政送件路徑。正式合作單位、醫事機構代碼、負責人、計畫主持人、聯絡人與簽章文件由主提案 owner 補齊。

## 3.3 計畫規劃：四大範疇寫法

| 範疇 | 建議寫法 | 避免事項 |
| --- | --- | --- |
| 範疇一：優化醫療工作條件 | 寫入 guided intake、一頁式醫師覆核摘要、減少重複問診、補問、缺欄整理與資訊分散。 | 不要承諾醫師人力留任率或門診總量提升，除非母計畫有基線與可歸因設計。 |
| 範疇二：多元人才培育 | 本案可支援 training / documentation / governance readiness；若母計畫指定 training owner，再列 AI governance、資料最小化、IRB/QI、資安課程。 | 第一版不列國外旅費。若要列，需由範疇二 owner 另寫目的、行程、人數、天數、補助比例。 |
| 範疇三：導入智慧科技醫療 | 主打。寫低摩擦問診入口、ASR optional confirmation、question governance、source label、missing-field visibility、一頁式摘要、AI/data/security governance、audit trail。 | 不得寫 AI 診斷、治療建議、自動分流、自動 EMR writeback。 |
| 範疇四：社會責任醫療永續 | 條件式支援：若母計畫有社區或篩檢路徑，本案支援回到門診前的資訊整理。 | 不主張社區追蹤、CRM、長期病人管理成效。 |

## 四、KPI 設計

KPI 要分成三層：第一層是 workflow 可用性，第二層是資料完整性與安全，第三層是治理與年度交付。不要在本期主張癌症死亡率、慢性病結局或長期預後，因為三年門診前摘要流程無法單獨歸因。

| KPI | 定義 | 年度目標 / 門檻 | 對應經費 |
| --- | --- | --- | --- |
| 摘要閱讀時間 | reviewer 開始閱讀至完成初步掌握之秒數；回報 median 與分布 | Y1 design target ≤60秒；Y2/Y3 回報 approved workflow 或 reviewer evidence | W2,W3,W4,W6 |
| 醫師有用性 | 5點量表：摘要是否幫助掌握主訴、時序、追問與缺漏 | median ≥4/5；未達標即回 schema 迭代 | W2,W6 |
| 最低必要欄位完成/標示率 | 最低必要欄位完成，或明確標示 unknown/missing 之比例 | ≥90%；不可把未填當完成 | W3,W4,W6 |
| 缺漏欄位可見率 | 應標示的重要缺漏中，被摘要明確標示之比例 | ≥90%；重大缺漏未顯示即 fail-safe 修改 | W2,W3,W4 |
| source label 完整率 | 每一條摘要資訊皆標示來源：病人、家屬、工作人員、ASR-confirmed 等 | 100%；無來源 AI 推論不得進醫師摘要 | W3,W4,W5 |
| unsafe wording unresolved count | 診斷、治療、自動分流、EMR writeback 等未核准語句 | 0 unresolved；出現即 freeze release | W4,W5 |
| staff-friction pass | 護理、櫃台、醫師端不增加不可接受的重複輸入、點擊、例外處理 | Y1 walkthrough；Y2 一輪改版後通過；Y3 SOP | W2,W3,W7 |
| governance readiness | AI/data/security/IRB/procurement owner 是否命名；進場 route 是否完成 | 未命名 owner 不碰真實資料 | W5,W6 |
| KPI-to-budget mapping | 每一經費列有 KPI、owner、source、evidence | 100%；未映射項目刪除或改列 | ALL |

## 五、經費規劃：三年 NT$10,000,000

經費設計採「工作包＋官方科目轉表」兩層。工作包對評審說明為什麼花錢；官方科目對主計與核銷說明怎麼支用。正式送件前，budget owner 必須把每項轉成健康台灣支用標準的項目名稱、單價、數量、年度、採購與驗收文件。

| 工作包 | 第一年 | 第二年 | 第三年 | 三年合計 | KPI / evidence |
| --- | --- | --- | --- | --- | --- |
| W1 Proposal coordination / PM / RA / KPI evidence | NT$900,000 | NT$900,000 | NT$700,000 | NT$2,500,000 | proposal package、KPI workbook、annual evidence |
| W2 Clinical workflow review / reviewer sessions | NT$450,000 | NT$450,000 | NT$300,000 | NT$1,200,000 | summary read time、clinician usefulness、staff-friction |
| W3 Question governance / intake / summary schema | NT$1,000,000 | NT$600,000 | NT$300,000 | NT$1,900,000 | question bank、source label、missing-field |
| W4 AI prototype / summary generation / review evidence | NT$900,000 | NT$700,000 | NT$300,000 | NT$1,900,000 | prototype、trace log、safety audit |
| W5 AI / data / security / privacy governance | NT$400,000 | NT$350,000 | NT$250,000 | NT$1,000,000 | governance checklist、procurement gate |
| W6 Evaluation / baseline / QI / IRB / limited pilot evidence | NT$250,000 | NT$400,000 | NT$350,000 | NT$1,000,000 | baseline、QI/IRB、evaluation report |
| W7 Optional ASR / intake station readiness | NT$350,000 | NT$150,000 | NT$0 | NT$500,000 | ASR-confirmed、intake station readiness |
| 總計 | NT$4,250,000 | NT$3,550,000 | NT$2,200,000 | NT$10,000,000 | 100% mapped |

## 5.1 官方科目概算

| 官方科目 | 三年概算 | 編列邏輯 |
| --- | --- | --- |
| 人事費 | NT$6,140,000 | PM/RA、KPI/evaluation RA、clinical reviewer protected time、question/schema/AI engineering、QA cycle、evaluation analyst。依支用標準與機構薪資核實。 |
| 業務費 | NT$3,630,000 | 外部審查/出席、文件包、資料蒐集、workflow walkthrough、LLM/API/cloud/ASR 租金或權利使用、治理工作坊、IRB、問卷/訪視等。 |
| 設備費 | NT$230,000 | clinic-owned intake station readiness；若改租用則轉業務費。設備費約占總額 2.3%，低於 30% 資本門上限。 |
| 合計 | NT$10,000,000 | 正式表仍需主提單位確認補助款/配合款、採購門檻、核銷科目與驗收文件。 |

## 5.2 單價依據與審查說服邏輯

| 單價/項目 | 依據與說明 |
| --- | --- |
| PM/RA 60,000/人月 | NSTC 碩士級研究人力最低 41,500/月；健康台灣支用標準要求薪資依申請單位標準核實，並列勞健保、勞退、年終等。60,000/人月是含負擔與專案管理工作的中低估算。 |
| KPI/evaluation RA 45,000/人月 | 接近碩士級研究人力下限，適合 baseline、scorecard、管考資料與 evidence log。 |
| AI engineering 85,000/人月 | AI/software prototype、trace logging、summary schema integration 屬特殊技能。支用標準允許具特殊專長、工作經驗與計畫貢獻者由執行機構訂定標準，經機關首長同意後核實支給。 |
| 臨床 reviewer package 12,500/session | 不是出席費；包含 reviewer protected time、案例閱讀、scorecard coding、缺漏欄位判讀與修正建議。若為外部單純出席，應按每次 2,500 上限；院內計畫人員則列人事或職掌，不能重複領出席費。 |
| 外部專家 2,500/meeting | 按中央政府各機關學校出席費要點上限設計；限非計畫支薪人員、具實質諮詢或審查。 |
| 問卷/訪視 200/份 | 健康台灣支用標準允許每份 50–300；本案採 200 元中位數，用於 clinician/staff survey 或訪談補償。 |
| IRB 100,000/case/year reserve | 涉及人體試驗或人體資料時，IRB 審查費每案以 100,000 為限；若 QI 判定不需 IRB，該預算需經核定轉至 evaluation/QI。 |
| LLM/API/cloud/ASR 10,000/service-month 或 package | 優先以租金/權利使用費處理，避免大量資本門；若為購置軟硬體、程式設計、平台建置，需依正式科目改列設備費或採購。 |
| 設備 230,000 | 僅作 clinic-owned intake station readiness，不列個人手機或個人平板。設備若單價 10,000 以上且使用年限 2 年以上，才列設備費；本案占比低於資本門 30% 上限。 |

## 六、年度查核點與 Go / No-Go

| 年度 | 查核點 | 應交付證據 | Go / No-Go |
| --- | --- | --- | --- |
| Y1 | Intended use / clinical boundary 鎖定 | intended-use 文件、禁止語句清單、CRM out-of-scope 註記 | 未完成不得做真實資料測試 |
| Y1 | Question set + summary schema v1 | 問題集、schema、source label、missing-field 規則 | 未達標不進 reviewer demo |
| Y1 | Synthetic reviewer evidence | 3–5 個 synthetic cases、timed review、scorecard | read time 與 usefulness 未達標則修 schema |
| Y2 | Governance-approved limited workflow evidence | QI/IRB 判定、流程紀錄、臨床 feedback | 未核准真實資料 route 時，改用 workflow simulation |
| Y2 | 模型/摘要安全與 audit | 版本紀錄、audit samples、red-team log | unsafe wording 未清零即 freeze release |
| Y3 | Final evidence package | KPI 報告、失敗案例與修正、維運 owner | 無 maintenance owner 不承諾長期服務 |
| Y3 | Next-stage governance brief | HIS/EMR/API/正式採購條件列表 | 不得把本案自動變成 production EMR writeback |

## 七、評審預答

| 質疑 | 回答 |
| --- | --- |
| 為什麼需要 NT$10M？ | 本案不是單一 chatbot，而是三年治理型門診前資訊流程：臨床問題治理、source label、missing-field、AI摘要、reviewer evidence、資安/資料治理、QI/IRB、年度管考與交接。每一列都有單價、數量、KPI 與 source，不是黑箱軟體費。 |
| 是否會變成 AI 診斷？ | 不會。AI 只做結構化、缺漏提示與摘要草擬；醫師保留判讀、診斷、處置。unsafe wording KPI 要求未核准診斷、治療、分流語句為 0。 |
| CRM 為何不列？ | package 已界定 CRM 由其他團隊處理。本案只做門診前 visit readiness 與醫師覆核摘要。把 CRM 放入會稀釋 scope、擴大採購與資安風險。 |
| KPI 是否太保守？ | 不是保守，而是可驗收。先用 workflow、安全、traceability KPI 建立可信度；Y2 governance 核准後再做 limited workflow evidence。這比空泛宣稱臨床結果更能通過查核。 |
| 摘要閱讀時間 ≤60 秒合理嗎？ | 可作設計目標，正式報告同時回報 actual。若超過 90 秒，必須縮短摘要或調整欄位。 |
| ASR/APP/API 要不要寫？ | 可寫 optional readiness，不可寫成核心成功條件。未確認 transcript 不進摘要；HIS/EMR writeback 不在本期承諾。 |

## 八、正式送件前必須確認

• 主提機構、合作機構、醫事機構代碼、計畫主持人、聯絡人與簽核流程。

• 本稿定位：standalone subproject、work package，或 parent proposal appendix。

• 三年 NT$10,000,000 是否維持為 AI 問診與醫師覆核摘要 package 討論額度。

• 真實病患資料 route：no data、QI/service、IRB research，或 mixed route。

• ASR、APP/API、intake station 是 funded item、demo-only，或後續採購。

• 正式會計科目、配合款、採購門檻、補助款與負面表列檢查。

• 所有 owner：clinical、AI/schema、AI/data governance、IT/security、evaluation、budget/procurement。

## 附錄：本稿使用的外部依據

| 來源 | URL |
| --- | --- |
| 行政院健康臺灣深耕計畫 | https://www.ey.gov.tw/Page/5A8A0CB5B41DA11E/f1618406-1ed7-4e72-bd4f-d1b6faaf8381 |
| 衛福部健康台灣深耕計畫專區 | https://dep.mohw.gov.tw/TDU/cp-1567-82709-121.html |
| 健康台灣深耕計畫經費支用標準（115年4月13日修正） | https://htsprout.nhri.org.tw/UploadFile/0415-attach1.pdf |
| 經費編列注意事項概要說明 | https://htsprout.nhri.org.tw/UploadFile/0915-attach1.pdf |
| 健康台灣深耕計畫下載區 | https://htsprout.nhri.org.tw/download.html |
| NSTC研究人力約用注意事項 | https://law.nstc.gov.tw/LawContent.aspx?id=FL028686 |
| 勞動部歷年最低工資 | https://www.mol.gov.tw/1607/28162/28166/28180/70460/76761/76833/post |
| 中央政府各機關學校出席費及稿費支給要點 | https://www.dbas.taichung.gov.tw/media/900350/%E4%B8%9918%E4%B8%AD%E5%A4%AE%E6%94%BF%E5%BA%9C%E5%90%84%E6%A9%9F%E9%97%9C%E5%AD%B8%E6%A0%A1%E5%87%BA%E5%B8%AD%E8%B2%BB%E5%8F%8A%E7%A8%BF%E8%B2%BB%E6%94%AF%E7%B5%A6%E8%A6%81%E9%BB%9E-1111220%E4%BF%AE%E6%AD%A3-%E5%90%AB%E9%99%84%E4%BB%B6.pdf |
