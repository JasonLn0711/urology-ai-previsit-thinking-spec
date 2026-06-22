# NYCU AI Previsit Expert Review Source Archive

Date archived: 2026-06-19

Purpose: preserve the expert-review recommendation package for the
`泌尿科門診前問診與醫師覆核摘要支持系統` proposal package, then use it as the
source of truth for the NYCU Wu-team AI previsit Health Taiwan proposal draft.

## Source Set

| Repo copy | Original file | Role | SHA-256 |
| --- | --- | --- | --- |
| `nycu-ai-previsit-kpi-budget-model-2026-06-19.xlsx` | `NYCU_AI_previsit_KPI_budget_model_2026-06-19.xlsx` | KPI matrix, work-package budget, cost basis, annual checkpoints, review-response matrix | `16b85fdb448c76844b67762acfb289d6aee1f052c50741f427fa26c920eece4d` |
| `nycu-ai-previsit-plan-kpi-budget-review-draft-2026-06-19.docx` | `NYCU_AI_previsit_plan_KPI_budget_review_draft_2026-06-19.docx` | Expert-review prose recommendations for plan structure, KPI, budget and scope control | `f8dc73cdf19c6322e4ef6bc592b3bbfd472431ad2c6e2e8d9ae909101d38c94e` |
| `nycu-ai-previsit-completed-package-2026-06-19.zip` | `NYCU_AI_previsit_completed_package_2026-06-19.zip` | Complete delivered package containing DOCX, PDF and XLSX versions | `6c2037fb2b3c93384d4ecdf3a126e1d887c14f284e457ccdf6b2a1d20a370ce7` |

## Extracted Package

The zip package was extracted under `extracted-package/`.

| Extracted file | SHA-256 |
| --- | --- |
| `NYCU_AI_previsit_plan_KPI_budget_review_draft_2026-06-19.docx` | `f8dc73cdf19c6322e4ef6bc592b3bbfd472431ad2c6e2e8d9ae909101d38c94e` |
| `NYCU_AI_previsit_plan_KPI_budget_review_draft_2026-06-19.pdf` | `b4baf677ce5e0509959432040e42ca04a24a715ef490cc68ca51f5232c9b2c1b` |
| `NYCU_AI_previsit_KPI_budget_model_2026-06-19.xlsx` | `16b85fdb448c76844b67762acfb289d6aee1f052c50741f427fa26c920eece4d` |

The extracted DOCX and XLSX match the top-level repo copies by checksum.

## Converted Review Copies

Converted text copies live under `converted/` for source review and future diffing:

- `nycu-ai-previsit-plan-kpi-budget-review-draft-2026-06-19.md`
- `nycu-ai-previsit-plan-kpi-budget-review-draft-2026-06-19.txt`
- `nycu-ai-previsit-kpi-budget-model-2026-06-19.md`

## Proposal Use Decision

The accepted writing direction from this package is:

- 主軸：範疇三「導入智慧科技醫療」。
- 副支援：範疇一「優化醫療工作條件」。
- 三年工作額度：NT$10,000,000 as the AI-only planning ceiling.
- Core package: guided intake, source label, missing-field visibility,
  one-page physician-review summary, AI/data/security governance, KPI evidence,
  and annual handoff evidence.
- Scope controls: CRM, patient messaging, patient follow-up, formal HIS/EMR
  writeback, AI diagnosis, AI treatment, autonomous triage, foreign travel and
  personal-device procurement stay outside this package unless separately
  activated by the parent proposal owner and governance route.

Use the analysis record at
`../../nycu-ai-previsit-expert-review-analysis.md` before editing the proposal
draft.
