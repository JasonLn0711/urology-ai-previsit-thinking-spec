---
title: "健康台灣深耕計畫申請書撰寫格式與章節定義規格"
document_type: "ai_agent_readable_markdown_specification"
version_date: "2026-07-09"
language: "zh-Hant-TW"
target_use: "供 AI agent、計畫撰寫者與審稿者撰寫健康台灣深耕計畫申請書"
target_body_page_limit: "核心本文不超過 20 頁；正式附件與簽章表單依官方格式辦理"
official_program: "健康台灣深耕計畫（114-118年）"
official_current_stage: "第二階段（116-118年度）徵求作業已公告重點說明會；正式第二階段計畫書格式若另公告，應優先覆蓋本規格"
basis_level:
  official_required: "以健康台灣深耕計畫官方網站、申請作業須知、計畫書格式、經費使用原則、負面表列及治理自我檢核表為準"
  derived_recommendation: "官方未細定之章節撰寫內容，由本規格依審查權重、表單欄位與計畫撰寫實務補足"
source_uploaded_reference:
  filename: "華山深耕計畫_AI_agent_readable_查核註記版.md"
  role: "作為社區健康促進、智慧篩檢、AI與Health-CRM閉環型計畫的參考樣本；不得機械照抄"
---

# 0. Agent Control Notes

本檔案的用途是把「健康台灣深耕計畫」申請書的官方格式、應填欄位、章節分工、撰寫規則、審查邏輯、20頁內壓縮策略，以及 AI agent 可執行的撰稿規格整合成一份可操作文件。

AI agent 或撰稿者應遵守下列規則：

1. **官方最新版優先。** 若健康台灣深耕計畫官網後續公告第二階段正式計畫書格式、申請作業須知或經費文件，本檔所有格式建議均須以最新版更新。
2. **不得任意改官方章節順序。** 第一階段官方格式明定「請勿任意調整計畫書架構或順序」。第二階段若沿用同樣邏輯，仍應保守遵守。
3. **章節各司其職。** 背景只說問題與缺口；規劃只說方法與步驟；效益只說 KPI 與查核；經費只說金額與編列依據；人力只說角色與分工；其他只放風險、治理、分工、附件索引。
4. **20頁是內部壓縮目標，不是官方上限。** 第一階段官方格式的正文上限為 40 頁，不含封面、目錄、自我檢核表、附件、附錄、利衝表、切結書、同意書及封底。本規格依使用者要求，將核心本文規劃為不超過 20 頁。
5. **所有指標必須可量化、可追蹤、可稽核。** 不得只寫「辦理活動、增加場次、提升滿意度」；需寫分子、分母、基線、目標值、資料來源、頻率與責任人。
6. **涉及人體研究、AI、健康資料、個資、資安者，必須補治理設計。** 包含 IRB、資料治理、AI治理、資安治理、人工覆核、模型卡、資料保存與退出機制。
7. **經費不可含糊。** 每一筆經費須能對應工作包、產出、查核點與KPI；不得重複編列，不得列負數，不得列負面表列項目。
8. **若資訊缺漏，標示 TODO，不得臆測。** 尤其是醫事機構代碼、合作機構、配合款、IRB狀態、既有補助案、採購金額、基線數據與KPI目標。

# 1. Executive Summary

## 1.1 結論

「健康台灣深耕計畫」有官方申請書格式、申請作業須知、線上填報平台操作手冊、經費使用原則、負面表列、AI治理自我檢核表、資安治理自我檢核表、資料治理自我檢核表、管考與查核點填報文件。

截至本規格產出日，官方網站已公告「第二階段（116-118年度）徵求案重點說明會」。若第二階段正式計畫書格式尚未另行公告，撰稿上可先以第一階段官方格式為母板，將年度規劃由 114-118 調整為 116-118；但送件前必須以官方最新公告版本校正。

## 1.2 官方格式的核心章節

官方格式包含下列結構：

1. 申請單位自我檢核項目表
2. 計畫概要
3. 申請機構簡介
4. 計畫規劃
5. 效益評估
6. 出國計畫書
7. 經費規劃
8. 人力配置
9. 其他
10. 公職人員利益衝突迴避自主檢核表
11. 未有重複申請計畫之聲明切結書
12. 參與計畫同意書

## 1.3 撰寫策略

本計畫書不應寫成一般研究計畫，也不應寫成單純採購需求書。它本質上是「政策補助型、執行管考型、可查核成果型」計畫書。

核心寫法是：

```yaml
policy_alignment: "對應四大範疇與18項具體目標"
problem_logic: "現況基線 → 結構性缺口 → 不處理的後果 → 本案介入必要性"
execution_logic: "工作包 → 分年目標 → 季查核點 → 交付物 → KPI"
budget_logic: "經費項目 → 工作包 → 查核點 → 產出 → 效益"
governance_logic: "IRB/個資/資安/AI治理/資料治理/風險控管"
sustainability_logic: "計畫結束後制度化、擴散、維運與財務承接"
```

# 2. Official Source Registry

下表列出本規格使用的主要官方資料。撰稿前應再次檢查官方網站是否有新版。

| source_id | 類型 | 名稱 | URL | 對本規格的用途 |
|---|---|---|---|---|
| OFFICIAL-HT-PORTAL | 官方網站 | 健康台灣深耕計畫網站 | https://htsprout.nhri.org.tw/ | 最新公告、下載專區、聯絡窗口 |
| OFFICIAL-HT-DOWNLOAD | 官方下載 | 下載專區 | https://htsprout.nhri.org.tw/download.html | 計畫書格式、申請作業須知、治理表、經費文件、查核點文件 |
| OFFICIAL-HT-MOHW | 官方說明 | 衛福部科技發展組「健康台灣深耕計畫」專區 | https://dep.mohw.gov.tw/TDU/cp-1567-82709-121.html | 四大範疇、18項具體目標、政策依據 |
| OFFICIAL-HT-PLAN | 官方計畫 | 健康台灣深耕計畫（114-118年） | https://htsprout.nhri.org.tw/dhplan.html | 總期程、總經費、政策目標、由下而上創新作法 |
| OFFICIAL-STAGE2 | 官方公告 | 第二階段（116-118年度）徵求案重點說明會 | https://htsprout.nhri.org.tw/dhplan_11507021633.html | 第二階段徵求作業與說明會資訊 |
| OFFICIAL-LEVEL1-PDF | 官方須知 | 第一階段申請作業須知與附件 | https://htsprout.nhri.org.tw/UploadFile/DHPlan_level1.pdf | 計畫書格式、章節、頁數、IRB、經費上限、審查權重 |
| OFFICIAL-BUDGET-REV | 官方公告 | 經費使用原則暨負面表列項目修訂版 | https://htsprout.nhri.org.tw/dhplan_09231320.html | 經費編列、負面表列、支用標準 |

# 3. Hard Requirements

## 3.1 格式與交件要求

以下為第一階段官方格式明列事項；第二階段若另有新規，依最新版調整。

