---
document_type: ai_agent_readable_budget_normalization
project_context: 健康台灣深耕計畫／信義門診部資本門預算編列
version: v0.1-verified-draft
generated_at: 2026-07-09
language: zh-TW
status: verified_with_review_required
primary_source_files:
  - title: National Yang Ming Chiao Tung University Mail - 請列入信義深耕計畫.pdf
    role: email_instruction_evidence
    note: 此 PDF 為 Gmail 列印頁，只能證明「請參考附件，麻煩編列預算」及附件名稱；PDF 本身未提供資本門明細全文。
  - title: 資本門.docx
    role: budget_item_source
    note: File Library 中找到的附件內容，作為本次資本門品項與單價之主要來源。
  - title: 草稿_ 忠孝 信義深耕計畫_ 0702給健康服務中心.docx
    role: project_context_source
    note: 作為信義門診部、合作機構、計畫範疇與 PSA／三高／智慧科技脈絡之內部草稿來源。
verification_sources:
  - name: 衛生福利部 健康台灣深耕計畫官方資訊
    url: https://dep.mohw.gov.tw/TDU/cp-1567-82247-121.html
  - name: 健康台灣深耕計畫專案辦公室 下載專區
    url: https://htsprout.nhri.org.tw/download.html
  - name: 健康台灣深耕計畫 經費使用原則
    url: https://htsprout.nhri.org.tw/UploadFile/0923-attach1.pdf
  - name: 健康台灣深耕計畫 經費使用原則暨負面表列項目
    url: https://htsprout.nhri.org.tw/UploadFile/0923-attach2.pdf
  - name: 健康台灣深耕計畫 經費支用標準
    url: https://htsprout.nhri.org.tw/UploadFile/0923-attach3.pdf
  - name: 臺北市立聯合醫院 115 年度營運計畫
    url: https://www-ws.gov.taipei/001/Upload/446/relfile/22012/9527498/61a9c268-3aed-4be6-9ed0-a55ac93f6dea.pdf
---

# 信義深耕計畫資本門預算編列：AI Agent 可讀版

## 0. Executive Decision

本文件將原始 `資本門.docx` 的品項轉成可供 AI agent、計畫撰寫者、主計與採購窗口使用的結構化 Markdown。

結論如下：

1. **建議可列入，但需補報價與規格證明**：全自動身高體重計、藍牙血壓計。
2. **可列入，但需補強計畫關聯性**：微電腦藍牙傳輸液晶視力檢查表。
3. **可嘗試列入，但審查風險較高**：診間叫號與麥克風導引系統。
4. **不建議列入補助款資本門**：碎紙機。理由是其容易被認定為一般行政設備；且健康台灣深耕計畫經費支用標準已將碎紙機列為普通性非消耗物品之不建議／不得購置示例。

原始資本門總額為 **586,000 元**。若移除碎紙機，建議送審金額為 **566,000 元**。若採更保守策略，另暫緩叫號與麥克風導引系統，則核心檢測設備金額為 **506,000 元**。

---

## 1. Source Extraction

### 1.1 Email Instruction

```yaml
email_subject: 請列入信義深耕計畫
sender: 莊美幸（主任）<DAI13@tpech.gov.tw>
recipient: 廖偉創 <DBC52@tpech.gov.tw>
cc:
  - 陳瑞泉（主任）<DAP60@tpech.gov.tw>
  - 洪淑如 <Z3805@tpech.gov.tw>
  - cre062400.cs13@nycu.edu.tw
sent_at: 2026-07-03 10:34 Asia/Taipei
instruction: 請參考附件，麻煩編列預算。
attachment_name: 資本門.docx
attachment_size: 16K
confidence: high
limitation: PDF 為信件列印頁，未內嵌 docx 附件內容。
```

### 1.2 Original Budget Items

原始附件文字如下，已標準化為表格。原文使用「藍芽」，本文件正式用語統一為「藍牙」，但保留原始語意。

