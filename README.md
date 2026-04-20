# Urology AI Previsit Thinking Spec

This repository stores the non-technical reasoning system behind a urology smart-previsit concept.

It is not a code repository, product repository, clinical protocol, or deployment plan. It is a thinking-layer repository: a place to make product intent, workflow reasoning, safety boundaries, evaluation logic, and future decisions explicit enough for review.

## Core Question

Can a guided previsit interview reduce repeated questioning and improve clinical readiness before a formal urology visit, while keeping diagnosis, triage, treatment advice, and final judgment with the clinician?

## Repository Role

This repository exists so that reviewers can inspect the logic before anyone expands scope. It captures:

- why the problem matters
- who the system serves
- where the workflow begins and ends
- what information should and should not be collected
- how the output should be shaped for clinician review
- what safety boundaries are non-negotiable
- how success and failure should be judged
- what trade-offs were made
- what must be answered before any real-world use

## What This Is Not

This repository is not:

- a medical advice system
- a diagnosis or triage system
- a clinical decision system
- a real patient data store
- a hospital integration plan
- a regulatory submission
- a claim that the concept is ready for deployment

## Source Relationship

This repository is a sibling of `planning-everything-track`. It depends on existing planning and demo notes as read-only background.

It does not move, rename, rewrite, or replace anything in `planning-everything-track`.

## Required Documents

- `THINKING_SPEC.md`: full non-technical thinking specification
- `DESIGN_PHILOSOPHY.md`: design values, reasoning, and rejected instincts
- `WORKFLOW_LOGIC.md`: encounter flow, decision points, and handoff logic
- `SAFETY_BOUNDARY.md`: clinical, privacy, wording, and governance boundaries
- `EVALUATION.md`: usefulness, safety, adoption, and decision metrics
- `TRADEOFF_ANALYSIS.md`: sacrifices, rejected alternatives, counterfactuals, and reuse
- `FAILURE_ANALYSIS.md`: likely failure modes, signals, and responses
- `EVOLUTION_PATH.md`: staged growth rules for future versions
- `meta/assumptions.md`: explicit assumptions behind the current spec
- `meta/constraints.md`: repository, content, clinical, and governance constraints
- `meta/open_questions.md`: unanswered questions for physician and workflow review

## Supplemental Document

- `NEXT_STEP.md`: meeting-to-decision workflow for using the thinking layer after a physician conversation
- `DISCOVERY_PROTOCOL.md`: detailed discovery runbook for the next physician or clinic workflow conversation
- `MEETING_CAPTURE_TEMPLATE.md`: structured capture template for workflow facts, repeated questions, boundaries, and decision signals
- `DECISION_RECORD_TEMPLATE.md`: auditable post-meeting decision record template
- `PAPER_PATENT_PRODUCT_EXTRACTION.md`: separation guide for paper framing, patent reasoning, and product decisions
- `records/`: dated pre-meeting briefs, capture notes, decision records, and extraction notes

## Clinical Question Governance Pack

- `clinical_question_governance.md`: evidence hierarchy, three-party needs analysis, inclusion rules, safety boundaries, and MVP direction
- `question_candidates_matrix.md`: candidate question matrix with evidence, intended user, workflow value, risk, and inclusion decision
- `doctor_needs.md`: physician-facing information needs, summary fields, red-flag observations, and missing-information priorities
- `nurse_needs.md`: nurse-facing support needs for completion assistance, diary instruction, medication review, containment support, and escalation review
- `mvp_question_set_recommendation.md`: recommended MVP question set by core, conditional, nurse-assisted, clinician-only, and deferred categories
- `source_evidence_map.md`: source-to-conclusion map distinguishing direct source support from workflow inference

## Operating Rule

The first useful version should be modest, reviewable, and safe:

1. collect repeated, high-value previsit information
2. repair missing information before handoff
3. let the patient, helper, or clinic staff review answers
4. produce a short clinician-review summary
5. leave interpretation and action with the clinician

## Audit Rule

Any future change should answer four questions:

1. Does this reduce workflow friction without adding hidden burden?
2. Does this preserve clinician authority?
3. Does this avoid real patient data unless governance is explicit?
4. Does this make the next decision clearer?