```yaml
submission_file:
  platform_upload: "合併為 1 個 PDF 檔"
  max_file_size: "小於 25MB"
  pdf_text_extractable: true
  avoid_scanned_image_pdf: true
print_submission:
  print_method: "雙面列印"
  binding: "膠裝"
  copies: "1式6份"
font:
  chinese: "標楷體"
  english_numbers: "Times New Roman"
  body_font_size: "12號字；目錄、標題、表格除外"
line_height: "固定行高 15 點"
margins:
  top: "1.5 cm"
  bottom: "1.5 cm"
  left: "1.5 cm"
  right: "1.5 cm"
  header: "0.5 cm"
  footer: "0.5 cm"
page_number: "須插入頁碼"
official_page_limit_first_stage:
  limit: "40頁"
  print_equivalent: "20張用紙"
  excluded: ["封面", "目錄", "申請單位自我檢核項目表", "附件", "附錄", "公職人員利益衝突迴避自主檢核表", "切結書", "同意書", "封底"]
structure:
  rule: "請勿任意調整計畫書架構或順序"
attachments:
  rule: "計畫書不收參考附件；如須附件說明，於計畫書列明網頁網址或 QR Code"
correction:
  rule: "格式不符者公告補正；須於公告後隔日起算3工作日內完成補正；補正以一次為限"
```

## 3.2 申請模式與期程

```yaml
program_period:
  full_program: "114-118年，5年"
  stage_1: "114-115年"
  stage_2: "116-118年"
application_modes:
  A: "醫療機構"
  B: "社區醫療群"
  C: "衛福部部定專科醫學會"
  D: "各醫事人員法規所定之公會"
stage_2_applicant_types:
  continuation: "第一階段經核定執行者，依第一階段辦理情形保留第二階段申請資格"
  new_application: "第一階段未獲核定執行或未參與者，第二階段另行徵求"
```

## 3.3 人體研究、IRB 與治理要求

```yaml
human_subjects:
  if_involves_human_research: true
  requirement: "須由計畫主持人提出 IRB 申請"
  if_irb_not_yet_approved_at_submission: "應提交 IRB 送審證明"
  before_contract: "須補齊 IRB 核准文件"
  if_irb_not_approved: "未經審查通過及繳附證明前，不予簽約"
data_ai_security:
  official_forms_available:
    - "AI治理自我檢核表"
    - "資安治理自我檢核表"
    - "資料治理自我檢核表"
```

## 3.4 經費硬限制

```yaml
budget_rules:
  budget_basis: "依官方經費使用原則、經費支用標準、負面表列項目編列"
  capex_limit: "資本門原則上以補助經費30%為上限；因計畫需要且敘明理由並經審查同意者例外"
  personnel_cost: "核實編列；包含薪資、勞健保、勞退；除政策調薪或法令因素並經同意外，不得流入"
  separate_account: "應以專帳登錄本計畫經費收支，不得移作他用"
  no_negative_line_items: true
  no_duplicate_funding: true
  procurement: "依政府採購、科研採購及申請單位內部程序辦理"
common_negative_list_examples:
  - "未列於經費細項分配表之項目"
  - "非範疇二之國外出差"
  - "彈性薪資"
  - "經常性維運性質修繕"
  - "一般行政事務性設施"
  - "主持費、管理費、內部場地費"
  - "受補助單位人員出席費、稿費、審查費、工作費、諮詢費、加班費"
  - "一般行政設備與非計畫必要設施"
```

## 3.5 審查導向

官方專業審查權重顯示，計畫書不是比文采，而是比「問題掌握、邏輯、可行性、KPI、公共價值與永續」。

```yaml
written_review_weight:
  plan_concept: "20%"
  fit_completeness_unique_value: "20%"
  kpi_and_measurement: "20%"
  expected_benefit_and_sustainability: "20%"
  policy_alignment_and_public_value: "20%"
key_review_risks:
  - "目標空泛"
  - "只寫活動場次或人次，缺少成果指標"
  - "KPI沒有分子分母、基線與年度目標"
  - "工作包、經費、查核點、KPI無法互相對應"
  - "AI與健康資料缺少倫理、法規、隱私與治理說明"
  - "經費重複編列或編列負面表列項目"
```

# 4. Recommended 20-Page Structure

官方第一階段格式正文上限為 40 頁。本規格依使用者要求，設定「核心本文不超過20頁」。封面、自我檢核、利衝表、切結書、同意書等官方表單可依官方是否排除於頁數外處理；若送件單位要求全檔20頁，則須進一步壓縮附件。

## 4.1 20頁版頁數配置

| 章節 | 建議頁數 | 目的 | 壓縮策略 |
|---|---:|---|---|
| 封面 | 不列入核心20頁 | 官方欄位 | 只填固定欄位，不加敘事 |
| 目錄 | 不列入核心20頁 | 官方固定 | 自動目錄 |
| 壹、申請單位自我檢核表 | 不列入核心20頁 | 合規檢核 | 官方表單照填 |
| 貳、計畫概要 | 2.0 | 說明為何要做 | 只寫政策依據、現況基線、缺口、整體解法、既有補助區隔 |
| 參、申請機構簡介 | 0.5 | 證明有能力做 | 限500字；不要寫歷史沿革 |
| 肆、計畫規劃 | 7.0 | 說明做什麼、怎麼做、分年怎麼推 | 以工作包與分年里程碑表取代長篇敘事 |
| 伍、效益評估 | 4.0 | 說明怎麼判斷成功 | KPI表、季查核點表、資料來源、回饋機制 |
| 陸、出國計畫書 | 0-1.0 | 僅範疇二可填 | 無出國計畫者寫「本計畫無出國計畫」 |
| 柒、經費規劃 | 3.5 | 說明錢怎麼用 | 分年總表、範疇表、重點經費說明、共用資源歸屬 |
| 捌、人力配置 | 1.0 | 說明誰負責 | 角色職責矩陣，不寫履歷全文 |
| 玖、其他 | 2.0 | 放治理、風險、資料、合作分工 | 用表格列風險、資料治理、AI/資安、擴散 |
| 拾-拾貳表單 | 不列入核心20頁 | 簽章合規 | 官方格式照填 |
| **核心本文合計** | **20.0頁以內** |  |  |

## 4.2 若必須全檔20頁內

若院方要求「含表單全檔20頁」，採更激進配置：

```yaml
貳計畫概要: "1.5頁"
參申請機構簡介: "0.5頁"
肆計畫規劃: "6頁"
伍效益評估: "3頁"
陸出國計畫書: "0頁或0.25頁"
柒經費規劃: "2.5頁"
捌人力配置: "1頁"
玖其他: "1.5頁"
官方表單: "壓縮為最少必要頁；不得刪除簽章欄位"
risk: "可能與官方格式頁面完整性衝突，須先詢問專案辦公室"
```

# 5. Chapter Responsibility Map

## 5.1 單一事實來源原則

同一件事只在一個章節詳述，其他章節只引用。

