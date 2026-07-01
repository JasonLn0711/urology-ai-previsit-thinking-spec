---
document_id: HTSprout_114_118_stage1_application_guidelines
source_file: 114申請作業須知.pdf
document_title: 「健康台灣深耕計畫（114-118年度）」第一階段（114-115年度）申請作業須知
issuing_agency: 衛生福利部
published_date_roc: 114-06-13
program_years_roc: 114-118
stage: 第一階段
stage_years_roc: 114-115
platform_url: https://HTSprout.nhri.org.tw
contact_email: HTSprout_apply@nhri.edu.tw
agent_readable_version: 1.0
intended_agent_tasks:
  - parse_application_requirements
  - validate_applicant_eligibility
  - generate_application_checklist
  - validate_budget_and_schedule
  - map_project_scope_to_review_criteria
  - prepare_submission_and_review_materials
roc_year_note: ROC year + 1911 = Gregorian year
---

# 「健康台灣深耕計畫」第一階段申請作業須知：AI Agent Readable Markdown

> 本檔為依據上傳 PDF 轉寫與結構化後的 AI-agent-readable 操作規格。正式申請仍應以衛生福利部與「健康台灣深耕計畫」平台公告為準。

## 1. Program Snapshot

```yaml
program_name: 健康台灣深耕計畫
full_period_roc: 114-118
stage_1_period_roc: 114-115
stage_2_period_roc: 116-118
policy_mission:
  - 維護全民健康與福祉
  - 整合社會福利及衛生醫療資源
  - 推動分級分流醫療防疫體系創新
  - 推動以人為中心、以社區為基礎之整合性照顧網絡
  - 推動以區域為範疇之家醫制度擴展
main_scopes:
  - 優化醫療工作條件
  - 規劃多元人才培訓
  - 導入智慧科技醫療
  - 社會責任醫療永續
```

## 2. Core Application Logic

```yaml
application_window:
  online_submission_start_roc: 114-06-16
  online_submission_end_roc: 114-07-15
  duration_calendar_days: 30
submission_channels:
  - formal_official_letter_to_MOHW
  - online_platform_upload
  - hard_copy_registered_mail
hard_copy_requirement:
  copies: 1式6份
  delivery_method: 以郵戳為憑
  address: 115204 臺北市南港區忠孝東路六段488號9樓，「健康台灣深耕計畫」專案管理中心
platform_url: https://HTSprout.nhri.org.tw
```

Agent validation rule:

```yaml
application_is_complete_if:
  - official_letter_submitted: true
  - platform_forms_completed: true
  - required_files_uploaded: true
  - hard_copy_sent_before_deadline: true
  - category_limit_satisfied: true
  - required_signatures_and_seals_present: true
```

## 3. Applicant Categories

| category | applicant_type | eligibility_logic | application_limit |
|---|---|---|---|
| A1 | 醫療機構：醫學中心（含準醫中） | 申請時須包含四個範疇，且須垂直及區域整合其他醫療機構合作申請 | 每申請單位於各類組限申請 1 件計畫 |
| A2 | 其他非 A1 醫療機構或醫師公會 | 可垂直及區域整合所轄縣市醫療機構合作申請 | 每申請單位於各類組限申請 1 件計畫 |
| A3 | 其他非 A1 醫療機構 | 可獨立申請 | 每申請單位於各類組限申請 1 件計畫 |
| B | 社區醫療群 | 由當地醫師公會代表整合所轄社區醫療群提出，或由第一合作醫院代表整合所屬社區醫療群提出 | 每申請單位於各類組限申請 1 件計畫 |
| C | 衛福部部定專科醫學會 | 限特定專科醫學會 | 每申請單位於各類組限申請 1 件計畫 |
| D | 各醫事人員法規所定之公會 | 依各醫事人員法規所定公會提出 | 每申請單位於各類組限申請 1 件計畫 |

Additional constraints:

```yaml
category_C_limit:
  basis:
    - 專科醫師分科及甄審辦法第二章第3條
    - 牙醫專科醫師分科及甄審辦法第二章第6條
medical_institution_as_lead:
  must_have:
    - 獨立醫事機構代碼
    - 關防
    - 統一編號
  invalid_if_missing: true
```

## 4. Required Documents

