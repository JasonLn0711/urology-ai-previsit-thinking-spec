---
document_type: ai_agent_readable_markdown
source_file: "健康台灣深耕計畫(116–118年)申請說明及前置作業260630.pptx"
source_slide_count: 8
created_at: "2026-07-01"
language: "zh-Hant-TW"
subject: "健康台灣深耕計畫（116–118年）申請說明及前置作業"
verification_status: "web_verified_with_caveats"
primary_use: "proposal_planning, eligibility_checking, budget_checking, ai_agent_tasking"
critical_caveat: "第二期116–118年正式申請細節仍須以衛福部與健康台灣深耕計畫專案網站最新公告為準；簡報中的預計時程不可直接視為正式法定期限。"
---

# 健康台灣深耕計畫（116–118年）申請說明及前置作業

## 0. Agent Operating Summary

```yaml
agent_goal: >
  將本簡報內容轉成可供 AI agent 解析、檢核與後續撰寫提案使用的結構化 Markdown，
  並加入網路查證後的正確性判斷與風險註記。
source_priority:
  - official_mohw_and_htsprout_announcements
  - official_application_guidelines_and_budget_rules
  - uploaded_pptx_content
  - reputable_news_reports_only_as_context_not_final_rule
recommended_agent_behavior:
  - do_not_treat_internal_or_projected_dates_as_final_deadlines
  - always_recheck_latest_htsprout_announcements_before_submission
  - map_goal_to_strategy_to_kpi_to_checkpoint_to_budget
  - verify_applicant_type_before_selecting_A_B_C_D_mode
  - apply_current_budget_rules_and_negative_list_before_costing
```

## 1. Source Register

| Source ID | Source Type | Source Name | Use in this Markdown | Reliability |
|---|---:|---|---|---:|
| S0 | uploaded_file | 原始簡報：健康台灣深耕計畫(116–118年)申請說明及前置作業260630.pptx | 原始內容來源 | high_for_slide_content |
| S1 | official_web | 衛福部科技發展組「健康台灣深耕計畫」專區 | 計畫緣起、四大範疇、18項目標 | highest |
| S2 | official_web | 健康台灣深耕計畫專案網站：申請資格 | 申請單位基本資格、資格證明文件 | highest |
| S3 | official_web | 健康台灣深耕計畫專案網站：申請資訊 / 申請流程 | 期程、第二階段分類、申請模式 A/B/C/D | highest |
| S4 | official_pdf | 衛福部《健康台灣深耕計畫（114–118年度）》政院核定版 | 總經費、期程、四範疇政策邏輯 | highest |
| S5 | official_pdf | 健康台灣深耕計畫申請說明 / 申請作業相關文件 | 申請文件、查核點、審查、經費上限 | highest |
| S6 | official_pdf | 健康台灣深耕計畫經費使用原則說明 | 經費編列、資本門、人事費、負面表列、查核 | highest |
| S7 | official_web | 健康台灣深耕計畫公告專區 / 數位管理平台公告 | 系統註冊、平台測試、最新公告追蹤 | high |
| S8 | reputable_news | 中央社 2026-06-28 報導：第2期7月徵求提案 | 近期政策動向參考；不可取代正式公告 | medium_high |

## 2. Verification Verdict