| 資訊類型 | 主章節 | 其他章節如何引用 | 不可重複的內容 |
|---|---|---|---|
| 政策依據、現況、問題 | 貳、計畫概要 | 肆只引用「詳見貳」 | 不在每個子計畫重新講一次政策背景 |
| 申請機構能力 | 參、申請機構簡介 | 捌只列人力角色 | 不把機構歷史塞進計畫規劃 |
| 工作包、方法、流程 | 肆、計畫規劃 | 伍、柒用工作包編號引用 | 不在KPI章重寫方法 |
| KPI、查核點、資料來源 | 伍、效益評估 | 肆只寫「對應KPI」 | 不在計畫規劃章塞滿指標公式 |
| 經費金額、編列依據 | 柒、經費規劃 | 肆只標對應經費類型 | 不在子計畫正文重複金額明細 |
| 人力與分工 | 捌、人力配置 | 肆只標 owner | 不在每個工作包寫完整履歷 |
| 風險、IRB、資安、資料治理、AI治理 | 玖、其他 | 貳/肆只簡述必要性 | 不把治理散落在各章導致不一致 |
| 利衝、切結、同意 | 拾-拾貳 | 自我檢核表勾選 | 不改官方簽章文字 |

## 5.2 章節功能定義

| 章節 | 核心問題 | 撰寫輸出 |
|---|---|---|
| 貳、計畫概要 | 為什麼這個計畫值得補助？ | 政策對應、現況基線、問題缺口、目標、整體解法、既有補助區隔 |
| 參、申請機構簡介 | 為什麼是你們做？ | 機構能力、場域、人力設備、過往成果，500字內 |
| 肆、計畫規劃 | 你們到底怎麼做？ | 範疇別或工作包別規劃、分年目標、方法步驟、產出、依賴關係 |
| 伍、效益評估 | 怎麼知道做成了？ | KPI、量化定義、基線、年度目標、季查核點、資料來源、回饋機制 |
| 陸、出國計畫書 | 是否有範疇二出國培訓？ | 無則明確寫無；有則列目的、內容、行程、經費 |
| 柒、經費規劃 | 每一筆錢是否必要且合規？ | 分年總表、各範疇配置、支用說明、資本門比例、配合款 |
| 捌、人力配置 | 誰負責哪些交付？ | 主持人、協同、子計畫負責人、研究人員、助理之職責矩陣 |
| 玖、其他 | 有哪些不適合放前面但審查必看？ | 風險管理、資料治理、AI治理、資安治理、IRB、合作分工、附件索引 |
| 拾-拾貳 | 法遵與簽章是否完整？ | 利衝自主檢核、無重複申請切結、合作機構同意書 |

# 6. Official Form Item-by-Item Writing Specification

以下逐項定義「要填什麼、不要填什麼、判斷標準」。

## 6.1 封面

```yaml
official_section: "封面"
required_fields:
  - "申請模式"
  - "計畫名稱"
  - "主提機構"
  - "合作機構"
  - "申請經費"
  - "執行期程"
  - "計畫主持人"
  - "聯絡人"
  - "單位、電話、傳真、電子郵件"
fill_this:
  plan_title: "用一句話呈現場域、介入方法、目標結果；避免過度抽象"
  application_mode: "A/B/C/D 僅選一類；合作團隊亦須一致檢核"
  institutions: "填完整機構全銜、醫事機構代碼或立案證書字號、統一編號"
  period: "第二階段建議填116年起至118年12月31日，除非官方另定"
  budget: "填補助經費與配合款；須與柒、經費規劃完全一致"
do_not_fill:
  - "不要放計畫摘要"
  - "不要放宣傳語"
  - "不要寫未確認合作機構"
acceptance_criteria:
  - "封面、申請單位自我檢核、經費表、同意書中的機構名稱一致"
  - "申請模式只選一類"
  - "期程與第二階段公告一致"
```

## 6.2 壹、申請單位自我檢核項目表

```yaml
official_section: "壹、申請單位自我檢核項目表"
purpose: "行政審查前的合規門檻"
fill_this:
  item_1_application_qualification:
    write: "確認申請資格與證明文件齊備"
    evidence: ["醫事機構代碼", "立案證明", "統一編號", "主提機構資格"]
  item_2_format:
    write: "確認依官方格式撰寫"
    evidence: ["章節順序未調整", "字體/頁數/PDF規格符合"]
  item_3_conflict_of_interest:
    write: "完成公職人員利益衝突迴避自主檢核；必要時揭露身分關係"
  item_4_no_duplicate_funding:
    write: "計畫內容與經費未向衛福部、其他部會、地方政府重複申請或重複獲補助"
  item_5_lead_institution_consent:
    write: "合作機構同意由主提機構代表申請，並簽署參與計畫同意書"
  item_6_one_mode_only:
    write: "確認申請單位及合作團隊在4類申請模式中各僅申請1件"
  item_7_same_system_or_alliance:
    write: "列明合作機構是否與主提機構同體系或聯盟；須與封面一致"
do_not_fill:
  - "不要把自我檢核表當成說明章節"
  - "不要用『詳如附件』取代勾選與說明"
acceptance_criteria:
  - "每項均有勾選"
  - "需簽章者已簽章"
  - "合作機構資訊與封面、同意書一致"
```

## 6.3 貳、計畫概要

```yaml
official_section: "貳、計畫概要"
official_hint: "依據、現況及問題分析；需提出與既有政府補助計畫之區隔或可相互接軌之模式"
recommended_length: "2頁"
chapter_role: "說清楚為什麼要做，不寫細部方法、不列經費明細"
required_subsections:
  - "政策依據與對應範疇"
  - "現況基線"
  - "問題分析"
  - "計畫目標"
  - "整體解法摘要"
  - "既有政府補助計畫區隔與接軌"
definition:
  policy_basis:
    write: "本案對應四大範疇中的哪幾項目標；說明與第二階段116-118的關係"
    avoid: "不要把四大範疇全文複製貼上"
  baseline:
    write: "以可查證數據描述現況，例如流程耗時、人力負擔、篩檢覆蓋、追蹤率、系統老舊程度、病人安全或醫療效率問題"
    avoid: "不要只寫『需求日益增加』"
  problem_analysis:
    write: "用3-5個結構性缺口，每個缺口都要有原因、影響、對應工作包"
    formula: "現況 → 缺口 → 後果 → 本案如何處理"
  objective:
    write: "3-5個總目標，每個目標須可被KPI驗證"
  solution_summary:
    write: "一張整體架構表，列工作包、對應範疇、核心產出"
  existing_funding_boundary:
    write: "列出與既有補助案的差異：不同場域、不同對象、不同系統層、不同成果，或說明接軌但不重複"
acceptance_criteria:
  - "讀完本章即可理解問題、必要性、目標與總體架構"
  - "每個問題都能對應到肆的工作包與伍的KPI"
  - "明確寫出不重複補助、不重複建置"
```

## 6.4 參、申請機構簡介

