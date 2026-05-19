# Deep-Cultivation Subproject Draft v0.1

Status: expert-review draft
Date: 2026-05-19
Working title: 泌尿科門診前問診與醫師覆核摘要支持系統

## Draft Boundary

This is a proposal-writing draft for the Health Taiwan Deep-Cultivation Plan format. It is not a final institutional submission, clinical protocol, IRB application, deployment plan, procurement specification, or EMR integration plan.

The draft follows the first-stage proposal structure currently archived under:

```text
records/2026-05-19/policy-documents/application/health-taiwan-phase1-proposal-format-114-115-0909.docx
```

Official-source logic used for this draft:

- The Health Taiwan Deep-Cultivation Plan is organized around four categories: `優化醫療工作條件`, `規劃多元人才培訓`, `導入智慧科技醫療`, and `社會責任醫療永續`.
- The latest local official format archive includes `計畫概要`, `申請單位簡介`, `計畫規劃`, `效益評估`, `年度查核點`, `經費規劃`, and `人力配置表`.
- Scope 3 smart-healthcare writing should explicitly address AI governance, cybersecurity governance, and data governance.
- The official execution package also includes category 3 execution information, AI governance self-checklist, cybersecurity governance self-checklist, data governance self-checklist, checkpoint reporting, final report, and site-visit records.

## Cover-Page Working Fields

| Field | Draft content |
| --- | --- |
| 子計畫名稱 | 泌尿科門診前問診與醫師覆核摘要支持系統 |
| Safe descriptive wording | 泌尿科門診前症狀蒐集與醫師覆核摘要輔助流程 |
| English working title | Urology Previsit Intake and Clinician-Reviewed Summary Support System |
| Main category | 範疇三：導入智慧科技醫療 |
| Secondary category | 範疇一：優化醫療工作條件 |
| Applicant / host unit | To be completed by hospital main proposal owner |
| Collaborating unit | To be completed: urology clinic, nursing station, IT/security, 吳老師團隊, other approved partners |
| Execution period | Match official first-stage period in the parent proposal |
| Data boundary | Synthetic / expert-review materials only until IRB, privacy, security, and institutional approvals are completed |
| Current decision | Revise + Narrow |
| First-version scope | Non-acute LUTS / OAB-like outpatient symptoms: nocturia, frequency, urgency, leakage, voiding difficulty, or weak stream |
| Explicitly parked | CRM follow-up implementation, vendor CRM planning, EMR writeback, diagnosis, treatment recommendation, autonomous triage |

## 壹、申請單位自我檢核項目表

This subproject must be merged into the main institution's official application package. The following items are not completed by this technical draft, but must be checked by the main proposal owner before submission.

| Official check item | Subproject implication | Current status |
| --- | --- | --- |
| 申請資格及檢附證明文件 | Confirm the main applicant and cooperating units are eligible under the chosen application mode. | Pending parent-proposal owner |
| 依格式撰擬計畫書 | This draft follows the official section order but must be transferred into the official Word template. | Draft only |
| 封面載明計畫名稱、縣市別、申請模式、計畫範疇、機構代碼 | This subproject provides a working title and category mapping only. | Pending institution |
| 利益衝突迴避自主檢核與身分關係揭露 | Needed for all applicable team members and institutions. | Pending institution |
| 未有重複申請補助切結 | Required if this subproject requests budget lines. | Pending institution |
| 參與計畫同意書 | Required for cooperating institutions / units. | Pending institution |
| 申請模式限申請規則 | The parent proposal must verify the chosen A/B/C/D mode and related limits. | Pending institution |

## 貳、計畫概要

### 一、子計畫摘要

本子計畫擬建立「泌尿科門診前問診與醫師覆核摘要支持系統」，以非急性泌尿科門診病人為初期對象，聚焦夜尿、頻尿、急尿、漏尿、排尿困難或尿流變弱等 LUTS / OAB-like 常見症狀。系統透過受治理之題庫、病人或家屬填答、缺漏欄位提示、來源標記與一頁式醫師覆核摘要，協助門診前整理主訴、症狀脈絡、困擾程度與用藥資訊完整度。