| source_id | 原始品項 | 原始單價 | 數量 | 原始小計 |
|---|---:|---:|---:|---:|
| CAP-001 | 全自動身高體重計（藍牙傳輸） | 60,000 | 2 台 | 120,000 |
| CAP-002 | 身高體重計外加軟體 | 30,000 | 2 套 | 60,000 |
| CAP-003 | 藍牙血壓計 | 60,000 | 2 台 | 120,000 |
| CAP-004 | 血壓計外加軟體 | 30,000 | 2 套 | 60,000 |
| CAP-005 | 微電腦藍牙傳輸液晶視力檢查表 | 43,000 | 2 台 | 86,000 |
| CAP-006 | 視力檢查表外加軟體 | 30,000 | 2 套 | 60,000 |
| CAP-007 | 診所專用叫號機與麥克風系統 | 10,000 | 6 台／套 | 60,000 |
| CAP-008 | 碎紙機 | 10,000 | 2 台 | 20,000 |
|  | **原始總額** |  |  | **586,000** |

---

## 2. Verification Summary

### 2.1 Policy Verification

```yaml
verified_policy_context:
  plan_name: 健康台灣深耕計畫
  plan_years: 114-118年
  official_categories:
    - 優化醫療工作條件
    - 規劃多元人才培育
    - 導入智慧科技醫療
    - 社會責任醫療永續
  relevant_categories_for_this_budget:
    - 導入智慧科技醫療
    - 社會責任醫療永續
    - 優化醫療工作條件（僅對叫號與流程改善項目有輔助關聯）
  capital_budget_rule:
    principle: 資本門原則上以補助款 30% 為上限，若有充分理由並經審查同意者例外。
  equipment_fee_rule:
    unit_price_threshold: 單價 10,000 元以上
    useful_life_threshold: 使用年限 2 年以上
    relation_requirement: 須與計畫執行直接相關
  fixed_asset_requirement:
    - 需依機構財產管理程序驗收、登帳與保管
    - 需保留報價單、規格書、驗收文件、保固資料及使用紀錄
```

### 2.2 Source Reliability

| 查核對象 | 查核結果 | 判斷 |
|---|---|---|
| Email PDF | 可證明有人要求將附件列入信義深耕計畫預算 | 可信，但不是資本門明細來源 |
| 資本門.docx | 可作為本次品項、單價、數量來源 | 可信，但缺廠牌、型號、報價單 |
| 健康台灣深耕計畫官方資料 | 可確認計畫範疇、經費文件、資本門與設備費原則 | 可信 |
| 公開市場價格 | 未能穩定找到完全相同規格與單價之公開報價 | 不應宣稱市場價格已驗證 |
| 信義門診部計畫草稿 | 可提供場域、合作機構、PSA／三高／智慧科技背景 | 內部草稿來源，仍需院方定稿確認 |

---

## 3. Normalized Budget Table for Submission

### 3.1 Recommended Submission Version

以下版本排除碎紙機，並將「外加軟體」明確改寫為「資料傳輸／介接軟體或授權」，避免被誤認為籠統軟體費。

| 類別 | 項目 | 單價（元） | 單位 | 數量 | 合計（元） | 支用說明或編列基準 | 審查風險 |
|---|---|---:|---|---:|---:|---|---|
| 資本門／設備費 | 全自動身高體重計（藍牙傳輸） | 60,000 | 台 | 2 | 120,000 | 用於社區與門診篩檢場域之身高、體重與 BMI 量測；支援資料傳輸，降低人工登錄錯誤，銜接個案追蹤與智慧健康管理流程。 | 低至中 |
| 資本門／設備費 | 身高體重計資料傳輸／介接軟體或授權 | 30,000 | 套 | 2 | 60,000 | 作為身高體重計與篩檢資料管理流程之必要介接元件；需提供軟體授權、介接規格、資料欄位與保固／維護條件。 | 中 |
| 資本門／設備費 | 藍牙血壓計 | 60,000 | 台 | 2 | 120,000 | 用於三高篩檢與心血管風險管理，支援血壓數值數位化紀錄，銜接社區篩檢、個案追蹤與門診前資料彙整。 | 低至中 |
| 資本門／設備費 | 血壓計資料傳輸／介接軟體或授權 | 30,000 | 套 | 2 | 60,000 | 作為血壓計與篩檢資料管理流程之必要介接元件；需提供資料傳輸方式、資安設定、授權範圍與驗收方式。 | 中 |
| 資本門／設備費 | 微電腦藍牙傳輸液晶視力檢查表 | 43,000 | 台 | 2 | 86,000 | 用於整合式健康檢測場域之視力檢查，支援量測流程標準化與資料數位化；需補強其與本計畫服務對象、場域流程及 KPI 之關聯。 | 中 |
| 資本門／設備費 | 視力檢查表資料傳輸／介接軟體或授權 | 30,000 | 套 | 2 | 60,000 | 作為視力檢查設備之資料傳輸或介接元件；需說明資料格式、使用情境、驗收標準及與整篩流程之關聯。 | 中至高 |
| 資本門／設備費 | 診間叫號與麥克風導引系統 | 10,000 | 台／套 | 6 | 60,000 | 用於門診候診動線與診間報到流程標準化，降低人工呼叫與重複詢問，改善候診秩序、個資保護與護理／櫃檯工作負荷。 | 中至高 |
|  | **建議送審小計** |  |  |  | **566,000** | 不含碎紙機。 |  |

