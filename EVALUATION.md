# Evaluation

## Evaluation Purpose

The MVP should answer whether the workflow is useful enough to continue.

It should not be evaluated as a production clinical system.

## Primary Success Criteria

- A nontechnical user can complete the flow without instruction.
- A clinician can read the summary in under 60 seconds.
- The summary does not diagnose, triage, or recommend treatment.
- The workflow uses no real patient data during discovery.
- Clinicians can judge whether the summary would save time.

## Workflow Metrics

- completion rate
- time to complete
- number of missing fields before and after prompts
- number of repeated questions reduced
- clinician usefulness rating
- staff burden rating
- patient confusion points
- number of summaries edited, ignored, or used

## Safety Metrics

- number of diagnostic claims
- number of treatment recommendations
- number of unclear red-flag statements
- number of privacy-boundary violations
- number of clinically misleading summaries

## Decision Criteria

Continue if:

- clinicians identify a real workflow use
- the summary is short enough to review
- the system reduces repeated questioning
- safety boundaries remain clear
- next experiment is small and concrete

Pause if:

- clinicians find the summary useless
- staff workflow has no place for it
- patients cannot complete it
- safety wording becomes ambiguous
- privacy scope becomes unclear