AI 與 ASR 僅作為降低輸入負擔、輔助結構化填答與摘要整理之工具。ASR 以 optional multilingual input layer 方式探索繁體中文、英語及東南亞語系輸入可用性，語音轉文字內容需經病人、家屬或工作人員確認後，才可進入摘要。系統不提供診斷、治療建議、自動分流、風險評分、檢查開立或 EMR 自動寫入。若產出 SOAP 架構內容，僅作為醫師覆核參考摘要，最終臨床判斷與正式病歷紀錄均由醫師決定。

現階段以合成資料 demo、專家審查與工作流程驗證為主。後續將依臨床端確認之 workflow slot、醫師可讀性評估、護理負擔評估、AI 治理、資安治理與資料治理條件，再規劃是否進入真實場域試行。

### 二、政策與計畫範疇對應

| Official category | Draft positioning |
| --- | --- |
| 範疇三：導入智慧科技醫療 | Primary. The subproject introduces governed question selection, optional ASR, structured intake, summary generation, auditability, and AI/data/cybersecurity governance as smart-healthcare workflow support. |
| 範疇一：優化醫療工作條件 | Secondary. The subproject evaluates whether previsit symptom collection and one-page summary support reduce repeated basic history-taking and avoidable missing-information repair. |
| 範疇二：規劃多元人才培訓 | Optional supporting element only if the parent plan includes clinician-engineer co-design training, IRB training, responsible-AI training, or student participation. |
| 範疇四：社會責任醫療永續 | Not first-version core. It may become future context only if community return flow, case management, or CRM follow-up is reopened under separate governance. |

### 三、核心問題

目前泌尿科非急性門診常見 LUTS / OAB-like 症狀病人，在進入診間前常有下列 workflow pain points:

- 症狀資訊抵達診間時才開始整理，醫師需重建主訴、時間軸與困擾程度。
- 夜尿、頻尿、急尿、漏尿、排尿困難等症狀常需要重複詢問基本欄位。
- 病人或家屬常無法立即提供完整藥單、藥袋或用藥名稱。
- 候診期間存在可利用的資訊整理時間，但尚未驗證最適合的使用時點。
- 若摘要太長、像問卷紀錄或含 AI 推論，醫師可能不會閱讀。
- 若 red-flag observations 顯示方式不當，可能被誤解成 AI triage。
- 若 ASR、摘要、SOAP、EMR wording 不受控，會被誤解成 AI 臨床決策或自動病歷。

### 四、子計畫目標

1. 建立非急性泌尿科門診前問診流程，聚焦 LUTS / OAB-like 症狀。
2. 建立受治理之題組與條件式追問邏輯，避免模型自由產生臨床問題。
3. 建立病人 / 家屬 / 工作人員來源標記與確認流程。
4. 建立缺漏欄位提示，協助診前整理而非取代醫護判斷。
5. 建立 red-flag observations 的安全呈現方式，只做病人回報觀察，不做診斷或分流。
6. 建立一頁式醫師覆核摘要格式，驗證醫師是否願意在 60 秒內閱讀。
7. 建立 optional multilingual ASR input layer 的可行性測試方法，避免 ASR 錯誤直接成為事實來源。
8. 建立 AI 治理、資安治理、資料治理與 future interoperability readiness 的提案文字。
9. 建立可查核 KPI、分年查核點與 budget-to-KPI mapping。

## 參、申請單位簡介

This section must be completed by the main proposal owner. The subproject can provide the following role descriptions.

| Role | Draft responsibility |
| --- | --- |
| 主提機構 | Owns the official proposal, budget, application mode, institutional approvals, and final submission. |
| 泌尿科臨床團隊 | Reviews patient group, question set, summary fields, unsafe wording, and clinical workflow slot. |
| 護理 / 門診行政團隊 | Reviews waiting-room feasibility, incomplete-intake handling, and staff burden. |
| 資訊 / 資安 / 個資治理單位 | Reviews system boundary, access control, audit log, ASR/data storage, cybersecurity, and future integration readiness. |
| AI / 工程合作團隊 | Maintains synthetic demo, governed question logic, summary generation design, evaluation scripts, and version traceability. |
| IRB / 研究治理支援 | Determines whether future pilot is research, QI, service improvement, or mixed; defines consent and training requirements. |