```yaml
required_documents_general:
  - applicant_or_unit_qualification_proof
  - plan_proposal_pdf
  - official_application_letter
  - 未有重複申請計畫之聲明切結書
  - 公職人員利益衝突迴避自主檢核表
required_if_collaborative_plan:
  - 多參計畫同意書
required_if_human_subject_research:
  - 醫學倫理委員會或人體試驗委員會核准文件
  - if_not_available_at_submission: 已送審證明文件
  - must_complete_before_contract: true
required_budget_document:
  - 健康台灣深耕計畫經費使用原則編列表
```

Plan proposal must include:

```yaml
proposal_sections:
  - 依據、現況及問題分析
  - 申請機構簡介
  - 計畫規劃
  - 效益評估
  - 出國計畫書（限範疇二「規劃多元人才培訓」需要時）
  - 經費規劃
  - 人力配置
  - 其他
  - 公職人員利益衝突迴避自主檢核表
  - 未有重複申請計畫之聲明切結書
  - 參與計畫同意書
```

## 5. Proposal Formatting Rules

```yaml
proposal_upload:
  format: PDF
  file_size_limit: 25MB
  merge_as_single_pdf: true
hard_copy:
  copies: 1式6份
  print: 雙面列印膠裝
font_rules:
  chinese_font: 標楷體
  english_font: Times New Roman
  font_size: 12號字
  fixed_line_height: 15pt
page_setup:
  margins_cm:
    top: 1.5
    bottom: 1.5
    left: 1.5
    right: 1.5
  header_footer_cm: 0.5
  page_number_required: true
page_limit:
  max_pages_after_export: 40
  max_sheets: 20
  excluded_from_page_limit:
    - 封面
    - 目錄
    - 申請單位自我檢核項目表
    - 附件
    - 附錄
    - 公職人員利益衝突迴避自主檢核表
    - 切結書
    - 同意書
    - 封底
```

Do not arbitrarily change proposal structure or section order. If format is non-compliant, the unit may be listed for correction after the deadline; correction must be completed within 3 working days after announcement.

## 6. Four Scopes and Goals

### Scope 1: 優化醫療工作條件

```yaml
scope_1:
  name: 優化醫療工作條件
  goals:
    - id: S1-G1
      name: 提高醫事人員核心價值與工作環境
      performance_indicators:
        - 提供具有競爭力的薪酬或福利，吸引優秀人才
        - 設立新的薪資制度，鼓勵醫療照護不足的人力科別
        - 實施靈活的工作時間、排班與輪班制
    - id: S1-G2
      name: 優化醫院內資源配置
      performance_indicators:
        - 消除資源浪費，精確需求預測與資源管理
        - 提升關鍵資源使用效率，減少專科間差異
    - id: S1-G3
      name: 擴大科技投資降低工作負荷
      performance_indicators:
        - 引入 AI 與機器人流程自動化處理重複性工作，如醫療影像分析與報告生成
    - id: S1-G4
      name: 制定醫事人力留任策略
      performance_indicators:
        - 培養團隊合作精神
        - 合理工作安排與支援措施，減少工作壓力
        - 建立員工關懷計畫，提供心理支持與工作生活平衡措施
  example_actions:
    - 優化或新增福利措施，並訂定成效評量指標
    - 推動彈性工時或區域聯防人力調度制度
```

### Scope 2: 規劃多元人才培訓

```yaml
scope_2:
  name: 規劃多元人才培訓
  goals:
    - id: S2-G1
      name: 提供持續教育和專業發展機會
      performance_indicators:
        - 專業培訓和進修機會
        - 鼓勵參加國內外學術會議和研討會
    - id: S2-G2
      name: 促進醫事人員跨領域合作和學習
      performance_indicators:
        - 鼓勵參與跨部門合作項目，增強綜合能力
        - 提供管理、技術、創新等多方面培訓
        - 提升數位工具與技術能力
    - id: S2-G3
      name: 提高急重難科醫師回流醫院誘因
      performance_indicators:
        - 急重難科醫師合理分配，確保高品質醫療服務
    - id: S2-G4
      name: 建立明確職涯發展路徑
      performance_indicators:
        - 制定清晰職涯發展計畫，提供晉升與發展機會
        - 實施導師制度，讓經驗豐富醫事人員指導新進人員
  example_actions:
    - 建立跨領域團隊合作及多元跨職類人才培訓模式
    - 選定特定病種之整合照護模式，與醫療機構或社區醫療群合作，發展臨床治療指引並深化訓練內涵
    - 試辦導入虛實整合臨床醫學訓練模組
```

