# Pre-Meeting Brief: Urology Smart-Previsit Discovery

## Status

Status: draft

Prepared for: 2026-04-23 10:00-11:00, online

Participants: 吳育德老師, 許富順醫師 / 泌尿科, Jason

## Meeting Mission

Leave the meeting with a decision-quality answer to one question:

Does a guided urology previsit workflow solve a real clinic problem strongly enough to justify one more small experiment?

The meeting is not a product pitch. It is a workflow discovery and boundary test.

## Starting Hypothesis

Some repeated urology intake questions can be collected before the physician-led visit, repaired for missing information, reviewed by the patient or helper, and summarized for clinician review.

This hypothesis should be revised or rejected if the clinic workflow, patient reality, staff burden, or safety boundary does not support it.

## Non-Negotiable Boundaries

Do not promise:

- diagnosis
- triage
- treatment advice
- real patient-data use
- production deployment
- hospital record integration
- voice-first interaction as the main workflow
- full medical-history capture

Use this wording if the conversation drifts:

"That may be a later question, but this meeting is only to decide whether a bounded previsit summary workflow is useful and safe enough for the next small artifact."

## Opening Script

"The goal is not to replace physician judgment. The goal is to understand whether a guided previsit flow can collect repeated, high-value information before the formal visit and give the clinician a short reviewable summary. If the workflow does not fit, pausing is an acceptable outcome."

"For safety, this concept does not diagnose, triage, recommend treatment, or use real patient data during discovery. Any red-flag information would be shown only as patient-reported observations for clinician review."

## Must-Win Outputs

By the end of the meeting, capture:

1. the current patient flow from check-in to physician entry
2. repeated questions or repeated information gaps
3. information that can be collected before physician entry
4. information that must remain physician-led
5. realistic operating mode: self-filled, nurse-assisted, family-assisted, or mixed
6. useful clinician summary format
7. safety or privacy objections
8. decision: continue, revise, narrow, or pause
9. smallest next artifact

If the meeting only produces a workflow map and a pause decision, that is still a valid result.

## 60-Minute Agenda

| Time | Focus | Output |
| --- | --- | --- |
| 0-5 min | Frame the purpose and safety boundary | shared scope |
| 5-15 min | Map current patient flow | workflow facts |
| 15-25 min | Identify repeated questions and missing context | candidate previsit information |
| 25-35 min | Separate previsit-safe topics from physician-led topics | boundary list |
| 35-45 min | Test patient and staff reality | operating-mode judgment |
| 45-53 min | Test summary usefulness | summary section order and noise list |
| 53-60 min | Decide next action | continue, revise, narrow, or pause |

If time is cut short, protect workflow facts, repeated questions, and boundary decisions first.

## Priority Questions

## A. Current Workflow

1. 病人從報到到醫師正式問診前，現在有哪些固定流程？
2. Who talks to the patient before the physician?
3. What information is collected at each step?
4. Where does information get repeated or lost?

## B. Repeated Questions

1. 哪些問題最常被醫師或護理師重複問？
2. Which answers would actually help before the physician enters?
3. Which questions are frequently answered unclearly?
4. Which questions are not worth asking early?

## C. Previsit-Safe Vs Physician-Led

1. 哪些資訊可以在候診時先問完？
2. 哪些題目一定要醫師親自問，不能前置？
3. Which red-flag observations are useful if phrased neutrally?
4. What wording would sound too diagnostic or unsafe?

## D. Patient And Staff Reality

1. 病人是自己操作，還是護理站協助操作？
2. 高齡病人、視力差、口音、台語/中文混用時，目前最常卡在哪裡？
3. Would assistance save time, shift burden, or add burden?
4. Where could this happen without slowing the clinic?

## E. Summary Usefulness

1. 最後要給醫師的是逐字紀錄、摘要、風險提示，還是檢查/補件建議？
2. What would the physician want to see first?
3. What would be noise?
4. What must be shown as missing?
5. Could this summary be read in under one minute?

## F. Decision

1. 成功指標是什麼：節省幾分鐘、減少幾次重複問答、提高資料完整度，或改善病人流速？
2. Should the project continue, revise, narrow, or pause?
3. What is the smallest useful next artifact?
4. Who should review that artifact?

## Capture Discipline

Use three labels while taking notes:

- `Fact`: directly stated workflow reality
- `Inference`: interpretation that needs confirmation
- `Decision signal`: evidence for continue, revise, narrow, or pause

Do not smooth over objections. Objections are design data.

## Parking Lot

Park these topics unless the physician says they are essential to deciding workflow value:

- hospital integration
- production deployment
- real patient data
- speech-first interaction
- full medical history
- billing workflow
- regulatory submission
- broad product roadmap

## Decision Gate

Continue if:

- repeated-question pain is real
- the physician can name useful previsit information
- a one-minute summary seems valuable
- staff burden is acceptable
- safety boundaries remain clear

Revise if:

- the idea is useful but the questions or summary are wrong
- self-filled use is unrealistic but assisted use may work
- only one symptom group or patient group seems appropriate

Narrow if:

- value exists only for a smaller use case
- the workflow should begin with one symptom cluster
- the summary should serve only one staff or physician handoff

Pause if:

- no workflow slot exists
- the physician would not read the summary
- staff burden increases too much
- safety or privacy concerns dominate
- existing intake methods already solve the problem

## Same-Day Output

By 2026-04-24 11:00, create or update:

- `meeting-capture.md`
- `decision-record.md`
- `extraction-notes.md`
- `../../meta/assumptions.md`
- `../../meta/open_questions.md`

Do not update the full thinking spec unless a core assumption is invalidated.
