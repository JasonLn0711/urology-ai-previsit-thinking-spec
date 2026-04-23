# Meeting Capture: Urology Smart-Previsit Discovery

## Status

Status: captured

This is a synthesized capture from the 2026-04-23 meeting transcript, post-meeting source archive, 許醫師 LINE follow-up materials, doctor-provided current Argon links, and the same-day 16:00 吳老師 follow-up discussion. The original four-case product review was not completed, so case-level usefulness remains pending Phase 0 review.

No real patient identifiers, identifying patient stories, diagnosis, triage, treatment advice, or production commitments are recorded here.

## Meeting Identity

| Field | Notes |
| --- | --- |
| Date | 2026-04-23 |
| Time | Recording/session label `260423_0958`; transcript spans roughly `00:01:30` to `00:48:15` |
| Format | Online |
| Participants | 吳育德老師, 許富順醫師 / 泌尿科, Jason |
| Primary question | Does guided previsit collection solve a real workflow problem? |
| Actual meeting shape | Shifted from four-case demo review into current workflow, vendor/funding, IP, privacy/security, and team-owned platform strategy. |
| Decision needed | Continue / revise / narrow / pause for next artifact, not deployment. |

Follow-up sources added later on 2026-04-23:

- `聯醫小幫手`: `https://chat.argon.chat/visitor?guid=rmw6oqqxgy`
- `陽明小幫手`: `https://chat.argon.chat/visitor?guid=avp6dg160g`
- 16:00 吳老師 discussion transcript/audio, archived in the planning repo source bundle.

## 1. Current Workflow Facts

| Step | Who is involved? | What happens now? | Information collected | Pain point or friction |
| --- | --- | --- | --- | --- |
| Pre-registration / before clinic | Patient, current platform concept | `聯醫AI小幫手` can be imagined as an earlier registration-helper mode. | Registration-adjacent and previsit context in future scope. | Higher privacy/security/HIS burden; not v1. |
| Arrival / check-in | Patient, clinic staff | The safer v1 story is already-registered waiting-room use. | No real v1 identifiers; future real system would need hospital approval. | Must avoid collecting ID/birthday in initial waiting-room flow. |
| Waiting period | Patient/family, possible QR helper | `陽明小幫手` waiting-room QR flow is the preferred near-term product story. | Initial/return branch; history and symptom-specific forms. | Good workflow slot, but staff/nurse burden still untested. |
| Nurse or staff contact | Nurse/staff | Patient should hand NHI card to clinic nurse; nurse/physician confirms next steps. | Missing information, medication names, follow-up-test discussion. | Need nurse review of repair prompts and operational feasibility. |
| Physician entry | Physician | Physician reviews summary and confirms/edits/ignores. | Chief concern, history, symptom domains, missing fields, exam-prep context. | Summary usefulness not yet line-level validated. |
| After visit begins | Physician/nurse | Physician/nurse decides whether any exam is appropriate. | Possible exam discussion, not automatic order. | v1 must not imply autonomous orders. |

Capture labels:

- Fact: source materials explicitly define initial/return visit, no ID/birthday for initial visit, and confirmation-only clinical action.
- Inference: waiting-room mode is the safest v1 story.
- Unknown: exact nurse staffing, queue flow, HIS path, privacy owner, and whether 許醫師 accepts the proposed first-three complaint-flow default.

## 2. Repeated Questions And Source-Derived Content

| Repeated question / content | Who asks it? | Why repeated? | Could it be collected earlier? | Keep, revise, or reject |
| --- | --- | --- | --- | --- |
| Main urinary concern | Patient/staff/physician | Required to route symptom-specific form. | Yes, synthetic v1 and future approved workflow. | Keep. |
| Initial vs return visit | Patient/staff | Changes question set. | Yes. | Keep. |
| Chronic disease history | Patient/staff/physician | Context for urology evaluation. | Yes in initial visit. | Keep. |
| Surgery history | Patient/staff/physician | Context for evaluation. | Yes in initial visit. | Keep. |
| Medication history | Patient/staff/physician | Often incomplete or vague. | Yes, with nurse repair. | Keep. |
| Allergy history | Patient/staff/physician | Safety context. | Yes in initial visit. | Keep. |
| Prior medication effect | Patient/physician | Return-visit decision context. | Yes for return visit. | Keep. |
| Side effects | Patient/physician | Return-visit safety context. | Yes for return visit. | Keep. |
| Desired follow-up tests to discuss | Patient/physician | Helps physician know patient expectations. | Yes, but as discussion request only. | Keep with cautious wording. |
| 12 complaint exam-prep matrix | Physician/nurse | Helps anticipate possible preparation. | Only as physician/nurse confirmation reminders. | Keep as review material, not order protocol. |
| ID number and birthday | Registration/system | Identifiers create privacy burden. | Not in v1 initial waiting-room flow. | Reject for v1. |

