# Discovery And Decision Pack

This folder contains the operating pack for physician, nurse, and workflow discovery.

It is meant to turn conversations into auditable decisions without mixing paper framing, patent reasoning, and product scope.

## Files

- `NEXT_STEP.md`: meeting-to-decision workflow
- `ASSERTIVE_WRITING_GATE.md`: pre-circulation gate for turning the assertive writing policy into paragraph-level checks, rewrite patterns, and review flow
- `INTENDED_USE_FREEZE.md`: proposal-prep freeze for intended use, target users, allowed outputs, non-use, data boundary, responsibility boundary, and clinical-friction rule
- `DEMO_SCOPE_FREEZE.md`: proposal-facing demo scope freeze for synthetic cases, included/excluded demo behavior, acceptance criteria, and no-go signals
- `CLINICAL_FRICTION_REDUCTION_ANALYSIS.md`: Health Taiwan proposal analysis for reducing physician/nurse/staff burden without turning medical staff into AI labelers or extra-workflow operators
- `DEEP_CULTIVATION_PROPOSAL_WRITING_GUIDE.md`: Health Taiwan deep-cultivation proposal writing structure for the urology previsit / CRM service-flow draft
- `../records/2026-05-21/a2-0048-smart-healthcare-center-precedent/README.md`: structured capture and postdoctoral comparison of the A2-0048 precedent proposal; use it as a format and execution-packaging reference, not as scope expansion guidance
- `DEEP_CULTIVATION_APPLICATION_DRAFT_V0_4.md`: current precedent-integrated official-package proposal draft; keeps the v0.3 narrow urology scope while adding official checklist, owner table, baseline measurement, KPI-budget-checkpoint mapping, governance paragraph, and review-response table
- `DEEP_CULTIVATION_POSTDOC_NEXT_STEP_REVIEW.md`: postdoctoral strategy review for shaping the urology previsit system as a Health Taiwan deep-cultivation workflow-transformation proposal; separates adopted, modified, and deferred suggestions
- `DEEP_CULTIVATION_OFFICIAL_FORMAT_CROSSWALK.md`: maps the archived official Health Taiwan proposal format to the current draft package and exposes missing institutional fields
- `DEEP_CULTIVATION_APPLICATION_DRAFT_V0_3.md`: prior official-format-aligned proposal draft for the urology previsit subproject
- `DEEP_CULTIVATION_APPLICATION_DRAFT_V0_2.md`: prior official-format proposal skeleton for the urology previsit subproject
- `DEEP_CULTIVATION_SUBPROJECT_UROLOGY_PREVISIT_V0_1.md`: official-format subproject draft for `泌尿科門診前問診與醫師覆核摘要支持系統`
- `DEEP_CULTIVATION_KPI_TO_BUDGET_TABLE.md`: KPI-to-budget map for budget traceability and work-package justification
- `DEEP_CULTIVATION_KPI_BUDGET_ANNUAL_INTEGRATION_TABLE.md`: integrates official proposal section, KPI, budget bucket, annual checkpoint, owner, and evidence artifact
- `DEEP_CULTIVATION_GOVERNANCE_CHECKLIST.md`: AI, cybersecurity, data, privacy, clinical, procurement, and interoperability governance checklist
- `DEEP_CULTIVATION_ANNUAL_CHECKPOINT_TABLE.md`: 115 prep and 116-118 checkpoint table for proposal monitoring and reporting
- `DEEP_CULTIVATION_SCORING_RUBRIC.md`: four-layer 100-point scoring rubric for clinical value, engineering maturity, governance, and MOHW application-format compliance; includes A/B/C evidence gates, score caps, reviewer micro-comments, and urology previsit / CRM interpretation rules
- `DEEP_CULTIVATION_MOHW_COMPLIANCE_RUBRIC.md`: expanded fourth 100-point layer for MOHW format, attachment, budget, submission, governance-checklist, and reporting compliance
- `DISCOVERY_PROTOCOL.md`: discovery runbook and conversation sequence
- `V1_PHASE0_CLINICIAN_REVIEW_PROTOCOL.md`: synthetic-only v1 clinician/nurse review protocol after the 2026-04-23 meeting
- `V1_PHASE0_EXECUTION_AND_ANALYSIS_PLAN.md`: reviewer ask, session, live capture, analysis, and decision-memo loop for running Phase 0
- `V1_PHASE0_PRIORITY_FLOW_SELECTION.md`: proposed first-three complaint-flow shortlist and substitution rule for Phase 0
- `MEETING_CAPTURE_TEMPLATE.md`: live or same-day capture template
- `DECISION_RECORD_TEMPLATE.md`: post-meeting decision record template
- `PAPER_PATENT_PRODUCT_EXTRACTION.md`: separation guide for paper, patent, and product implications

## Use Rule

Use these files to prepare for and synthesize real reviewer conversations. Store dated outputs under `../records/`.

When drafting proposal, article, paper, reviewer-brief, or lab-brief language from this folder, use `../core/ASSERTIVE_WRITING_POLICY.md`. Discovery evidence should sharpen the argument, not make the writing defensive.

Before using reviewer time for v1 Phase 0, run the demo repo readiness gate:

`UROLOGY_PREVISIT_BASE_URL=http://127.0.0.1:4176 npm run phase0:check`

The 2026-04-23 gate passed `81/81`; rerun it if files or the local server route change.

If a discovery result changes stable system logic, update `../core/`. If it changes question inclusion, update `../clinical-question-governance/`.
