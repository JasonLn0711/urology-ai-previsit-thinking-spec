# Evolution Path

## Evolution Principle

The system should grow only when the previous stage proves useful.

Do not move from guided summary to clinical decision-making without a separate governance review.

## Stage 1: Thinking Layer

Goal: clarify problem, workflow, safety boundaries, and evaluation logic.

Output:

- thinking spec
- workflow map
- physician questions
- safety boundary
- evaluation criteria

## Stage 2: Synthetic Guided Demo

Goal: show the workflow without real patient data.

Output:

- guided question flow
- synthetic answers
- missing-information prompts
- clinician-review summary

## Stage 3: Clinician Feedback

Goal: learn what is useful, noisy, unsafe, or missing.

Output:

- revised question tree
- revised summary format
- workflow-fit judgment
- go / no-go decision

## Stage 4: Assisted Workflow Trial

Goal: determine whether patient self-entry, nurse assistance, or family assistance is most realistic.

Output:

- assisted-use protocol
- staff burden estimate
- completion and confusion points

## Stage 5: Summary Format Standardization

Goal: make the summary more useful without increasing scope.

Output:

- one-page summary standard
- missing-information section
- clinician-review flags
- patient constraint section

## Stage 6: Governance Review

Goal: decide whether any real patient-data pilot is justified.

Required before this stage:

- privacy review
- consent model
- data retention rule
- clinician responsibility statement
- patient communication text
- failure reporting process

## Stage 7: Limited Pilot

Goal: test real workflow value under approved constraints.

Not allowed without explicit approval:

- diagnosis
- treatment suggestion
- autonomous triage
- silent storage
- hidden data sharing
- production claims

## Stage 8: Integration Discussion

Goal: discuss hospital integration only after workflow value is proven.

Integration should remain downstream of workflow validation, privacy governance, and clinician acceptance.
