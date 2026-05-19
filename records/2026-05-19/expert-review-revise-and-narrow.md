# Expert Review: Revise And Narrow

Date: 2026-05-19
Status: accepted latest expert-review direction

## Decision

The current expert-review conclusion is:

```text
Revise + Narrow.
```

The direction is worth including in the Health Taiwan deep-cultivation proposal, but the first version must not be written as a complete urology outpatient AI system.

The first version should focus on:

```text
非急性泌尿科門診前問診 + 醫師覆核摘要
```

The first patient group should be:

```text
非急性 LUTS / OAB-like 症狀病人：
夜尿、頻尿、急尿、漏尿、排尿困難或尿流變弱
```

Blood in urine, fever/chills, flank pain, and currently being unable to urinate may remain as `patient-reported red-flag observations`, but they should not be the first-version main pathway.

## Proposal Category Fit

The best Health Taiwan deep-cultivation fit is:

| Category | Role |
| --- | --- |
| 範疇三：導入智慧科技醫療 | Primary category. AI / ASR / governed question selection / summary support should be written as smart-healthcare tools for clinical workflow support. |
| 範疇一：優化醫療工作條件 | Secondary category. The system may evaluate whether structured previsit collection reduces repeated history-taking and improves information completeness. |

The proposal should not emphasize model novelty. It should emphasize:

- smoother outpatient workflow
- fewer repeated basic questions, to be evaluated
- more complete previsit information, to be evaluated
- clearer governance
- measurable KPI
- AI, data, and cybersecurity governance

## Recommended Name

Primary Chinese name:

```text
泌尿科門診前問診與醫師覆核摘要支持系統
```

English name:

```text
Urology Previsit Intake and Clinician-Reviewed Summary Support System
```

Safe descriptive wording:

```text
泌尿科門診前症狀蒐集與醫師覆核摘要輔助流程
```

Avoid names or claims such as:

- `AI triage`
- `AI diagnosis`
- `AI SOAP generator`
- `EMR automation`
- `AI 醫療系統`
- `AI 診斷`
- `AI 分流`
- `自動病歷`
- `自動產生 EMR`
- `判斷急重症`

## Core Positioning

Allowed proposal wording:

```text
本系統用於門診前蒐集病人或家屬可安全提供之症狀資訊，整理缺漏欄位，產生醫師覆核用摘要草稿。系統不提供診斷、治療建議、自動分流或醫令建議，最終判斷仍由醫師完成。
```

Even safer for SOAP / EMR:

```text
系統產出 SOAP 架構之醫師覆核參考摘要，內容限於病人或家屬回報之症狀、時間脈絡、困擾程度、缺漏欄位與來源標記；不自動寫入 EMR，不產生診斷、治療建議或正式病歷內容，是否採納由醫師決定。
```

## First-Version Patient Group

The first version should target:

```text
非急性、已排定泌尿科門診、主訴為夜尿、頻尿、急尿、漏尿、排尿困難或尿流變弱的成人病人。
```

Rationale:

- These patients have many repeated history-taking fields.
- Many fields can be safely reported by patients or family members.
- This group avoids leading with higher-risk diagnostic pathways.
- LUTS / OAB-like symptoms fit a previsit information-preparation workflow better than acute triage.

Do not make visible hematuria the first main pathway. Blood in urine is clinically important, but formal risk assessment requires more clinical information and governance.

## First Workflow Slot

Most feasible first workflow slot:

```text
報到後 -> 候診期間 -> 病人或家屬用 QR code / tablet 填寫
-> 系統產生摘要
-> 護理或診間端只看缺漏與 red-flag observations
-> 醫師看一頁 summary
```

Key rule:

```text
不要一開始要求護理師補完所有欄位。
```

Nurses should not become questionnaire customer support. First version should make patient/family self-entry the default, with nursing involvement only for:

- incomplete intake that still matters
- clearly conflicting answers
- red-flag observations requiring human review

Partial summary is acceptable if the patient does not complete every field.

## First-Version Exclusions Or Manual-Review Cases

| Patient or situation | Reason | First-version handling |
| --- | --- | --- |
| Currently completely unable to urinate | May require immediate human judgment | Show observation only: `病人回報目前尿不出來，請依院內流程人工確認。` |
| Fever/chills plus flank pain | May involve infection or upper urinary tract concern | No diagnosis or action advice; route to human review. |
| Large visible blood or clots | Sensitive risk communication | Show observation only; clinician/nurse review. |
| Cannot understand questions and no family support | High wrong-answer risk | Paper or manual workflow. |
| ASR content cannot be confirmed | ASR cannot become a fact source by itself | Do not generate finalized summary; mark unconfirmed. |
| Emergency or unscheduled patient | Different workflow | Keep outside first-version outpatient previsit scope. |