## 肆、計畫規劃

### 一、第一版適用族群

First-version target:

```text
非急性、已排定泌尿科門診、主訴為夜尿、頻尿、急尿、漏尿、排尿困難或尿流變弱的成人病人。
```

First-version rationale:

- 症狀欄位重複度高，適合診前先整理。
- 多數資訊可由病人或家屬安全回報。
- 風險治理負擔低於直接以血尿或急性症狀作為主軸。
- 容易設計成門診流程改善，而不是 AI diagnosis / AI triage。

First-version manual-review or exclusion cases:

| Situation | Draft handling |
| --- | --- |
| 目前完全尿不出來 | 顯示病人回報 observation，請依院內流程人工確認。 |
| 發燒畏寒合併腰側痛 | 不顯示診斷或處置建議，只標示人工覆核。 |
| 大量可見血尿或血塊 | 顯示病人回報 observation，交由醫護覆核。 |
| 無法理解題目且無家屬協助 | 使用紙本或人工流程；不強迫完成數位問診。 |
| ASR 內容無法確認 | 不產生正式摘要；標示未確認。 |
| 急診或未排程病人 | 不納入第一版門診 previsit scope。 |

### 二、第一版 workflow slot

Working hypothesis:

```text
報到後 -> 候診期間 -> 病人或家屬用 QR code / tablet 填寫
-> 系統產生 partial or complete summary
-> 護理或診間端只看缺漏與 red-flag observations
-> 醫師看一頁 summary
```

Design rules:

- 病人 / 家屬自填為主。
- 未完成也可產生 partial summary。
- 護理師不負責補完所有欄位。
- 護理介入限於填不完、明顯矛盾、red-flag observations、用藥資料不完整且院方認為需要補問的情境。
- 真實 workflow slot 尚待多寶與臨床端確認，不可在 proposal 中寫成已驗證。

### 三、系統功能模組

| Module | First-version content | Boundary |
| --- | --- | --- |
| Patient / family intake | 主訴、開始時間、困擾程度、LUTS / OAB-like 症狀、藥袋/藥單完整度、希望醫師先知道事項 | 不收正式診斷、不做醫囑、不取代醫師問診 |
| Optional multilingual ASR | 繁體中文、英語、東南亞語系可用性探索 | 語音轉文字需確認；高錯誤成本欄位不可 ASR-only |
| Governed question bank | 10-14 core questions plus triggered modules | 模型不能自由生成未核准臨床問題 |
| Missing-field display | 未填、不確定、矛盾回答、需追問欄位 | 缺漏不轉成風險等級 |
| Source labeling | patient / family / staff-assisted / ASR-confirmed | 來源必須顯示給醫師 |
| Red-flag observation display | 可見血尿、發燒畏寒、腰側痛、目前尿不出來 | 只做 observation；不自動分流 |
| Clinician-review summary | 一頁式 summary；可採 SOAP 架構但限醫師覆核參考 | 不自動寫入 EMR，不產生正式病歷 |
| Audit and version trace | 題庫版本、規則版本、摘要版本、確認狀態、review status | Pilot 前需定義存取與保存規則 |
| Future interoperability readiness | FHIR / TW Core IG 只作治理準備 | 不承諾現階段串接 HIS/EMR |
| Future CRM readiness | 只保留為未來治理議題 | 現階段 parked |

### 四、題組設計

#### Level 1: all first-scope users

1. 誰填寫：本人 / 家屬協助 / 工作人員協助。
2. 今天最想請醫師看的問題。
3. 問題開始時間。
4. 困擾程度 0-10。
5. 白天是否明顯頻尿。
6. 夜尿幾次。
7. 是否突然很急、難以忍住。
8. 是否漏尿。
9. 排尿是否疼痛、刺痛、灼熱。
10. 是否看過血尿或血塊。
11. 是否尿不太出來或目前完全尿不出來。
12. 是否發燒、畏寒、腰側痛。
13. 是否能提供目前藥單或藥袋。
14. 是否還有希望醫師先知道的事。