| Claim | Slide / File Statement | Web Verification Result | Verdict | Agent Handling |
|---|---|---|---|---|
| 計畫為 114–118 年五年期 | 簡報以 116–118 年第二階段為主，並提及總期程 114–118 年 | 官方資料確認總執行期程為 5 年，分第一階段 114–115 與第二階段 116–118 | verified | use_as_structural_basis |
| 四大範疇、18項子目標 | 簡報列出四大範疇與18項目標 | 衛福部官方專區列明四大範疇與18項具體目標 | verified | use_as_proposal_taxonomy |
| 總經費 489 億元 | 簡報寫「核定總經費達489億元」 | 政院核定版明列 489億3,481萬9千元；簡報為四捨五入 | verified_rounded | use_exact_amount_when_needed |
| 申請資格 | 醫療機構、社區醫療群、部定專科醫學會、醫事人員公會 | 官方申請資格頁與申請說明文件一致 | verified | use_for_eligibility_gate |
| 申請模式 A/B/C/D | 簡報列出 A/B/C/D 類與每類限制 | 官方申請資訊頁一致；每申請單位於各類組限申請1件 | verified | use_for_mode_selection |
| A1/A2/A3經費上限 | 簡報呈現第二階段116–118年經費上限，並特別框選 A2 | 官方文件顯示 A1/A2/A3、B/C/D 分年經費上限；簡報與官方第二階段表格一致 | verified | use_as_budget_ceiling_not_requested_amount |
| 116–118 年線上申請 | 簡報說「預計以線上方式申請，相關細節尚未公布」 | 官方文件已有線上填報、平台註冊與測試資訊；但第二期正式細節仍須看最新公告 | partially_verified | mark_as_pending_final_announcement |
| 第2期7月徵求提案 | 簡報政策摘要提及第2期預計今年7月對外徵求提案 | 中央社報導同樣稱第2期7月對外徵案；但官方申請流程頁仍載明新增計畫原預定115年第4季公告 | caveat_required | treat_as_policy_signal_not_submission_rule |
| 經費須排除負面表列 | 簡報 checklist 提醒排除負面表列 | 官方公告與經費使用原則有負面表列與限制項目 | verified | run_budget_negative_list_check |

## 3. Project Identity

```yaml
project_name: "健康台灣深耕計畫"
official_period_roc: "114–118年"
official_period_ce: "2025–2029"
current_focus_period_roc: "116–118年"
current_focus_period_ce: "2027–2029"
competent_authority: "衛生福利部"
project_management_center: "健康台灣深耕計畫專案管理中心 / 專案辦公室"
implementation_style:
  - bottom_up_problem_diagnosis
  - local_solution_design
  - vertical_and_regional_integration
  - annual_or_stage_based_review
```

## 4. Core Policy Logic

### 4.1 核心理念

本計畫重點不是單純補助硬體或讓大型醫院擴張資源，而是要求申請單位「診斷當地問題，提出在地解方」。其底層邏輯是：

1. 讓地方醫療場域提出真實痛點。
2. 透過垂直整合與區域合作，避免資源集中於少數大型機構。
3. 用中長期經費與查核機制，促成可持續的醫療體系改善。
4. 以 KPI、查核點、年度審查和經費核定把政策目標落到執行成果。

### 4.2 四大範疇與18項目標

```yaml
scope_1:
  name: "優化醫療工作條件"
  goals:
    - "提高醫事人員核心價值與工作環境"
    - "優化醫院內資源配置"
    - "擴大科技投資降低工作負荷"
    - "制定醫事人力留任策略"
scope_2:
  name: "規劃多元人才培訓"
  goals:
    - "提供持續教育和專業發展機會"
    - "促進醫事人員跨領域合作和學習"
    - "提高急重難科醫師的回流醫院誘因"
    - "建立明確的職涯發展路徑"
  emphasis_from_slide:
    - "特別重視急重難罕醫療團隊之培訓"
    - "生醫、疫苗研發、智慧醫療、再生醫療、感染防疫等領域人才培養"
scope_3:
  name: "導入智慧科技醫療"
  goals:
    - "AI科技協助臨床醫療"
    - "引進國際接軌的醫療科技及技術"
    - "優化醫療照護流程和效率"
    - "醫療數據共享和安全"
    - "朝智慧醫院發展"
scope_4:
  name: "社會責任與醫療永續"
  goals:
    - "落實分級醫療，以社區醫療為基礎，整合照護體系"
    - "協助政府提升醫療資源的可及性和公平性"
    - "營造健康生活型態"
    - "致力於減少碳足跡，推動綠色醫院"
    - "建立環境、社會和治理 ESG 管理模式"
  emphasis_from_slide:
    - "配合健康台灣政策目標或策略，例如888三高防治計畫、提高重要癌症篩檢率、提高癌症早期診斷占比"
    - "有效節能減碳策略"
```