### 3.2 Excluded or Review-Only Items

| 類別 | 項目 | 單價（元） | 單位 | 數量 | 合計（元） | 建議處理 | 原因 |
|---|---|---:|---|---:|---:|---|---|
| 不建議列入補助款 | 碎紙機 | 10,000 | 台 | 2 | 20,000 | 移除；若院內確有需求，改由院內一般行政或自籌經費處理，並先洽主計與承辦窗口確認。 | 高度可能被認定為一般行政設備；健康台灣深耕計畫經費支用標準已將碎紙機列為普通性非消耗物品之不建議／不得購置示例。 |

---

## 4. Arithmetic Check

```yaml
calculation:
  height_weight_scale:
    base: 60000 * 2
    software: 30000 * 2
    subtotal: 180000
  bluetooth_blood_pressure_monitor:
    base: 60000 * 2
    software: 30000 * 2
    subtotal: 180000
  lcd_vision_chart:
    base: 43000 * 2
    software: 30000 * 2
    subtotal: 146000
  queue_microphone_system:
    base: 10000 * 6
    subtotal: 60000
  shredder:
    base: 10000 * 2
    subtotal: 20000
  original_total: 586000
  recommended_total_excluding_shredder: 566000
  conservative_total_excluding_shredder_and_queue_system: 506000
```

### 4.1 Capital Ratio Formula

```yaml
capital_ratio_formula: recommended_capital_total / total_subsidy_amount
example_if_total_subsidy_is_15000000:
  recommended_total_excluding_shredder: 566000
  ratio: 3.77%
  interpretation: 低於 30% 原則上限，但仍需以正式申請補助款總額重新計算。
```

---

## 5. Reasonableness Review by Item

### CAP-001 / CAP-002：全自動身高體重計與資料傳輸軟體

```yaml
fit_to_project: high
reason:
  - 身高、體重、BMI 是社區健康篩檢與三高風險管理的基礎資料。
  - 藍牙或資料傳輸功能可降低人工登錄錯誤。
  - 若能銜接篩檢資料庫、個案追蹤或門診前摘要，與「導入智慧科技醫療」具直接關聯。
risk:
  - 單價是否合理無法僅憑附件判斷。
  - 需確認軟體不是重複計價或僅為一般 app。
required_evidence:
  - 廠牌、型號、規格書
  - 報價單至少一式，建議取得多家比價資料
  - 資料傳輸欄位與格式
  - 驗收標準
  - 保固與維護條件
  - 若屬醫療器材，需提供 TFDA 許可證、登錄或合規文件
recommended_action: retain_with_evidence
```

### CAP-003 / CAP-004：藍牙血壓計與資料傳輸軟體

