# Deep-Cultivation Application Draft v0.2

Status: superseded official-format proposal skeleton

Date: 2026-05-20

Working title: 泌尿科門診前問診與醫師覆核摘要支持系統

Current drafting entrypoint: `DEEP_CULTIVATION_APPLICATION_DRAFT_V0_3.md`.

Before reusing any paragraph from this v0.2 skeleton in outward-facing writing, run `ASSERTIVE_WRITING_GATE.md` and `../core/ASSERTIVE_WRITING_POLICY.md`.

## Draft Boundary

This file preserves the earlier proposal-writing skeleton for Health Taiwan Deep-Cultivation application drafting. Current circulation should use v0.3 and keep final institutional submission, signed official proposal routing, clinical protocol approval, IRB application, procurement specification, production deployment planning, and HIS/EMR integration under their separate governance routes.

Before any external circulation, the parent proposal owner must confirm the latest official template, applicant route, institutional fields, page limits, required signatures, and hospital-specific instructions.

## Source And Format Basis

Live source spot-check on 2026-05-20:

- HTSprout download page still lists application, execution, budget, and meeting-QA files.
- The plan page still frames Health Taiwan Deep-Cultivation as a `114-118` five-year plan across four categories.
- The application-flow page still states first stage runs to the end of 115 and second stage runs 116-118.
- The AI Center page still emphasizes AI governance, cybersecurity governance, data governance, and FHIR / TW Core IG readiness for Scope 3 smart-healthcare drafting.

Local source set:

- `../records/2026-05-19/policy-documents/application/health-taiwan-phase1-proposal-format-114-115-0909.docx`
- `../records/2026-05-19/policy-documents/application/health-taiwan-phase1-application-guidelines.pdf`
- `../records/2026-05-19/policy-documents/execution/ai-governance-self-checklist.docx`
- `../records/2026-05-19/policy-documents/execution/cybersecurity-governance-self-checklist.docx`
- `../records/2026-05-19/policy-documents/execution/data-governance-self-checklist.docx`
- `../records/2026-05-19/policy-documents/budget/`
- `../records/2026-05-19/policy-documents/qa/`

## Cover-Page Working Fields

| Official field | Draft value / action |
| --- | --- |
| 計畫名稱 | Parent proposal owner to confirm |
| 子計畫名稱 | 泌尿科門診前問診與醫師覆核摘要支持系統 |
| Safe descriptive wording | 泌尿科門診前症狀蒐集與醫師覆核摘要輔助流程 |
| English working title | Urology Previsit Intake and Clinician-Reviewed Summary Support System |
| Main category | 範疇三：導入智慧科技醫療 |
| Secondary category | 範疇一：優化醫療工作條件 |
| Optional supporting category | 範疇二 only if training is explicitly budgeted and owned |
| Future supporting category | 範疇四 only if community return flow / CRM is separately governed |
| Applicant | Pending parent proposal owner |
| Application mode | Pending parent proposal owner |
| Host department | Pending hospital owner; likely urology plus outpatient workflow owner |
| Collaborating units | Urology, nursing/outpatient administration, IT/security, AI/engineering team, governance support |
| Execution period | Must match parent proposal route |
| Data boundary | Synthetic / expert-review materials only until governance approval |
| Current scope | Non-acute LUTS / OAB-like outpatient previsit intake and clinician-review summary |
| Explicitly excluded | Diagnosis, treatment advice, autonomous triage, risk score, queue priority, direct EMR writeback, real patient data during discovery |

## 壹、申請單位自我檢核項目表

This section must be completed by the official applicant.

Subproject-specific preflight:

| Check item | Current status | Needed action |
| --- | --- | --- |
| Applicant legal identity | Pending | Confirm applicant name, code, responsible person, contact, and application route |
| Application mode | Pending | Confirm A/B/C/D mode and whether this is continuation or new application |
| Partner consent / MOU | Pending | Identify whether urology, nursing, IT/security, and external technical team need written participation documents |
| Conflict-of-interest disclosure | Pending | Parent proposal owner to collect |
| Duplicate funding declaration | Pending | Parent proposal owner to verify |
| Official template version | Local archive uses 0909 first-stage format | Re-check live official source before circulation |
| Scope 3 governance forms | Draft-only | Prepare AI, cybersecurity, and data-governance checklist responses |
| Budget rule compliance | Not yet itemized | Use `DEEP_CULTIVATION_KPI_TO_BUDGET_TABLE.md` before budget drafting |

## 貳、計畫概要

### 一、子計畫摘要

本子計畫擬建置「泌尿科門診前問診與醫師覆核摘要支持系統」，以非急性泌尿科門診病人為初期對象，聚焦夜尿、頻尿、急尿、漏尿、排尿困難或尿流變弱等 LUTS / OAB-like 常見症狀。系統透過受治理之題庫、病人或家屬填答、缺漏欄位提示、來源標記與一頁式醫師覆核摘要，於報到後或候診期間整理可安全蒐集之門診前資訊，協助醫師快速掌握主訴、症狀脈絡、困擾程度與用藥資訊完整度。