## 3. Previsit-Safe Information

| Information | Useful before physician entry? | Patient can answer? | Helper can answer? | Risk or wording concern |
| --- | --- | --- | --- | --- |
| Main concern | Yes | Yes | Yes, source-labeled | Do not infer diagnosis. |
| Initial/return visit | Yes | Yes | Yes | Keep simple and non-legalistic. |
| Duration / timeline | Yes | Yes | Sometimes | Use approximate ranges. |
| Bother / severity | Likely | Yes | Helper should not replace patient feeling | Label source. |
| Medication list/name | Yes | Partly | Yes with bag/list | Ask exact Chinese/English med name when vague. |
| Allergy/chronic disease/surgery history | Yes | Yes | Yes with source label | Do not collect real identifiers. |
| Follow-up tests patient wants to discuss | Yes for return visit | Yes | Yes | Must be "wants to discuss", not "system recommends". |
| Exam-prep reminders | Yes for physician/nurse review | No autonomous patient instruction | No autonomous patient instruction | Confirmation-only; no ordering language. |
| Satisfaction survey | Future pilot | Yes | Yes | Not v1 real collection. |

## 4. Physician-Led Information

| Topic | Why must it remain physician-led? | Boundary wording |
| --- | --- | --- |
| Diagnosis | Requires clinical judgment and examination/labs. | The summary reports answers only. |
| Urgency or triage judgment | Requires clinic SOP and clinician accountability. | The summary does not assign urgency. |
| Treatment choice | Requires clinician decision and patient context. | The summary does not recommend treatment. |
| Exam ordering | Requires physician/nurse confirmation and local workflow. | The exam-prep tab shows reminders only; no order is placed. |
| Physical exam interpretation | Requires clinical training and encounter. | The summary does not replace exam. |
| HIS writeback | Requires information-office, privacy/security, legal, and hospital approval. | v1 uses mock export only. |
| Regulatory classification | Depends on intended use, claims, outputs, and deployment. | Regulatory status is not determined. |

## 5. Patient And Staff Constraints

| Constraint | How often does it matter? | Workflow impact | Possible response |
| --- | --- | --- | --- |
| Older adult usability | Likely common | Large touch targets and simple language needed. | Keep static browser v1 simple; later patient usability test. |
| Vision difficulty | Likely | Could increase staff/family assistance. | Keep readable layout; test later. |
| Low literacy | Likely | Can cause vague or missing answers. | Nurse repair and source labels. |
| Mandarin / Taiwanese / mixed language | Likely | Language support may matter. | Phase 0 asks reviewer for priority; do not overbuild now. |
| Phone-use difficulty | Likely | Self-filled mode may not work for all. | Support family/staff-assisted concept. |
| Need for nurse assistance | Unknown | Could save or shift burden. | Phase 0 nurse/staff review required. |
| Need for family assistance | Likely | Source confusion risk. | Preserve family/source labels. |
| Embarrassment or sensitive symptoms | Likely in urology | Affects answer completeness. | Calm wording and optional context. |

## 6. Summary Feedback