#### Level 2: triggered modules

| Trigger | Follow-up scope |
| --- | --- |
| Nocturia / frequency / urgency | 白天大約次數、急尿頻率、睡前喝水、咖啡茶酒、是否可記錄 3 天排尿日誌 |
| Leakage | 頻率、量、情境、是否使用護墊或尿布 |
| Voiding difficulty | 尿流變弱、需用力、斷斷續續、尿不乾淨 |
| Visible blood | 紅色/茶色/血塊、一次或反覆、是否伴隨疼痛或發燒；正式風險因子留給醫師或 later governed module |

#### Level 3: nursing review

Nursing review should be limited to:

- 需要協助完成 intake。
- red-flag observations。
- 藥單/藥袋不完整。
- 明顯矛盾回答。
- 紙本或家屬協助需求。
- 是否需要醫師先看摘要。

#### Level 4: physician-only

Do not ask the patient or system to decide:

- OAB / BPH / UTI / cancer。
- 是否需要膀胱鏡、CT、尿動力。
- 是否需要抗生素、導尿、手術。
- 是否低風險。
- 是否不用看醫師。
- 尿液檢查結果自我解讀。
- PVR、DRE、pelvic exam、影像結果判讀。

### 五、醫師覆核摘要格式

The clinician-facing output should be a fast handoff card, not a questionnaire transcript.

Required top five fields:

| Order | Field | Example |
| ---: | --- | --- |
| 1 | 主訴 + 開始時間 + 填答來源 | 主訴：夜尿增加；約 3 個月；本人填寫，家屬協助確認。 |
| 2 | 主要陽性症狀 | 夜尿 3 次以上、急尿、漏尿、排尿灼熱、尿流弱。 |
| 3 | Patient-reported red-flag observations | 回報：可見血尿 / 發燒畏寒 / 腰側痛 / 目前尿不出來。需人工覆核。 |
| 4 | 用藥與資料完整度 | 可提供藥袋照片 / 只記得部分藥名 / 無法確認目前用藥。 |
| 5 | 缺漏欄位與醫師可追問點 | 未填：是否有血塊、夜尿次數不確定、目前是否仍尿不出來。 |

Remove or hide from first one-page summary:

- 完整 ASR 逐字稿。
- 系統追問推理鏈。
- 診斷候選。
- 風險等級。
- 檢查建議。
- 治療建議。
- 自動 SOAP 病歷。

Safe SOAP / EMR sentence:

```text
本系統可將病人或家屬回報之門診前資訊整理為 SOAP 架構之醫師覆核參考摘要，內容限於主訴、症狀脈絡、困擾程度、用藥完整度、缺漏欄位與來源標記；系統不產生診斷、治療建議、分流決策或正式病歷內容，也不自動寫入 EMR，最終紀錄與臨床判斷均由醫師決定。
```

### 六、red-flag observations 安全邊界

Red-flag observations are not triage.

| Patient report | Safe display |
| --- | --- |
| 可見血尿 | 病人回報曾看見尿液呈紅色、茶色或血塊。請臨床人員覆核。 |
| 發燒畏寒 | 病人回報近期發燒或畏寒。請依院內流程人工確認。 |
| 腰側痛 | 病人回報腰部兩側疼痛。請臨床人員覆核。 |
| 目前尿不出來 | 病人回報目前尿不出來或明顯排尿困難。請依院內流程人工確認。 |

Do not write:

- 建議立即急診。
- 高風險。
- 疑似感染。
- 疑似腎盂腎炎。
- 疑似癌症。
- 低風險可等待。
- 無需就醫。
- 需要導尿。
- 需要抗生素。
- 建議做 CT / 膀胱鏡。

### 七、AI / ASR / data handling

Allowed AI roles:

- 依受治理題庫進行 next-question selection。
- 將已確認的結構化回答整理為摘要。
- 標示缺漏欄位。
- 協助產生醫師覆核參考摘要。
- 保留題庫版本、規則版本、摘要版本與 review status。

Disallowed AI roles:

- 診斷。
- 分流。
- urgency score / risk score。
- 檢查建議。
- 治療建議。
- 藥物建議。
- 自動寫入 EMR。
- 告訴病人是否需要或不需要就醫。

