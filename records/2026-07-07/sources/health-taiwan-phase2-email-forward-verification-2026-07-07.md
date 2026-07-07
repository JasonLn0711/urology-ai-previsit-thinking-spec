---
document_type: "ai_agent_readable_markdown"
title: "健康台灣深耕計畫第二階段說明會 - 郵件轉知與官方查核摘要"
document_id: "health-taiwan-sprout-phase2-brief-20260707"
version: "1.0"
language: "zh-TW"
created_at: "2026-07-07T17:24:27+08:00"
timezone: "Asia/Taipei"
verification_status: "partially_verified"
source_file_sha256: "a0928fad5a390848341dea2eb1971d9ee363fe19f5c8a3536fe1058320b35809"
confidentiality: "internal_use_minimized_personal_data"
---

# 健康台灣深耕計畫第二階段說明會  
## AI Agent 可讀摘要與查核紀錄

## 0. Agent Operating Rules

1. 對外部事實，以官方公開來源為最高優先序：健康台灣深耕計畫官網、衛福部／國衛院相關頁面與附件。
2. 本文件的上傳來源是一份 Gmail 郵件列印 PDF。該 PDF 只顯示轉寄信內容與附件檔名，沒有內嵌附件實體檔案。不得推論附件內容。
3. PDF 文字擷取有部分亂碼，日期與地址等資訊以「渲染頁面人工判讀」及「官方網頁」交叉確認。
4. 中華民國年與西元年換算：
   - 114 年 = 2025 年
   - 115 年 = 2026 年
   - 116 年 = 2027 年
   - 118 年 = 2029 年
5. 若後續要撰寫計畫書、預算、投標文件或對外承諾，必須先取得完整附件：
   - `健康台灣深耕計畫(116–118年)申請說明及前置作業260630.pdf`
   - `申請作業須知-附件1_計畫書格式.docx`
6. 本文件是「任務摘要與查核紀錄」，不是正式申請作業須知，也不是計畫書。

---

## 1. Executive Summary

這封郵件的核心目的，是轉知「健康台灣深耕計畫第二階段（116-118 年度）徵求案重點說明會」相關資訊，並請收件者參考資料、報名線上說明會。

經官方網站查核，該說明會資訊可信，重點如下：

- 說明會名稱：健康台灣深耕計畫第二階段（116-118 年度）徵求案重點說明會
- 說明會日期：115 年 7 月 10 日，星期五，即 2026-07-10
- 報名期限：115 年 7 月 7 日，星期二，即 2026-07-07
- 會議形式：實體與線上同步
- 實體地點：衛生福利部一樓大禮堂，台北市南港區忠孝東路 6 段 488 號
- 線上方式：MS Teams；會議連結由主辦單位於會前寄送
- 實體席次限制：官方公告表述為「上下午場各單位以 1 人實體出席為原則」；線上每單位至多提供 2 個電子郵件帳號申請加入
- 郵件建議：因實體名額有限，建議線上參加

重要判斷：  
這封信不是核定通知、不是補助通過通知、也不是正式需求書。它是說明會轉知與報名提醒。後續若要寫提案或報價，不能只依這封信判斷需求，必須取得正式作業須知、計畫書格式、經費規範與會議簡報。

---

## 2. Source Document Extraction

### 2.1 Uploaded Email PDF

來源檔案：

```text
National Yang Ming Chiao Tung University Mail - 轉寄_ 【健康台灣深耕計畫】轉寄中央健康台灣深耕計畫專案辦公室之重要公告及7_1會議簡報.pdf
```

技術檢查：

```yaml
source_type: gmail_exported_pdf
page_count: 2
embedded_attachment_count: 0
pdf_sha256: "a0928fad5a390848341dea2eb1971d9ee363fe19f5c8a3536fe1058320b35809"
extraction_note: "PDF 文字層有部分亂碼；已使用頁面渲染圖與官方網站交叉查核。"
```

### 2.2 Email Forwarding Chain

