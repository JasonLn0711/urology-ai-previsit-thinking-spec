# 115 年健康台灣深耕計畫臨時會議：查核、決策狀態與下一步

Status: source preserved / transcript reviewed / minutes-for-review captured /
official rules verified 2026-07-17 / superseded by 2026-07-22 Xinyi pause

## FIRST PRINCIPLE

- Scarce resource: 團隊注意力、已完成證據的可恢復性，以及未來重啟時的合格醫療群與院方決策證據。
- Canonical home: 本 repo 保存完整逐字稿、查核結果、決策狀態與執行連結。
- Planning role: `planning-everything-track` 只保留 `xinyi_deep_cultivation_application_paused`、容量影響、canonical locator 與下一關卡。
- Evidence path: LINE 原文與會後紀錄 → 校正 ASR 逐字稿 → 官方申請須知／Q&A → 115 年家醫整合計畫 → 院方與主管機關後續書面證據。
- Scope control: 7/17 的社區醫療群路徑保留為可恢復設計；7/22 起信義申請工作暫停，正式送件只由明確重啟決定與完整資格證據共同開啟。
- Next gate: 確認 8/7 報告會是否仍適用信義團隊；未來明確重啟時，再鎖定群員、合作醫院、主提機構與工作包。

## Source manifest

- 會議日期：2026-07-17
- 會議時間：會後紀錄為 14:00–14:25；校正 ASR 約延伸至 14:33，差異待核定版確認。
- 來源性質：ASR 訂正、語意重建、時間戳逐句稿與先前 GPT 查核分析的 agent-readable 合併檔。
- 後續來源：[完整 LINE 紀錄](line-xinyi-application-eligibility-b2-pivot-record.md)中的 14:49 會後紀錄送審訊息、四則照片 placeholder 與兩個附件檔名。
- XLSX 保存副本：[115 年社區醫療群申請書](sources/nhi-taipei-community-medical-group-application-form-115-2026-06-26.xlsx)，SHA-256 `5a6be5103f12d09b8e359187fd049228d6c194639bee1f4866888c3e695cc6d0`。
- PDF 保存副本：[115 年家醫整合照護計畫公告版](sources/nhi-family-physician-integrated-care-program-115-announcement-2026-06-26.pdf)，SHA-256 `6effe3393e230c77c74fcb092c3a0a57566ae51d9d1af3dd7cc2bcac4960a362`，與官網 PDF 相同。
- Repo 副本：[校正逐字稿與原分析](sources/health-taiwan-phase2-emergency-meeting-corrected-asr-agent-readable-2026-07-17.md)
- 原始來源：`/home/jnclaw/Downloads/115年健康台灣深耕計畫臨時會議_ASR訂正版_查核與下一步_agent-readable.md`
- SHA-256：`ad61d90fe99bf5c3ad6848bc81ff92f8aff9cd4a5220218b679def35bd0d4649`
- Fidelity：repo 副本與 Downloads 原檔均為 799 行、54,099 bytes，SHA-256 完全相同；Downloads 原檔保留不動。
- Source boundary：沒有原始音檔，因此逐句語者與低可信詞語仍保留 `推定／待確認`。14:49 紀錄標示「敬請審閱」，可提升主席、紀錄、出席單位與決議的證據層級，核定版仍是下一個 validation layer。

## 2026-07-22 後續狀態

- `confirmed`: 陳美如主任於群組公告，申請仍須以醫療群提出，因此信義深耕計畫暫停。
- `scope change`: 7/17 的 `medical_group_feasibility_assessment_active` 成為歷史狀態；目前為 `xinyi_deep_cultivation_application_paused`。
- `stewardship`: 本紀錄的官方查核、B2 路徑與 action register 完整保留，作為未來明確重啟後的 validation layer。
- `pending confirmation`: 8/7 報告會是否仍需信義團隊出席或提供簡報。

Current source: [7/15–7/22 complete LINE record](../2026-07-22/line-xinyi-deep-cultivation-complete-record-and-pause-status.md).

## 會議建立的核心決策

