# Core System Logic

This folder contains the stable, non-technical system logic.

Use it to review product intent, user model, workflow reasoning, safety boundaries, evaluation logic, trade-offs, failure modes, and evolution rules.

## Files

- `THINKING_SPEC.md`: integrated thinking spec and master narrative
- `DESIGN_PHILOSOPHY.md`: design values, first principles, and rejected instincts
- `WORKFLOW_LOGIC.md`: encounter sequence, decision points, and handoff logic
- `SAFETY_BOUNDARY.md`: clinical, privacy, wording, and governance boundaries
- `EVALUATION.md`: usefulness, safety, adoption, and decision metrics
- `TRADEOFF_ANALYSIS.md`: sacrifices, rejected alternatives, counterfactuals, and reuse
- `FAILURE_ANALYSIS.md`: likely failure modes, signals, and responses
- `EVOLUTION_PATH.md`: staged growth rules for future versions

## Use Rule

Core files should change only when the system's durable logic changes.

Clinical question details belong in `../clinical-question-governance/`. Meeting templates belong in `../discovery/`. Dated evidence belongs in `../records/`.
