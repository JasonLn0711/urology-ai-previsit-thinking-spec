# Discovery And Decision Pack

This folder contains the operating pack for physician, nurse, and workflow discovery.

It is meant to turn conversations into auditable decisions without mixing paper framing, patent reasoning, and product scope.

## Files

- `NEXT_STEP.md`: meeting-to-decision workflow
- `DEEP_CULTIVATION_PROPOSAL_WRITING_GUIDE.md`: Health Taiwan deep-cultivation proposal writing structure for the urology previsit / CRM service-flow draft
- `DEEP_CULTIVATION_SUBPROJECT_UROLOGY_PREVISIT_V0_1.md`: official-format subproject draft for `泌尿科門診前問診與醫師覆核摘要支持系統`
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

Before using reviewer time for v1 Phase 0, run the demo repo readiness gate:

`UROLOGY_PREVISIT_BASE_URL=http://127.0.0.1:4176 npm run phase0:check`

The 2026-04-23 gate passed `81/81`; rerun it if files or the local server route change.

If a discovery result changes stable system logic, update `../core/`. If it changes question inclusion, update `../clinical-question-governance/`.