### 1. 2026-07-17 時點：信義案進入醫療群可行性評估，正式送件決策待定

`00:17:12` 的「信義的部分就先暫停嗎」是一個詢問，後續沒有形成取消決議。結案前 `00:32:22–00:32:42` 的派工，以及 14:49 會後紀錄，建立了以下執行方向：

- 莊美幸主任與吳岳霖主任回報何院長。
- 由院方討論信義案「執行還是不執行」。
- 會後紀錄要求信義院外門診部「盡速評估是否重新成立醫療群」，並以社區醫療群方式提報。
- 後續進度回到 LINE 群組更新。

因此本 repo 採用以下狀態：

```yaml
xinyi_project:
  historical_status_2026_07_17: medical_group_feasibility_assessment_active
  current_status_2026_07_22: xinyi_deep_cultivation_application_paused
  application_submission: pending
  directed_route: B_community_medical_group
  route_activation: deferred_until_explicit_restart
  decision_owner:
    - 何清幼院長
    - 忠孝院區執行團隊
```

7/17 現有證據支持「積極評估新群、送件尚待決定」。7/22 最新公告把 active assessment 更新為暫停；因此目前不啟動新群成立、B2 資格完成或申請送出工作。

### 1.1 會議身分與時間證據更新

- 主席：陳美如主任，`confirmed by minutes-for-review`。
- 紀錄：林宏嶽管理師，`confirmed by minutes-for-review`。
- 出席單位：智慧健康醫療中心、忠孝院區代表、創新永續發展中心、社區健康福祉整合管理中心；這不是個人出席名單。
- 李芋婷於會前因病請假，來源支持其未出席。
- 正式散會時間先採送審紀錄的 14:25；ASR 延伸至約 14:33 的差異保留待核定版校正。

### 2. 會議處理的是申請治理，不是醫療診斷

這次問題發生在申請的第一道門：誰可以合法送件、用哪一個類別、誰能蓋章、如何代表醫療群。計畫內容的臨床價值、AI 功能與 PSA 流程，要在合格申請架構建立後才進入專業審查。

白話流程是：

```text
新群可行性＋院方送件決定
  → 合格社區醫療群與主提機構
  → 正式公文、統編、關防與切結書
  → 醫療群共同服務與預算重寫
  → 主管機關資格／程序審查
  → 計畫內容專業審查
```

A2 是非 A1 醫院或醫師公會的整合案；A3 是非 A1 醫院的獨立案。B2 則可由第一合作醫院、診所或衛生所代表所屬社區醫療群。信義門診部若依健保公開分類屬一般診所，便有 B2 候選路徑，同時仍需完成實際醫療群與機構授權證據。

會後紀錄所寫的「無法以 A 醫療機構名義申請」是中正、信義兩個院外門診部的個案結論。它不是說所有醫療機構都不能申請 A 類；A 類本來就是醫院型計畫，這次卡住的是院外門診部不具 A2／A3 所要求的醫院身分。

### 3. 社區醫療群是一個持續照護網絡

115 年家醫整合計畫的一般組成與運作包含：

- 同一地區至少 5 家健保特約西醫診所，或符合文件所列的聯合診所／特定次醫療區域例外。
- 群內診所的專任醫師專科比例符合規範。
- 與 1–2 家特約醫院建立合作；地區醫院家數另有彈性。
- 由醫事人員提供 24 小時會員諮詢專線。
- 建立上轉、醫院處理結果回傳、回轉原診所與後續追蹤。
- 辦理共同照護、個案研討、社區衛教、會員管理與成效評核。
- 由健保署轄區業務組審核成立與運作；臺北市的窗口是 `臺北業務組`。

所以「成立醫療群」代表五家以上診所與合作醫院承擔長期共同照護責任。它是一個可被查核的醫療服務架構，不是五張同意書或一次性申請外殼。

### 3.1 LINE 會中附件各自解決什麼問題

