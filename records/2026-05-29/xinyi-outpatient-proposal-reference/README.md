# Reference Analysis: Subproject Three Digital Musculoskeletal Function And Home Follow-Up Proposal

Status: captured and analyzed

Date captured: 2026-05-29

Source PDF copied from:

```text
/home/jnclaw/every_on_git_jnclaw/project_aura/260529_0937_withProfWu/attached-子計畫三：數位化肌肉骨骼功能評估與居家追蹤計畫-15頁擴充版.pdf
```

Local source files:

- `sources/attached-subproject-3-digital-msk-function-home-followup-15p-expanded.pdf`
- `sources/full-text.txt`
- `sources/pdfinfo.txt`
- `sources/source-pdf.sha256`

Checksum:

```text
5f711ce86731fb1b7eb6533a37cd7746f7040b67b94100a60f543ba3ad3c2c05
```

PDF metadata:

| Field | Captured value |
| --- | --- |
| Pages | 18 |
| Producer | WeasyPrint 62.3 |
| Page size | A4 |
| File size | 589,965 bytes |

## 1. Source Identity

| Field | Captured content |
| --- | --- |
| Proposal title | 臺北市智慧健康城市整合發展計畫 - 子計畫三：數位化肌肉骨骼功能評估與居家追蹤計畫 |
| Expanded subtitle | 完整15頁專案政策推動與技術實施計畫書 |
| Main technical focus | 智慧手機感測、計算機視覺 ROM、動態疼痛地圖、遠距全週期閉環追蹤 |
| Sponsor | 臺北市政府衛生局 |
| Executing unit | 臺北市立聯合醫院, 復健醫學科 / 總院決策中心 / 區門診部 |
| Cooperating units | 臺北市政府資訊局、各局處人事室、社區長照與關懷據點 |
| Execution period | 116/01/01 to 118/12/31 |
| Total budget | NT$10,000,000 |

## 2. Full Section Map

| Section | Function in the reference |
| --- | --- |
| Cover | Establishes topic, sponsor, executors, cooperators, period, and total budget. |
| Table of contents | Lists 13 sections, ending with KPI and budget tables. |
| 1. Background and goal | Positions musculoskeletal disease as a high-burden aging and workplace issue. |
| 2. Traditional assessment pain points | Explains hardware cost, white-coat/context distortion, manual ROM error, and paper-questionnaire follow-up failure. |
| 3. Digital mobile platform architecture | Presents a three-layer edge, cloud, and clinical/patient architecture. |
| 4. Smartphone IMU gait analysis | Defines phone-based gait signal extraction and clinical indicators. |
| 5. Computer vision ROM measurement | Defines camera-based skeletal keypoint capture and ROM estimation. |
| 6. Digital pain map and questionnaires | Converts pain location, pain quality, VAS, ODI, WOMAC, and NDI into digital intake. |
| 7. Risk-group routing | Defines workplace sedentary users and community older adults as target populations. |
| 8. Home rehab adherence and SDM | Links digital exercise prescription, adherence tracking, and shared decision-making. |
| 9. Three-year implementation matrix | Breaks 36 months into six stages. |
| 10. Organization and manpower | Creates software, clinical, and outreach work groups. |
| 11. Privacy and cybersecurity | Describes de-identification, TLS 1.3, API controls, DMZ, IDS, and FHIR. |
| 12. KPI table | Gives year-by-year quantitative targets. |
| 13. Budget table | Allocates NT$10,000,000 across nine accounting categories. |

## 3. Technical Components Captured

| Component | Reference detail | Useful pattern for urology proposal |
| --- | --- | --- |
| Edge sensing client | iOS / Android app, phone IMU, phone camera | Use a simple patient/family intake surface, not new device complexity. |
| Cloud engine | CNN skeleton model, gait features, RESTful API | Use backend only as workflow support; keep AI as a governed service layer. |
| Clinical dashboard | physician / therapist dashboard and patient tracking | Use clinician-review summary and care-team follow-up dashboard language. |
| IMU gait analysis | 100 Hz acceleration and gyroscope signals, filtering, heel-strike / toe-off logic | Adopt the pattern of translating raw signal to clinical-readable fields, but use urology symptom fields instead of gait metrics. |
| CV ROM | keypoint localization, vector-angle calculation, dynamic tracking | Useful as a technical completeness pattern only. Not part of urology scope. |
| Digital pain map | anatomical localization, VAS, pain quality | Analogous to urology symptom localization, severity, bother, duration, and source-labeled notes. |
| Adaptive questionnaires | ODI, WOMAC, NDI with adaptive skip logic | Strong pattern for governed question routing and short intake. |
| Home adherence | digital exercise prescription and adherence tracking | Analogous to CRM follow-up and reminder completion if CRM is reopened. |