### Scope 3: 導入智慧科技醫療

```yaml
scope_3:
  name: 導入智慧科技醫療
  goals:
    - id: S3-G1
      name: AI 科技協助臨床醫療
      performance_indicators:
        - 以 AI 取代大規模重複性影像判讀
        - AI 醫療解決方案由醫院延伸至居家場域
        - 更多 AI 解決方案進入臨床應用並輔助醫師決策
        - AI 自然融入健康照護價值鏈，從醫療教育、疾病診斷到大眾健康維護
    - id: S3-G2
      name: 引進國際接軌醫療科技及技術
      performance_indicators:
        - 透過技術轉移引進國際先進醫療技術
        - 更新醫療科技設備，符合國際標準並提升服務品質與效率
        - 與本土企業創新研發，開發具國際競爭力的醫療產品
    - id: S3-G3
      name: 優化醫療照護流程和效率
      performance_indicators:
        - 透過電子病歷系統簡化病患資料管理
        - 盤點與整合現有醫療流程，簡化從報到、出院到長照流程
        - 利用大數據與 AI 分析、預測需求、優化資源配置與人員調度
    - id: S3-G4
      name: 醫療數據共享和安全
      performance_indicators:
        - 建立安全醫療數據共享平台，促進研究與創新
        - 醫院資訊系統取得資安認證及檢測
        - 確保患者數據隱私與安全
    - id: S3-G5
      name: 朝智慧醫院發展
      performance_indicators:
        - 導入數位化基礎設施與技術
        - 門診及病房採取智慧流程與系統
  example_actions:
    - 發展視覺影像模型，自動生成影像報告，減少醫事與護理人員負擔
    - 發展 AI 賦能應用模式，包含生成式、非生成式等，使用成熟且經臨床 AI 取證驗證中心驗證之產品
    - 上架、訂閱或使用 SMART on FHIR 之 AI 產品
```

### Scope 4: 社會責任醫療永續

```yaml
scope_4:
  name: 社會責任醫療永續
  goals:
    - id: S4-G1
      name: 落實分級醫療制度，以社區醫療為基礎，整合照護體系
      performance_indicators:
        - 醫療院所多元發展醫療照護，發展與建立連續性照護及長期照護整合
        - 促進不同醫療專業合作，共同制定與執行患者治療計畫
        - 發展個性化醫療，依患者需求與健康狀況提供量身訂製服務
    - id: S4-G2
      name: 協助政府提升醫療資源可及性與公平性
      performance_indicators:
        - 派遣醫療團隊到偏遠地區，縮小醫療資源差距
        - 協助維穩離島或非山非市地區醫療機構 24 小時急重症照護量能並提升品質
    - id: S4-G3
      name: 營造健康生活型態
      performance_indicators:
        - 提供個別化健康生活處方與全方位健康管理
        - 提供社區健康資源，例如健康資訊中心與健康促進計畫
    - id: S4-G4
      name: 減少碳足跡，推動綠色醫院
      performance_indicators:
        - 透過減少醫療設施直接碳排放實現脫碳
        - 醫院新建或擴建時，自設計到營運皆納入環保與永續性
    - id: S4-G5
      name: 建立 ESG 管理模式
      performance_indicators:
        - 定期發布永續報告，透明揭露醫院永續發展狀況
  example_actions:
    - 推動分級醫療橫向連接與垂直整合
    - 成立跨醫事職類在宅醫療照護小組
    - 建立在宅醫療照護數位資料與品質指標
    - 合作醫院派遣醫療團隊至偏遠地區提供持續性或緊急醫療服務
    - 建立急重症轉診網絡與綠色通道
```

## 7. Budget Caps

Unit: 新臺幣；values are upper limits and may be adjusted after case review.