```yaml
top_level_sender:
  name: "莊美幸"
  role: "專案主任"
  organization_domain: "tpech.gov.tw"
  sent_at: "2026-07-07T08:31:00+08:00"
  instruction: "資料請參考；再請報名線上說明會。"

forwarded_sender:
  name: "林素妃"
  role: "行政中心主任"
  sent_at: "2026-07-03T18:12:00+08:00"
  instruction: "資料請參考；再請報名線上說明會。"

original_sender:
  name: "張芷瑜"
  unit: "臺北市立聯合醫院 創新永續發展中心"
  role: "管理師"
  email: "A5667@tpech.gov.tw"
  sent_at: "2026-07-03T16:42:00+08:00"
```

隱私處理：

```yaml
recipient_list_handling:
  full_internal_recipient_list: "omitted"
  reason: "不影響任務決策，且包含大量個人姓名與內部信箱。"
```

---

## 3. Verified Public Facts

| Fact ID | 查核事項 | 查核結果 | 信心 | 主要來源 |
|---|---|---:|---:|---|
| VF-001 | 健康台灣深耕計畫存在，且為 114-118 年計畫 | 正確 | High | 官方簡介、官方下載頁 |
| VF-002 | 總經費為 489 億元 | 官方簡介與計畫頁面均列出 | High | 官方簡介、計畫頁 |
| VF-003 | 計畫四大範疇 | 優化醫療工作條件、規劃多元人才培訓、導入智慧科技醫療、社會責任醫療永續 | High | 官方簡介、計畫頁 |
| VF-004 | 第二階段為 116-118 年度 | 正確 | High | 官方公告 |
| VF-005 | 第二階段徵求案重點說明會日期 | 115-07-10，星期五 | High | 官方公告、議程附件、郵件渲染頁面 |
| VF-006 | 報名截止日 | 115-07-07，星期二 | High | 官方公告、議程附件、郵件渲染頁面 |
| VF-007 | 會議形式 | 實體與線上同步 | High | 官方公告、議程附件、郵件渲染頁面 |
| VF-008 | 實體地點 | 衛生福利部一樓大禮堂，台北市南港區忠孝東路 6 段 488 號 | High | 官方公告 |
| VF-009 | 線上工具 | MS Teams，連結會前寄送 | High | 官方公告 |
| VF-010 | 實體席次限制 | 官方表述為「上下午場各單位以 1 人實體出席為原則」 | High | 官方公告 |
| VF-011 | 線上帳號限制 | 官方表述為每單位至多提供 2 個電子郵件帳號申請加入 | High | 官方公告 |
| VF-012 | 上傳 PDF 內的兩個附件內容 | 未取得實體附件，無法查核內容 | High | PDF 結構檢查：embedded_attachment_count = 0 |

---

## 4. Official Meeting Details

```yaml
event:
  name: "健康台灣深耕計畫第二階段（116-118年度）徵求案重點說明會"
  date_roc: "115-07-10"
  date_iso: "2026-07-10"
  weekday: "Friday"
  mode:
    - "in_person"
    - "online_ms_teams"
  physical_location:
    venue: "衛生福利部一樓大禮堂"
    address: "台北市南港區忠孝東路6段488號"
  registration:
    method: "online_form"
    deadline_roc: "115-07-07"
    deadline_iso: "2026-07-07"
    in_person_limit: "上下午場各單位以1人實體出席為原則"
    online_account_limit: "每單位至多2個電子郵件帳號申請加入"
  meeting_link_delivery:
    expected_by_roc: "115-07-09"
    expected_by_iso: "2026-07-09"
    method: "email"
```

---

## 5. Agenda

官方議程附件列出的時程如下。

### 上午場

| 時間 | 議程 |
|---|---|
| 09:30-10:00 | 報到 |
| 10:00-10:10 | 開場致詞 |
| 10:10-11:30 | 計畫補助徵求說明 |
| 11:30-11:50 | Q&A |
| 11:50-12:00 | 總結 |
| 12:00-13:00 | 中午休息，午餐自理 |

### 下午場

| 時間 | 議程 |
|---|---|
| 13:00-14:10 | 計畫經費編列及支用規範說明 |
| 14:10-14:30 | Q&A |
| 14:30-14:40 | 休息 |
| 14:40-16:10 | 數位管理平台操作說明 |
| 16:10-16:30 | Q&A |
| 16:30 | 賦歸 |

---

## 6. Public Program Context

