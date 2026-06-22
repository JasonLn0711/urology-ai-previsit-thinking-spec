# 深耕計畫填寫項目定義表：AI 問診與醫師覆核摘要版

狀態：2026-06-19，依廖醫師 PSA 版本格式拆解

用途：讓每個填寫項目各司其職，避免疊床架屋。

## Writing Rule

每一節只回答一個問題：

```text
封面 = 這是什麼案子
概要 = 為什麼值得做
單位簡介 = 誰適合做
計畫規劃 = 要怎麼做
效益評估 = 怎麼證明有用
經費規劃 = 每筆錢買到哪個可驗收工作
人力配置 = 誰負責哪個工作
其他 = 還有哪些 gate / 附件 / 待確認
```

2026-06-02 official meeting minutes add the parent proposal budget context:
信義 AI 智慧問診提報約 NT$15M 且包含 CRM。This item-definition table still
defines the Jason / 陽明交大 AI-only writing package at three-year NT$10M.

## 封面

| 欄位 | 定義 | 本案填寫方向 | 不要寫 |
| --- | --- | --- | --- |
| 計畫名稱 | 一句話說清楚交付內容 | 泌尿科門診前問診與醫師覆核摘要支持系統 | CRM、AI 醫師、智慧診斷 |
| 縣市別 | 主提機構所在地 | 臺北市，待主提單位確認 | 多縣市願景 |
| 申請模式 | 官方 A/B/C/D mode | 依主提單位確認；暫沿用範本 A/A1 | 自行猜測正式模式 |
| 計畫範疇 | 對應 Health Taiwan 類別 | 主打範疇三；副支援範疇一 | 把四大範疇都寫滿 |
| 主提機構 | 正式送件單位 | 待主提單位確認 | 用陽明交大代替醫療機構，除非正式指定 |
| 合作機構 | 實際協作單位 | 國立陽明交通大學團隊；其他依主提案確認 | CRM 團隊 |
| 申請經費 | 本案工作上限 | 三年 NT$10,000,000 討論額度；可註明母案 AI 智慧問診約 NT$15M 含 CRM | 把 CRM 預算列入本團隊工作包 |
| 執行期程 | 官方年度 | 待主提案年度定案 | 任意年度 |
| 主持人 / 聯絡人 | 簽核責任 | 待主提單位確認 | 未授權姓名 |

## 壹、申請單位自我檢核項目表

定義：行政送件檢核，不是技術說明。

本案填寫重點：

- 格式、資格證明、利益衝突、未重複申請、參與同意、簽章由主提單位完成。
- 陽明交大可提供 AI 問診、摘要設計、治理文件、KPI evidence。

不要寫：

- 長篇 AI 技術細節。
- CRM 或病人追蹤。
- 未確認的臨床導入承諾。

## 貳、計畫概要

定義：用一頁內說明「問題、方法、貢獻、範圍」。

本案段落結構：

1. 問題：泌尿科門診前資訊分散、重複問診、缺漏欄位、摘要整理負擔。
2. 方法：AI 問診、source label、missing-field visibility、一頁式醫師覆核摘要。
3. 貢獻：提升 visit readiness，協助醫師快速掌握主訴與追問方向。
4. 範圍：醫師保留診斷與治療責任；本案不做 CRM、不做自動分流、不做 EMR writeback。

不要寫：

- 技術炫耀。
- 癌症偵測率改善。
- 慢病治療成效。
- CRM 追蹤。

## 參、申請單位簡介

定義：說明團隊為何適合執行本案。

本案填寫方向：

- 陽明交大團隊提供 AI 問診、資料治理、摘要 schema、workflow evidence、KPI 設計。
- 醫療機構提供臨床場域、臨床 reviewer、治理 owner、行政送件。

不要寫：

- 把陽明交大寫成臨床決策 owner。
- 把 CRM 團隊或 CRM 建置寫進本案。

## 肆、計畫規劃

定義：說明工作怎麼分、怎麼做、怎麼治理。

### 範疇一：優化醫療工作條件

寫：

- 減少重複問診。
- 減少缺欄補問。
- 一頁式摘要縮短醫師閱讀時間。
- staff-friction review 確認不轉嫁工作。

不要寫：

- 病人管理 CRM。
- 回診提醒。
- 病人黏著度。

### 範疇三：導入智慧科技醫療

寫：