## Clinician Summary: Required Shape

Physicians are unlikely to read a raw questionnaire record. The output should be a fast outpatient handoff card.

The first clinician-facing summary should prioritize five fields:

| Order | Field | Example style |
| ---: | --- | --- |
| 1 | 主訴 + 開始時間 + 填答來源 | `主訴：夜尿增加；約 3 個月；本人填寫，家屬協助確認。` |
| 2 | 主要陽性症狀 | Only list positives: nocturia 3+ times, urgency, leakage, dysuria, weak stream. |
| 3 | Patient-reported red-flag observations | `回報：可見血尿 / 發燒畏寒 / 腰側痛 / 目前尿不出來。需人工覆核。` |
| 4 | 用藥與資料完整度 | `可提供藥袋照片 / 只記得部分藥名 / 無法確認目前用藥。` |
| 5 | 缺漏欄位與醫師可追問點 | `未填：是否有血塊、是否目前仍尿不出來、夜尿次數不確定。` |

## Remove From First Clinician Summary

Remove or hide from the physician one-page summary:

| Remove | Reason |
| --- | --- |
| Full system reasoning for why it asked the next question | Too noisy for clinic; keep in reviewer/governance view if needed. |
| Full ASR transcript | Too long and error-prone; preserve only in audit/review evidence if confirmed. |
| Diagnosis candidates, risk labels, exam suggestions, treatment suggestions | Pushes the system into AI diagnosis / AI triage / clinical decision support. |

## Question Set Structure

Core questions can remain about 10-14 items, but not every patient should receive every question.

### Level 1: Ask Everyone In The First Scope

1. Who filled this out: patient / family help / staff help?
2. Main urology concern today.
3. Symptom start time.
4. Bother score 0-10.
5. Daytime frequency increase.
6. Nocturia count.
7. Urgency / hard to hold.
8. Leakage.
9. Pain, stinging, or burning while urinating.
10. Visible blood or clots.
11. Difficulty urinating or unable to urinate.
12. Fever, chills, or flank pain.
13. Can provide medicine list or medication bags.
14. Optional patient note.

### Level 2: Triggered Modules

Use triggered modules instead of asking every detail to everyone:

- nocturia / frequency / urgency: approximate daytime count, urgency frequency, bedtime fluid, coffee/tea/alcohol, 3-day diary feasibility
- leakage: frequency, amount, situation, pad/diaper use
- voiding difficulty: weak stream, straining, intermittency, incomplete emptying
- visible blood: visible blood/clots, repeated or one-time, pain/fever co-report; keep smoking history and risk-factor assessment for clinician or later governed module

### Level 3: Nursing Review

Nursing should only review:

- needs help completing the intake
- red-flag observations
- incomplete medication list
- conflicting answers
- paper/family-assistance need
- whether the physician should see the summary first

### Level 4: Physician-Only

Do not let patients self-judge:

- OAB / BPH / UTI / cancer
- cystoscopy / CT / urodynamics need
- antibiotics / catheter / surgery
- low risk
- no need to see physician
- urinalysis interpretation
- PVR, DRE, pelvic exam, or imaging interpretation

## ASR / Multilingual Input

ASR should be written as:

```text
Optional multilingual input layer
```

Do not write ASR as the main function.

Proposal-safe ASR wording:

```text
系統將探索多語語音輸入在門診前問診的可用性，所有語音轉文字內容均需經病人、家屬或工作人員確認後，才進入摘要。
```

Language direction:

- Traditional Chinese
- English
- Southeast Asian languages such as Vietnamese, Indonesian, Thai, Filipino, depending on hospital service population

Do not promise `多語醫療語意準確` in the first version.

High-error-cost fields should not rely on ASR alone:

| Field | Risk | Handling |
| --- | --- | --- |
| Medication names | ASR can misrecognize names | Medication bag photo or manual confirmation. |
| Dosage | One number error can matter | Do not interpret dosage in first version. |
| Time | Three days / three weeks / three months can be confused | Confirm with choices. |
| Nocturia count | Numeric error | Convert speech to selectable choice and confirm. |
| Blood-in-urine description | Sensitive | Require confirmation. |
| Allergy history | High risk | Exclude from first version or route to manual confirmation. |

## EMR / SOAP Boundary

Avoid:

- `自動產生 EMR`
- `自動完成 SOAP 病歷`
- `AI 協助醫師寫病歷`
- `病歷自動化`
- `AI medical record generation`
- `AI documentation assistant`

Use:

- `醫師覆核用 SOAP 架構參考摘要`
- `SOAP-structured clinician-review summary`
- `病人回報資訊整理草稿`
- `門診前資訊摘要`
- `醫師可採納、修改或忽略`
- `不自動寫入 EMR`
- `不包含診斷與治療建議`
- `不取代正式病歷撰寫`