```yaml
official_section: "參、申請機構簡介"
official_hint: "說明各機構執行能力，包括人力、設備、過去相關執行成果等，限500字內"
recommended_length: "0.5頁"
chapter_role: "證明執行能力，不寫計畫內容"
fill_this:
  - "主提機構定位與服務量能"
  - "與本計畫直接相關的人力、設備、資訊系統、場域、社區網絡"
  - "過去相關計畫、篩檢、AI、資安、資料治理或照護整合成果"
  - "合作機構的必要性與互補能力"
do_not_fill:
  - "不要寫完整院史"
  - "不要寫與本案無關的得獎紀錄"
  - "不要重複貳的政策背景"
acceptance_criteria:
  - "500字內"
  - "每一句都能支持『為何此機構能執行本案』"
```

## 6.5 肆、計畫規劃

```yaml
official_section: "肆、計畫規劃"
official_hint: "依範疇說明分年推動目標、架構與策略，含執行方法及步驟"
recommended_length: "7頁"
chapter_role: "本章是執行藍圖；只寫工作包、方法、流程、分年里程碑，不寫KPI公式與經費明細"
preferred_structure:
  option_a_by_scope: "依範疇一至四撰寫，適合多範疇獨立內容"
  option_b_by_work_package: "以工作包為主，並在每個工作包標示對應範疇；適合跨範疇整合型計畫"
recommended_for_integrated_projects: "option_b_by_work_package"
work_package_schema:
  id: "WP1"
  title: "工作包名稱"
  related_scope: ["範疇三", "範疇四"]
  problem_addressed: "對應貳的哪個問題缺口"
  target_population: "服務或研究對象"
  method: "執行方法與流程"
  yearly_milestones:
    "116": "建置/試辦/基線"
    "117": "擴大/驗證/優化"
    "118": "成效/擴散/制度化"
  key_outputs: ["系統", "SOP", "資料集", "儀表板", "課程", "照護流程"]
  dependencies: ["IRB", "採購", "HIS介接", "合作場域"]
  risk_controls: ["備援流程", "資安控管", "人工覆核"]
  owner: "負責角色"
  linked_kpis: ["KPI-01", "KPI-02"]
  linked_budget_lines: ["BUD-01", "BUD-02"]
writing_rules:
  - "每個工作包只解決1-2個問題，不要包山包海"
  - "每個工作包都要有可交付成果"
  - "分年目標要呈現成熟度：建置 → 擴大 → 驗證/擴散"
  - "方法步驟要足以讓審查委員判斷可行性"
  - "涉及AI時，需說明資料、模型、驗證、人工覆核、責任邊界"
  - "涉及醫療流程時，需說明病人安全、導流、臨床確認與異常處理"
do_not_fill:
  - "不要把整體願景在每個工作包重複一次"
  - "不要在本章塞滿KPI計算公式"
  - "不要在本章列詳細單價"
acceptance_criteria:
  - "每個工作包均能對應一個問題、一組查核點、一批經費、一組KPI"
  - "分年目標合理，不集中在最後一年才產出"
```

## 6.6 伍、效益評估

```yaml
official_section: "伍、效益評估"
official_items:
  - "績效指標"
  - "年度查核點說明"
recommended_length: "4頁"
chapter_role: "說明如何判定成功；不重寫方法、不重列預算"
kpi_schema:
  id: "KPI-01"
  scope: "範疇三/範疇四"
  indicator_name: "指標名稱"
  construct: "此指標真正衡量的構念，例如流程效率、照護可近性、資料治理成熟度、病人安全"
  definition: "明確量化定義"
  numerator: "分子"
  denominator: "分母"
  baseline_year: "115或計畫啟動前最近完整年度"
  baseline_value: "現況數據"
  target_values:
    "116": "第一年目標"
    "117": "第二年目標"
    "118": "第三年目標"
  data_source: "HIS/CRM/問卷/查核紀錄/儀表板/人工稽核"
  measurement_frequency: "月/季/半年/年"
  responsible_role: "負責角色"
  exclusion_rules: "排除條件"
  verification_artifact: "可供查核的證據文件"
good_kpi_examples:
  - "異常個案30日內完成首次聯繫率 = 30日內完成首次聯繫之異常個案數 / 當季新開立異常追蹤工單數 × 100%"
  - "AI模型外部驗證敏感度 = 外部驗證集中模型正確判定高風險者 / 外部驗證集中真實高風險者 × 100%"
  - "篩檢流程數位化比例 = 使用電子表單與QR報到完成建檔之人次 / 全部院外篩檢建檔人次 × 100%"
bad_kpi_examples:
  - "辦理宣導活動10場"
  - "提升民眾健康意識"
  - "完成平台建置"
  - "提高滿意度"
bad_kpi_fix:
  event_count: "可以當過程指標，但須搭配成果指標，例如觸達後報到率、異常追蹤完成率、流程等待時間下降"
  platform_completion: "須轉為可驗收功能清單、上線率、使用率、資料品質或流程時間改善"
quarterly_checkpoint_schema:
  year: "116"
  quarter: "Q1"
  work_content: "工作內容"
  checkpoint: "可查核成果"
  cumulative_progress_percent: "年累計預定進度"
  cumulative_budget_spent: "年累計預定支用數"
  checkpoint_description: "查核點說明"
  expected_outcome: "預期成果與效益"
  due_date: "預定完成日期"
checkpoint_rules:
  - "查核點要能提交證據，不只是描述工作"
  - "每季都要有交付物或可衡量進展"
  - "查核點應連到工作包與KPI"
  - "第一年可重建置與基線；第二年應有推廣與效益；第三年應有驗證、擴散、制度化"
acceptance_criteria:
  - "每項KPI都有分子分母、基線、116-118年度目標"
  - "每季查核點都有交付物與預期成果"
  - "KPI與查核點可由資料來源驗證"
```

## 6.7 陸、出國計畫書

```yaml
official_section: "陸、出國計畫書"
official_hint: "限範疇二「規劃多元人才培訓」才可填列"
recommended_length: "0頁；若有則最多1頁"
if_no_overseas_plan:
  write: "本計畫無出國計畫，未編列國外旅費。"
if_has_overseas_plan:
  required_fields:
    - "目的"
    - "詳細內容"
    - "行程"
    - "經費概算"
    - "主題"
    - "會議名稱或培訓內容"
    - "時程"
    - "國別/城市"
    - "參加人員"
    - "經費需求"
  budget_basis:
    - "國外出差旅費報支要點"
    - "中央政府各機關派赴國外各地區出差人員生活費日支數額"
do_not_fill:
  - "非範疇二不得編列國外出差"
  - "不要寫泛泛的參訪交流，須能對應人才培訓目標與回國擴散成果"
```

## 6.8 柒、經費規劃