| 附件 | 白話用途 | 證據邊界 |
| --- | --- | --- |
| `115年家醫計畫社區醫療群申請書.xlsx` | 向健保署臺北業務組申請／異動社區醫療群所需的院所、醫師、專線與合作資料 | 已保存；8 sheets 涵蓋封面、合作／醫師資料、專線、品質與轉診、附件及切結書。官網提供 ODS/XLS，LINE 檔為 XLSX。 |
| `1150626-115年全民健康保險家庭醫師整合性照護計畫(公告).pdf` | 說明醫療群如何組成、運作、轉診、提供專線及接受評核 | 已保存；repo、Downloads 與官網 PDF SHA-256 完全相同。 |

這兩份文件是「先取得並運作醫療群資格」的依據；健康台灣深耕 B 類仍有自己的申請書、主提資格、切結書、KPI 與經費審查。完成家醫醫療群申請，是 B 類路徑的必要治理層，並不自動等於深耕計畫核定。

XLSX 的 8 個工作表可以白話理解為：

- `封面`：誰要申請、群體名稱與基本識別。
- `合作基本資料`：合作醫院與合作單位是誰。
- `醫師基本資料`：確認參與醫師與專科組成符合規範。
- `諮詢專線設置情形`：24 小時專線設在哪裡、由誰接聽。
- `品質及轉診機制`：診所與醫院如何共同照護、上轉、回轉與追蹤。
- `附件一／附件二`：補充醫療品質與實質合作流程。
- `切結書`：由醫療群承諾核心業務、個資與會員照護依規執行。

會後紀錄使用「重新成立醫療群」是本次任務用語；它尚未提供舊群名稱、代碼或法律沿革，因此正式文件仍應以臺北業務組核定的新群／重組結果為準。

### 4. 診所誘因是治理設計的必要條件

逐字稿 `00:05:32–00:06:32` 顯示：既有群對 PSA 計畫的參與價值、400 元性質與分配方式尚不清楚，群內又沒有泌尿科，診所端因而缺少明確誘因。這項訊號應轉成可簽署的分工：

- 診所負責的對象辨識、說明、轉介、結果接收與後續追蹤。
- 門診部／合作醫院負責的專科評估、檢查與處置回傳。
- 可依法申報或由計畫支應的項目、支付依據與分配原則。
- 個資、醫療責任、異常追蹤與未完成轉診的 owner。
- 每家院所的工作量、KPI 與查核證據。

官方家醫計畫明列：申請管理、24 小時專線、轉診追蹤、衛教、共同照護與會員登錄等核心業務，由醫療服務機構承擔。會中 `00:10:53` 所稱「稍微有點角色就可以解套」可轉化為上述實質工作包，讓醫療群的角色可執行、可追蹤、可驗收。

## GPT 分析逐項查核