本子計畫以降低臨床工作摩擦與醫療人員負荷為核心原則。系統不要求醫師或護理師成為 AI 標註者，也不以增加醫護人員額外研究工作作為導入前提。護理介入以既有流程與必要人工確認為限，不以護理師補完 AI 問卷作為系統成立前提。

AI 與 ASR 作為降低輸入負擔、輔助結構化填答與摘要整理之智慧科技工具。系統架構將診斷、治療決策、自動分流、風險評分、檢查開立與 EMR 正式寫入保留於醫師及院內治理流程。若產出 SOAP 架構內容，其定位為醫師覆核參考摘要，最終臨床判斷與正式病歷紀錄均由醫師決定。

### 二、政策與範疇對應

| Official category | Draft positioning |
| --- | --- |
| 範疇三：導入智慧科技醫療 | Primary. The subproject introduces governed intake, optional ASR, structured summary generation, auditability, version tracking, and AI/data/cybersecurity governance as smart-healthcare workflow support. |
| 範疇一：優化醫療工作條件 | Secondary. The subproject evaluates whether previsit information compression reduces repeated questioning, documentation preparation, missing-information repair, system switching, and cognitive load. |
| 範疇二：規劃多元人才培訓 | Optional. Include only if clinician-engineer co-design, responsible-AI training, IRB/data-governance training, or student/RA participation is funded and owned. |
| 範疇四：社會責任醫療永續 | Future. Include only if community screening return flow, case management, or CRM follow-up becomes a separately governed phase. |

### 三、核心問題

非急性泌尿科門診常見症狀具有重複性，病人資訊常在進入診間後才開始整理，造成醫師需重新建構主訴、時間軸、困擾程度與用藥脈絡。若資訊缺漏，醫師或護理人員需臨時補問；若病人敘述零散，醫師需在有限門診時間內完成理解、判斷與紀錄。

本子計畫處理的核心問題是：

```text
門診前可安全蒐集的病人回報資訊，尚未被低摩擦地整理成醫師可快速覆核的工作流產物。
```

### 四、計畫目標

1. 建立非急性泌尿科門診前問診流程，聚焦 LUTS / OAB-like 症狀。
2. 建立受治理之題庫與條件式追問邏輯。
3. 建立病人 / 家屬 / 工作人員 / ASR-confirmed 來源標記。
4. 建立缺漏欄位提示與不確定性標示。
5. 建立 patient-reported red-flag observation 的安全呈現方式。
6. 建立一頁式醫師覆核摘要。
7. 建立 optional multilingual ASR input layer 的安全確認流程。
8. 建立 clinical friction reduction 評估框架。
9. 建立 AI、資安、資料治理與 future interoperability readiness 文件。
10. 建立 KPI-to-budget、年度查核點與提案審查 evidence map。

## 參、申請單位簡介

This section must be completed by the parent proposal owner.

Subproject role draft:

| Role | Draft responsibility |
| --- | --- |
| 主提機構 | Owns official submission, budget, eligibility, institutional approval, and parent KPI |
| 泌尿科臨床團隊 | Reviews target population, question scope, summary format, unsafe wording, and workflow slot |
| 護理 / 門診行政團隊 | Reviews waiting-room feasibility, exception handling, nurse burden, and staff-assist boundary |
| 資訊 / 資安 / 個資治理單位 | Reviews security, access, retention, audit logs, ASR/data handling, and future integration readiness |
| AI / 工程團隊 | Maintains synthetic demo, versioned question logic, summary-generation design, test artifacts, and evidence package |
| IRB / 研究治理支援 | Determines whether future work is research, QI, service improvement, or mixed |
| 行政 / 採購窗口 | Reviews vendor, procurement, equipment, outsourcing, and post-project ownership |

## 肆、計畫規劃

### 一、第一版適用族群

```text
非急性、已排定泌尿科門診、主訴為夜尿、頻尿、急尿、漏尿、排尿困難或尿流變弱的成人病人。
```

Manual review / exclusion cases:

| Situation | First-version handling |
| --- | --- |
| Currently unable to urinate | Patient-reported observation; human review by local process |
| Fever/chills with flank pain | Observation only; no diagnosis or action advice |
| Visible blood or clots | Observation only; clinician review |
| Unable to understand questions | Paper or human workflow; do not force digital completion |
| ASR content cannot be confirmed | Do not enter content into summary |
| Emergency or unscheduled acute patient | Excluded from first-version previsit workflow |

### 二、Workflow Slot

Working hypothesis:

```text
registration completed
-> waiting-room QR/tablet intake
-> patient/family answer confirmation
-> missing-field and source-label processing
-> one-page clinician-review summary
-> clinician confirms, edits, ignores, or rejects
```

Clinical-friction constraint:

```text
The workflow is acceptable only if it reduces net burden and does not require clinicians or nurses to perform routine AI data-labeling, duplicate entry, or major workflow retraining.
```

### 三、System Modules

