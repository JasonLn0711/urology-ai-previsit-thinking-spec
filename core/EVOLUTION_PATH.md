# Evolution Path

## Evolution Principle

The system should grow only when the previous stage proves useful and safe.

Do not move from previsit summary support to clinical decision support without a separate governance review. Growth should be evidence-driven, not excitement-driven.

## Stage 1: Thinking Layer

Goal: clarify the problem, user model, workflow logic, safety boundaries, evaluation criteria, and open questions.

Exit evidence:

- complete thinking specification
- explicit assumptions
- explicit constraints
- physician discovery questions
- safety boundary written plainly

## Stage 2: Discovery Walkthrough

Goal: show the intended interaction using non-real patient examples so reviewers can judge workflow usefulness without privacy exposure.

Exit evidence:

- clinician can understand the flow
- safety boundary is visible
- reviewers can identify useful, noisy, or missing fields
- no real patient data is needed

## Stage 3: Clinician Feedback

Goal: learn whether the summary would help a real urology visit.

Exit evidence:

- list of repeated questions worth pre-collecting
- list of physician-led topics
- feedback on summary length and grouping
- continue, revise, narrow, or pause decision

## Stage 4: Revised Question Tree

Goal: turn feedback into a narrower and more accurate question set.

Exit evidence:

- removed noisy fields
- added only high-value missing fields
- simplified unclear wording
- documented why each field remains

## Stage 5: Assisted-Use Workflow Test

Goal: decide whether self-filled, nurse-assisted, family-assisted, or mixed use is realistic.

Exit evidence:

- estimated staff burden
- common assistance needs
- patient confusion points
- recommended operating mode

## Stage 6: Summary Standardization

Goal: make the clinician-review summary consistent, short, and safe.

Exit evidence:

- one-page summary structure
- neutral review flags
- visible missing-information section
- language or accessibility needs section
- clinician readability under one minute

## Stage 7: Governance Review

Goal: decide whether any real patient-data pilot is justified.

Required before this stage:

- consent plan
- data retention rule
- deletion rule
- access rule
- clinician responsibility statement
- patient-facing role explanation
- failure reporting process

## Stage 8: Limited Pilot

Goal: test real workflow value under explicit approval and narrow limits.

Still not allowed without separate approval:

- diagnosis
- treatment suggestion
- autonomous triage
- hidden storage
- hidden sharing
- production claims

## Stage 9: Integration Discussion

Goal: discuss connection to existing clinic workflows only after workflow value, safety, privacy, responsibility, and adoption are clear.

Integration is not proof of value. It is only justified after value is already visible.

## Versioning Rule

Each future version should explain:

- what changed
- why it changed
- what evidence supported the change
- which boundary was affected
- which open question was answered