```yaml
program:
  name: "健康台灣深耕計畫"
  overall_period_roc: "114-118"
  overall_period_iso: "2025-2029"
  approved_total_budget: "489億元"
  administering_public_authority: "衛生福利部"
  program_office_operator: "國家衛生研究院受委託辦理"
  policy_direction:
    - "優化醫療工作條件"
    - "規劃多元人才培訓"
    - "導入智慧科技醫療"
    - "社會責任醫療永續"
  second_phase:
    period_roc: "116-118"
    period_iso: "2027-2029"
    nature: "徵求作業與說明會"
```

官方目的的可操作化理解：

- 不是單純採購設備，也不是單點軟體導入。
- 重點在醫療體系或制度問題的下而上深掘。
- 需提出能改善臨床流程、區域聯防、分級醫療、醫事人力負荷、智慧醫療導入或醫療永續的方案。
- 若涉及智慧醫療或 AI，不能只描述模型功能，必須補上資安治理、資料治理、AI 治理與可持續維運架構。

---

## 7. Reasonableness Check for AI / Smart Healthcare Proposal

若後續要將「智慧健康量測站、問卷、Avatar、AI 問答、生命徵象整合、院端摘要」放入健康台灣深耕計畫，較合理的定位如下：

```yaml
likely_relevant_scope:
  primary: "範疇三：導入智慧科技醫療"
  possible_secondary:
    - "優化醫療工作條件：降低前線人員重複問答與行政負荷"
    - "社會責任醫療永續：提升社區或門診前端健康服務可近性"
```

合理敘事：

- 以「流程輔助、資料收集、健康服務前端分流輔助、工作負荷降低」為核心。
- 將生命徵象、問卷、結果頁、工作人員摘要定位為「輔助資訊」，不是診斷或正式分級醫療決策。
- 若使用 AI，需明確描述：
  - 人在迴路：最後由醫護或工作人員確認。
  - 模型邊界：不做診斷、不取代醫師、不直接給正式醫療處置。
  - 資料治理：資料欄位、資料標準、保存、權限、稽核。
  - 資安治理：身份驗證、傳輸加密、網路區隔、日誌、供應商管理。
  - AI 治理：透明揭露、風險分級、性能監測、偏差與安全事件處理。
  - 互通標準：FHIR、TW Core、必要時使用 LOINC/SNOMED CT/RxNorm 等語意標準。

不合理或高風險敘事：

- 聲稱 AI 可自動診斷、正式分診、取代醫師或直接給治療建議。
- 沒有資料治理，只說「會收集資料給 AI 分析」。
- 沒有資安設計，只說「放雲端」。
- 沒有驗收指標，只列功能清單。
- 沒有說明醫院、外部廠商、學研單位之間的責任邊界與資料權限。

---

## 8. Immediate Action Items

```yaml
action_items:
  - id: A001
    owner: "Jason / project coordinator"
    action: "確認是否已於115-07-07前完成報名。"
    priority: "P0"
    status: "open"

  - id: A002
    owner: "Jason / project coordinator"
    action: "若尚未報名，立即向臺北市立聯合醫院承辦人或健康台灣深耕計畫專案辦公室確認是否可補登記或取得會議連結。"
    priority: "P0"
    status: "open"

  - id: A003
    owner: "Jason / project coordinator"
    action: "取得郵件所列兩個附件的實體檔案，尤其是申請說明及前置作業 PDF、計畫書格式 DOCX。"
    priority: "P0"
    status: "open"

  - id: A004
    owner: "proposal_team"
    action: "閱讀官方經費編列及支用規範，避免先報價再發現經費科目不符。"
    priority: "P1"
    status: "open"

  - id: A005
    owner: "technical_lead"
    action: "將智慧醫療方案拆成流程、資料、系統、資安、AI治理、驗收指標六個模組。"
    priority: "P1"
    status: "open"

  - id: A006
    owner: "legal_compliance"
    action: "判斷是否涉及人體研究、醫療器材、個資法、資通安全責任、IRB或TFDA路徑。"
    priority: "P1"
    status: "open"
```

---

## 9. Questions for the 7/10 Briefing or Organizer

### 9.1 申請資格與合作模式

1. 臺北市立聯合醫院各院區、健康服務中心、學研單位、外部廠商的角色如何定義？
2. 是否允許醫院作為主提單位，學校或公司作為合作單位？
3. 外部廠商的軟體、人力、雲端、設備與維護費用可否列入補助？
4. 合作單位是否需簽署參與計畫同意書、利益迴避、資安或個資承諾？