| 分析主張 | 查核結果 | 採用方式 |
| --- | --- | --- |
| 信義案進入條件式暫停，沒有正式取消 | `refined by 2026-07-22 group notice` | 7/17 曾進入重新成立醫療群可行性評估；7/22 最新狀態為暫停，群組與協助路徑保留。 |
| 會議核心是申請資格與治理 | `confirmed` | 採用；官方 A/B 類資格與逐字稿一致。 |
| B2 可由第一合作醫院、診所或衛生所代表社區醫療群 | `confirmed` | 採用；正式申請時仍需鎖定實際主提。 |
| 新群不是湊到五家就完成 | `confirmed` | 採用；專科比例、合作醫院、專線、轉診與分區業務組核定均為正式要求。 |
| 三家聯醫門診部加兩家外部診所一定可成立新群 | `not confirmed` | 列為臺北業務組書面確認題；公開規則沒有提供此個案的自動通過保證。 |
| 洗腎診所有門診就一定可加入 | `not confirmed` | 院所須先是合格健保特約西醫診所，並納入群體專科比例與完整申請審核；透析服務本身不是充分條件。 |
| 不能都是同一聯醫體系 | `not found in cited central public rules` | 列為臺北業務組個案確認題，不作既定限制。 |
| 7 月 30 日送件、一週完成審核 | `meeting-reported / public confirmation not found` | 保留為承辦口述待書面確認；健康台灣深耕正式截止仍為 2026-08-17。 |
| 臺北市應洽北區業務組 | `corrected` | 正式窗口是健保署臺北業務組；北區業務組轄桃園、新竹、苗栗。 |
| 醫療群不能只是資格外殼 | `confirmed` | 採用；家醫計畫明列核心業務與不得委由非醫療服務機構執行。 |
| 診所誘因是實際瓶頸 | `confirmed as meeting evidence` | 採用為治理需求；`PSA 400 元` 的法源與支付性質仍待確認。 |
| 連江案資格沒有問題 | `meeting working assessment` | 逐字稿明確如此判斷；正式申請機構、類別與文件仍由連江案 owner 完成個案查核。 |
| 中正／華山改走醫療群並縮編 | `confirmed as meeting direction` | CRM 移除／延後，保留社篩系統擴充與肌少症／步態分析；林宏嶽與 Kevin 會後重整。 |
| A2 延續案以既有第一階段項目為主 | `confirmed as meeting direction` | 保留延續性與成果鏈，新增子案另經 owner 與審查風險評估。 |
| B 類固定補助 900 萬元 | `corrected` | 官方為 116–118 年各年上限 990 萬元，實際核定與逐年撥付依審查及成果。 |
| 年終獎金可直接放管理費 | `corrected` | 管理費可列規定內加班費與計畫衍生補充保險費；獎金／津貼是獨立專款項目，限範疇一 1-1／1-2 並依核定制度辦理。 |
| 資本租賃禁止 | `confirmed` | 第二階段經費負面表列第 22 項明列 `資本租賃`。 |
| 語者名單可視為正式出席名單 | `partly resolved` | 主席陳美如、紀錄林宏嶽與四個出席單位已由送審紀錄確認；個人出席名單仍待核定版。 |
| LINE 的公告版 PDF 與官網原檔相同 | `confirmed` | 三方 SHA-256 完全相同。 |
| LINE 的 XLSX 與官網檔逐位元相同 | `not applicable across formats` | LINE 為 XLSX，官網列 ODS/XLS；已確認申請表內容角色與 8 sheets，保留格式差異。 |

## 三個案件與延續案的會議狀態

| 案件 | 2026-07-17 會議狀態 | 證據層級 | 下一關卡 |
| --- | --- | --- | --- |
| 信義 | `xinyi_deep_cultivation_application_paused` | 7/22 群組公告；7/17 送審會後紀錄＋ASR 為歷史路徑 | 確認 8/7 報告要求；未來明確重啟後再啟用醫療群與 B2 資格 checklist。 |
| 中正／華山 | `continue_with_existing_group_and_rescope` | 送審會後紀錄確認中正方向；ASR 提供工作包細節 | 加入既有鄰近醫療群，以每年 990 萬元重整社篩擴充、肌少症／步態。 |
| 連江 | `eligibility_not_blocked_in_meeting` | 主席會中判斷 | 由該案 owner 完成醫院主提與正式申請文件查核。 |
| 既有 A2 延續案 | `continue_reapplication` | 會議方向明確 | 延續第一階段成果鏈，新增工作包由總院與審查策略控制。 |

## 信義醫療群可行性評估的 deferred activation 路徑

送審會後紀錄曾將「重新成立醫療群」列為信義的正式評估方向。7/22 起兩條路徑均保留為未來重啟選項，現在不構成 active assignment。

| 路徑 | 能力 | 啟動證據 | 主要成本／風險 |
| --- | --- | --- | --- |
| 加入既有醫療群 | 沿用既有治理、專線、合作醫院與核定狀態 | 群名、代碼、正式接受、成員名冊、主提與分工 | 需要說清楚診所價值、PSA／AI 工作量、經費與責任。 |
| 成立新醫療群 | 依信義服務需求設計完整群體流程 | 至少五家合格診所或適用例外、專科比例、合作醫院、專線、申請核定 | 找院所、協商利益、建立治理與趕上時程的負荷較高。 |