Safest sentence:

```text
本系統可將病人或家屬回報之門診前資訊整理為 SOAP 架構之醫師覆核參考摘要，內容限於主訴、症狀脈絡、困擾程度、用藥完整度、缺漏欄位與來源標記；系統不產生診斷、治療建議、分流決策或正式病歷內容，也不自動寫入 EMR，最終紀錄與臨床判斷均由醫師決定。
```

## Red-Flag Observation Boundary

Red-flag observations are not triage.

Safe wording:

| Patient report | Safe display |
| --- | --- |
| Visible blood | `病人回報曾看見尿液呈紅色、茶色或血塊。請臨床人員覆核。` |
| Fever/chills | `病人回報近期發燒或畏寒。請依院內流程人工確認。` |
| Flank pain | `病人回報腰部兩側疼痛。請臨床人員覆核。` |
| Currently unable to urinate | `病人回報目前尿不出來或明顯排尿困難。請依院內流程人工確認。` |

Avoid:

- recommend emergency department
- assign high risk
- suspected infection
- suspected pyelonephritis
- suspected cancer
- low risk / can wait
- no need to seek care
- needs catheter
- needs antibiotics
- recommend CT / cystoscopy

If the hospital already has a red-flag process, the system may say `依院內流程通知護理站或醫師`. If no local process exists, use only `人工覆核提示`, not automated triage.

## Proposal Writing: Allowed, Limited, Avoid

### Can Write In Main Text

| Can write | Safe framing |
| --- | --- |
| outpatient previsit intake support | structured previsit intake workflow |
| clinician-reviewed summary | one-page clinician-review summary |
| multilingual input | explore Traditional Chinese, English, and Southeast Asian language input usability |
| ASR | optional input layer |
| SOAP structure | clinician-review reference summary format |
| missing-field prompts | show incomplete or uncertain fields |
| source labeling | separate patient, family, and staff-assisted input |
| governance | AI, cybersecurity, and data governance under scope 3 |
| synthetic demo | basis for expert review and workflow design |
| future EMR | governance planning only, no current integration commitment |

### Can Write With Limits

| Topic | Safe wording |
| --- | --- |
| reduce repeated questions | `評估是否可降低重複問診` |
| physician one-minute summary | `以醫師 1 分鐘內可閱讀為設計目標，待臨床 review 驗證` |
| improve outpatient efficiency | `評估對門診資訊完整性與閱讀效率之影響` |
| ASR burden reduction | `探索 ASR 是否降低病人輸入負擔` |
| SOAP draft | `SOAP 架構之醫師覆核參考摘要` |
| EMR | `未來若涉及 EMR 參考或串接，將另行完成治理審查` |

### Do Not Write

| Do not write | Reason |
| --- | --- |
| AI diagnoses urology disease | Out of scope. |
| AI triages patients | Clinical decision / triage risk. |
| AI recommends treatment | High risk. |
| AI orders tests | High risk. |
| automatically writes EMR | Formal record and responsibility issue. |
| already reduces consultation time | Not yet validated. |
| physicians will definitely adopt it | Not yet validated. |
| ASR can already handle multilingual medical scenarios | Not yet validated. |
| improves diagnostic accuracy | The system does not diagnose. |
| reduces medical errors | Requires clinical evidence. |
| replaces nurse intake | Creates staffing and responsibility risk. |

## KPI Recommendations

### Phase 1: Design / Validation KPI

| KPI | Measurement | Safety |
| --- | --- | --- |
| Synthetic-case flow completion | 5-10 synthetic cases complete intake -> summary | High |
| Physician readability score | 3-5 physicians rate summary 1-5 | High |
| Summary read time | Median seconds to read one-page summary | High |
| Missing-field marking accuracy | System missing fields compared with manual review | High |
| Unsafe wording count | Diagnosis / treatment / triage words remain 0 in safety tests | High |
| Source-label completeness | Patient/family/staff source labels present | High |
| ASR confirmation rate | User can confirm transcript after voice input | Medium |
| Multilingual input usability pilot | Synthetic or volunteer non-clinical scripts by language | Medium |

### Phase 2: Clinical-Setting KPI Only After Governance

| KPI | Required condition |
| --- | --- |
| repeated-question time reduction | baseline and pilot comparison |
| information completeness improvement | defined core fields and pre/post comparison |
| actual physician use rate | hospital pilot |
| nursing burden change | nursing time record |
| patient completion rate | real or simulated field workflow |
| patient satisfaction | questionnaire and ethics/governance |
| EMR adoption rate | formal medical-record workflow governance |

### Do Not Use As KPI

