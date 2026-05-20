# Assertive Writing Implementation Record

Status: accepted repository writing-governance update
Date: 2026-05-20

## Trigger

The project writing method must be confident and non-defensive. Safety boundaries remain mandatory, but the writing must not make the system sound weak, apologetic, or uncertain before stating its contribution.

## Decision

This repository now treats assertive writing as a governance requirement for outward-facing materials.

Accepted stance:

```text
The project is a deliberately scoped clinical workflow-support system that reduces previsit information friction, prepares clinician-reviewable summaries, preserves clinician authority, and creates a governed path for smart-healthcare deployment.
```

Rejected stance:

```text
This is only a small demo and cannot do clinical work.
```

## Implemented Artifacts

| Artifact | Purpose |
| --- | --- |
| `../../core/ASSERTIVE_WRITING_POLICY.md` | Canonical repo-wide writing doctrine. |
| `../../discovery/ASSERTIVE_WRITING_GATE.md` | Pre-circulation paragraph-level review gate. |
| `../../README.md` | Root entrypoint now points to policy and gate. |
| `../../discovery/DEEP_CULTIVATION_PROPOSAL_WRITING_GUIDE.md` | Proposal drafting now requires contribution-first, non-defensive writing. |
| `../../discovery/NEXT_STEP.md` | June 2 preparation now includes assertive writing gate before circulation. |
| `../../discovery/DEEP_CULTIVATION_APPLICATION_DRAFT_V0_3.md` | Current application draft revised to state contribution first and boundary second. |
| `../../discovery/DEEP_CULTIVATION_SCORING_RUBRIC.md` | Scoring rubric now includes assertive narrative gate and penalties for defensive narrative. |
| `../../discovery/DEEP_CULTIVATION_MOHW_COMPLIANCE_RUBRIC.md` | D-layer compliance now includes narrative-confidence preflight. |
| `../../meta/constraints.md` | Defensive outward-facing tone is now a repository constraint. |

## Practical Rule

Before any proposal section, paper paragraph, article draft, reviewer brief, lab brief, or slide narrative leaves this repo, run:

```text
contribution -> workflow value -> deliberate scope -> governance boundary -> next evidence gate
```

## Boundary

This update does not require rewriting raw records, meeting transcripts, source quotations, or dated evidence notes. Those may preserve original cautious wording.

This update applies to outward-facing synthesis and proposal language.

## Next Review Action

Before the next teacher or hospital-stakeholder review, check the latest circulated draft against:

- `../../core/ASSERTIVE_WRITING_POLICY.md`
- `../../discovery/ASSERTIVE_WRITING_GATE.md`
- `../../discovery/DEEP_CULTIVATION_APPLICATION_DRAFT_V0_3.md`
- `../../discovery/DEEP_CULTIVATION_SCORING_RUBRIC.md`
