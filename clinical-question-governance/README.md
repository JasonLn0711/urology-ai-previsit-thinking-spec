# Clinical Question Governance

This folder governs which urology previsit questions should be asked, who should answer them, and how they should appear in patient, nurse, and physician workflows.

It is evidence-facing and review-facing. It is not a diagnosis protocol, treatment pathway, or production questionnaire.

## Files

- `clinical_question_governance.md`: overall clinical question governance report
- `question_candidates_matrix.md`: candidate question matrix with evidence, workflow value, risk, and inclusion decision
- `doctor_needs.md`: physician-facing information needs, summary needs, red-flag observations, and missing-information priorities
- `nurse_needs.md`: nurse-facing support needs for completion assistance, diary instruction, medication review, containment support, and review triggers
- `mvp_question_set_recommendation.md`: recommended MVP question set by core, conditional, family-assisted/source-labeled, nurse-repair, clinician-only, and deferred categories
- `source_evidence_map.md`: source-to-conclusion map distinguishing direct evidence support from workflow inference

## Use Rule

When a question is added, removed, or reworded, update the matrix first. Then update the MVP recommendation and source evidence map if the decision changes.

Do not add patient-facing questions that bypass the safety boundary in `../core/SAFETY_BOUNDARY.md`.
