# Evaluation

## Evaluation Purpose

The first evaluation should answer whether the workflow is useful enough to continue.

It should not reward novelty, technical sophistication, or broad claims. It should reward usefulness, safety, clarity, and adoption realism.

## Current Evaluation Phase

After the 2026-04-23 meeting, the active evaluation is `Phase 0: synthetic clinician/nurse review`.

Phase 0 may use only synthetic cases, local product-preview artifacts, and approved current-system benchmark screenshots or synthetic walkthroughs. It measures whether expert reviewers can understand the workflow, find useful summary lines, reject noisy or unsafe wording, compare v1 against the current `聯醫小幫手` / `陽明小幫手` boundary, and choose a narrow next research step. Live review notes should be captured in the demo repo's Phase 0 capture sheet before analysis. It does not measure clinical effectiveness, patient outcomes, real waiting time, or hospital production performance.

Phase 0 is successful only if it produces an evidence-backed decision:

- continue
- revise
- narrow
- pause
- governance review before any next step

The detailed runbook lives in `../discovery/V1_PHASE0_CLINICIAN_REVIEW_PROTOCOL.md`. The execution and analysis loop lives in `../discovery/V1_PHASE0_EXECUTION_AND_ANALYSIS_PLAN.md`.

Before reviewer time is requested, the demo repo readiness gate should pass:

`UROLOGY_PREVISIT_BASE_URL=http://127.0.0.1:4176 npm run phase0:check`

Latest 2026-04-23 run passed `81/81`, covering the live route, five synthetic cases, live capture sheet, current-system benchmark table, scorecard, priority-flow worksheet, safety boundaries, smoke checks, and tests.

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

For Phase 0, use synthetic-review variants of these metrics:

- summary read time per synthetic case
- clinician usefulness rating from 1 to 5
- nurse/staff burden rating from 1 to 5
- safety clarity rating from 1 to 5
- number of useful lines, noisy lines, missing fields, and unsafe phrases
- first three complaint flows confirmed, revised, or narrowed for next review
- fields accepted, revised, removed, or deferred for future export/HIS discussion
- current-system benchmark decisions: match, omit, defer, or governance review

The current proposed first-three review default is:

- `頻尿或夜尿`
- `小便困難或尿不出來`
- `血尿或健檢發現潛血`

Treat this as a reviewer-session scaffold only. It is not evidence of clinical priority until 許醫師 confirms or changes it.

Demo support for the scaffold now covers five synthetic cases overall, including `synthetic-hematuria-occult-blood` for the hematuria / occult-blood flow. This improves review readiness but still does not create clinical validation.

## Safety Metrics

Track:

- number of diagnostic claims
- number of treatment suggestions
- number of unclear red-flag statements
- number of patient misunderstandings about system role
- number of privacy-boundary violations
- number of summaries that sound more certain than the source answers
- number of cases where the clinician says the summary could mislead

For Phase 0, any real patient identifier, real queue/appointment data, live HIS behavior, diagnosis, treatment, triage, risk score, probability output, autonomous exam-ordering phrase, or copied current-vendor behavior without permission is a stop condition.

## Adoption Metrics

Track:

- whether the clinic can name a real workflow slot
- whether nurses or staff see the system as help or burden
- whether patients need assistance and how much
- whether clinicians would actually read the output
- whether the output format fits the visit rhythm

## Deep-Cultivation KPI Layer

For the Health Taiwan deep-cultivation framing, evaluation should also support KPI-to-budget reasoning. These indicators should be treated as draft targets until confirmed by hospital stakeholders.

For the current proposal-prep working table, use `../discovery/DEEP_CULTIVATION_KPI_TO_BUDGET_TABLE.md`. For annual monitoring, use `../discovery/DEEP_CULTIVATION_ANNUAL_CHECKPOINT_TABLE.md`.

| KPI area | Candidate measure | Boundary |
| --- | --- | --- |
| Visit readiness | Clinician can review summary in under one minute | Measures handoff usefulness, not diagnostic accuracy |
| Missing-information repair | Fewer missing key previsit fields after guided prompts | Use synthetic or governance-approved data only |
| Repeated work reduction | Fewer repeated history questions in walkthrough or pilot | Compare against current workflow |
| Completion feasibility | Patient/helper/staff-assisted completion rate reaches an agreed target | Target needs clinical workflow calibration |
| Staff burden | Nurse or staff burden remains acceptable | Do not shift physician work into hidden staff work |
| Clinical friction budget | Extra clicks, system switches, training time, and exception-handling burden remain acceptable | Do not make clinicians or nurses work harder for the AI system |
| Workforce burden reduction | Evidence suggests reduced repeated questioning, documentation preparation, or unnecessary interruptions | Measures Health Taiwan workforce value, not model novelty |
| Clinician usefulness | Clinician usefulness score reaches an agreed threshold | The summary remains editable and rejectable |
| Safety boundary | Zero diagnosis, treatment, or autonomous triage claims | Non-negotiable safety KPI |
| Auditability | 100% of outputs preserve source and review-status metadata in pilot-ready design | Required before real pilot use |
| CRM readiness | SOP exists for reminder, lab-draw, return-visit, or case-management follow-up | Follow-up remains governed and clinician/service-owned |
| Governance readiness | IRB, privacy, security, procurement, and MOU gates have named owners | Proposal-execution KPI, not a clinical outcome |

Budget lines should map to one of these KPI areas. If a feature has no KPI and no governance owner, it should not be treated as a core deep-cultivation deliverable.

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

For v1 Phase 0, `governance review before next step` is also a valid written decision when the next proposal touches real patient data, hospital systems, IP/vendor rights, regulatory claims, or deployment ownership.

Current-system benchmark review can change the next artifact, but it should not expand v1 automatically. If the benchmark shows a gap, the preferred next artifact is a comparison table and reviewer decision, not an immediate feature sprint.
