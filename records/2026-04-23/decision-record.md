# Decision Record: 2026-04-23 Urology Smart-Previsit Discovery

## Status

Status: synthesized

The morning meeting did not complete the original four-case clinician review. It did produce enough workflow, funding, IP, vendor, and source-material evidence to continue as a safe-local v1 product preview and to run a Phase 0 synthetic clinician/nurse review before any real-data pilot.

## Decision Identity

| Field | Notes |
| --- | --- |
| Decision record ID | DR-2026-04-23-001 |
| Date | 2026-04-23 |
| Decision owner | Jason |
| Reviewers / source owners | 吳育德老師, 許富順醫師 / 泌尿科 |
| Related capture note | `meeting-capture.md` plus planning transcript/source archive |
| Current status | synthesized; needs 許醫師 follow-up review before acceptance |

## Decision

Continue, but only as a bounded safe-local v1 product preview and Phase 0 clinician/nurse review.

Do not proceed to production deployment, real patient data, live HIS/registration integration, autonomous exam ordering, diagnosis, treatment recommendation, triage, real-data learning loops, or regulatory classification claims.

## Evidence Summary

| Evidence | Source | Strength | Implication |
| --- | --- | --- | --- |
| Current workflow has repeated questioning and physician-time pressure | Meeting transcript, 許醫師 slides, Gemini synthesis routed as hypothesis | Medium | Throughput is a valid research framing, but minutes-saved claims still need measurement. |
| Clinician can name useful previsit-safe information | 許醫師 QA/rules file and meeting discussion | Strong | v1 should center on initial/return visit history, medication/allergy/surgery/chronic disease, symptom-specific forms, and confirmation-only exam-prep reminders. |
| Waiting-room `陽明小幫手` has a clearer v1 workflow slot than registration support | 許醫師 QA/rules file | Strong | Lead with already-registered waiting-room flow; keep `聯醫AI小幫手` registration support as future scope. |
| One-minute clinician-review summary would be read | Meeting signal was positive but not case-level | Medium | Build/read a summary in Phase 0; do not claim validated adoption yet. |
| Staff burden is acceptable | Not directly validated | Weak | Nurse review must be tested explicitly in Phase 0. |
| Patient or assisted completion is realistic | Discussed, not tested | Weak | Keep family/source labels and nurse repair; patient usability remains a future test. |
| Safety boundaries remain acceptable if wording is descriptive | Meeting discussion plus regulatory/privacy source review | Medium | Keep diagnosis/treatment/ordering/HIS/regulatory claims outside v1. |
| IP/vendor/funding questions are unresolved | Meeting transcript and next-action notes | Strong | Any real build beyond v1 requires patent/vendor/institution review. |

## Confirmed Boundaries

| Boundary | Status | Notes |
| --- | --- | --- |
| No diagnosis | unchanged | Show patient-reported observations only. |
| No triage | unchanged | No urgency labels, risk scores, or time-critical directives. |
| No treatment advice | unchanged | No medication or treatment recommendations. |
| No autonomous exam ordering | strengthened | QA exam-prep matrix is confirmation-only source material. |
| No real patient data during v1 | strengthened | Use synthetic cases only; no real ID, birthday, phone, MRN, queue, appointment, or hospital identifier. |
| Clinician review required | unchanged | The product prepares a summary for review; it does not decide. |
| Regulatory status not determined | strengthened | TFDA/FDA positioning is a formal review gate. |
| No live HIS/registration/messaging | strengthened | Export/mock API is discussion material only. |

If any boundary changes, stop and create a governance review before continuing.

## Assumptions Tested

| Assumption | Keep, revise, reject, or unknown? | Evidence |
| --- | --- | --- |
| The first useful version is guided, not autonomous | Keep | QA file supports structured flow and physician/nurse confirmation. |
| Repeated questions create meaningful workflow friction | Keep as hypothesis | Meeting and slides support this, but quantitative measurement is not done. |
| A short clinician-review summary would be useful | Keep as hypothesis | Positive meeting signal, but no line-level review yet. |
| Patients may need nurse or family assistance | Keep | Existing v1 source-label and nurse-repair model remains appropriate. |
| Missing-information prompts are safer than interpretation | Keep | Fits no-diagnosis boundary and nurse workflow. |
| Real patient data should remain out of discovery | Keep | Privacy/regulatory gates unresolved. |
| HIS integration is the immediate next technical step | Reject for v1 | Too much governance blast radius before summary value is proven. |
| TFDA non-device status can be claimed now | Reject | Classification must remain formal review gate. |

## Open Questions To Close

