# Urology AI Previsit Thinking Spec

<img src="http://estruyf-github.azurewebsites.net/api/VisitorHit?user=JasonLn0711&repo=urology-ai-previsit-thinking-spec&countColor=%237B1E7B" alt="Visitor count"/>
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
│   ├── DEEP_CULTIVATION_SYSTEM_POSITIONING.md
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
│   ├── DEEP_CULTIVATION_PROPOSAL_WRITING_GUIDE.md
│   ├── DISCOVERY_PROTOCOL.md
│   ├── MEETING_CAPTURE_TEMPLATE.md
│   ├── DECISION_RECORD_TEMPLATE.md
│   └── PAPER_PATENT_PRODUCT_EXTRACTION.md
├── records/
│   ├── README.md
│   ├── 2026-04-23/
│   ├── 2026-05-03/
│   ├── 2026-05-12/
│   └── 2026-05-19/
└── meta/
    ├── assumptions.md
    ├── constraints.md
    ├── open_questions.md
    └── repo_architecture_review.md
```

## Folder Responsibilities

- `core/`: stable system logic. Use this when checking product intent, workflow boundaries, safety philosophy, evaluation logic, and evolution rules.
- `clinical-question-governance/`: evidence-based question governance. Use this when deciding which urology previsit questions belong in MVP, conditional modules, family/source-labeled support, nurse repair, or clinician-only workflows.
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
- For the Health Taiwan deep-cultivation system positioning: `core/DEEP_CULTIVATION_SYSTEM_POSITIONING.md`
- For writing the Health Taiwan deep-cultivation proposal: `discovery/DEEP_CULTIVATION_PROPOSAL_WRITING_GUIDE.md`
- For scoring a Health Taiwan deep-cultivation draft objectively: `discovery/DEEP_CULTIVATION_SCORING_RUBRIC.md`
- For the expanded MOHW format/application-compliance score: `discovery/DEEP_CULTIVATION_MOHW_COMPLIANCE_RUBRIC.md`
- For safety boundaries: `core/SAFETY_BOUNDARY.md`
- For clinical question governance: `clinical-question-governance/clinical_question_governance.md`
- For the candidate question matrix: `clinical-question-governance/question_candidates_matrix.md`
- For the recommended MVP question set: `clinical-question-governance/mvp_question_set_recommendation.md`
- For the next physician/nurse discovery conversation: `discovery/NEXT_STEP.md`
- For the 2026-05-03 urgent-care AI triage future-direction signal: `records/2026-05-03/yu-urgent-care-ai-triage-reference.md`
- For the 2026-05-19 local ASR-ready adaptive demo readiness record: `records/2026-05-19/demo-asr-readiness-record.md`
- For the 2026-05-19 北市聯醫 deep-cultivation meeting transcript: `records/2026-05-19/taipei-city-hospital-deep-cultivation-meeting-transcript.md`
- For the 2026-05-19 北市聯醫 concise summary and strategic signal: `records/2026-05-19/deep-cultivation-summary-and-signals.md`
- For the official Health Taiwan Deep-Cultivation policy reference: `records/2026-05-19/health-taiwan-deep-cultivation-policy-reference.md`
- For the downloaded official Health Taiwan policy document archive: `records/2026-05-19/policy-documents/README.md`
- For related Health Taiwan examples and proposal patterns: `records/2026-05-19/health-taiwan-related-examples.md`
- For whether to include this repo and the demo repo in the proposal: `records/2026-05-19/repo-inclusion-recommendation.md`
- For the imported 北市聯醫 deep-cultivation working note: `records/2026-05-19/taipei-city-hospital-deep-cultivation-working-note.md`
- For the 2026-05-19 deep-cultivation decision and CRM/service-flow framing: `records/2026-05-19/deep-cultivation-decision-record.md`
- For repository architecture decisions: `meta/repo_architecture_review.md`

## Current Planning Signal

The latest dated planning evidence is the 2026-05-19 北市聯醫 deep-cultivation meeting.

Near-term framing should emphasize:

- PSA / community screening as the clinical entry point
- SOP, return-to-hospital flow, case management, and CRM as the service backbone
- urology previsit / visit-readiness / clinician-review summary as the current system role
- APP, AI, ASR, kiosk, API, and reminders as workflow tools, not autonomous clinical decision tools
- proposal writing should start from clinical workflow pain, service landing, KPI, governance, and budget mapping, not from model novelty
- the official policy/rule archive now lives under `records/2026-05-19/policy-documents/`
- draft scoring should use the four independent 100-point layers in `discovery/DEEP_CULTIVATION_SCORING_RUBRIC.md`, including the MOHW format-compliance layer before formal submission
- the expanded D-layer rubric in `discovery/DEEP_CULTIVATION_MOHW_COMPLIANCE_RUBRIC.md` should be treated as a source-freshness and official-format preflight, not just an administrative checklist
- Aging Clock as research-adjacent until the data source, aging definition, biomarker scope, intervention, and service fit are clarified
- the concise strategic label: `AI Systems Engineering for Healthcare Deployment`
- policy alignment with `健康台灣深耕計畫(114-118年)`: smart healthcare, working-condition improvement, talent training, and sustainable/social-responsibility healthcare
- related examples support the pattern: workflow improvement, staff-burden reduction, AI as a tool, system integration, governance, and KPI

This does not change the core safety boundary: no diagnosis, no treatment advice, no autonomous triage, no real patient data during discovery, and no HIS/EMR/EHR integration without separate governance.

The accepted system-positioning supplement is `core/DEEP_CULTIVATION_SYSTEM_POSITIONING.md`. Use it when updating the sibling `urology-ai-previsit-demo` repo or drafting the June 2 deep-cultivation subproject, especially to avoid drifting from previsit support into AI triage claims.

## Operating Rule

The first useful version should be modest, reviewable, and safe:

1. collect repeated, high-value previsit information
2. repair missing information before handoff
3. let the patient or helper review a patient-facing confirmation
4. give clinic staff a separate missing-information repair workbench when needed
5. preserve answer source when family or nurse input is involved
6. produce a short clinician-review summary
7. leave interpretation and action with the clinician

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