## 5. Applicant Eligibility

### 5.1 Eligible Applicant Types

```yaml
eligible_applicants:
  - type: "醫療機構"
    examples:
      - "醫學中心"
      - "準醫學中心"
      - "區域醫院"
      - "地區醫院"
      - "其他依法設立之醫療機構"
  - type: "社區醫療群"
    representative_options:
      - "由當地醫師公會代表整合所轄社區醫療群提出申請"
      - "由第一合作醫院代表整合所屬社區醫療群提出申請"
  - type: "衛福部部定專科醫學會"
  - type: "各醫事人員法規所定之公會"
```

### 5.2 Required Eligibility Evidence

```yaml
required_eligibility_documents:
  - "與本案有關之依法設立或登記證明文件影本"
  - "法人登記證書或許可登記證明文件"
  - "醫療機構開業證明、執業執照、立案證明或其他合法設立證明"
  - "必要時主管機關可要求提供正本查驗"
```

## 6. Application Modes

```yaml
application_modes:
  A:
    name: "醫療機構"
    subtypes:
      A1:
        description: "醫學中心或準醫學中心"
        requirements:
          - "申請時須包含四個範疇"
          - "須垂直及區域整合其他醫療機構5家以上合作申請"
      A2:
        description: "其他非A1之醫療機構或醫師公會，可垂直及區域整合所轄縣市醫療機構合作申請"
        note: "原始簡報的經費補助表特別框選A2，若要以A2規劃，需先確認主提單位身分與合作網絡。"
      A3:
        description: "其他非A1之醫療機構可獨立申請"
  B:
    name: "社區醫療群"
    requirements:
      - "由當地醫師公會代表整合所轄社區醫療群提出申請"
      - "或由第一合作醫院代表整合所屬社區醫療群提出申請"
  C:
    name: "衛福部部定專科醫學會"
  D:
    name: "各醫事人員法規所定之公會"
mode_rule: "每申請單位於各類組限申請1件計畫"
```

## 7. Project Timeline

### 7.1 Official Phase Structure

```yaml
total_project_period:
  roc: "114–118年"
  ce: "2025–2029"
  duration: "5年"
phase_1:
  roc: "114年計畫核定日起至115年底"
  ce: "2025 approval date to 2026-12-31"
phase_2:
  roc: "116年起至118年底"
  ce: "2027-01-01 to 2029-12-31"
phase_2_applicant_types:
  continuation:
    description: "第一階段經核定執行者，視第一階段辦理情形保留第二階段申請資格"
    caveat: "第二階段內容可能滾動修正，延續型須依修正後內容調整計畫後提出申請"
  new_plan:
    description: "第一階段未獲核定或未參與者"
    official_page_status: "官方申請資訊頁仍記載預定於115年第4季辦理第二階段徵求公告"
```

### 7.2 Slide 5: 116–118年計畫預計作業期程

```yaml
slide_5_title: "衛福部116-118年計畫預計作業期程"
calendar_year_roc: "115年"
visible_months: ["02", "03", "04", "05", "06", "07", "08~~~"]
notable_items:
  - item: "系統開發完成項目"
    subitems:
      - "機構期中/成果報告繳交"
      - "機構變更作業"
      - "國衛院期中/成果/變更收件"
      - "國衛院成果報告審查"
  - item: "教育訓練二場"
    subitems:
      - "機構期中報告繳交"
      - "機構變更作業"
      - "國衛院報告繳交與變更"
    visible_dates:
      - "115/2/10 國衛院同仁教育訓練"
      - "115/2/12 私協、社協教育訓練"
      - "115/2/25 機構教育訓練"
    visible_note: "第一階段已核定通過的253筆計畫，因未匯入計畫詳細資料，線上作業僅提供計畫主持人變更；變更可執行時程須等候公告。"
  - item: "審查平台測試"
    subitems:
      - "期中報告繳交"
      - "系統上線"
    visible_note: "115/4 機構期中報告繳交、變更作業線上執行"
  - item: "網頁平台開發完成 / 審查平台開發完成"
    subitems:
      - "第二階段計畫申請作業"
      - "計畫收件作業"
      - "計畫審查作業"
      - "計畫核定作業"
  - item: "相關人員教育訓練"
  - item: "測試、上線"
  - item: "機構第二階段申請作業上線"
    status_from_slide: "待定"
    approximate_visible_timing: "115年8月以後"
bottom_note_from_slide: "116-118年計畫預計以線上方式申請，相關細節尚未公布。"
agent_warning: "以上屬簡報預計作業期程，不等同正式申請期限。正式投件前必須重新查詢官方公告。"
```