### 9.2 智慧醫療與 AI

1. AI 系統若只作問卷引導、摘要與流程輔助，是否歸入「導入智慧科技醫療」？
2. 若系統連接生命徵象量測站，是否需要 FHIR/TW Core 格式？
3. 是否要求 AI 治理自我檢核表、資安治理自我檢核表、資料治理自我檢核表？
4. 是否需要模型效能監測、偏差監測、人工覆核與事故通報流程？
5. 使用雲端部署、LLM API 或第三方模型是否有特別限制？

### 9.3 醫療法規與資料

1. 若只做健康篩檢前端問卷與提醒，不做診斷，是否仍需 IRB？
2. 若蒐集生命徵象與問卷資料，是否可用去識別化資料進行成效評估？
3. 是否需先完成 DPIA、個資盤點、資安風險評估或資料保存年限規範？
4. 系統是否可不寫回 HIS，只產生 staff review summary？
5. 若未與 HIS 串接，仍是否需要符合院方互通標準？

### 9.4 經費與驗收

1. 軟體開發、系統整合、資安檢測、維護、教育訓練、使用者研究可否列支？
2. POC、MVP、正式上線三種交付形式是否可分年規劃？
3. 驗收指標應偏向使用率、流程效率、照護品質、醫護負擔降低，或政策指標？
4. 既有廠商與新系統整合的責任邊界如何訂定？
5. 是否要求採購程序、共同供應契約或公開招標？

---

## 10. Risk Register

| Risk ID | 風險 | 嚴重度 | 機率 | 建議控制 |
|---|---|---:|---:|---|
| R001 | 只根據轉寄信就開始報價或承諾功能 | High | Medium | 等正式作業須知、計畫書格式、經費規範到位後再估價 |
| R002 | 把說明會通知誤認為正式需求書 | High | Medium | 明確標示本文件僅為 briefing notice |
| R003 | 實體名額「1人」被誤讀為整場只有 1 人 | Medium | Low | 依官方說法解讀為各單位原則上 1 人實體出席 |
| R004 | 報名截止日已到，無法取得線上連結 | High | Medium | 立即聯絡承辦人與專案辦公室確認補救方式 |
| R005 | 附件未取得，導致前置作業理解不完整 | High | High | 向寄件者或 Gmail 原信下載附件 |
| R006 | AI 方案被寫成診斷或正式分診，增加法規風險 | High | Medium | 改寫為流程輔助、資料整理、工作人員覆核 |
| R007 | 未納入資安、資料、AI 治理，計畫合理性不足 | High | Medium | 依官方範疇三注意事項補齊治理設計 |
| R008 | 未設成效指標，只列設備與功能 | Medium | Medium | 設計可量化 KPI：等待時間、完成率、工作負荷、資料品質、使用者滿意度 |
| R009 | 跨機構資料交換無標準 | High | Medium | 優先評估 FHIR + TW Core 與必要語意標準 |
| R010 | 未釐清醫院、慧誠、智德萬、學校之責任邊界 | High | High | 用 RACI 表與資料流圖先定義分工 |

---

## 11. Suggested Proposal Framing

以下是後續計畫書可以採用的中性框架。這不是正式提案文字，只是方向。

```text
本案擬建置以健康量測、結構化問卷、前端互動引導與工作人員摘要為核心之智慧健康服務前端流程。系統不作診斷、不取代醫護人員判斷，而是協助醫療或健康服務場域收集標準化資料、降低重複行政作業、提升民眾完成問卷與健康服務導引之效率。資料治理上，將依院方資訊規範規劃欄位、權限、保存與稽核機制；若涉及跨系統交換，優先評估 FHIR 與 TW Core 架構。AI 應用將採人在迴路、透明揭露、風險控管與持續監測原則，以符合智慧醫療導入之治理要求。
```

---

## 12. Source Map

### 12.1 Uploaded Source

```yaml
uploaded_source:
  title: "National Yang Ming Chiao Tung University Mail - 轉寄_ 【健康台灣深耕計畫】轉寄中央健康台灣深耕計畫專案辦公室之重要公告及7_1會議簡報.pdf"
  type: "gmail_exported_pdf"
  pages: 2
  date_visible_on_pdf: "2026-07-07"
  contains_attachments_as_files: false
```