| Summary section | Useful, noisy, missing, or unsafe? | Reviewer comments | Action |
| --- | --- | --- | --- |
| Safety notice | Useful | Needed to avoid clinical-use confusion. | Keep visible. |
| Chief concern | Likely useful | Core physician scan item. | Test line-level in Phase 0. |
| Symptom pattern | Likely useful | Not yet case-level reviewed. | Time physician read. |
| Duration and burden | Likely useful | Fits previsit summary concept. | Keep but confirm order. |
| Neutral review flags | Useful if descriptive | Must not become risk labels. | Use "reported/missing/needs confirmation". |
| Missing information | Likely useful | Core nurse repair function. | Nurse reviewer must score prompts. |
| Medicine uncertainty | Useful | QA file explicitly asks exact med-name repair. | Keep. |
| Exam-prep matrix | Useful as source material | Must be confirmation-only. | Ask 許醫師 to approve first three flows. |
| Export/mock API | Future discussion only | High governance risk if overstated. | Keep mock-only. |

## 7. Safety And Privacy Concerns

| Concern | Raised by whom / source | Severity | Required response |
| --- | --- | --- | --- |
| Diagnostic wording | Safety boundary / regulatory sources | High | Avoid likely/probable/risk/probability. |
| Treatment implication | Safety boundary | High | No treatment recommendations. |
| Autonomous exam ordering | QA-derived workflow risk | High | "Confirm/consider whether appropriate"; no "order". |
| Real patient data | PDPA/hospital governance | High | Synthetic only in v1. |
| ID/birthday collection | 許醫師 QA/rules | High | Initial waiting-room flow does not ask these. |
| HIS/writeback | Meeting + EMR rules | High | Mock export only until hospital review. |
| Consent/IRB | Research governance | High before pilot | Phase 0 uses experts/synthetic only; real patient study needs review. |
| Vendor/IP | Meeting | High | Clarify patent/vendor boundaries before team-owned build promise. |
| Regulatory status | TFDA/FDA references | High | Do not claim non-device or approval. |

## 8. Decision Signals

| Signal | Evidence | Supports continue, revise, narrow, or pause? |
| --- | --- | --- |
| Repeated-question pain exists | Meeting and slides describe repeated history/medication/exam-prep questions. | Continue as hypothesis. |
| Summary would be read | Positive physician signal but no timed review. | Continue to Phase 0, not adoption claim. |
| Staff burden acceptable | Not validated. | Requires nurse/staff review. |
| Patient completion realistic | Not validated. | Future usability test; keep assisted-use labels. |
| Safety boundary acceptable | v1 can stay descriptive and synthetic. | Continue if wording remains safe. |
| Workflow slot exists | Waiting-room `陽明小幫手` is plausible. | Continue with narrow scope. |
| Existing process already sufficient | Not shown. | Unknown. |
| IP/vendor/funding blockers | Strong unresolved signals. | Governance gate before real build/deployment. |
| Current Argon links exist | Doctor-provided links expose current public app framing. | Add benchmark review before changing v1 scope. |
| Same-day 吳老師 follow-up emphasized productization and actual operation review | Follow-up transcript is noisy but directionally consistent. | See current app operation with synthetic/no-real-data walkthrough before Phase 1. |

## 9. Rejected Assumptions

| Assumption | Evidence against it | Change needed |
| --- | --- | --- |
| HIS integration should start immediately | Privacy/security/legal/info-office/vendor blast radius too high. | Use export/mock API only. |
| TFDA classification can be claimed now | Official guidance depends on intended use and claims. | Keep regulatory status not determined. |
| Four-case review was completed | Transcript shifted to strategy. | Mark case-level review pending Phase 0. |
| Multi-specialty expansion should start now | Urology workflow and rights not closed. | Keep as future hypothesis. |
| Data flywheel can use physician-edited notes now | Consent, IRB, de-identification, retention, audit, and model-update governance unresolved. | Future governance question only. |

## 10. Unanswered Questions