```yaml
official_section: "柒、經費規劃"
official_items:
  - "分年經費總表"
  - "各範疇經費配置表"
recommended_length: "3.5頁"
chapter_role: "讓審查委員看懂經費必要性、合理性、合規性與不重複性"
budget_line_schema:
  id: "BUD-01"
  year: "116"
  scope: "範疇三"
  work_package_id: "WP1"
  item_name: "經費項目"
  object_class: "人事費/業務費/設備費/其他"
  current_or_capital: "經常門/資本門"
  amount_twd: 0
  unit_price: 0
  quantity: 0
  basis: "單價估算、採購估價、薪資基準、官方支用標準"
  output: "此經費產出的交付物"
  linked_checkpoint: "116-Q2"
  linked_kpi: "KPI-01"
  shared_resource: true
  shared_by: ["WP2", "WP3"]
  duplicate_funding_check: "無重複申請或重複補助"
  negative_list_check: "不屬於負面表列"
  procurement_note: "依政府採購法或科研採購規定辦理"
must_include:
  - "分年補助經費與配合款"
  - "經常門：人事費、業務費"
  - "資本門：設備費"
  - "各範疇經費配置"
  - "資本門比例"
  - "共用資源歸屬表"
  - "重點經費支用說明"
  - "核刪備案或優先序"
common_budget_quality_rules:
  - "每筆經費都要有支用說明或編列基準"
  - "設備費須說明與計畫直接相關，單價一萬元以上且使用年限二年以上"
  - "平台、系統、伺服器、網頁或軟體開發不可誤列為電腦處理費"
  - "IRB審查費可列，但每一人體試驗案以官方上限及核實報支為準"
  - "不得出現負數科目"
  - "不得以『行政管理』吸收大額無明細經費"
  - "共用平台只能由一個工作包或子計畫編列，其他工作包註明沿用"
acceptance_criteria:
  - "總表、範疇表、各子計畫表加總完全一致"
  - "資本門比例符合上限或有例外理由"
  - "所有經費與工作包、查核點、KPI可交叉追蹤"
```

## 6.9 捌、人力配置

```yaml
official_section: "捌、人力配置表"
official_columns:
  - "類別"
  - "姓名"
  - "現職"
  - "在本計畫內擔任之具體工作性質、項目及範圍"
recommended_length: "1頁"
chapter_role: "證明分工清楚、責任可追蹤、專業能力足以完成工作包"
role_schema:
  role_category: "計畫主持人/協同主持人/子計畫負責人/研究人員/助理"
  name: "姓名；未定可填擬聘並標示TODO"
  current_position: "現職"
  assigned_work:
    - "對應工作包"
    - "負責交付物"
    - "負責KPI或查核點"
    - "每週或每月投入方式"
  required_expertise: "醫療/護理/資訊/AI/資安/統計/個管/行政"
  backup_role: "代理或備援"
do_not_fill:
  - "不要貼完整履歷"
  - "不要只寫『協助計畫執行』"
  - "不要讓多人職責完全相同"
acceptance_criteria:
  - "每個工作包都有owner"
  - "每個KPI都有資料與執行負責人"
  - "IRB、資安、資料治理、採購、經費核銷至少有明確窗口"
```

## 6.10 玖、其他

```yaml
official_section: "玖、其他"
recommended_length: "2頁"
chapter_role: "放置審查必看但官方前面無專章之事項"
recommended_subsections:
  - "相關單位分工與配合事項"
  - "風險管理與備援"
  - "資料治理、資安治理、AI治理"
  - "IRB與倫理"
  - "永續維運與擴散"
  - "附件、附錄、外部資料網址或QR Code"
risk_schema:
  risk_id: "RISK-01"
  risk: "風險名稱"
  trigger: "何種情況代表風險發生"
  impact: "對時程、經費、KPI、病安或法遵的影響"
  leading_indicator: "早期預警指標"
  mitigation: "預防措施"
  contingency: "發生後備案"
  owner: "負責角色"
  linked_checkpoint: "116-Q2"
data_governance_schema:
  data_category: "一般個資/特種個資/醫療資料/影像/問卷/系統紀錄"
  purpose: "使用目的"
  legal_or_consent_basis: "法定事由、告知同意、IRB核准"
  identifiability: "可識別/假名化/去識別/彙總"
  storage_location: "院內/雲端/混合"
  access_roles: ["醫師", "護理", "個管", "研究人員", "資訊人員"]
  retention_period: "保存年限"
  deletion_or_exit: "刪除、退出、停止追蹤機制"
  audit_log: "稽核紀錄"
ai_governance_schema:
  model_use: "輔助篩檢/風險分層/行政決策/臨床輔助"
  not_for: "診斷/治療指示/自動分流等禁止或需人工確認事項"
  training_data: "資料來源與代表性"
  validation: "內部/外部/時間切分驗證"
  metrics: ["AUC", "sensitivity", "specificity", "PPV", "NPV", "calibration", "bias analysis"]
  human_oversight: "誰覆核、何時覆核、如何更正"
  model_card: "是否產出模型卡"
  drift_monitoring: "漂移監測與再訓練條件"
security_schema:
  access_control: "角色權限"
  encryption: "傳輸/儲存加密"
  pseudonymization: "HMAC/salt/key management/mapping table separation"
  logging: "存取與異動稽核"
  incident_response: "事件通報與處理"
acceptance_criteria:
  - "足以回答審查委員對資料、AI、資安、IRB、風險與永續的疑問"
  - "不重複前面章節的執行細節"
```

## 6.11 拾、公職人員利益衝突迴避自主檢核表

```yaml
official_section: "拾、公職人員利益衝突迴避自主檢核表"
chapter_role: "法遵表單，不是敘事章節"
fill_this:
  - "申請機構與計畫相關人員是否涉及公職人員利益衝突迴避法之身分關係"
  - "如有，依法揭露"
  - "須由應簽章者完成簽章"
do_not_fill:
  - "不要自行改寫官方法律文字"
  - "不要省略身分關係檢核"
acceptance_criteria:
  - "表單完整"
  - "與自我檢核表第3項一致"
```

## 6.12 拾壹、未有重複申請計畫之聲明切結書

```yaml
official_section: "拾壹、未有重複申請計畫之聲明切結書"
chapter_role: "確認無重複申請或重複獲補助"
fill_this:
  - "主提機構全銜"
  - "合作機構全銜"
  - "計畫主持人簽章"
  - "機構全銜與用印"
  - "日期"
pre_submission_check:
  - "列出所有正在申請或已獲補助之相近計畫"
  - "確認內容、經費、設備、服務對象、場域沒有重複申請"
  - "如為接軌既有計畫，須在貳與柒說清楚邊界"
do_not_fill:
  - "不要簽署前未做內部補助清查"
```

## 6.13 拾貳、參與計畫同意書

```yaml
official_section: "拾貳、參與計畫同意書"
chapter_role: "合作機構正式同意參與主提機構申請"
fill_this:
  - "合作機構全銜"
  - "主提機構全銜"
  - "機構負責人簽章"
  - "機構用印"
  - "日期"
acceptance_criteria:
  - "每一合作機構均有同意書"
  - "合作機構名稱與封面、自我檢核表、分工表一致"
  - "合作內容已在玖或肆明確分工"
```

# 7. Deep Writing Definitions

## 7.1 問題定義

```yaml
problem_definition_formula:
  current_state: "現在怎麼運作，有什麼基線數據"
  gap: "與政策目標、臨床需求、社區需求或治理要求之間的落差"
  cause: "造成落差的根本原因"
  consequence: "不處理會造成什麼風險或成本"
  intervention_need: "為何本計畫是必要且適當的介入"
  linked_work_package: "WP-ID"
```