ASR rules:

| Field | Rule |
| --- | --- |
| General free text | May use ASR if transcript is shown and confirmed. |
| Medication names | Prefer medication-bag photo or manual confirmation; avoid ASR-only. |
| Dosage | Do not interpret in first version. |
| Time | Convert to selectable choices and confirm. |
| Nocturia count | Convert to choice and confirm. |
| Blood-in-urine description | Require confirmation. |
| Allergy/history | Exclude from first version or route to manual confirmation. |

### 八、治理規劃

#### AI governance

- Define model / prompt / rule version before any pilot.
- Maintain a governed question bank and change log.
- Make summary generation transparent enough for clinician review.
- Preserve clinician confirm/edit/ignore/reject status.
- Track unsafe wording tests: diagnosis, treatment, triage, risk score, exam ordering, EMR writeback.
- Establish owner for incident reporting and wording correction.

#### Cybersecurity governance

- No real patient data during discovery.
- Before pilot, define access control, authentication, device handling, storage, log retention, deletion, and incident response.
- Any APP, API, ASR server, kiosk, tablet, cloud, or vendor platform must undergo security review.
- Do not connect to hospital systems without explicit governance and institutional approval.

#### Data governance

- Separate synthetic, patient-reported, family-reported, staff-supplemented, and ASR-confirmed sources.
- Define data minimization and retention before real workflow.
- Define whether the future pilot is research, quality improvement, service improvement, or mixed.
- Complete IRB / consent / privacy review before real patient-data use if required.
- Treat FHIR / TW Core IG as future readiness, not current integration.

### 九、分年推動規劃

Because the official first-stage format uses 114-115 planning tables, this draft writes first-stage deliverables in that form. If the parent proposal uses a revised period, the same logic should be shifted to the required official dates.

#### 114 年 9 月 1 日至 115 年 3 月 31 日

| Work content | Checkpoint | Expected evidence | Progress |
| --- | --- | --- | ---: |
| Confirm scope and patient group | Expert-reviewed scope locked to non-acute LUTS / OAB-like patients | Decision record and revised proposal text | 15% |
| Workflow validation design | Draft waiting-room QR/tablet workflow and partial-summary fallback | Workflow diagram and review questions | 25% |
| Question governance | Draft core 10-14 question set plus triggered modules | Question-governance table | 35% |
| Summary template | Draft one-page clinician-review summary | Synthetic summary templates | 45% |
| Safety boundary | Red-flag observation wording and unsafe wording list | Safety checklist | 55% |
| Governance planning | AI / data / cybersecurity governance mapping | Governance gate checklist | 65% |

#### 115 年 4 月 1 日至 115 年 12 月 31 日

| Work content | Checkpoint | Expected evidence | Progress |
| --- | --- | --- | ---: |
| Synthetic walkthrough | 5-10 synthetic cases run through intake to summary | Case outputs and review log | 70% |
| Clinician readability review | 3-5 physicians review summary readability and usefulness | Score sheet and comments | 78% |
| Nursing burden review | Nursing / clinic staff review missing-field handling burden | Nurse burden note and revision items | 84% |
| ASR feasibility review | Optional multilingual ASR tested on non-clinical synthetic / volunteer scripts | ASR confirmation-rate note | 88% |
| KPI finalization | Define final KPI baseline, formula, owner, target, evidence source | KPI table | 92% |
| Pilot-readiness decision | Decide continue / revise / narrow / pause before real patient-data planning | Decision record | 100% |

#### 116-118 future extension, only if first-stage review succeeds

| Year | Possible extension | Gate |
| --- | --- | --- |
| 116 | Limited governed pilot preparation | IRB/privacy/security approval, hospital workflow owner, clinician summary acceptance |
| 117 | Real-world workflow evaluation | Baseline comparison, staff burden data, physician use data |
| 118 | Scale-up or integration-readiness planning | Evidence of workflow value, governance maturity, budget owner, no unresolved responsibility gap |

## 伍、效益評估

### 一、績效指標

The following KPI are proposal-safe because they measure design, validation, governance, and workflow feasibility rather than clinical outcome claims.