| Question | Why it matters | Who can answer? | Next step |
| --- | --- | --- | --- |
| Which 3 of the 12 complaint flows should v1 prioritize? | Prevents broad unfocused review. | 許醫師 | Ask in follow-up and Phase 0. |
| Should the provisional first three be `頻尿或夜尿`, `小便困難或尿不出來`, and `血尿或健檢發現潛血`? | Gives Phase 0 a narrow opening scaffold. | 許醫師 | Confirm, replace, or reorder before treating as accepted. |
| Named personas or neutral role labels? | Affects hospital acceptability. | 許醫師 / 吳老師 | Ask before final v1 handoff. |
| Which exam-prep wording is acceptable before physician confirmation? | Prevents ordering language. | 許醫師 / nurse lead | Line-level review. |
| What does 許醫師 patent or planned filing cover? | Prevents rights conflict. | 許醫師 / counsel / tech-transfer | IP boundary meeting. |
| Does vendor agreement restrict team-owned implementation? | Prevents vendor conflict. | 許醫師 / hospital/vendor owner | Contract/SOW review. |
| Who owns privacy/security/HIS review at 聯醫? | Required before real pilot. | 聯醫 operations/info office | Identify named owners. |
| Can a nurse/staff reviewer join Phase 0? | Staff burden is untested. | 許醫師 / clinic team | Request reviewer. |
| Which current-system functions must v1 match or intentionally omit? | Prevents blind copying and scope creep. | 許醫師 / current-system owner | Review Argon links/screenshots using synthetic inputs only. |
| Is `初步建議` / `檢查方向` wording allowed in v1? | Patient-facing advice may create clinical/regulatory risk. | 許醫師 / governance reviewers | Keep v1 stricter until approved. |
| Is local/on-prem deployment required for Phase 1? | Affects security, maintenance, encryption, and hardware owner. | 吳老師 / 許醫師 / hospital IT | Treat as architecture gate, not v1 dependency. |

## 11. Initial Decision

| Field | Notes |
| --- | --- |
| Decision | Continue as safe-local v1 plus Phase 0 clinician/nurse review |
| Reason | The source materials justify a concrete synthetic review artifact, but not real-data deployment. |
| Smallest next artifact | Phase 0 review protocol and scorecard |
| Reviewer | 許醫師 plus nurse/staff reviewer if available |
| Boundary that must remain | No diagnosis, no triage, no treatment advice, no real patient data, no autonomous exam ordering, no live HIS/registration/messaging |
| Evidence still needed | Summary read time, nurse burden, confirmed/revised first three flows, unsafe wording list, IP/vendor/funding/HIS/privacy owners |

Follow-on implementation support: `synthetic-hematuria-occult-blood` was added to the demo repo so the proposed hematuria / occult-blood flow can be reviewed as a synthetic v1 case.

Follow-on evidence-capture support: `docs/research/v1-phase0-review-capture.md` was added to the demo repo so the next review can produce structured evidence before analysis and decision memo writing.

Follow-on readiness support: `npm run phase0:check` was added in the demo repo so Phase 0 can verify the live v1 route, five synthetic cases, capture sheet, current-system benchmark table, scorecard, priority-flow worksheet, safety boundaries, smoke checks, and tests before reviewer time is used. Latest run against `http://127.0.0.1:4176/app/v1/` passed `81/81`.

Follow-on benchmark support: the doctor-provided current Argon links were added to the Phase 0 review path. They should be used to create a match/omit/defer table, not to copy vendor behavior or expand v1 into registration, advice, exam direction, HIS, or local/on-prem deployment.

Follow-on strategy support: the same-day 16:00 吳老師 discussion supports productization, actual-operation review, possible future local/on-prem architecture, and scale via hospital/community-clinic networks. These are Phase 1 or later gates, not v1 deliverables.

## 12. Same-Day Summary Draft

| Section | Notes |
| --- | --- |
| Clinical need | Reduce repeated previsit information gathering and make physician time more focused. |
| User need | Patient/family can report; nurse repairs gaps; physician scans a short summary. |
| Workflow pain points | Repeated history/medication/symptom/exam-prep questioning; current vendor cost and scaling constraints. |
| Pre-collectable information | Initial/return branch, chronic disease, surgery, medication, allergy, symptom forms, return medication effect/side effects/test discussion. |
| Physician-led information | Diagnosis, triage, treatment, exam ordering, interpretation, production HIS writeback. |
| Summary format | Needs timed physician review; v1 should show chief concern, symptom domains, missing fields, medication context, and source labels. |
| Safety concerns | Real data, identifiers, HIS, ordering language, TFDA/FDA certainty, IP/vendor conflict. |
| Recommendation | Continue to v1 Phase 0 only. |
| Next owner / action | Jason prepares scorecard/protocol; 許醫師 chooses first flows/persona/wording and identifies governance owners. |