良好寫法：

> 目前院外篩檢之現場建檔仍仰賴紙本與人工登錄，導致報到等待時間長、資料重複輸入與異常個案追蹤斷點。此缺口使篩檢服務停留在單次活動，難以形成可追蹤的健康管理閉環。本計畫以電子表單、QR報到、HIS介接與CRM追蹤工單建立資料連續性，對應WP1與WP3。

不良寫法：

> 由於社會高齡化，本計畫非常重要，將提升服務品質。

## 7.2 目標定義

```yaml
objective_schema:
  objective_id: "OBJ-01"
  target_group: "服務對象"
  action: "要改變什麼"
  output: "交付什麼"
  outcome: "造成什麼可衡量改善"
  timeframe: "116-118"
  metric: "對應KPI"
```

每個目標都應符合 SMART：

```yaml
specific: "具體"
measurable: "可量化"
achievable: "有資源與時程可達成"
relevant: "對應四大範疇與問題缺口"
time_bound: "有年度與季別"
```

## 7.3 工作包定義

工作包不是章節標題，而是管理單位。每個工作包都必須能被管考。

```yaml
work_package_minimum_fields:
  - "id"
  - "name"
  - "problem_addressed"
  - "scope_alignment"
  - "target_population"
  - "method"
  - "annual_milestones"
  - "quarterly_checkpoints"
  - "deliverables"
  - "owner"
  - "budget_lines"
  - "kpis"
  - "risks"
  - "dependencies"
```

## 7.4 KPI 定義

KPI 必須避免「不可證明」與「不可比較」。

```yaml
kpi_minimum_fields:
  - "indicator_name"
  - "construct"
  - "numerator"
  - "denominator"
  - "baseline"
  - "annual_targets"
  - "data_source"
  - "frequency"
  - "owner"
  - "verification_artifact"
```

KPI分類：

| 類型 | 可用 | 注意 |
|---|---|---|
| 流程效率 | 報到時間、建檔時間、資料回寫時間 | 需有計畫前基線 |
| 服務可近性 | 覆蓋里別、偏鄉/弱勢觸達率 | 需定義母群 |
| 照護品質 | 異常追蹤率、轉介完成率 | 需定義追蹤期間 |
| AI效能 | AUC、敏感度、特異度、校準度 | 需定義驗證集與ground truth |
| 資料治理 | 權限稽核完成率、資料品質錯誤率 | 需有稽核紀錄 |
| 永續擴散 | 制度化流程數、跨院區導入數 | 需避免只計算活動場次 |

## 7.5 查核點定義

查核點不是行程表，而是「可查核的交付證據」。

```yaml
checkpoint_quality_gate:
  evidence_required: true
  not_only_activity_count: true
  linked_to_budget: true
  linked_to_kpi: true
  cumulative_progress_defined: true
  due_date_defined: true
```

良好查核點：

> 116 Q2 完成電子表單、QR報到與身分驗證模組測試，提出測試報告1份；完成試辦場域SOP與資料欄位字典；年累計進度40%。

不良查核點：

> 辦理系統建置與會議。

## 7.6 經費定義

經費審查重點是「必要、合規、合理、可追蹤、不重複」。

```yaml
budget_quality_gate:
  necessary: "沒有這筆錢是否無法完成工作包"
  compliant: "不屬負面表列，符合支用標準"
  reasonable: "單價與數量有依據"
  traceable: "能對應工作包、查核點、交付物"
  non_duplicate: "沒有與其他子計畫、其他補助案重複"
```

# 8. Non-Repetition Policy

## 8.1 禁止重複清單

| 常見重複 | 處理方式 |
|---|---|
| 每章都重講高齡化、智慧醫療、健康台灣 | 只在貳講一次，後文用「本計畫對應前述缺口」 |
| 每個子計畫都重列同一套雲端平台 | 在共用資源表定義一次，其他子計畫寫「沿用WP1共用底層」 |
| KPI在肆與伍都寫完整公式 | 肆只列KPI ID；伍寫完整公式 |
| 經費在工作包與柒都列完整明細 | 工作包只標經費類型與預算ID；柒列完整表 |
| 人力在每個章節都重寫 | 捌集中列職責矩陣 |
| 風險散落各章 | 玖集中列風險管理表；肆僅列關鍵依賴 |
| 資安只用口號到處貼 | 玖用可稽核控制項；其他章只引用 |

## 8.2 交叉引用格式

```yaml
cross_reference_examples:
  - "本工作包對應問題缺口 P-01，詳見貳、二。"
  - "KPI定義詳見伍、KPI-03。"
  - "經費明細詳見柒、BUD-05。"
  - "資料治理與資安控制詳見玖、二。"
```

# 9. Recommended Table of Contents for a ≤20 Page Application

以下為可直接交給撰稿 agent 的目錄框架。

```markdown
# 健康台灣深耕計畫（116-118年度）計畫申請書

## 封面
- 申請模式：
- 計畫名稱：
- 主提機構：
- 合作機構：
- 申請經費：
- 執行期程：
- 計畫主持人：
- 聯絡人：

## 目錄

## 壹、申請單位自我檢核項目表
（依官方表格填列）

## 貳、計畫概要
### 一、政策依據與對應範疇
### 二、現況基線與問題分析
### 三、計畫目標
### 四、整體解法與工作包架構
### 五、與既有政府補助計畫之區隔或接軌

## 參、申請機構簡介
### 一、主提機構能力
### 二、合作機構能力與互補分工

## 肆、計畫規劃
### 一、整體架構與服務/資料流
### 二、工作包一：〔名稱〕
### 三、工作包二：〔名稱〕
### 四、工作包三：〔名稱〕
### 五、分年推動策略與里程碑
### 六、關鍵依賴與執行方法

## 伍、效益評估
### 一、績效指標總表
### 二、年度查核點表
### 三、資料來源與衡量方法
### 四、滾動修正與PDCA機制

## 陸、出國計畫書
（無則填：本計畫無出國計畫，未編列國外旅費。）

## 柒、經費規劃
### 一、分年經費總表
### 二、各範疇經費配置表
### 三、主要經費項目與編列依據
### 四、共用資源歸屬與避免重複編列
### 五、經費核刪優先序與最低可行版本

## 捌、人力配置
### 一、人力配置表
### 二、角色責任矩陣

## 玖、其他
### 一、合作單位分工與配合事項
### 二、風險管理與備援
### 三、IRB、資料治理、資安治理與AI治理
### 四、永續維運與擴散模式
### 五、附件網址或QR Code索引

## 拾、公職人員利益衝突迴避自主檢核表
（依官方表格填列）

## 拾壹、未有重複申請計畫之聲明切結書
（依官方表格簽章）

## 拾貳、參與計畫同意書
（每一合作機構均須簽署）
```

# 10. Guidance for Community Health / AI / CRM Integrated Plans