| category | 114 | 115 | 116 | 117 | 118 |
|---|---:|---:|---:|---:|---:|
| A1 醫學中心/準醫中 | 100,000,000 | 150,000,000 | 150,000,000 | 150,000,000 | 150,000,000 |
| A2 非 A1 合作型醫療機構/醫師公會 | 50,000,000 | 75,000,000 | 75,000,000 | 75,000,000 | 75,000,000 |
| A3 非 A1 獨立申請醫療機構 | 25,000,000 | 37,500,000 | 37,500,000 | 37,500,000 | 37,500,000 |
| B 社區醫療群 | 6,600,000 | 9,900,000 | 9,900,000 | 9,900,000 | 9,900,000 |
| C 衛福部部定專科醫學會 | 6,600,000 | 9,900,000 | 9,900,000 | 9,900,000 | 9,900,000 |
| D 各醫事人員法規所定公會 | 3,000,000 | 4,500,000 | 4,500,000 | 4,500,000 | 4,500,000 |

```yaml
budget_notes:
  - 經費上限非保證核定金額
  - 衛生福利部保留依案件量評估後彈性調整運用權利
  - 預算須經立法院決議審議通過
  - 編列資本門原則以 30% 為上限；因執行需要且敘明理由並經審查同意者不在此限
```

## 8. Funding Use Principles

```yaml
expense_categories:
  personnel:
    - 行政或研究人力費
    - 臨床試驗與研究相關醫療專業及管理人員薪資
    - 保險
    - 公提離職儲金或公提勞工退休金
  business:
    - 稿費
    - 審查費
    - 講座鐘點費
    - 臨時人員費用
    - 文具紙張
    - 郵電
    - 印刷
    - 租金
    - 權利使用費
    - 設備使用服務費
    - 維護費
    - 調查訪問費
    - 受試者掛號費、診療費、檢驗費、車馬費
    - 受試者保險費
    - 受試者營養費
    - 人體試驗委員會審查費
    - 電腦處理費
    - 資料蒐集費
    - 材料費
    - 出席費
    - 國內旅費
    - 國外旅費（僅範疇二）
    - 聘請國外顧問、專家及學者來臺工作費用
    - 餐費
    - 雜支費
  equipment:
    - 軟硬體設備購置與裝置費用
    - 原則: 單價一萬元以上且使用年限二年以上者
```

### Negative List / Restricted Items

The following should generally not appear in detailed budget allocation unless specific exception conditions are satisfied:

```yaml
negative_list:
  - 未列於經費細項分配表之項目
  - 預算編列人員出差國外（範疇二規劃多元人才培訓除外）
  - 彈性薪資
  - 經常性維運性質之修繕經費
  - 非本計畫購置設備之維護費，除非為執行本計畫所需且成果可計入本計畫
  - 一般行政事務性設施：書櫃、辦公桌椅、冰箱、沙發、茶几、咖啡機等
  - 土地取得及建築設施費用
  - 原已獲行政院核定建築工程且承諾由單位內基金支應者
  - 建築物耐震補強工程、新增工程自償性建築設施、體育設施、餐廳
  - 計畫主持費、管理費、一般行政維護費、內部場地費等；內部場地有對外收費且供辦理計畫使用者例外
  - 受補助單位人員出席費、稿費、審查費、工作費、引言人費、諮詢費、加班費
  - 其他政府部門計畫案配合款或自籌款
  - 不佔缺兼任醫事人員鐘點費及交通費、職業災害保險費
  - 非醫療照護空間環境控制、整修、美化環境
  - 外賓參訪名勝古蹟等出遊費用
  - 行政辦公用品、贈送外賓紀念品、獎牌或獎狀費用
  - 手機、非全單位共同使用之平板電腦
  - 因應肺炎疫情相關經費
  - 專利技轉費
  - 以個人名義參加國際組織或研究團體會費，除非能證明增加本單位實質效益且提供佐證
```

## 9. Review Process

```yaml
review_modes:
  administrative_review:
    purpose: 檢查申請資格、申請方式、資料完整性
    reject_if:
      - 申請資格不符
      - 申請方式不符
      - 逾期繳交
  professional_review:
    A_category:
      written_review_weight: 50
      physical_meeting_review_weight: 50
    B_C_D_category:
      written_review_required: true
      physical_meeting_if_needed: true
```

### Written Review Criteria

