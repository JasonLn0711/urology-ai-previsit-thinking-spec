# Evaluation

## Evaluation Purpose

The first evaluation should answer whether the workflow is useful enough to continue.

It should not reward novelty, technical sophistication, or broad claims. It should reward usefulness, safety, clarity, and adoption realism.

## Primary Success Criteria

The concept is successful enough to continue only if:

- a patient or helper can complete the flow without heavy instruction
- the clinician can read the summary in under one minute
- the summary helps reduce repeated questioning or missing context
- the summary avoids diagnosis, triage, and treatment advice
- staff burden is acceptable
- privacy boundaries remain clear
- the next experiment is small and concrete

## Usefulness Metrics

Track:

- completion rate
- time to complete
- unanswered key fields before and after missing-information prompts
- repeated questions reduced
- clinician usefulness rating
- staff burden rating
- patient confusion points
- summary sections used, edited, ignored, or rejected
- physician estimate of time saved

## Safety Metrics

Track:

- number of diagnostic claims
- number of treatment suggestions
- number of unclear red-flag statements
- number of patient misunderstandings about system role
- number of privacy-boundary violations
- number of summaries that sound more certain than the source answers
- number of cases where the clinician says the summary could mislead

## Adoption Metrics

Track:

- whether the clinic can name a real workflow slot
- whether nurses or staff see the system as help or burden
- whether patients need assistance and how much
- whether clinicians would actually read the output
- whether the output format fits the visit rhythm

## Decision Rules

Continue if:

- repeated-question pain is real
- previsit-safe information is clearly identifiable
- the summary is useful and short
- safety boundaries remain stable
- the next artifact is narrow

Revise if:

- the problem is real but the questions are wrong
- self-filled use is unrealistic but assisted use is plausible
- the summary grouping is wrong
- fields are too broad, noisy, or hard to answer
- the workflow helps one subgroup more than the general clinic

Pause if:

- clinicians would not read the summary
- staff burden increases without clear benefit
- no clinic workflow slot exists
- privacy or safety objections dominate
- existing intake methods already solve the problem well enough

## Review Standard

Every evaluation should produce a written decision: continue, revise, narrow, or pause. The decision should include the evidence, not just the conclusion.
