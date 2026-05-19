# Urology AI Previsit Thinking Spec

This repository is the thinking and governance layer for a urology previsit interview system.

It is not a code repo, demo repo, clinical protocol, diagnosis engine, real patient data store, hospital integration plan, or regulatory submission.

## First-Principles Role

The repository exists to answer one question:

Can a guided previsit interview collect useful patient-reported information before a urology visit while keeping diagnosis, triage, treatment, and final judgment with clinicians?

Every file should serve one of four purposes:

1. Define the system logic.
2. Govern which questions are clinically appropriate.
3. Prepare or capture clinician/nurse discovery.
4. Record assumptions, constraints, open questions, and dated review evidence.

If a file does not serve one of those purposes, it should not live here.

## Repository Map

```text
urology-ai-previsit-thinking-spec/
├── README.md
├── core/
│   ├── README.md
│   ├── THINKING_SPEC.md
│   ├── DESIGN_PHILOSOPHY.md
│   ├── WORKFLOW_LOGIC.md
│   ├── SAFETY_BOUNDARY.md
│   ├── EVALUATION.md
│   ├── TRADEOFF_ANALYSIS.md
│   ├── FAILURE_ANALYSIS.md
│   └── EVOLUTION_PATH.md
├── clinical-question-governance/
│   ├── README.md
│   ├── clinical_question_governance.md
│   ├── question_candidates_matrix.md
│   ├── doctor_needs.md
│   ├── nurse_needs.md
│   ├── mvp_question_set_recommendation.md
│   └── source_evidence_map.md
├── discovery/
│   ├── README.md
│   ├── NEXT_STEP.md
│   ├── DISCOVERY_PROTOCOL.md
│   ├── MEETING_CAPTURE_TEMPLATE.md
│   ├── DECISION_RECORD_TEMPLATE.md
│   └── PAPER_PATENT_PRODUCT_EXTRACTION.md
├── records/
│   ├── README.md
│   └── 2026-04-23/
└── meta/
    ├── assumptions.md
    ├── constraints.md
    ├── open_questions.md
    └── repo_architecture_review.md
```

## Folder Responsibilities

- `core/`: stable system logic. Use this when checking product intent, workflow boundaries, safety philosophy, evaluation logic, and evolution rules.
- `clinical-question-governance/`: evidence-based question governance. Use this when deciding which urology previsit questions belong in MVP, conditional modules, nurse-assisted review, or clinician-only workflows.
- `discovery/`: meeting and review operating pack. Use this before and after physician/nurse conversations.
- `records/`: dated evidence trail. Use this for specific meeting briefs, captures, decision records, and extraction notes.
- `meta/`: assumptions, constraints, open questions, and repository-level architecture review.

## Source Relationship

This repository is a sibling of `planning-everything-track`.

It may read planning context as background, but it does not move, rename, rewrite, or replace files in `planning-everything-track`.

The separate demo repository, `urology-ai-previsit-demo`, owns implementation, UI, synthetic cases, tests, and demo artifacts. This repository owns the reasoning and governance that should constrain that demo.

Current architecture decision: keep the thinking/governance repo and demo repo separate. The rationale and revisit criteria are recorded in `meta/repo_architecture_review.md`.

## Current Useful Reading Paths

- For a full non-technical system spec: `core/THINKING_SPEC.md`
- For safety boundaries: `core/SAFETY_BOUNDARY.md`
- For clinical question governance: `clinical-question-governance/clinical_question_governance.md`
- For the candidate question matrix: `clinical-question-governance/question_candidates_matrix.md`
- For the recommended MVP question set: `clinical-question-governance/mvp_question_set_recommendation.md`
- For the next physician/nurse discovery conversation: `discovery/NEXT_STEP.md`
- For repository architecture decisions: `meta/repo_architecture_review.md`
- For the 2026-05-19 deep-cultivation repo-routing decision:
  `records/2026-05-19/deep-cultivation-repo-routing.md`

## Operating Rule

The first useful version should be modest, reviewable, and safe:

1. collect repeated, high-value previsit information
2. repair missing information before handoff
3. let the patient, helper, or clinic staff review answers
4. produce a short clinician-review summary
5. leave interpretation and action with the clinician

## Redundancy Rule

Some overlap is intentional:

- `core/THINKING_SPEC.md` is the integrated master narrative.
- Files under `core/` split the master narrative into reviewable dimensions.
- Files under `clinical-question-governance/` are not a replacement for `core/`; they apply the safety and workflow logic to concrete clinical questions.
- Files under `discovery/` are operating templates, not source-of-truth clinical evidence.
- `records/` keeps dated evidence and should not be rewritten into evergreen doctrine unless a decision is accepted.

Avoid adding new root-level Markdown files unless they are entrypoints. New substantive documents should go into `core/`, `clinical-question-governance/`, `discovery/`, `records/`, or `meta/`.

## Audit Rule

Any future change should answer four questions:

1. Does this reduce workflow friction without adding hidden burden?
2. Does this preserve clinician authority?
3. Does this avoid real patient data unless governance is explicit?
4. Does this make the next decision clearer?