| item | weight |
|---|---:|
| 計畫內容構想 | 20 |
| 計畫符合度、完整性及獨特價值 | 20 |
| 績效指標與衡量方式 | 20 |
| 預期效益與永續性 | 20 |
| 政策契合度與公共價值 | 20 |
| Total | 100 |

### Physical Meeting Review Criteria

| item | weight |
|---|---:|
| 申請單位/團隊之專業能力與分工機制 | 10 |
| 計畫符合度、完整性及獨特價值 | 15 |
| 計畫期程及執行進度規劃之合理性 | 15 |
| 計畫績效指標 | 20 |
| 計畫預期效益及應用 | 20 |
| 計畫經費組成合理性 | 15 |
| 簡報及答詢 | 5 |
| Total | 100 |

## 10. Physical Meeting Review Rules

```yaml
physical_meeting:
  attendees_limit: 3
  briefing_time_minutes: 10
  q_and_a_time_minutes: 10
  total_minutes: 20
  arrival_requirement: 簡報時間前30分鐘完成報到
  hard_copy_briefing_materials:
    copies: 1式30份
    submission_time: 會議開始前30分鐘報到時一併繳交
  electronic_file:
    accepted_formats:
      - PPTX
      - PDF
    disallowed_format:
      - PPT
    file_size_limit: 20MB
  recording_policy: 全程禁止錄音、攝影、錄影
```

## 11. Project Timeline and Stage Logic

```yaml
full_project_term_years: 5
must_apply_with_5_year_plan: true
stages:
  stage_1:
    years_roc: 114-115
    period: 自114年核定日起至115年底
  stage_2:
    years_roc: 116-118
    period: 自116年起至118年底
stage_2_applicant_types:
  continuation_plan:
    definition: 第一階段經核定執行者，視第一階段辦理情形保留第二階段申請資格
    condition: 第二階段計畫執行內容可能依情形滾動修正
  new_plan:
    definition: 第一階段未獲核定執行或未參與者
    expected_call_time: 115年第4季辦理第二階段徵求公告
```

## 12. Contract and Disbursement Rules

```yaml
contract_stage_1:
  applicable_years: 114-115
  funding_payments:
    - payment: 1
      year_roc: 114
      percentage: 40
      condition: 契約簽訂後撥付
    - payment: 2
      year_roc: 115
      percentage: 30
      condition: 115-04-30前檢附114年度查核點填報紀錄，且第1期款累計動支率達65%以上
    - payment: 3
      year_roc: 115
      percentage: 30
      condition: 檢附成果報告並經甲方認可後撥付
```

Important contract dates:

```yaml
critical_dates:
  expenditure_closing_each_year:
    date: 每年12月15日前
    action: 依規定辦理經費結報
  midterm_report:
    due_roc: 114-12-15
    copies: 1式3份
  final_report:
    due_roc: 115-10-31
    copies: 1式6份
    include: 電腦文書檔
  stage_2_plan_submission_for_continuation:
    years_roc: 116-118
    copies: 1式6份
    timing: 公告期限前
change_request:
  deadline: 情事異動發生後14日內
  overdue_policy: 逾期不予受理
```

Risk rules:

```yaml
contract_risk_rules:
  duplicate_execution_by_third_party_or_MOHW:
    consequence: 返還已撥付全部計畫經費；計畫主持人三年內不得再接受補助
  final_report_late:
    start: 115-10-31次日起
    penalty: 每逾期1日，以契約經費總額千分之一計算違約金
    upper_bound: 不超過計畫經費總額
  final_report_overdue_2_months:
    consequence: 視為不能履行契約；返還已撥付全部計畫經費；主持人一至五年內不得再接受補助
  poor_execution_or_unallowable_expense:
    possible_actions:
      - 扣減補助
      - 停撥
      - 終止契約
      - 追繳不當支出
```

## 13. Reporting Format