| 範疇 | 績效指標 | 衡量或量化基準定義 | 現況數據 | 第一階段達成值 |
| --- | --- | --- | --- | --- |
| 範疇三 | 合成案例流程完成率 | Synthetic cases completing intake -> missing-field display -> clinician summary | 0; not yet formally counted | 5-10 cases completed |
| 範疇三 | 醫師摘要可讀性評分 | 3-5 physicians score one-page summary 1-5 for readability/usefulness | Not yet validated | Median >=4/5 or revise decision recorded |
| 範疇三 | Summary read time | Median seconds required for physician to read one-page summary | Not yet validated | Design target <=60 seconds; actual measured and reported |
| 範疇三 | 缺漏欄位標示準確性 | Missing fields flagged by system compared with manual review on synthetic cases | Not yet measured | >=90% on synthetic review or failure cases listed |
| 範疇三 | Unsafe wording count | Generated summaries contain diagnosis / treatment / triage / risk-score / exam-order / EMR-writeback terms | Current target: zero | 0 unsafe terms in safety test set |
| 範疇三 | 來源標記完整率 | Patient/family/staff/ASR-confirmed source shown in summary | Partial design exists | 100% in synthetic outputs |
| 範疇三 | ASR confirmation rate | ASR-derived text or structured answers confirmed before summary entry | Not yet measured | Feasibility result reported; no unconfirmed ASR enters summary |
| 範疇一 | 重複問診欄位減少可行性 | Expert review of whether summary can reduce repeated basic questions | Not yet proven | Expert decision: continue/revise/narrow/pause with comments |
| 範疇一 | 護理負擔可接受性 | Nurse/staff review of missing-field handling time and responsibility | Not yet validated | Max acceptable nurse time and no-go conditions documented |
| 範疇三 | 治理文件完成度 | AI, data, cybersecurity governance gates listed with owners | Draft only | Governance gate checklist completed |

Do not use as KPI in this first version:

- diagnostic accuracy
- treatment accuracy
- triage accuracy
- acute-risk detection rate
- early cancer detection rate
- mortality reduction
- malpractice reduction
- percentage of physician interview replaced
- automatic medical-record completion rate

### 二、年度查核點說明

#### 114 年 9 月 1 日至 115 年 3 月 31 日

| 工作內容 | 查核點 | 累計預定進度 | 累計預定支用數 | 查核點說明 |
| --- | --- | ---: | --- | --- |
| Scope and workflow design | First-version patient group and waiting-room workflow draft completed | 25% | Parent budget to fill | Prevents writing a broad AI medical system |
| Question governance | Core and triggered question set drafted | 35% | Parent budget to fill | Ensures questions are governed, not model-invented |
| Summary template | One-page clinician-review summary template drafted | 45% | Parent budget to fill | Tests whether physicians have a readable output |
| Safety wording | Red-flag observation wording and unsafe wording blacklist completed | 55% | Parent budget to fill | Prevents AI triage/diagnosis interpretation |
| Governance mapping | AI/data/cybersecurity governance checklist drafted | 65% | Parent budget to fill | Aligns with scope 3 governance expectations |

#### 115 年 4 月 1 日至 115 年 12 月 31 日

| 工作內容 | 查核點 | 累計預定進度 | 累計預定支用數 | 查核點說明 |
| --- | --- | ---: | --- | --- |
| Synthetic validation | 5-10 synthetic cases complete intake-to-summary flow | 70% | Parent budget to fill | Demonstrates flow feasibility without real patient data |
| Physician review | 3-5 physicians review summary readability and usefulness | 78% | Parent budget to fill | Tests whether summary would be read |
| Nurse/staff review | Staff burden and missing-field handling boundary documented | 84% | Parent budget to fill | Prevents hidden nurse workload |
| ASR feasibility | Optional multilingual ASR confirmation workflow tested on non-clinical scripts | 88% | Parent budget to fill | Tests input convenience without making ASR core claim |
| KPI finalization | KPI baseline, target, owner, and evidence source table completed | 92% | Parent budget to fill | Makes proposal measurable |
| First-stage decision | Continue / revise / narrow / pause decision completed | 100% | Parent budget to fill | Gates any real patient-data or pilot planning |