本節參考上傳之華山院區計畫樣本的結構邏輯，作為「社區健康促進＋智慧篩檢＋AI風險分層＋CRM閉環照護」類型計畫的撰寫建議。該樣本採三子計畫結構：子計畫一建立數位篩檢平台、健康艙、Power BI與共用資安底層；子計畫二建立AI肌少症/功能衰退/跌倒風險分層與LINE/LIFF追蹤；子計畫三建立Health-CRM與PDCA追蹤導流閉環。此種設計的優點是能把「流程數位化、風險智慧化、關係管理化」串成單一服務閉環，而非三個互不相干的採購案。

## 10.1 建議架構

```yaml
integrated_plan_architecture:
  WP1_shared_digital_screening:
    role: "共用資料、流程、篩檢平台、身分驗證、電子表單、HIS介接"
    should_own: ["共用雲端/地端架構", "資安底層", "Power BI底層", "健康量測節點"]
    should_not_own: ["AI模型責任", "長期個管營運"]
  WP2_ai_risk_stratification:
    role: "AI輔助篩檢、風險分層、模型驗證、人工覆核"
    should_own: ["資料字典", "模型卡", "驗證設計", "分流SOP", "高風險樣本設計"]
    should_not_own: ["全院CRM主檔", "四癌政策資格總責"]
  WP3_health_crm_closed_loop:
    role: "招募、觸達、追蹤工單、導流、再篩、PDCA"
    should_own: ["CRM主檔", "追蹤工單", "個案生命週期", "盲區改善", "再篩回流"]
    should_not_own: ["重複建置LINE/Power BI底層"]
```

## 10.2 共用資源歸屬表

| 共用資源 | 建議歸屬 | 其他工作包處理方式 |
|---|---|---|
| 雲端/地端資料平台 | WP1 | WP2/WP3沿用，不重複編列 |
| 資安架構 | WP1 | 全計畫共用，玖章統一描述 |
| Power BI底層 | WP1 | WP3做增量模組，不重複買底層 |
| 健康量測站/健康艙 | WP1 | WP2使用量測資料，不重複購置 |
| LINE/LIFF入口 | WP2 | WP3沿用作觸達通路 |
| CRM主檔 | WP3 | WP1/WP2回寫資料，不各自建主檔 |
| IRB與資料治理 | 依資料與研究範圍分責 | 玖章統一呈現，避免矛盾 |

## 10.3 送件前必修風險

此類AI與健康資料計畫，審查風險通常不在創意，而在可稽核性。送件前至少修正下列事項：

```yaml
critical_fix_queue:
  - issue: "篩檢政策與服務對象"
    action: "若寫依國健署癌症篩檢政策，須用最新版資格條件；若本案只做四癌，須說明肺癌LDCT不納入本案範圍或依院方核定辦理"
  - issue: "IRB時序"
    action: "IRB核准前不得寫成正式前瞻收案；可寫場域洽談、MOU、SOP、資料字典、教育訓練"
  - issue: "Power BI/Gateway資料出院表述"
    action: "不要直接宣稱特種個資絕對不出院；須寫清楚DirectQuery/Import、資料集、彙總、去識別、權限與稽核"
  - issue: "SHA-256去識別化"
    action: "避免單純hash；改寫為HMAC-SHA-256或加鹽雜湊、金鑰分離、mapping table隔離、最小必要欄位"
  - issue: "AI模型"
    action: "補模型卡、資料集代表性、ground truth、外部驗證、敏感度/特異度、校準、偏差分析、人工覆核"
  - issue: "經費"
    action: "不得有負數科目；不得把平台/伺服器/網頁架設錯列電腦處理費；共用資源不得重複編列"
```

# 11. Submission Quality Gates

送件前逐項檢查。

## 11.1 行政格式

```yaml
format_gate:
  - "[ ] 使用官方最新版格式"
  - "[ ] 章節順序未任意調整"
  - "[ ] PDF小於25MB"
  - "[ ] PDF可擷取文字，非掃描圖片"
  - "[ ] 字體、行高、邊界、頁碼符合規定"
  - "[ ] 頁數符合官方上限與內部20頁目標"
  - "[ ] 正式函文、線上填報、書面份數符合公告"
```

## 11.2 內容邏輯

```yaml
logic_gate:
  - "[ ] 貳章有現況基線、問題缺口、既有補助區隔"
  - "[ ] 肆章每個工作包都有目標、方法、產出、owner、年度里程碑"
  - "[ ] 伍章每個KPI都有公式、基線、116-118目標、資料來源、責任人"
  - "[ ] 每季查核點都有可提交證據"
  - "[ ] 經費、工作包、KPI、查核點可以互相對應"
  - "[ ] 人力分工沒有重疊或責任空洞"
  - "[ ] 風險與備案具體，不是口號"
```

## 11.3 經費與補助

```yaml
budget_gate:
  - "[ ] 分年經費總表加總正確"
  - "[ ] 各範疇經費配置表加總正確"
  - "[ ] 資本門比例符合30%上限或已有例外理由"
  - "[ ] 沒有負數科目"
  - "[ ] 沒有負面表列項目"
  - "[ ] 沒有重複申請或重複編列"
  - "[ ] 每筆經費有支用說明或編列基準"
  - "[ ] 共用資源只由單一工作包編列"
  - "[ ] 若有配合款，來源與比例清楚"
```

## 11.4 IRB、資料、AI、資安

```yaml
governance_gate:
  - "[ ] 人體研究已判定是否需IRB"
  - "[ ] 需IRB者已送審或取得核准；核准前工作內容未寫成正式收案"
  - "[ ] 個資與健康資料有告知、同意、目的、保存、退出與刪除機制"
  - "[ ] AI輸出定位清楚：輔助、非診斷、需人工確認"
  - "[ ] AI模型有模型卡、驗證設計、偏差分析與漂移監測"
  - "[ ] 資安架構有權限、加密、稽核、事件通報"
  - "[ ] 假名化/去識別化方法能防低熵欄位字典攻擊"
```

## 11.5 簽章與合作

```yaml
signature_gate:
  - "[ ] 公職人員利益衝突迴避自主檢核表完整"
  - "[ ] 未有重複申請計畫之聲明切結書已簽章"
  - "[ ] 每一合作機構均有參與計畫同意書"
  - "[ ] 合作機構名稱在封面、自我檢核表、同意書、分工表一致"
  - "[ ] 主提機構與合作機構權責明確"
```

# 12. AI Agent Output Contract

## 12.1 Input Required from Human Owner

AI agent 開始撰寫前，應向 owner 收集下列資料；若缺漏，使用 `TODO:` 標示，不得臆測。

```yaml
required_inputs:
  administrative:
    - "申請模式"
    - "主提機構全銜、醫事機構代碼、統一編號"
    - "合作機構全銜與代碼"
    - "計畫主持人、聯絡人、職稱、電話、email"
    - "申請經費、配合款、執行期程"
  planning:
    - "計畫名稱"
    - "對應範疇與目標"
    - "現況基線數據"
    - "既有政府補助案清單"
    - "工作包或子計畫構想"
    - "目標服務對象與場域"
  execution:
    - "採購項目與估價"
    - "資訊系統介接需求"
    - "人力配置與薪資基準"
    - "合作單位分工"
  governance:
    - "是否涉及人體研究"
    - "IRB狀態"
    - "個資/健康資料類型"
    - "AI模型用途"
    - "資安架構"
  evaluation:
    - "KPI基線"
    - "年度目標"
    - "資料來源"
    - "季查核點"
```