## 8. Funding and Budget

### 8.1 Official Total Budget

```yaml
official_total_budget:
  amount_ntd: 48934819000
  display_tw: "新臺幣489億3,481萬9千元"
  slide_display: "489億元"
  verification_note: "簡報金額為四捨五入後的政策溝通版本；正式文件或報價分析應使用精確數字或註明約數。"
```

### 8.2 Stage 2 Annual Funding Ceilings: 116–118

| Application Mode | 116年 | 117年 | 118年 | Notes |
|---|---:|---:|---:|---|
| A1 醫療機構 | 1.5億元 | 1.5億元 | 1.5億元 | 醫學中心／準醫中，須四範疇與5家以上整合 |
| A2 醫療機構 | 7,500萬元 | 7,500萬元 | 7,500萬元 | 簡報特別框選；應確認申請單位是否符合A2 |
| A3 醫療機構 | 3,750萬元 | 3,750萬元 | 3,750萬元 | 非A1醫療機構獨立申請 |
| B 社區醫療群 | 990萬元 | 990萬元 | 990萬元 | 由醫師公會或第一合作醫院代表整合 |
| C 衛福部部定專科醫學會 | 990萬元 | 990萬元 | 990萬元 | 部定專科醫學會 |
| D 醫事人員法規所定公會 | 450萬元 | 450萬元 | 450萬元 | 法定醫事人員公會 |

### 8.3 Budget Rules and Execution Controls

```yaml
budget_controls:
  capital_expenditure_cap:
    principle: "資本門原則以30%為上限"
    stage_1: "114–115年總經費之30%"
    stage_2: "116–118年各年經費之30%"
    exception: "計畫執行需要且敘明理由，經審查同意者不在此限"
  personnel_costs:
    principle: "依計畫需求核實編列"
    must_include:
      - "勞保"
      - "健保"
      - "其他依法應負擔費用"
  execution_rate:
    expected_minimum: "年度第一階段經費執行率應達80%以上"
    risk_if_below: "未達標且無合理原因者，可能刪減第二階段補助"
  accounting:
    - "設立專帳登錄收支"
    - "不得移作他用"
    - "跨院計畫由申請單位負責管理"
  negative_list_examples:
    - "出差國外費用，範疇二人才培訓例外"
    - "管理費，例如水電、清潔、電話、加班費、健保補充保費等"
    - "外賓參訪出遊費用"
    - "紀念品或獎牌費用"
    - "肺炎疫情相關經費"
    - "專利技轉費"
    - "主持人費"
    - "受補助單位人員出席費、稿費、審查費、工作費、諮詢費、加班費等"
    - "不佔缺兼任醫事人員費用"
    - "一般行政事務性設施"
    - "非計畫購買之設備維護費"
    - "手機、個人平板電腦"
    - "建築工程相關費用"
agent_budget_instruction: >
  經費上限不是可直接填滿的金額。agent 必須先建立工作包、KPI、查核點與成本基礎，
  再檢查經費是否支撐成果、是否落入負面表列、是否符合最新經費支用標準。
```

## 9. Proposal Writing Checklist

### 9.1 Core Proposal Logic

