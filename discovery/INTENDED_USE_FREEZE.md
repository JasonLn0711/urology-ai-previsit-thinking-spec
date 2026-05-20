# Intended Use Freeze

Status: proposal-prep freeze v0.1

Date: 2026-05-20

Purpose: define the intended use and explicit non-use before drafting the Health Taiwan Deep-Cultivation proposal v0.2.

## Controlling Documents

Use this file together with:

- `DEEP_CULTIVATION_PROPOSAL_WRITING_GUIDE.md`
- `DEEP_CULTIVATION_POSTDOC_NEXT_STEP_REVIEW.md`
- `CLINICAL_FRICTION_REDUCTION_ANALYSIS.md`
- `ASSERTIVE_WRITING_GATE.md`
- `../core/DEEP_CULTIVATION_SYSTEM_POSITIONING.md`
- `../core/ASSERTIVE_WRITING_POLICY.md`
- `../core/SAFETY_BOUNDARY.md`
- `../core/EVALUATION.md`

## One-Sentence Intended Use

```text
本系統用於非急性泌尿科門診病人於報到後或候診期間，透過受治理之門診前問診流程蒐集病人或家屬可安全提供之症狀資訊，整理缺漏欄位、來源標記與一頁式醫師覆核摘要，以降低重複問診、資料缺漏與臨床工作摩擦。
```

Short English working statement:

```text
A low-friction urology previsit intake and clinician-reviewed summary support workflow for scheduled non-acute outpatient visits.
```

## Target Setting

| Field | Freeze |
| --- | --- |
| Department | Urology |
| Care setting | Scheduled outpatient clinic |
| Clinical acuity | Non-acute, stable outpatient context |
| Workflow slot | After registration / waiting-room QR code or tablet intake |
| Primary user | Patient or family/helper |
| Secondary user | Clinic staff only when needed |
| Reviewer | Urologist / clinician |
| Proposal role | Health Taiwan smart-healthcare workflow support with clinical decision authority preserved at clinician level |

## Target Symptom Scope

First-version scope:

- nocturia
- frequency
- urgency
- leakage
- voiding difficulty
- weak stream

These are treated as LUTS / OAB-like outpatient visit-preparation symptoms.

## Patient-Reported Observation Scope

The following are handled as patient-reported observations for human review:

- visible blood in urine or blood clots
- fever or chills
- flank pain
- currently unable to urinate or severe voiding difficulty

Allowed wording:

```text
病人回報[觀察內容]，請臨床人員依院內流程人工覆核。
```

Disallowed wording:

```text
疑似感染 / 疑似癌症 / 建議急診 / 需要導尿 / 需要抗生素 / 高風險
```

## System Outputs

Allowed outputs:

- patient-facing confirmation page
- missing-information list
- source-labeled structured intake record
- patient-reported red-flag observation display
- one-page clinician-review summary
- optional SOAP-structured reference summary for clinician review only
- audit and version metadata design

Disallowed outputs:

- final diagnosis
- differential diagnosis
- risk score
- urgency score
- queue priority
- treatment recommendation
- medication instruction
- exam or procedure recommendation
- formal EMR note
- direct HIS / EMR / EHR writeback

## Non-Use Freeze

This system must not be used as:

- AI triage
- AI diagnosis
- AI doctor
- automated clinical decision support
- emergency intake workflow
- official medical-record generator
- autonomous routing or department-assignment tool
- patient-facing treatment advice system
- production hospital integration without separate governance

## Data Boundary

Current proposal-prep and demo materials may use:

- synthetic cases
- non-real examples
- reviewer comments without patient identifiers
- public policy and governance references

Current proposal-prep and demo materials must not use:

- real patient identifiers
- real medical record numbers
- real appointment or queue data
- real HIS / EMR records
- identifiable patient audio
- identifiable patient transcript
- unapproved clinical deployment data

Any future real-patient workflow requires a separate decision on IRB, consent, privacy, retention, deletion, access control, security, responsibility, and hospital ownership.

## Responsibility Boundary

| Actor | Responsibility |
| --- | --- |
| Patient / family | Report answers as best as possible; confirm visible summary before handoff if supported |
| Clinic staff | Assist only in defined cases such as inability to complete, contradiction, missing medicine information, or local red-flag workflow |
| Clinician | Owns interpretation, final judgment, documentation, and patient communication |
| System | Organizes patient-reported information, shows missing fields and source labels, avoids overclaiming |
| Project team | Maintains safety boundary, versioning, auditability, and proposal evidence |
| Hospital owner | Defines workflow slot, governance path, procurement path, and operational ownership before real use |

## Clinical Friction Rule

This intended use is valid only if the system reduces net clinical friction.

Before adding a feature, ask:

1. Does it reduce an existing burden?
2. Whose burden does it reduce?
3. Does it create hidden burden for physicians, nurses, clinic staff, IT, or administrators?
4. Does it require new routine labeling, new dashboards, new logins, or major retraining?
5. Can the burden reduction be measured?

If the answer is unclear, keep the feature outside first-version proposal scope.

## Proposal-Safe Paragraph

```text
本子計畫定位為低摩擦智慧醫療流程支持工具，第一版聚焦非急性泌尿科門診前症狀蒐集與醫師覆核摘要。系統整理病人或家屬回報之門診前資訊、標示缺漏欄位、保留來源標記，並產生一頁式醫師覆核摘要，以降低重複問診、資訊缺漏修補與文書準備負擔。診斷、治療建議、自動分流、風險評分、正式病歷內容與 HIS/EMR 寫入均保留於醫師及院內治理流程，最終臨床判斷與正式紀錄由醫師決定。
```

## Freeze Decision

For Health Taiwan proposal v0.2, this intended-use freeze is the controlling boundary.

Any proposal text, KPI, budget line, system diagram, or demo feature that violates this freeze should be revised or moved to a separately governed future phase.