### 12.2 Official Public Sources Checked

```yaml
official_sources:
  - id: S001
    title: "健康台灣深耕計畫第二階段（116-118年度）徵求案重點說明會"
    url: "https://htsprout.nhri.org.tw/dhplan_11507021633.html"
    used_for:
      - "說明會日期"
      - "報名截止日"
      - "會議形式"
      - "出席限制"
      - "目的與申請對象"

  - id: S002
    title: "議程附件：健康台灣深耕計畫第二階段徵求案重點說明會"
    url: "https://htsprout.nhri.org.tw/UploadFile/1150702-attach1.pdf"
    used_for:
      - "上午場議程"
      - "下午場議程"
      - "報名網址摘要"
      - "報名成功與會議確認信說明"

  - id: S003
    title: "健康台灣深耕計畫簡介"
    url: "https://htsprout.nhri.org.tw/introduce.html"
    used_for:
      - "計畫緣起"
      - "總經費489億元"
      - "四大範疇"
      - "專案辦公室與聯絡資訊"

  - id: S004
    title: "健康台灣深耕計畫(114-118年)"
    url: "https://htsprout.nhri.org.tw/dhplan.html"
    used_for:
      - "計畫期間"
      - "核定資訊"
      - "489億元總經費"
      - "四大範疇與政策目標"

  - id: S005
    title: "下載專區"
    url: "https://htsprout.nhri.org.tw/download.html"
    used_for:
      - "確認官方下載區存在"
      - "確認資安治理、資料治理、AI治理相關文件在下載區列示"

  - id: S006
    title: "健康台灣深耕計畫範疇3-導入智慧科技醫療-懶人包"
    url: "https://htsprout.nhri.org.tw/UploadFile/HDPlan_fund_1140702_17.pdf"
    used_for:
      - "智慧醫療應用需重視資安治理、資料治理、AI治理"
      - "FHIR、TW Core、資料互通、AI治理等方向"
```

---

## 13. Verification Notes

```yaml
verification_notes:
  checked_at: "2026-07-07T17:24:27+08:00"
  public_official_page_found: true
  official_agenda_found: true
  google_form_status:
    morning_form: "查核時顯示 no longer accepting responses"
    interpretation: "可能已截止或表單已關閉；不等同於所有補登記方式皆不可行，需向承辦確認。"
  email_pdf_attachments:
    listed_in_email:
      - "健康台灣深耕計畫(116–118年)申請說明及前置作業260630.pdf"
      - "申請作業須知-附件1_計畫書格式.docx"
    embedded_in_uploaded_pdf: false
    verified_content: false
  key_correction:
    - "PDF 文字層日期有亂碼，應以渲染頁面及官方公告為準。"
    - "實體名額限制應依官方說法解讀為各單位原則上1人實體出席，而非整場只有1人。"
    - "本郵件僅是說明會轉知，不是正式需求書、核定書或報價依據。"
```

---

## 14. Minimal Machine-Readable Summary

```yaml
brief:
  event_name: "健康台灣深耕計畫第二階段（116-118年度）徵求案重點說明會"
  event_date_iso: "2026-07-10"
  registration_deadline_iso: "2026-07-07"
  event_mode: ["physical", "online_ms_teams"]
  physical_location: "衛生福利部一樓大禮堂，台北市南港區忠孝東路6段488號"
  organizer_public: "健康台灣深耕計畫專案辦公室；衛福部委託國家衛生研究院辦理"
  email_source_org: "臺北市立聯合醫院"
  immediate_task: "確認是否已報名；取得附件；參加或取得說明會資料"
  proposal_relevance:
    likely_scope: "範疇三：導入智慧科技醫療"
    must_include: ["資安治理", "資料治理", "AI治理", "FHIR/TW Core feasibility", "人在迴路", "驗收KPI"]
  unavailable_materials:
    - "健康台灣深耕計畫(116–118年)申請說明及前置作業260630.pdf"
    - "申請作業須知-附件1_計畫書格式.docx"
  do_not_assume:
    - "附件內容"
    - "正式申請期限"
    - "可補助經費項目"
    - "醫院具體需求"
    - "外部廠商合作模式"
```