```yaml
fit_to_project: high
reason:
  - 三高篩檢與腦心血管疾病預防皆需血壓量測。
  - 數位傳輸可支援個案追蹤、異常提醒、資料彙整與門診前摘要。
  - 與信義深耕計畫的三高、心血管風險管理與社區篩檢脈絡一致。
risk:
  - 「藍牙血壓計 60,000 元」若只是一般家用型設備，價格明顯偏高；若為醫療院所用自動量測站或具雲端／院內系統介接，則需以規格與報價證明。
  - 需確認量測準確度、校正機制與醫療器材合規文件。
required_evidence:
  - 醫療級規格與量測準確度資料
  - 校正與維護流程
  - 資料傳輸與資安設計
  - TFDA 或相關醫療器材合規文件
  - 報價單與比價資料
recommended_action: retain_with_stronger_specification
```

### CAP-005 / CAP-006：微電腦藍牙傳輸液晶視力檢查表與軟體

```yaml
fit_to_project: medium
reason:
  - 可作為整合式健康檢測場域設備。
  - 若計畫將信義門診部定位為多項健康服務入口，視力檢查可作為輔助健康檢測項目。
main_issue:
  - 本計畫核心敘事是 PSA、三高、腦心血管風險與智慧門診前資料整合；視力檢查與核心目標的直接性較弱。
risk:
  - 若未補強使用情境，可能被審查認為與計畫主軸關聯不足。
required_evidence:
  - 視力檢查納入服務流程的位置
  - 服務對象與預估使用量
  - 與健康服務中心整篩流程的關聯
  - 資料傳輸與紀錄方式
  - 報價與規格書
recommended_action: retain_only_if_linked_to_integrated_screening_workflow
```

### CAP-007：診間叫號與麥克風導引系統

```yaml
fit_to_project: medium
reason:
  - 可支援門診報到、候診動線與診間導引。
  - 若設計為叫號、導流、分流與個資保護流程之一部分，可連結優化醫療工作條件與流程效率改善。
problematic_original_rationale: 能大幅降低櫃檯負擔，避免護理人員喊到聲音沙啞。
corrected_rationale: 用於門診候診動線與診間報到流程標準化，降低人工呼叫與重複詢問，改善候診秩序、個資保護與護理／櫃檯工作負荷。
risk:
  - 容易被認定為一般行政或庶務設備。
  - 單價剛好 10,000 元，雖可能達設備費門檻，但仍需確認是否符合資本門列支與院內財產管理規則。
required_evidence:
  - 部署位置與數量配置理由
  - 每日門診／篩檢人流量
  - 導入前後流程改善指標
  - 個資保護或去識別叫號設計
  - 報價單與設備規格
recommended_action: conditional_retain_with_workflow_justification
```

### CAP-008：碎紙機

```yaml
fit_to_project: low
risk_level: high
reason:
  - 容易被認定為一般行政設備，而非計畫直接必要設備。
  - 健康台灣深耕計畫經費支用標準對普通性非消耗物品已有負面示例，包含碎紙機。
  - 若以個資保護為理由，仍應先確認是否可由既有院內行政設備或自籌款支應。
recommended_action: remove_from_subsidy_budget
fallback:
  - 若院方堅持保留，需先取得承辦窗口、主計或計畫辦公室書面確認。
```

---

## 6. Corrected Budget Wording

### 6.1 原始語句

> 診所專用叫號機與麥克風系統：10000元*6台。能大幅降低櫃檯負擔，避免護理人員喊到聲音沙啞。

### 6.2 建議正式文件語句

> 診間叫號與麥克風導引系統：每套 10,000 元，共 6 套，合計 60,000 元。用於門診候診動線與診間報到流程標準化，降低人工呼叫與重複詢問，改善候診秩序、個資保護與護理／櫃檯工作負荷，並支援篩檢個案於門診部與診間間之流向管理。

### 6.3 更保守版本

> 診間叫號與導引系統：每套 10,000 元，共 6 套，合計 60,000 元。用於信義門診部篩檢與候診流程之動線管理，支援報到、候診、診間通知與個資保護，以降低人工導引負荷並提升服務流程效率。是否列入資本門，需由主計與計畫承辦窗口確認。

---

## 7. Agent Validation Rules

