# Deep-Cultivation v0.4 Precedent Integration Record

Status: accepted implementation record

Date: 2026-05-21

Repo version after update: `v0.4.0`

## Trigger

The team reviewed the A2-0048 Health Taiwan deep-cultivation precedent proposal and decided to learn from its official proposal packaging while preserving the current urology previsit scope.

## Decision

Use the precedent as a format and execution-packaging reference.

Do not expand the system into a broad smart-hospital ecosystem.

The accepted direction is:

```text
Keep the narrow urology previsit workflow.
Adopt the precedent's official-format discipline.
Do not inherit the precedent's scope breadth or clinical-decision language.
```

## Implemented Changes

- Added `discovery/DEEP_CULTIVATION_APPLICATION_DRAFT_V0_4.md`.
- Promoted v0.4 as the current proposal-writing entrypoint.
- Added official package checklist, category-to-claim map, owner table, baseline measurement plan, KPI-budget-checkpoint table, governance paragraph, governance flow diagram and review-response table.
- Updated KPI / budget / annual checkpoint integration to point to v0.4.
- Updated annual checkpoint table to include owner-table and review-response readiness.
- Updated official-format crosswalk from v0.3 to v0.4.
- Updated proposal-writing guide and repo README routing.
- Bumped repo version from `v0.3.0` to `v0.4.0` with `scripts/bump_version.py`.

## What Changed In Proposal Quality

v0.3 was already correctly scoped.

v0.4 makes the package more proposal-ready by adding:

- owner visibility
- baseline measurement
- review-response readiness
- official package completeness
- KPI, budget, checkpoint and evidence traceability
- stronger AI/data/cybersecurity governance wording

## What Did Not Change

The clinical safety boundary did not change.

Still excluded:

- diagnosis
- treatment advice
- autonomous triage
- queue priority
- automatic EMR writeback
- production HIS/EMR integration
- real patient data before governance approval
- first-phase CRM follow-up

## Next Gate

Before transferring v0.4 into the official Word template, the parent proposal owner must confirm:

1. applicant and application mode
2. official period and budget ceiling
3. partner list and consent route
4. PI/contact fields
5. owner names for clinical, workflow, IT/security, AI/data governance, evaluation and budget
6. whether ASR is funded or optional only
7. whether CRM and FHIR remain future readiness