| Question | Answered, revised, or still open? | Notes |
| --- | --- | --- |
| What is the current flow from check-in to physician entry? | Partly answered | Waiting-room `陽明小幫手` is the clearest v1 slot; exact nurse handoff workflow still needs review. |
| Which questions are repeated most often? | Partly answered | QA file gives complaint categories and training logic; Phase 0 should verify priority and noise. |
| Which information can be safely pre-collected? | Partly answered | History and symptom forms are safe in synthetic v1; real collection needs governance. |
| Which topics must remain physician-led? | Answered for v1 | Diagnosis, triage, treatment, exam ordering, interpretation, and HIS writeback. |
| Which operating mode is realistic? | Revised | Prefer already-registered waiting-room QR preview over registration-helper mode. |
| What summary format would be read? | Still open | Needs timed physician review of v1 summaries. |
| What would make the concept unsafe or unacceptable? | Partly answered | Real data, identifiers, live integration, ordering language, risk/probability outputs, vendor/IP conflict. |

## Next Small Artifact

| Field | Notes |
| --- | --- |
| Artifact | Phase 0 clinician/nurse review packet for v1 |
| Purpose | Test summary usefulness, nurse repair prompts, exam-prep wording, and first three complaint flows using synthetic data only. |
| Reviewer | 許醫師 plus at least one nurse/staff workflow reviewer if possible. |
| Done definition | Filled scorecard, line-level useful/noisy/unsafe notes, confirmed/revised first three flows or narrowed scope, completed flow worksheet, and explicit continue/revise/narrow/pause/governance-review decision. |
| Explicit non-goals | No real patient data, real queue/registration behavior, HIS writeback, diagnosis, treatment, triage, autonomous orders, or classification claim. |

Proposed first-three default for the Phase 0 opening review: `頻尿或夜尿`, `小便困難或尿不出來`, and `血尿或健檢發現潛血`. This is not accepted evidence until 許醫師 confirms or changes it.

Follow-on implementation support: the demo repo now includes `synthetic-hematuria-occult-blood`, so all three proposed flows can be reviewed with runnable synthetic cases.

Live evidence capture support: the demo repo now includes `docs/research/v1-phase0-review-capture.md` to collect boundary checks, five-case read times, first-three-flow decisions, nurse burden, exam-prep wording, export concerns, governance gates, and one decision during the review.

Readiness-gate support: the demo repo now exposes `npm run phase0:check`. The latest run against `http://127.0.0.1:4176/app/v1/` passed `76/76`, covering route availability, five synthetic cases, live capture, scorecard, worksheet, safety boundaries, smoke checks, and tests.

## Paper Implication

What this decision could contribute:

- A workflow study framing: physician-reviewed previsit summarization may reduce repeated information gathering by separating patient/family intake, nurse repair, and clinician-owned interpretation.
- A design-safety framing: useful AI/LLM value can be constrained to summarization, source labeling, missing-field repair, and confirmation-only exam-prep context.

Evidence still missing:

- timed summary review
- staff burden feedback
- patient/family usability
- measured repeated-question reduction
- clinic workflow fit beyond physician strategy discussion

## Patent Reasoning Implication

System logic clarified:

- waiting-room previsit flow
- initial/return visit branching
- source-labeled patient/family/staff answers
- missing-field repair before clinician handoff
- neutral physician summary
- confirmation-only exam-prep matrix
- mock export/API boundary

What must not be claimed yet:

- questionnaire novelty by itself
- clinical diagnosis automation
- treatment or triage automation
- proven time savings
- proven hospital adoption
- freedom to operate around 許醫師 patent or vendor system

## Product Implication

Adoption signal:

- Positive physician collaboration signal.
- Clear cost/funding pain from personal subsidy.
- Source materials provide concrete workflow requirements.

Rejection or blocker signal:

- No completed four-case review yet.
- Nurse burden not validated.
- IP/vendor/institution ownership unresolved.
- Privacy/security/HIS/regulatory gates unresolved.

## Phase 0 Protocol

Use `../../discovery/V1_PHASE0_CLINICIAN_REVIEW_PROTOCOL.md`.

The decision after Phase 0 should be one of:

- continue with revised v1
- revise the workflow/wording
- narrow to first three complaint flows
- revise the proposed first-three shortlist
- pause
- governance review before any next build

## Pause Triggers

Pause or re-review if:

- safety wording drifts into diagnosis
- real patient data is proposed without governance
- staff burden becomes unacceptable
- clinicians would not read the output
- no workflow slot exists
- IP/vendor boundary blocks implementation
- next artifact becomes broader than the evidence supports

## Final Reviewer Note

This decision is justified because the meeting and source materials support a bounded workflow problem and a concrete synthetic product preview, but they do not yet justify real patient data, hospital integration, clinical-use claims, or broad platform commercialization.