| Module | First-version content | Boundary |
| --- | --- | --- |
| Patient / family intake | Chief concern, timing, bother, LUTS / OAB-like symptoms, medicine-list completeness, concern for clinician | No diagnosis or medical advice |
| Optional ASR | Exploratory input layer only | Confirm transcript/structured answer before summary |
| Governed question bank | Core questions plus approved triggered modules | No free-form model-generated clinical questioning |
| Missing-field display | Unknown, missing, contradictory, or skipped items | No risk score |
| Source labeling | Patient / family / staff-assisted / ASR-confirmed | Visible in clinician summary |
| Observation display | Visible blood, fever/chills, flank pain, unable to urinate | Human-review wording only |
| Clinician-review summary | One-page summary; optional SOAP-structured reference | Not formal EMR content |
| Audit/version trace | Question set, summary schema, rule/model/prompt version, review status | Required before pilot-ready claim |
| Future CRM readiness | Reminder / return-flow logic only if reopened | No current implementation commitment |
| Future interoperability readiness | FHIR / TW Core IG mapping if relevant | No current HIS/EMR integration claim |

### 四、Implementation Work Packages

| Work package | Deliverable | Owner needed |
| --- | --- | --- |
| WP1 Intended use and scope freeze | `INTENDED_USE_FREEZE.md`, `DEMO_SCOPE_FREEZE.md` | Project owner + clinical reviewer |
| WP2 Workflow and UI evidence | patient flow, clinician summary, reviewer packet | AI/engineering + clinic reviewer |
| WP3 Question governance | final first-version question set and triggered modules | Urology clinician |
| WP4 Summary and auditability | one-page summary, source trace, review status | AI/engineering + clinician |
| WP5 Clinical friction evaluation | extra clicks, system switching, staff burden, training burden | clinic staff + evaluator |
| WP6 Governance package | AI, cybersecurity, data, privacy, IRB, procurement checklist | hospital governance owners |
| WP7 KPI and budget mapping | KPI-to-budget table and annual checkpoint table | proposal owner + budget owner |

## 伍、效益評估

Use `DEEP_CULTIVATION_KPI_TO_BUDGET_TABLE.md` for the working table.

Core KPI categories:

- clinician summary read time
- repeated-question reduction feasibility
- missing-information repair
- nurse/staff burden acceptability
- clinical friction budget
- source-label completeness
- unsafe wording count
- ASR confirmation safety
- governance checklist completion
- KPI-to-budget traceability

Claims reserved for later governed evidence:

- diagnosis accuracy
- triage accuracy
- mortality reduction
- early cancer detection rate
- automatic medical-record completion
- production clinical effectiveness

## 陸、年度查核點

Use `DEEP_CULTIVATION_ANNUAL_CHECKPOINT_TABLE.md`.

Current recommended structure:

```text
115 Q2-Q4: proposal prep, synthetic evidence, governance preflight
116: governed pilot preparation and first workflow validation
117: limited workflow evaluation if governance approval exists
118: scale-up or integration-readiness decision only if evidence supports it
```

## 柒、經費規劃

Use `DEEP_CULTIVATION_KPI_TO_BUDGET_TABLE.md` before itemizing budget.

Budget rule:

```text
No KPI, no core budget line.
No governance owner, no patient-data or integration budget line.
```

Candidate budget buckets:

- project coordination / RA
- clinician and staff review sessions
- web/tablet intake prototype
- optional ASR evaluation
- summary generation and auditability implementation
- AI/data/cybersecurity governance work
- usability / human-factors evaluation
- future interoperability readiness mapping
- vendor/procurement planning only if a module is reopened

## 捌、人力配置

Draft role table:

| Role | Needed for | Notes |
| --- | --- | --- |
| PI / subproject owner | clinical and proposal accountability | pending hospital confirmation |
| Urology clinical lead | question set, summary review, safety wording | must own clinical boundary |
| Nursing/outpatient workflow reviewer | staff burden and waiting-room fit | should not become routine AI operator |
| IT/security reviewer | security, access, future integration readiness | needed before real data |
| Data/AI governance reviewer | AI lifecycle, transparency, auditability | required for Scope 3 logic |
| Engineer / AI system designer | demo, structured intake, summary, logs | synthetic-only until approval |
| RA / coordinator | reviewer sessions, KPI evidence, documentation | budget must map to KPI |
| Procurement/admin contact | vendor and budget route | needed if outsourcing/equipment is requested |

## Open Items Before Hospital Circulation

| Item | Current status |
| --- | --- |
| Formal applicant | Pending |
| Application mode | Pending |
| Parent proposal relationship | Pending |
| Hospital-specific blank format | Pending |
| Budget ceiling and allowed categories | Pending |
| Required partner signatures | Pending |
| Whether this is continuation or second-stage new application | Pending |
| Real workflow slot confirmation | Pending |
| Governance owners | Pending |
| Whether future CRM is reopened | Pending |

## Reviewer Summary

This v0.2 draft should be judged by whether it is:

- officially format-aware
- clinically narrow
- low-friction for staff
- governed before real data
- KPI-to-budget traceable
- clear about what is excluded

It should not be judged by number of AI features.