- diagnostic accuracy
- treatment accuracy
- triage accuracy
- acute-risk detection rate
- early cancer detection rate
- mortality reduction
- malpractice reduction
- percentage of physician interview replaced
- automatic medical record completion rate

## Fifteen Expert Questions

### Workflow

1. Should this intake happen before registration, after registration while waiting, before nursing station, or inside the consultation room?
2. Which first patient group is best: nocturia/frequency/urgency/leakage/voiding difficulty/hematuria? Please rank.
3. Which patients should be excluded from first version?
4. If the patient completes only 60 percent, is the partial summary still useful?
5. What is the maximum nurse time acceptable per patient for missing-field handling?

### Summary

6. Would physicians read a one-page summary? What is the maximum acceptable read time?
7. Which five fields must be at the top?
8. Which fields are noise?
9. Should missing fields appear at the top or bottom?
10. Should patient/family/staff source be visibly marked?

### Safety

11. Should red-flag observations go first to nurses or directly into physician summary?
12. Does the hospital already have a manual workflow for current inability to urinate, fever/chills, flank pain, or visible blood?
13. Which wording makes the system sound like diagnosis or triage?

### Proposal

14. Should this module be in the main proposal text, appendix, or demo evidence?
15. Is `SOAP 架構之醫師覆核參考摘要` safe, or could it be misunderstood as automatic medical record writing?

## Meeting Opening Script

```text
老師，我這次不是想請您看 AI 技術本身，而是想請您判斷這個流程在真實泌尿科門診裡有沒有位置。

目前定位很保守：病人或家屬在門診前或候診時，提供一些可安全回報的症狀資訊，例如主訴、開始時間、夜尿次數、是否漏尿、是否尿痛、是否看見血尿、是否目前尿不出來、藥單是否完整。系統只做三件事：整理病人回報、標示缺漏欄位、產生一頁式醫師覆核摘要。

這不是 AI 診斷、不是 AI 分流、不是治療建議，也不自動寫入 EMR。若用 SOAP 架構，也只是醫師覆核參考摘要，最後是否採納由醫師決定。ASR 也只是 optional input layer，支援繁體中文、英語或東南亞語系輸入，語音內容仍需要確認。

我今天最想請您幫我判斷三件事：第一，病人什麼時候填最合理；第二，醫師會不會看這份 summary；第三，哪些內容可以安全寫進深耕計畫，哪些 claim 會太危險。CRM follow-up 這次先不做，先確認 previsit intake 和 clinician-review summary 是否值得繼續。
```

## Main Proposal Draft Paragraph

```text
本子項目擬建立「泌尿科門診前問診與醫師覆核摘要支持流程」，以非急性泌尿科門診病人為初期對象，聚焦夜尿、頻尿、急尿、漏尿、排尿困難等常見症狀。系統透過受治理之題庫、病人或家屬填答、缺漏欄位提示、來源標記與一頁式醫師覆核摘要，協助門診前整理主訴、症狀脈絡、困擾程度與用藥資訊完整度。

AI 與 ASR 僅作為降低輸入負擔、輔助結構化填答與摘要整理之工具；ASR 支援繁體中文、英語及東南亞語系之可用性探索，語音轉文字內容需經確認後才進入摘要。系統不提供診斷、治療建議、自動分流、風險評分、檢查開立或 EMR 自動寫入。若產出 SOAP 架構內容，僅作為醫師覆核參考摘要，最終臨床判斷與正式病歷紀錄均由醫師決定。

現階段以合成資料 demo、專家審查與工作流程驗證為主，後續將依臨床端確認之 workflow slot、醫師可讀性評估、護理負擔評估、AI 治理、資安治理與資料治理條件，再規劃是否進入真實場域試行。
```

## Source Notes

The expert response cited official Health Taiwan, HTSprout, MOHW AI Center, AUA/SUFU, and NICE sources. This record stores the expert's synthesis and should be paired with the local official archive under `policy-documents/` and the source-backed notes:

- `health-taiwan-deep-cultivation-policy-reference.md`
- `health-taiwan-related-examples.md`
- `policy-documents/README.md`
- `policy-documents/manifest.md`

## Implication For Current Repo

Future writing should reflect:

- main direction can continue, but proposal text must be revised
- first version must narrow to non-acute LUTS / OAB-like stable outpatients
- proposal should be primarily under scope 3 smart healthcare and secondarily under scope 1 workflow improvement
- CRM follow-up is parked until a future confirmed next step
- ASR is optional multilingual input, not core clinical value
- SOAP / EMR wording must stay as clinician-review reference summary, not automatic record generation
- red-flag observations need SOP wording before stronger workflow claims
- KPI must be split into design/validation KPI and later clinical-setting KPI
