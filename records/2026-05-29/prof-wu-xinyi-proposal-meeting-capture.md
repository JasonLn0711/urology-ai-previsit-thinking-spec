# Meeting Capture: Prof. Wu 2026-05-29 Follow-Up

Status: captured

## Meeting Identity

| Field | Notes |
| --- | --- |
| Date | 2026-05-29 |
| Approximate start | 09:37 |
| Primary source | `/home/jnclaw/every_on_git_jnclaw/project_aura/260529_0937_withProfWu/transcript_260529_0937_withProfWu_final (gpt-correct).txt` |
| Auxiliary sources | Gemini clean transcript and timestamped final transcript in the same Project AURA folder |
| Participants | Prof. Wu and Jason |
| Scope in this repo | 信義生醫 / 院外門診部 deep-cultivation proposal, reference proposal analysis, and urology-previsit proposal package update |

## Source Priority

Use the gpt-correct transcript as the primary meeting source. The Gemini and timestamped transcripts are useful for confirming wording around budget, KPI, page limit, and the next discussion date.

The transcript also covered CDE / TFDA medical-cybersecurity slides, white-box source-code scanning, training class opportunities, medical-device certification document pipelines, Hui-Cheng demo/API cooperation, and GPT Pro / Codex Pro. Those are recorded here only as meeting context. The urology proposal action in this repo is item six from the meeting task list.

## Completed CDE / TFDA Items

Jason reports that these meeting tasks are already completed and should not be reopened in this proposal package:

- CDE / TFDA medical-cybersecurity script: keep sections 0-8 stable and reorganize section breaks from section 9 onward.
- Confirm sections 9-26 as complete narrative units for NotebookLM slide generation.
- Recheck white-box testing, CONTEC CMS8000, Abbott firmware, deployment control, supply chain, and source-code scanning paragraphs.

Planning implication:

```text
Do not spend deep-cultivation proposal capacity on the CDE / TFDA sectioning task.
```

## Proposal Signal

Prof. Wu confirmed that Jason had already prepared a version of the 信義生醫 / 院外門診部 proposal. The active revision request is:

```text
總經費改成三年一千萬元。
每一項經費都要對應明確 KPI。
整份 proposal 控制在 20 頁以內。
2026-06-02 前準備好討論版本。
```

The attached subproject-three PDF from 美如主任 should be used as a reference, but not copied uncritically. Prof. Wu explicitly noted that the reference was GPT-generated and still needs human review.

## Reference Proposal Relationship

The new attached reference is another outpatient-department proposal, apparently for a different subproject. It is useful because it shows a complete three-year, NT$10,000,000 proposal package with:

- cover and identity fields
- official-looking section order
- three-year execution period
- detailed implementation phases
- work groups and role table
- cybersecurity and privacy section
- year-by-year KPI table
- line-item budget table totaling NT$10,000,000

Use it as a formatting and completeness precedent. Do not import its clinical scope, risk-triage language, direct HIS claims, or aggressive outcome claims into the urology previsit proposal.

## Current Urology Proposal Decision

Promote the proposal package from v0.4 to v0.5 with these updates:

| Decision | v0.5 handling |
| --- | --- |
| Budget ceiling | Set working ceiling to NT$10,000,000 total over three years. |
| Budget rule | Every budget bucket must map to KPI, owner, evidence artifact, and annual checkpoint. |
| Page limit | Treat 20 pages as the discussion-version cap. Write section lengths as budgeted pages. |
| Reference proposal | Archive the PDF and create a structured analysis record under `records/2026-05-29/xinyi-outpatient-proposal-reference/`. |
| Discussion date | Prepare the discussion version for Tuesday, 2026-06-02. |
| Scope | Keep the urology previsit / clinician-review summary and workflow-friction reduction scope. |
| Boundary | CRM, HIS/EMR integration, real patient data, and autonomous clinical decision support stay governed future phases unless reopened by named owners. |

## Action Items

| Item | Owner | Repo / file |
| --- | --- | --- |
| Copy reference PDF into the urology thinking-spec record | Jason / Codex | `records/2026-05-29/xinyi-outpatient-proposal-reference/sources/` |
| Extract and analyze the reference proposal | Jason / Codex | `xinyi-outpatient-proposal-reference/README.md` |
| Create v0.5 proposal discussion draft | Jason / Codex | `discovery/DEEP_CULTIVATION_APPLICATION_DRAFT_V0_5.md` |
| Update KPI-budget tables for NT$10,000,000 | Jason / Codex | `discovery/DEEP_CULTIVATION_KPI_TO_BUDGET_TABLE.md` and integration table |
| Update planning locator/status | Jason / Codex | planning repo project tracker and day note |
| Prepare 2026-06-02 talking points | Jason | use v0.5 draft, KPI table, and reference analysis |

## Meeting Evidence Constraints

- Prof. Wu's exact requested budget constraint is confirmed by both the gpt-correct and timestamped transcripts: NT$10,000,000 over three years.
- The page limit is confirmed as 20 pages for the proposal discussion version.
- The reference PDF should be treated as a useful pattern and an imperfect AI-generated draft.
- This meeting does not authorize real patient data, production HIS/EMR writeback, autonomous triage, diagnosis, or treatment recommendation.
