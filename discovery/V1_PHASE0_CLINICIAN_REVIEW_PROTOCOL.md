# V1 Phase 0 Clinician Review Protocol

Date: 2026-04-23
Scope: synthetic-only clinician and nurse review of the v1 local product preview

## Purpose

Phase 0 asks one research question:

> Can the safe-local v1 product preview help a urology clinic judge previsit information readiness before the physician encounter, without collecting real patient data or implying diagnosis, triage, treatment, or exam ordering?

This is not a clinical trial, not a hospital deployment, not a real patient pilot, and not a regulatory classification decision. It is a structured expert review of a synthetic product preview.

## First-Principles Boundary

The review starts from five layers:

1. Source: meeting transcript, 許醫師 QA/rules, 2024 TUA guideline, and public regulatory/privacy references.
2. Boundary: synthetic data only; physician review required; no real identifiers; no live HIS, registration, messaging, diagnosis, treatment, triage, or autonomous exam orders.
3. Artifact: local browser v1 route, handoff packet, and source-derived exam-prep mockup.
4. Measurement: reviewer task performance, usefulness ratings, safety wording issues, missing/noisy fields, and workflow fit.
5. Decision: continue, revise, narrow, pause, or governance review before any real-data pilot.

## Review Participants

Minimum useful panel:

- 1 urology physician reviewer, ideally 許醫師.
- 1 nurse or clinic staff reviewer who understands waiting-room and NHI-card handoff workflow.
- 1 product/research note taker.

Optional panel:

- hospital information-office observer for future export/HIS questions
- privacy/security/legal observer for gate-setting only
- 吳老師 for research/product supervision

Do not invite real patients in Phase 0 unless a separate ethics/privacy decision is made.

## Materials

Use:

- local v1 route: `/home/jnln3799/every_on_git_ubuntu/urology-ai-previsit-demo/app/v1/`
- v1 handoff packet: `/home/jnln3799/every_on_git_ubuntu/urology-ai-previsit-demo/docs/v1-mvp-handoff-packet.md`
- review scorecard: `/home/jnln3799/every_on_git_ubuntu/urology-ai-previsit-demo/docs/research/v1-review-scorecard.md`
- live capture sheet: `/home/jnln3799/every_on_git_ubuntu/urology-ai-previsit-demo/docs/research/v1-phase0-review-capture.md`
- source materials archived in planning and copied in the demo repo

Do not use:

- real patient stories with identifying details
- real medical-record screenshots
- real queue, ID, birthday, phone, or hospital identifiers
- real HIS writeback
- current vendor internals beyond materials that 許醫師 is permitted to share

## Review Tasks

### Task 1: Boundary Read

Ask each reviewer to read the visible safety boundary and say whether the product role is clear.

Capture:

- wording that sounds safe
- wording that sounds like clinical use, diagnosis, treatment, triage, or ordering
- any missing boundary statement

Pass condition:

- reviewer can describe v1 as synthetic, review-only, and non-production.

### Task 2: Case Selection And Intake

Show all five synthetic cases and the `陽明小幫手` waiting-room rule card.

Confirm that the three proposed priority flows have runnable synthetic support:

- `頻尿或夜尿`: `synthetic-frequency-older-adult`
- `小便困難或尿不出來`: `synthetic-emptying-difficulty`
- `血尿或健檢發現潛血`: `synthetic-hematuria-occult-blood`

Capture:

- whether initial/return-visit branching matches clinic reality
- whether no-ID/no-birthday rule is visible enough
- whether medication/allergy/chronic disease/surgery history collection is appropriate for v1
- whether source labels are understandable

Pass condition:

- reviewer can identify which information is useful before physician entry and which should be hidden or moved.

### Task 3: Nurse Review

Ask the nurse/staff reviewer to inspect missing-field repair prompts and operational readiness.

Capture:

- prompts they would ask
- prompts they would skip
- prompts that add burden
- prompts that need different wording
- whether exact medication-name repair is actionable

Pass condition:

- nurse/staff reviewer can name at least one prompt that is useful and no prompt requires them to diagnose or triage.

### Task 4: Physician Summary

Ask the physician reviewer to read each summary with a timer.

Capture:

- read time
- top three useful lines
- top three noisy or unsafe lines
- missing fields
- whether the summary would be used, edited, ignored, or rejected

Pass condition:

- at least one priority flow produces a summary that the physician says is useful enough to revise or continue.

### Task 5: Exam-Prep Mockup

Show the 12-complaint matrix as physician/nurse confirmation reminders.

Capture:

- which three complaint categories should be prioritized first
- which reminders are acceptable before physician confirmation
- which reminders must be hidden until nurse/physician review
- any wording that sounds like an autonomous order

Pass condition:

- reviewers can approve or revise confirmation-only wording for at least three complaint categories.

### Task 6: Export / Mock API

Show the copyable summary and mock JSON only as a future HIS discussion artifact.

Capture:

- fields that should exist in a future export
- fields that should not exist
- whether the mock payload wrongly implies real HIS writeback
- who must approve any future integration discussion

Pass condition:

- reviewers agree that v1 remains mock export only, or request removal of risky export fields.

### Task 7: Research Gate

Ask whether the next step should be continue, revise, narrow, pause, or governance review.

Capture:

- next research artifact
- owner
- due date
- evidence still missing
- stop conditions

Pass condition:

- decision is explicit and tied to evidence, not enthusiasm.

## Measurements

Record per reviewer:

- role: physician / nurse / staff / information office / privacy-security / supervisor
- reviewed surfaces: Intake, Nurse, Physician, Exam Prep, Export, Research
- summary read time per case
- usefulness rating: 1 to 5
- safety clarity rating: 1 to 5
- burden rating: 1 to 5, where 5 means too burdensome
- top useful fields
- fields to remove
- missing fields
- unsafe wording count
- ordering/diagnosis/treatment wording count
- approved priority complaint categories
- decision: continue / revise / narrow / pause / governance review

Use notes, not real patient data.

## Decision Rules

Continue if:

- physician would read the summary
- nurse/staff reviewer sees usable repair prompts
- at least three priority complaint flows can be reviewed with confirmation-only wording
- no real-data or clinical-use boundary is broken
- next artifact is narrow

Revise if:

- workflow pain is real but fields, wording, summary order, or role separation are wrong
- waiting-room story is right but v1 surface is too noisy
- export/mock API needs different structure before HIS discussion

Narrow if:

- value is clear only for a subset, such as frequency/nocturia, voiding difficulty, hematuria, elevated PSA, or medication-history repair
- broad 12-complaint coverage is too large for first clinical review

Pause if:

- reviewers would not read the summary
- nurse/staff burden rises without clear payoff
- safety wording cannot be made neutral
- no clinic workflow slot exists
- IP/vendor/privacy/security questions block even synthetic follow-up

Governance review before next step if:

- anyone proposes real patient data
- anyone proposes live HIS, registration, messaging, analytics, or cloud storage
- anyone proposes clinician-facing recommendations, risk scores, probability outputs, triage, or autonomous orders
- IP/vendor scope is unclear enough that implementation should stop

## Regulatory And Privacy Review Frame

Do not make classification claims from Phase 0.

Use official sources only as gate-setting references:

- Taiwan PDPA treats medical, health-check, medical-record, and related data as personal/sensitive categories that require a lawful basis and safety measures before collection/processing/use.
- Taiwan electronic medical record rules create additional security, audit, contract, cloud-location, and exchange requirements once electronic medical records or hospital systems are involved.
- TFDA AI/ML SaMD guidance is relevant if the project becomes AI/ML medical-device software or seeks registration; it does not settle this v1 product preview classification.
- FDA CDS guidance/FAQ shows why basis-visible clinician review and avoiding risk/probability/time-critical directives matters, but US guidance does not decide Taiwan deployment status.

## Done Definition

Phase 0 is complete when the repo contains:

- filled v1 review scorecard
- list of approved first three complaint flows or a decision to narrow differently
- line-level unsafe/noisy/useful wording notes
- decision record with continue/revise/narrow/pause/governance-review outcome
- updated open questions for funding, IP, HIS, privacy/security, regulatory, and pilot design
- no real patient data
- no production integration commitment

## Next Step After Phase 0

If Phase 0 passes, the next research step is not automatic deployment.

The next step should be one of:

- revise the synthetic v1 surfaces and repeat clinician review
- narrow to three complaint flows and prepare a formal pilot-readiness packet
- prepare a hospital governance pre-review packet for privacy/security/HIS/IP/regulatory owners
- pause until IP/vendor or institutional ownership is clear