```yaml
validation_rules:
  - rule_id: R001
    rule: 每一資本門品項必須有明確廠牌、型號、規格書與報價單。
    severity: blocking
  - rule_id: R002
    rule: 每一設備需說明與健康台灣深耕計畫範疇、KPI 或服務流程的直接關聯。
    severity: blocking
  - rule_id: R003
    rule: 單價達 10,000 元以上且使用年限達 2 年以上者，才可優先判斷為設備費／資本門候選。
    severity: blocking
  - rule_id: R004
    rule: 一般行政設備不得僅以便利性列入補助款。
    severity: high
  - rule_id: R005
    rule: 碎紙機不得預設可列支；需移除或取得書面確認。
    severity: high
  - rule_id: R006
    rule: 外加軟體不得籠統書寫，需明確描述為資料傳輸、介接、授權、資安設定或驗收所需元件。
    severity: high
  - rule_id: R007
    rule: 若設備涉及醫療量測，需確認醫療器材許可、登錄或其他合規文件。
    severity: high
  - rule_id: R008
    rule: 不得把公開市場價格未查得之單價寫成已驗證合理價格。
    severity: high
```

---

## 8. Agent Task Plan

```yaml
agent_tasks:
  - task_id: extract.source_budget_items
    input: 資本門.docx
    output: source_items_table
    status: done
  - task_id: normalize.item_names
    instruction: 將藍芽統一為藍牙；將外加軟體改寫為資料傳輸／介接軟體或授權。
    status: done
  - task_id: calculate.subtotals
    instruction: 驗算單價、數量與合計。
    status: done
  - task_id: verify.policy_context
    instruction: 使用官方健康台灣深耕計畫、經費使用原則、負面表列與經費支用標準查核。
    status: done
  - task_id: classify.eligibility
    instruction: 將品項分為可列入、條件列入、不建議列入。
    status: done
  - task_id: request.missing_evidence
    instruction: 向院方或廠商要求廠牌、型號、報價、規格書、醫療器材合規文件、軟體授權與介接說明。
    status: pending
  - task_id: produce.final_budget_table
    instruction: 依主計／承辦窗口確認結果，產出正式計畫書經費表。
    status: pending
```

---

## 9. Missing Evidence Checklist

送審前至少補齊以下資料：

```yaml
missing_evidence:
  procurement:
    - 廠牌
    - 型號
    - 規格書
    - 報價單
    - 比價資料或價格合理性說明
    - 保固期間
    - 維護條件
    - 驗收標準
  compliance:
    - 是否屬醫療器材
    - TFDA 許可證、登錄或其他合規文件
    - 財產登帳方式
    - 使用年限
  data_integration:
    - 藍牙或資料傳輸方式
    - 資料欄位
    - 資料格式
    - 系統介接對象
    - 是否寫入院內系統或僅匯出報表
    - 個資與資安設定
  project_alignment:
    - 對應計畫範疇
    - 對應服務流程
    - 對應 KPI
    - 預估服務人次
    - 部署地點
```

---

## 10. Final Recommended Narrative

本批資本門設備建議定位為「信義門診部社區篩檢與智慧健康資料化流程之基礎量測與導引設備」。身高體重、血壓與視力檢查設備可支援整合式健康檢測場域之標準化量測，並透過資料傳輸或介接軟體，降低人工登錄錯誤，強化個案追蹤、異常管理與門診前資料彙整。診間叫號與麥克風導引系統則作為候診動線、報到通知與診間流向管理工具，用於改善篩檢與門診服務流程。

惟正式送審時，應避免將品項描述為一般行政便利設備。每一品項均需回扣至健康台灣深耕計畫之範疇、服務流程、KPI、資料治理或醫療工作流程改善。碎紙機建議自本次補助款資本門移除，或另由院內一般行政經費處理。

---

## 11. Final Budget Options

```yaml
budget_options:
  option_a_original_source:
    description: 完全保留原始附件所有品項
    total_ntd: 586000
    recommendation: 不建議，因碎紙機風險高。
  option_b_recommended:
    description: 保留檢測設備、介接軟體、叫號導引系統，移除碎紙機
    total_ntd: 566000
    recommendation: 建議版本，但叫號導引系統需補強流程合理性。
  option_c_conservative:
    description: 僅保留檢測設備與介接軟體，移除碎紙機與叫號導引系統
    total_ntd: 506000
    recommendation: 最保守版本，審查風險最低。
```