## 12.2 Agent Writing Workflow

```yaml
workflow:
  step_1_parse_official_template:
    action: "確認官方最新版格式、章節順序、頁數、經費規定"
  step_2_build_fact_table:
    action: "整理所有確定事實、TODO、假設，不直接寫入正文"
  step_3_define_problem_tree:
    action: "將問題拆成3-5個結構性缺口"
  step_4_define_work_packages:
    action: "每個缺口對應一個工作包或子計畫"
  step_5_define_kpis:
    action: "每個工作包至少1-3個成果型KPI"
  step_6_map_budget:
    action: "每筆經費對應工作包、查核點與KPI"
  step_7_write_sections:
    action: "依官方順序寫，不重複內容"
  step_8_validate:
    action: "跑Quality Gates；修正缺口"
  step_9_owner_review:
    action: "標出需owner確認之法遵、經費、合作、IRB、基線數據"
```

## 12.3 Agent Final Output Requirements

```yaml
final_outputs:
  main_markdown:
    required: true
    description: "AI agent readable markdown plan draft"
  issue_table:
    required: true
    columns: ["issue_id", "severity", "location", "problem", "recommended_action", "owner"]
  fact_assumption_table:
    required: true
    columns: ["item", "status", "source", "confidence", "needs_owner_confirmation"]
  budget_check_table:
    required: true
    checks: ["sum", "capex_ratio", "negative_lines", "duplicate_lines", "negative_list"]
  kpi_check_table:
    required: true
    checks: ["formula", "baseline", "targets", "data_source", "owner"]
```

# 13. Minimal Fillable Skeleton

以下是最小可填版本，適合交給 AI agent 生成申請書初稿。

```markdown
---
plan_name: "TODO"
application_mode: "TODO"
lead_institution: "TODO"
cooperating_institutions: []
period: "116-118"
total_budget_twd: TODO
scopes: []
---

# 健康台灣深耕計畫（116-118年度）計畫申請書

## 壹、申請單位自我檢核項目表
TODO: 依官方表格填列。

## 貳、計畫概要

### 一、政策依據與對應範疇
TODO: 說明本案對應四大範疇與18項目標中的哪些目標。

### 二、現況基線與問題分析
| problem_id | 現況基線 | 結構性缺口 | 不處理後果 | 對應工作包 |
|---|---|---|---|---|
| P-01 | TODO | TODO | TODO | WP1 |

### 三、計畫目標
| objective_id | 目標 | 對象 | 116目標 | 117目標 | 118目標 | 對應KPI |
|---|---|---|---|---|---|---|
| OBJ-01 | TODO | TODO | TODO | TODO | TODO | KPI-01 |

### 四、整體解法與工作包架構
| WP | 名稱 | 對應範疇 | 解決問題 | 主要產出 | 負責單位 |
|---|---|---|---|---|---|
| WP1 | TODO | TODO | P-01 | TODO | TODO |

### 五、與既有政府補助計畫之區隔或接軌
TODO: 列出既有計畫、差異、接軌點、避免重複方式。

## 參、申請機構簡介
TODO: 500字內。

## 肆、計畫規劃

### 一、整體架構與服務/資料流
TODO: 用一張流程表描述。

### 二、工作包一：TODO
- 問題對應：
- 服務對象：
- 執行方法：
- 116年度：
- 117年度：
- 118年度：
- 主要交付物：
- 風險與備案：
- 對應KPI：
- 對應經費：

## 伍、效益評估

### 一、績效指標總表
| KPI | 範疇 | 指標 | 量化定義 | 現況數據 | 116 | 117 | 118 | 資料來源 |
|---|---|---|---|---:|---:|---:|---:|---|
| KPI-01 | TODO | TODO | TODO | TODO | TODO | TODO | TODO | TODO |

### 二、年度查核點表
| 年度 | 季別 | 工作內容 | 查核點 | 年累計進度 | 年累計支用數 | 預期成果與效益 | 預定完成日期 |
|---|---|---|---|---:|---:|---|---|
| 116 | Q1 | TODO | TODO | 25% | TODO | TODO | TODO |

## 陸、出國計畫書
本計畫無出國計畫，未編列國外旅費。  
或依官方格式填列。

## 柒、經費規劃

### 一、分年經費總表
TODO

### 二、各範疇經費配置表
TODO

### 三、主要經費項目與編列依據
| BUD | 年度 | 範疇 | 工作包 | 項目 | 經常/資本 | 金額 | 編列基準 | 對應查核點 |
|---|---|---|---|---|---|---:|---|---|
| BUD-01 | 116 | TODO | WP1 | TODO | TODO | TODO | TODO | TODO |

### 四、共用資源歸屬與避免重複編列
TODO

## 捌、人力配置
| 類別 | 姓名 | 現職 | 具體工作性質、項目及範圍 |
|---|---|---|---|
| 計畫主持人 | TODO | TODO | TODO |

## 玖、其他

### 一、合作單位分工與配合事項
TODO

### 二、風險管理與備援
| 風險 | 觸發條件 | 影響 | 預防措施 | 備案 | 負責人 |
|---|---|---|---|---|---|
| TODO | TODO | TODO | TODO | TODO | TODO |

### 三、IRB、資料治理、資安治理與AI治理
TODO

### 四、永續維運與擴散模式
TODO

## 拾、公職人員利益衝突迴避自主檢核表
TODO: 依官方表格填列。

## 拾壹、未有重複申請計畫之聲明切結書
TODO: 依官方表格簽章。

## 拾貳、參與計畫同意書
TODO: 每一合作機構均須簽署。
```

# 14. Practical Recommendation

若要把計畫書寫到審查可讀，最重要的不是增加篇幅，而是建立四條可追蹤鏈：

```yaml
traceability_chains:
  problem_to_solution:
    rule: "每個問題缺口都要能找到對應工作包"
  work_to_budget:
    rule: "每個工作包都要能找到對應經費"
  budget_to_checkpoint:
    rule: "每筆主要經費都要能找到查核點與交付物"
  checkpoint_to_kpi:
    rule: "每個查核點都要能支撐至少一項KPI或階段成果"
```

若這四條鏈斷掉，計畫看起來再完整，也會被審查委員判定為「內容散、經費不明、績效不可查核」。

---

# 15. Owner Review Items Before Formal Submission

```yaml
owner_review_required:
  - "第二階段正式計畫書格式是否已公告"
  - "申請模式與經費上限"
  - "合作機構名單與同意書"
  - "既有補助案清查"
  - "IRB是否需要與送審狀態"
  - "個資、健康資料、AI與資安治理表是否需一併提交"
  - "經費支用標準是否為最新修訂版"
  - "KPI基線數據是否已由院方或系統匯出"
  - "配合款來源與比例"
  - "採購方式與期程"
```