```yaml
report_upload:
  format: PDF
  file_size_limit: 25MB
  merge_as_single_pdf: true
hard_copy:
  copies: 1式6份
  print: 雙面列印膠裝
font_rules:
  chinese_font: 標楷體
  english_font: Times New Roman
  font_size: 12號字
  fixed_line_height: 20pt
report_sections:
  - 摘要及關鍵字/詞
  - 報告內容
  - 前言
  - 計畫目標及規劃
  - 執行方法及步驟
  - 結果與討論
  - 執行成果
  - 查核點達成情形
  - 預期績效指標達成情形
  - 經費使用情形
  - 人力運用情形
  - 結論與建議
  - 參考文獻
  - 附件或附錄（含佐證資料）
```

If there is an international travel plan and actual travel occurred, an overseas report must be attached and submitted with the midterm/final report.

## 14. Agent Validation Checklist

Use this checklist to evaluate whether a draft application is ready for submission.

```yaml
validation_checklist:
  eligibility:
    - identify_category_A1_A2_A3_B_C_D
    - verify_one_plan_per_category_group
    - verify_applicant_has_required_legal_or_institutional_status
    - if_lead_is_medical_institution_verify_medical_institution_code_seal_and_uniform_number
  scope_design:
    - map_project_to_at_least_one_scope
    - if_A1_verify_four_scopes_are_included
    - verify_each_work_item_has_yearly_targets_114_to_118
    - verify_quarterly_checkpoints_and_stage_outputs
  documents:
    - verify_plan_pdf_uploaded_under_25MB
    - verify_hard_copy_1_set_6_copies_prepared
    - verify_official_letter
    - verify_conflict_of_interest_checklist
    - verify_no_duplicate_application_declaration
    - if_collaborative_verify_participation_consent_letters
    - if_human_subjects_verify_irb_or_submission_proof
  budget:
    - check_budget_cap_by_category_and_year
    - check_capital_expenditure_ratio_lte_30_percent_unless_justified_and_approved
    - check_no_negative_list_items
    - verify_personnel_business_equipment_separation
    - verify_budget_matches_work_items_and_expected_outputs
  review_preparation:
    - prepare_written_review_alignment_to_5_written_criteria
    - if_A_category_prepare_10_min_briefing_and_10_min_QA
    - ensure_briefing_file_is_PPTX_or_PDF_under_20MB
    - prepare_30_hard_copies_for_meeting_if_required
  contract_and_reporting:
    - track_114_12_15_midterm_report
    - track_115_10_31_final_report
    - track_each_year_12_15_expenditure_closing
    - track_change_requests_within_14_days
```

## 15. Recommended Agent Extraction Schema

```json
{
  "applicant": {
    "name": "",
    "category": "A1|A2|A3|B|C|D",
    "institution_code": "",
    "uniform_number": "",
    "lead_unit": "",
    "collaborating_units": []
  },
  "project": {
    "title": "",
    "period_roc": {"start": "", "end": ""},
    "scopes": [],
    "goals": [],
    "work_items": [],
    "quarterly_checkpoints": [],
    "yearly_targets_114_118": {}
  },
  "budget": {
    "total_requested_ntd": 0,
    "yearly_budget_ntd": {},
    "personnel_ntd": 0,
    "business_ntd": 0,
    "capital_ntd": 0,
    "capital_ratio": 0,
    "negative_list_risks": []
  },
  "documents": {
    "proposal_pdf": false,
    "qualification_proof": false,
    "official_letter": false,
    "conflict_of_interest_checklist": false,
    "no_duplicate_declaration": false,
    "participation_consent_letters": false,
    "irb_approval_or_submission_proof": false,
    "budget_use_plan": false
  },
  "submission": {
    "online_completed": false,
    "official_letter_sent": false,
    "hard_copy_sent": false,
    "hard_copy_postmark_date_roc": "",
    "deadline_risk": "low|medium|high"
  },
  "review_alignment": {
    "written_review_score_risks": [],
    "physical_meeting_required": false,
    "briefing_ready": false
  }
}
```

## 16. Contact Information

```yaml
project_management_center:
  phone:
    - "(02)8590-6973"
    - "(02)8590-6974"
  staff:
    - name: 劉小姐
      phone: "(037)206-166 ext. 33108"
    - name: 陳小姐
      phone: "(037)206-166 ext. 33109"
  email: HTSprout_apply@nhri.edu.tw
MOHW_contact:
  name: 黃小姐
  phone: "(02)8590-7574"
question_form:
  url: https://forms.gle/1ymHk6Fhk3BWDVJ68
```