### 三、預期效益

Expected benefits that can be safely written:

- Establish a governed previsit intake workflow for a high-repetition urology outpatient symptom group.
- Improve readiness of clinician review by structuring patient-reported information before the encounter.
- Evaluate whether a one-page summary can reduce repeated basic history-taking.
- Preserve source attribution for patient, family, staff, and ASR-confirmed input.
- Make missing information visible without converting uncertainty into risk labels.
- Establish red-flag observation wording that supports human review without automated triage.
- Create a governance-ready design for AI, cybersecurity, and data handling.

Claims to avoid until measured:

- 已降低醫師問診時間。
- 已提升診斷準確率。
- 已降低急診或醫療風險。
- 醫師一定會採用。
- 護理負擔一定降低。
- ASR 已可處理多語醫療語意。
- 已可串接 EMR。
- 已可臨床使用。

## 陸、出國計畫書

Not proposed for this subproject v0.1.

If the parent proposal includes scope 2 training or international benchmarking, it should be written separately and should not be used to justify this first-version technical workflow unless there is a direct training deliverable.

## 柒、經費規劃

This draft does not assign final numbers. The parent proposal owner must fill amounts according to the official funding standards, institutional budgeting rules, procurement rules, and matching funds.

### 一、budget-to-KPI logic

| Budget line type | Justified only if tied to | Draft note |
| --- | --- | --- |
| Personnel / coordinator | Workflow capture, expert review, KPI tracking, governance documentation | Reasonable first-stage line if parent plan has staff allocation |
| APP / web / tablet intake work | Patient/family completion, source labeling, summary output, audit trace | Include only if a build or prototype is in first-stage scope |
| ASR / speech module | ASR confirmation-rate KPI and input-burden evaluation | Optional; should not dominate budget |
| Security / privacy / governance review | APP/API/ASR/data workflow, audit log, access control | Needed before any real pilot |
| Clinician/nurse review sessions | Summary readability and staff burden KPI | Needed for validation |
| Vendor outsourcing | Clear scope, procurement path, acceptance criteria, deliverables | Avoid until internal vs vendor ownership is decided |
| CRM/API/platform | Future parked phase only | Do not budget in current first version unless parent proposal explicitly reopens it |
| EMR integration | Not first-version scope | Do not budget as current implementation |

### 二、draft cost categories

| Official-style category | Possible item | Current v0.1 recommendation |
| --- | --- | --- |
| 經常門 / 人事費 | Coordinator, research assistant, engineer support, governance support | Fill only if the parent proposal allocates personnel |
| 經常門 / 業務費 | Expert review meeting, usability review, documentation, security consultation | Suitable for design/validation stage |
| 資本門 | Tablet / kiosk / local server / microphone equipment | Use only if a real field workflow is approved; otherwise avoid premature hardware |
| 其他 | Translation review, accessibility review, data-governance consultation | Only if tied to KPI and governance gates |

### 三、procurement boundary

- Do not specify a vendor at v0.1.
- Do not write CRM platform procurement as current execution.
- If any APP/API/ASR work is outsourced, define acceptance criteria:
  - no diagnosis/treatment/triage output
  - source labels preserved
  - ASR confirmation required
  - unsafe wording tests pass
  - audit/version trace available
  - no real patient data without approval

## 捌、人力配置表

| Role | Suggested FTE / effort | Responsibility |
| --- | --- | --- |
| Clinical PI / urology lead | Parent proposal to fill | Clinical scope, patient group, summary fields, safety wording |
| Co-PI / AI-healthcare lead | Parent proposal to fill | AI governance, technical direction, workflow evaluation |
| Clinic workflow owner | Parent proposal to fill | Registration/waiting-room slot, device/fallback, staff role |
| Nursing representative | Parent proposal to fill | Missing-field handling, red-flag observation review, workload limits |
| IT / cybersecurity representative | Parent proposal to fill | Access control, security review, device/platform boundary |
| Data governance / privacy representative | Parent proposal to fill | Data minimization, retention, consent/IRB path |
| Engineer / prototype owner | Parent proposal to fill | Prototype, synthetic cases, audit trace, summary generation |
| Project coordinator / RA | Parent proposal to fill | Meeting logistics, KPI tracking, documentation, evidence package |