在現有時程內，加入一個願意實質合作且治理正常的既有群，具有較短的啟動路徑；這是風險與時程判斷，不取代院方與臺北業務組的正式決定。

## Action register

2026-07-22 disposition: `EM-0717-01` 至 `EM-0717-07` 與信義相關的 `EM-0717-09` 轉為 deferred activation checklist；`EM-0717-08` 的中正／華山工作與 `EM-0717-10`、`EM-0717-11` 的來源完整性工作由各自 owner 決定是否續行。新增的 active gate 是 [XY-0722-01](../2026-07-22/line-xinyi-deep-cultivation-complete-record-and-pause-status.md#action-register) 的 8/7 報告確認。

| ID | Action | Owner | Trigger | Completion evidence |
| --- | --- | --- | --- | --- |
| EM-0717-01 | 完成信義重新成立醫療群可行性評估與送件 go/no-go | 何清幼院長＋忠孝／信義執行團隊 | 會後立即 | 候選群員、專科比例、合作醫院、時程與院方核定決策。 |
| EM-0717-02 | 可行時完成新群成立與 B2 申請架構 | 忠孝社區照護／院方行政 owner | EM-0717-01 = go | 群名、代碼、核定狀態、成員、合作醫院、執行中心。 |
| EM-0717-03 | 確認信義門診部或替代主提的 B2 資格 | 計畫主責＋院方行政 | 候選群確定後 | 專案辦公室書面答覆＋代碼、統編、關防、發函／簽約路徑。 |
| EM-0717-04 | 書面確認新群申請期限、審核時程與三加二組合 | 健保署臺北業務組聯絡 owner | 選擇新群路徑時 | email、公文或正式承辦紀錄。 |
| EM-0717-05 | 定義 PSA 400 元的法源、支付對象與分配 | PSA owner＋財務／醫療群 owner | 診所協商前 | 支付規範、試算表與院所同意。 |
| EM-0717-06 | 將 B2 服務寫成轉介、結果回傳、回轉與追蹤 | 臨床／社區照護＋AI／資料 owner | 群體與主提確定後 | workflow、RACI、資料流、KPI/evidence matrix。 |
| EM-0717-07 | 依每年整案上限 990 萬元重編工作包 | budget owner＋各 workstream owner | EM-0717-01 = go | 三年預算、工作包取捨、管理費與獎金／津貼分類檢核。 |
| EM-0717-08 | 重整中正／華山方案 | 林宏嶽＋Kevin | 會後立即 | 社篩擴充＋肌少症／步態範圍、B 類敘事與預算版。 |
| EM-0717-09 | 確認步態分析與陽性個案收案的 IRB／治理路徑 | PI／IRB liaison | 收案設計前 | 研究／服務目的判定、IRB 或治理核定、受試者與人事費依據。 |
| EM-0717-10 | 完成會後紀錄審閱並取得個人出席名單 | 林宏嶽管理師＋會議主席 | 審閱完成時 | 院方核定版；同步校正散會時間與語者姓名。 |
| EM-0717-11 | 取得四張照片；XLSX/PDF 保存與 hash 已完成 | LINE group admin | media available | redacted photo manifest；如需 XLSX 跨格式驗證，再取得官網 ODS/XLS。 |

## Suggested B2 outcome chain

```text
社區診所辨識與初步評估
  → 門診前資料／PSA 需求整理
  → 信義門診部或合作醫院專科服務
  → 檢查與處置結果回傳
  → 回轉原診所
  → 慢性病、預防保健與持續追蹤
```

可衡量 KPI：轉介完成率、結果回傳時效、回轉率、陽性個案後續完成率、持續照護率、重複填寫／檢查下降、門診前資料完整率、醫師行政時間、醫療群實際參與率與病人滿意度。最終指標由確定的醫療群流程、資料可得性與審查要求共同鎖定。

## Connection map

- [7/15–7/22 complete LINE and pause-status record](../2026-07-22/line-xinyi-deep-cultivation-complete-record-and-pause-status.md)：提供目前暫停狀態、群組保留、支援路徑與 8/7 確認 gate。
- [7/16–7/17 LINE 資格中斷與會後紀錄](line-xinyi-application-eligibility-b2-pivot-record.md)：保留會前、會中附件訊號與 14:49 送審紀錄原文；本紀錄據此更新最新狀態。
- [使用者提供的早期 GPT 分析](sources/user-supplied-gpt-analysis-xinyi-eligibility-b2-2026-07-17.md)：提供 LINE 階段制度解釋；本紀錄加入會議決策與經費細節查核。
- [6/2 院外門診部正式會議紀錄](../2026-06-02/outpatient-deep-cultivation-official-meeting-minutes.md)：保存 A-route 母案、原始預算與 owner 歷史；本紀錄提供後續 route scope change。
- [6/23 華山／信義正式會議紀錄](../2026-06-23/taipei-city-hospital-huashan-xinyi-deep-cultivation-official-meeting-minutes.md)：保存合併提案與工作包關係；本紀錄更新其申請主體與整案上限。
- [7/14 正式申請資料包](../2026-07-14/README.md)：保存作業須知與模板；本紀錄決定何時才啟動 B2 欄位與切結書。
- [官方格式 crosswalk](../../discovery/DEEP_CULTIVATION_OFFICIAL_FORMAT_CROSSWALK.md)：把新群可行性、送件決定與 B2 evidence gate 送入表單欄位控制。
- [MOHW compliance rubric](../../discovery/DEEP_CULTIVATION_MOHW_COMPLIANCE_RUBRIC.md)：把院方 go/no-go、主提資格與實質醫療群列為 release gate。
- [Next step](../../discovery/NEXT_STEP.md)：目前保存材料並確認 8/7 報告要求；明確重啟後再啟用醫療群可行性與院方送件 gate。
- [Open questions](../../meta/open_questions.md)：保存臺北業務組、主提、醫療群、400 元與 IRB 的未決證據。
- [Planning project locator](../../../planning-everything-track/data/projects/2026-05-lianyi-deep-cultivation-plan.md)：只鏡像狀態、容量與下一關卡。

## Official sources verified online on 2026-07-17

1. [健康台灣深耕計畫第二階段申請作業須知](https://htsprout.nhri.org.tw/UploadFile/1150713-attach1.pdf)：A/B 資格、B 類每年 990 萬元上限、8 月 17 日期限、經費原則與資本租賃負面表列。
2. [第二階段說明會 Q&A](https://htsprout.nhri.org.tw/UploadFile/1150715-attach2.pdf)：B2 一群一案、分院統編／關防、管理費與獎金／津貼經費分類。
3. [115 年全民健康保險家庭醫師整合性照護計畫](https://www.nhi.gov.tw/ch/dl-99916-05ffb2d8dd25414cbb6f1be0511ee703-1.pdf)：至少五家診所、專科比例、合作醫院、24 小時專線、轉診回轉與核心業務。
4. [健康台灣深耕計畫第二階段公告](https://htsprout.nhri.org.tw/dhplan_11507131400.html)：2026-07-13 至 2026-08-17 的正式申請期間。
5. [健保署臺北業務組服務轄區](https://www.nhi.gov.tw/ch/cp-3330-47420-2343-1.html)：臺北市、新北市、基隆市、宜蘭縣、金門縣與連江縣。
6. [健保署臺北業務組專屬表單](https://www.nhi.gov.tw/ch/cp-3797-5fcae-3303-1.html)：列有 115 年家醫計畫社區醫療群申請書 ODS/XLS。
7. [健保署 115 年家醫整合計畫公告](https://www.nhi.gov.tw/ch/cp-19992-048aa-3258-1.html)：115-06-26 公告與官方附件入口。

## Security and release boundary

本資料包保留決策與制度證據；Webex token、會議編號與密碼不進 tracked files。送審會議紀錄提升主席、紀錄、出席單位與執行方向的證據層級；XLSX/PDF 已保存驗證。個人出席、散會時間差異、四張照片與申請資格在核定版／實體影像／書面回覆到位後完成最終驗證。