- guided intake。
- source label。
- missing-field visibility。
- AI 摘要草擬。
- version / audit / safety wording。
- optional ASR only if KPI supports it。

不要寫：

- AI 診斷。
- 自動建議檢查。
- 自動分流。
- 自動病歷。
- HIS/EMR writeback。

### 範疇二與範疇四

寫法：

- 範疇二：只有在主提案指定 training owner 時納入。
- 範疇四：只有作為母計畫背景，不把本案寫成社區追蹤或 CRM 服務。

## 伍、效益評估

定義：只寫可以量測的成效。

本案 KPI：

| KPI | 定義 | 衡量方式 |
| --- | --- | --- |
| Summary read time | 醫師讀完一頁摘要所需時間 | timed reviewer scorecard |
| Clinician usefulness | 醫師覺得摘要是否有用 | 1-5 scorecard |
| AI 問診 completion | 最低必要欄位完成或被標示缺漏比例 | synthetic / approved walkthrough |
| Missing-field visibility | 重要缺漏欄位是否被標出 | missing-field report |
| Source-label completeness | 每個摘要欄位是否有來源標記 | audit sample |
| Unsafe wording count | 是否出現診斷 / 治療 / 分流 / EMR 字眼 | safety checklist |
| Staff-friction review | 是否增加護理 / 櫃台負擔 | staff-friction worksheet |

不要寫：

- CRM 留存率。
- 回診完成率。
- 癌症死亡率。
- 三高改善率。
- 治療成效改善。

## 陸、出國計畫書

定義：只有範疇二人才培訓且主提案要求時才填。

本案預設：

```text
不編列。
```

## 柒、經費規劃

定義：把每筆錢連到 KPI、owner、evidence。

本案目前討論配置：

| 預算項目 | 合計 | 定義 |
| --- | ---: | --- |
| Proposal coordination、PM、RA、KPI evidence | 2,500,000 | 提案、KPI、年度 evidence、專家回饋管理 |
| Clinical workflow review and reviewer sessions | 1,200,000 | 醫師 / staff review、summary timing、workflow friction |
| Question governance、intake flow、summary schema | 1,900,000 | 問題集、低摩擦填答、摘要結構 |
| AI 問診與摘要 prototype / implementation evidence | 1,900,000 | prototype、合成案例、audit sample |
| AI/data/security/privacy governance | 1,000,000 | governance checklist、unsafe wording control |
| Evaluation、baseline、QI/IRB preparation | 1,000,000 | baseline、evaluation、final report |
| Optional ASR / intake station readiness | 500,000 | 僅在 input burden / accessibility KPI 成立時啟用 |
| Total | 10,000,000 | AI-only package |

不要寫：

- CRM budget。
- patient messaging。
- production deployment。
- 未對應 KPI 的設備。

## 捌、人力配置表

定義：誰負責哪個工作。

本案角色：

| 角色 | 責任 |
| --- | --- |
| Parent proposal owner | 正式送件、簽核、合作單位 |
| Clinical reviewer | 題組、摘要欄位、usefulness、unsafe wording |
| Workflow owner | 門診 slot、staff-friction、例外流程 |
| Engineering owner | AI 問診流程、摘要 schema、audit sample |
| AI/data governance owner | versioning、source label、資料最小化 |
| IT/security owner | 若進入真實系統或資料，確認 access / security route |
| Evaluation owner | scorecards、KPI workbook、annual evidence |
| Budget owner | 正式會計科目、單價、數量、年度拆分 |

不要列：

- CRM operator。
- CRM vendor。
- CRM maintenance owner。

## 玖、其他

定義：放未決問題、附件、審查回覆準備。

本案應列：

- NT$10M 是否為正式討論上限。
- 第一版 workflow slot。
- 摘要 top 5 fields。
- ASR 是否需要。
- real-data route：no data、QI/service、IRB research、mixed。
- official accounting categories。
- reviewer scorecard package。

不要列：

- CRM team coordination。
- CRM interface。
- CRM procurement。

## 拾至拾參：法定表件與審查意見回覆

定義：行政簽核與 review-response。

本案準備：

- 未重複申請聲明由主提單位完成。
- 參與計畫同意書由主提單位協調。
- 審查意見回覆表可先準備：為何不是 AI 診斷、為何需要 1000 萬、如何驗收、如何保護醫師權責。