## 玖、其他

### 一、open decisions before final proposal

1. Is the first workflow slot truly `報到後 / 候診中`?
2. Should the patient use personal phone QR code, clinic tablet, kiosk, or paper fallback?
3. Will physicians read a one-page summary? What is the maximum acceptable read time?
4. Which five fields must appear at the top?
5. Which fields are noise and should be moved to reviewer/governance view?
6. Should red-flag observations go first to nurse, physician, or both?
7. Does the hospital already have a manual process for visible blood, fever/chills, flank pain, and current inability to urinate?
8. Is `SOAP 架構之醫師覆核參考摘要` acceptable wording?
9. What is the maximum acceptable nurse time per patient?
10. Which budget lines are internal work, and which require procurement?

### 二、risk table

| Risk | Why it matters | Mitigation |
| --- | --- | --- |
| No real workflow slot | System becomes demo-only | Validate with Duobao / clinic before final proposal |
| Physicians ignore summary | No workflow value | Test 3-5 synthetic summaries and read time |
| Hidden nursing burden | Burden shifts rather than decreases | Limit nursing role and measure burden |
| AI wording overclaims | May be read as clinical decision support | Maintain unsafe wording blacklist |
| ASR error becomes fact | Medication/time/number errors can matter | Require confirmation; avoid ASR-only high-risk fields |
| Red flags become triage | Observation wording may imply urgency decision | Use human-review wording only |
| EMR wording misunderstood | May imply formal documentation automation | Use reference-summary wording only |
| Real data collected too early | Privacy/IRB/security risk | Synthetic-only until governance complete |
| Budget not tied to KPI | Formal review risk | Map every budget line to measurable KPI |

### 三、recommended one-paragraph final-safe version

```text
本子項目擬建立「泌尿科門診前問診與醫師覆核摘要支持系統」，以非急性泌尿科門診病人為初期對象，聚焦夜尿、頻尿、急尿、漏尿、排尿困難或尿流變弱等 LUTS / OAB-like 常見症狀。系統透過受治理之題庫、病人或家屬填答、缺漏欄位提示、來源標記與一頁式醫師覆核摘要，協助門診前整理主訴、症狀脈絡、困擾程度與用藥資訊完整度。AI 與 ASR 僅作為降低輸入負擔、輔助結構化填答與摘要整理之工具；系統不提供診斷、治療建議、自動分流、風險評分、檢查開立或 EMR 自動寫入。若產出 SOAP 架構內容，僅作為醫師覆核參考摘要，最終臨床判斷與正式病歷紀錄均由醫師決定。
```

### 四、source files for this draft

Local internal sources:

- `records/2026-05-19/expert-review-revise-and-narrow.md`
- `core/DEEP_CULTIVATION_SYSTEM_POSITIONING.md`
- `discovery/DEEP_CULTIVATION_PROPOSAL_WRITING_GUIDE.md`
- `discovery/DEEP_CULTIVATION_MOHW_COMPLIANCE_RUBRIC.md`
- `records/2026-05-19/policy-documents/manifest.md`
- `records/2026-05-19/policy-documents/application/health-taiwan-phase1-proposal-format-114-115-0909.docx`
- `records/2026-05-19/policy-documents/execution/category3-execution-information-list-114-115-phase1.xlsx`
- `records/2026-05-19/policy-documents/execution/ai-governance-self-checklist.docx`
- `records/2026-05-19/policy-documents/execution/cybersecurity-governance-self-checklist.docx`
- `records/2026-05-19/policy-documents/execution/data-governance-self-checklist.docx`

Official web sources verified during drafting:

- `https://htsprout.nhri.org.tw/download.html`
- `https://htsprout.nhri.org.tw/dhplan_09090949.html`
- `https://htsprout.nhri.org.tw/dhplan.html`
- `https://htsprout.nhri.org.tw/dhplan_07141746.html`
- `https://aicenter.mohw.gov.tw/AC/cp-7200-82982-208.html`