## 4. Clinical And Service Logic

The reference uses a complete service pathway:

```text
screening / self-assessment
-> risk classification
-> outpatient or specialist routing
-> home rehabilitation prescription
-> adherence monitoring
-> SDM review
-> KPI and scale-up
```

The useful lesson for the urology proposal is not the specific musculoskeletal pathway. The useful lesson is that a fundable proposal reads as a complete service system, not as an isolated AI demo.

For the urology previsit proposal, the parallel structure should be:

```text
urology outpatient or screening context
-> guided previsit / follow-up intake
-> missing-field and source-label visibility
-> clinician-review summary
-> workflow or CRM follow-up queue if reopened
-> KPI-backed evaluation
```

## 5. Target Populations And Routing

The reference names two target groups:

| Group | Proposed assessment | Proposed route |
| --- | --- | --- |
| City-government sedentary workers | NDI, ODI, shoulder/neck ROM | workplace stretch support, outpatient rehab, or specialist referral depending on risk level |
| Community older adults | IMU gait, knee ROM, WOMAC | community exercise, outpatient fall-prevention program, or specialist review depending on risk level |

Useful pattern:

- name the target group
- define the first workflow entry point
- define what the system produces
- define who reviews the output
- define what KPI proves the pathway worked

Urology adaptation:

- target: non-acute urology outpatients or PSA/community-screening follow-up group
- entry point: after registration, waiting room, or approved screening follow-up
- output: one-page clinician-review summary and CRM-ready follow-up fields
- reviewer: clinician and care team
- KPI: summary read time, completion, missing-field visibility, follow-up completion, staff-friction score, safety wording count

## 6. Implementation Timeline Pattern

The reference divides three years into six phases:

| Year / phase | Reference content | Urology adaptation |
| --- | --- | --- |
| 116 phase 1 | project team, SRS, prototype UI/UX | owner confirmation, intended-use freeze, question bank, summary schema, v0.5 proposal transfer |
| 116 phase 2 | app beta, questionnaires, IRB, small validation | synthetic cases, clinician/staff review, safety wording tests, IRB/QI route if real data is planned |
| 117 phase 3 | app store release, HIS/API test, training | governed limited pilot only if approved; no automatic production HIS/EMR writeback |
| 117 phase 4 | 30 screening events, 2,000 users, midterm audit | limited workflow evaluation and follow-up metrics if site ownership exists |
| 118 phase 5 | citywide scale, 8,000 users, adherence data | scale decision after evidence, CRM or interoperability only if governance passes |
| 118 phase 6 | final report, conference, journal paper | final evaluation report, maintenance plan, and publication only if data governance supports it |

## 7. Organization Pattern

The reference creates three work groups:

| Work group | Reference responsibility | Urology adaptation |
| --- | --- | --- |
| Software and algorithm group | app, algorithms, UI/UX, cloud maintenance | intake workflow, summary schema, CRM-ready fields, versioned evidence |
| Clinical validation and SDM group | IRB, clinical validation, prescriptions, HIS view | clinical question approval, summary review, safety boundary, QI/IRB route |
| Workplace/community outreach group | site scheduling, screening, case routing | outpatient workflow owner, registration/waiting-room slot, follow-up owner, staff-burden review |

The urology proposal should keep this role-based clarity, but avoid naming production responsibilities before the hospital confirms owners.

## 8. KPI Pattern Captured

The reference KPI table has three useful qualities:

- KPI are grouped by year.
- KPI include numeric thresholds.
- KPI connect system build, validation, deployment, security, and service outcomes.

Captured reference targets include:

| Year | KPI examples |
| --- | --- |
| 116 | app beta 100%; IRB approval 100%; clinical correlation r >= 0.85; at least 5 needs interviews |
| 117 | 30 screening events; at least 2,000 users; report generation <=3 seconds; pass source scan and penetration test with no medium/high vulnerabilities |
| 118 | 50 total screening events; at least 8,000 total users; referral completion >=75%; home rehab adherence >=65% |

Urology KPI translation:

| Reference KPI type | Urology counterpart |
| --- | --- |
| app beta | guided intake and clinician-summary prototype ready |
| IRB approval | IRB/QI route determined before real patient data |
| clinical correlation | clinician usefulness and summary-read-time scorecards |
| needs interviews | workflow-slot and staff-friction reviews |
| screening events | approved limited walkthrough or pilot sessions |
| source scan / penetration test | security review, safety wording test, audit trail check |
| referral completion | follow-up or return-visit completion only if CRM phase is funded and governed |

## 9. Budget Pattern Captured

The reference budget totals NT$10,000,000:

| Budget item | Three-year total |
| --- | ---: |
| Software R&D and algorithm customization | 2,000,000 |
| Clinical-patient platform and HIS interface | 1,200,000 |
| Dedicated core R&D and clinical personnel | 3,240,000 |
| Cloud computing and server rental | 600,000 |
| Cybersecurity and third-party testing | 450,000 |
| Screening hardware and mobile-station supplies | 300,000 |
| Clinical validation and gold-standard comparison | 120,000 |
| Education materials and final presentation | 390,000 |
| Project operations and administration | 1,700,000 |

Useful lesson:

```text
Budget tables must show the work type, annual split, total, and why the line exists.
```

Urology adaptation:

- Replace broad app/HIS claims with intake-summary workflow, reviewer evidence, governance, and CRM-ready fields.
- Keep security/testing visible.
- Keep personnel/coordination visible because KPI evidence, review sessions, and documentation require work.
- Keep equipment conditional until the workflow site confirms tablets, microphones, or intake stations.

## 10. Governance And Safety Review

The reference includes a useful governance section, but the urology draft should tighten it.

Adopt:

- special-category health data awareness
- de-identification and minimum necessary data
- TLS and API security controls
- access control and audit logging
- cybersecurity testing
- separation between app/front end and hospital core systems

Modify:

- Treat HIS/EMR/FHIR integration as future readiness or a governed later phase.
- Avoid stating that output is automatically shown in HIS unless hospital IT approval exists.
- Avoid implying automatic red/yellow/green medical routing without clinician-owned protocol.
- Replace "forced appointment" or "high-risk citizen must not be missed" with staff-review follow-up workflow language.

## 11. Quality Issues In The Reference

These issues should not be copied into the urology proposal:

| Issue | Why it matters |
| --- | --- |
| PDF title says 15 pages but file has 18 pages | Page-control mismatch should be fixed before circulation. |
| Section numbering is inconsistent | Section 5 uses 4.1 / 4.2 and section 8 uses 10.1 / 10.2. |
| Generated math artifacts appear | Examples include `ext{ Hz}`, `rac`, and malformed vector notation. |
| `Cloud Cloud Engine` wording appears | Needs professional terminology cleanup. |
| Strong clinical claims lack citations in the extracted text | Claims such as risk increases and thresholds need source support. |
| Direct HIS and FHIR output is asserted early | Requires governance, IT, procurement, and privacy approval. |
| Triage and forced-routing language is too strong | For proposal safety, use human-review follow-up and approved SOP language. |
| Budget purpose language is sometimes broader than KPI evidence | Each budget line should map to an owned KPI and evidence artifact. |

## 12. Recommended Use In v0.5

Use this reference as a checklist, not as source language.

Recommended adoption into `DEEP_CULTIVATION_APPLICATION_DRAFT_V0_5.md`:

- cover identity and budget visible at the top
- 20-page discussion-version page budget
- 13-section maximum structure
- year-by-year milestone table
- organization and responsibility table
- KPI table with numeric targets
- NT$10,000,000 budget table with KPI mapping
- governance section before KPI and budget

Recommended exclusions:

- autonomous triage or clinical routing claims
- direct production HIS/EMR writeback
- current FHIR integration claims
- broad citywide scale numbers before site ownership exists
- medical-device or clinical-effectiveness claims without evidence

## 13. Urology Proposal Translation

For the 信義生醫 / 院外門診部 urology proposal, the positive-scope framing should be:

```text
本計畫建立一套可於院外門診部或指定門診流程導入的泌尿科門診前症狀蒐集與醫師覆核摘要支持流程。系統以低摩擦問診、來源標記、缺漏欄位可見化、醫師覆核摘要與治理紀錄為核心，支援醫師更快掌握病人主訴與追問方向，並以三年期 KPI 驗證門診前資訊完整性、摘要可讀性、工作摩擦降低與治理成熟度。
```

This keeps the proposal active, useful, and credible while preserving clear clinical authority and governance boundaries.