```yaml
proposal_logic_chain:
  - "推動目標"
  - "執行策略"
  - "績效指標 KPI"
  - "查核點"
  - "經費規劃"
  - "合作機構"
principle: "各要素必須環環相扣；目標要能被策略執行，成效要能被KPI衡量，進度要能被查核點追蹤，經費要直接支撐成果。"
```

### 9.2 Detailed Checklist

```yaml
checklist:
  goal_and_focus:
    - "目標精準對應計畫四大核心範疇"
    - "欲解決的臨床痛點或願景具體明確"
    - "具備由下而上的專業整合價值"
  methods_and_strategy:
    - "具備清晰的短中長期執行期程"
    - "策略可行性高，且能支撐推動目標"
    - "具體執行步驟能直接導向預期成果"
  kpi:
    - "指標符合SMART原則"
    - "能量化或質化呈現醫療品質成效"
    - "指標與產出成果、經費投入有直接對應"
  checkpoints:
    - "已設定明確階段性查核點，例如每季"
    - "具體查核方式或檢驗標準明確"
    - "可落實進度追蹤與執行風險控管"
  budget:
    - "預算編列符合官方公告經費編列原則"
    - "已排除負面表列不補助事項"
    - "經費分配能合理支撐策略並產出KPI"
  collaborators:
    - "是否有合作機構"
    - "是否簽署合作同意書或參與計畫同意書"
    - "院內外連結，例如藥劑部與藥師公會、社區藥局"
    - "院際或教研連結，例如醫院與教研部門合作"
```

## 10. Application Package Requirements

```yaml
application_package:
  standard_documents:
    - "計畫書格式文件"
    - "申請者/單位簽署之未有重複申請計畫之聲明切結書"
    - "合作提出之計畫：主提單位須取得團隊內各機構簽署之參與計畫同意書"
    - "計畫主持人簽署之公職人員利益衝突迴避自主檢核表"
    - "資格證明文件影本"
  if_human_subjects_research:
    - "醫學倫理委員會或人體試驗委員會核准文件"
    - "若申請時未能提交核准文件，須先提交已送審證明，並於簽約前補齊"
  submission_mode_from_official_first_stage_reference:
    - "正式函文送書面資料"
    - "線上填報"
    - "計畫書1式6份"
    - "正式期限依公告；第一階段參考為自公告日起30日內"
agent_caution: "第二階段116–118年最終文件份數、線上流程、截止期限可能依新公告調整。"
```

## 11. Review and Risk Controls

```yaml
review_process:
  stages:
    - "行政審查"
    - "專業審查"
  administrative_rejection_risks:
    - "不符合申請資格"
    - "不符合申請模式"
    - "不符合申請方式"
  professional_review_threshold:
    score: "總平均75分含以上為合格"
    note: "合格者仍為擇優補助，不代表必然獲補助"
  funding_risks:
    - "預算須俟立法院審查通過並依實際核定預算撥付"
    - "除第一階段外採逐年簽約"
    - "年度補助額度將依執行成效評核結果核定"
    - "執行不力可能變更付款方式或終止契約"
    - "不當或不法使用經費將追繳"
    - "重複申請、內容抄襲等情事可能終止計畫並追回補助"
```

## 12. Smart Healthcare / AI Proposal Notes

若提案涉及範疇三「導入智慧科技醫療」，AI agent 不應只寫「導入AI系統」或「建置平台」。至少要補上以下設計層：

```yaml
smart_healthcare_design_layers:
  clinical_workflow:
    - "要改善哪一個臨床、行政或照護流程"
    - "導入前後的人力負荷、等待時間、錯誤率或照護品質差異"
  data_governance:
    - "資料來源"
    - "資料品質"
    - "欄位標準"
    - "資料使用權限"
    - "資料保存與稽核"
  cybersecurity:
    - "身分驗證與授權"
    - "存取紀錄"
    - "加密"
    - "資安事件通報與備援"
  ai_governance:
    - "模型適用範圍"
    - "輸入輸出限制"
    - "人工覆核"
    - "偏誤與錯誤監測"
    - "模型更新與版本控管"
  medical_device_or_regulatory_check:
    - "是否可能涉及醫療器材或臨床決策支援"
    - "是否需要TFDA或IRB等路徑評估"
  interoperability:
    - "是否需要與院內HIS/EMR/LIS/PACS或FHIR資料流整合"
    - "若採FHIR，需定義resource、profile、API與權限控管"
```

## 13. Agent Task Template for Proposal Preparation

```yaml
task_1_identify_applicant:
  inputs_needed:
    - "主提單位名稱"
    - "主提單位類型"
    - "是否為醫學中心或準醫學中心"
    - "合作機構清單"
  output:
    - "recommended_application_mode"
    - "eligibility_gap_list"

task_2_define_problem:
  inputs_needed:
    - "地方或院內痛點"
    - "目標族群"
    - "現況數據"
    - "政策連結"
  output:
    - "problem_statement"
    - "root_cause_hypothesis"
    - "policy_alignment_matrix"

task_3_build_work_packages:
  inputs_needed:
    - "四大範疇對應"
    - "預期成果"
    - "合作單位分工"
  output:
    - "work_package_table"
    - "responsibility_matrix_RACI"

task_4_define_kpi_and_checkpoints:
  inputs_needed:
    - "baseline"
    - "target"
    - "measurement_method"
    - "quarterly_milestones"
  output:
    - "SMART_KPI_table"
    - "quarterly_checkpoint_table"

task_5_budget_design:
  inputs_needed:
    - "工作包"
    - "人力需求"
    - "設備與系統需求"
    - "委外或採購需求"
  output:
    - "budget_table"
    - "negative_list_check_result"
    - "capital_expenditure_ratio"
    - "funding_ceiling_check"

task_6_risk_and_governance:
  inputs_needed:
    - "資料流"
    - "系統架構"
    - "臨床風險"
    - "資安需求"
  output:
    - "risk_register"
    - "AI_data_security_governance_section"
    - "IRB_TFDA_assessment_note"
```

## 14. Minimal Proposal Skeleton

```markdown
# 計畫名稱

## 壹、計畫摘要
- 申請單位：
- 申請模式：A1 / A2 / A3 / B / C / D
- 計畫期間：116–118年
- 對應範疇：
- 核心問題：
- 在地解方：
- 預期效益：

## 貳、問題診斷與政策對應
- 現況與痛點
- 目標族群
- 地方 / 區域醫療缺口
- 對應健康台灣範疇與子目標

## 參、執行策略與工作包
| Work Package | Scope | Lead | Partners | Deliverables | Timeline |
|---|---|---|---|---|---|

## 肆、KPI 與查核點
| KPI | Baseline | Target | Measurement | Checkpoint | Evidence |
|---|---:|---:|---|---|---|

## 伍、合作機構與治理架構
- 合作機構
- 角色分工
- 決策機制
- 會議與回報節奏

## 陸、資訊系統、資料治理與資安設計
- 系統架構
- 資料流
- 權限控管
- 稽核紀錄
- AI治理 / 模型治理
- IRB / TFDA / 法遵評估

## 柒、經費規劃
| Budget Item | Amount | Work Package | KPI Link | Funding Rule Check | Negative List Check |
|---|---:|---|---|---|---|

## 捌、風險管理
| Risk | Likelihood | Impact | Mitigation | Owner |
|---|---:|---:|---|---|
```

## 15. Final Caveats for Agents

```yaml
must_not_assume:
  - "簡報內預計時程等於正式公告期限"
  - "經費上限等於可直接申請滿額"
  - "A2被框選即代表申請單位一定符合A2"
  - "智慧醫療提案只要寫AI功能即可"
  - "硬體採購可作為主要論述；政策更重視醫療流程、人才、區域整合與成果"

must_verify_before_submission:
  - "最新第二階段徵求公告"
  - "最新計畫書格式"
  - "最新經費支用標準"
  - "最新負面表列與限制項目"
  - "平台註冊與線上填報規則"
  - "合作同意書格式"
  - "IRB / TFDA / 資安治理要求"
```
