# V1 Phase 0 Execution And Analysis Plan

Date: 2026-04-23
Depends on: `V1_PHASE0_CLINICIAN_REVIEW_PROTOCOL.md`

## Purpose

This plan converts Phase 0 from a protocol into an executable review loop.

The protocol defines what evidence matters. This file defines how to run the session, analyze the evidence, and decide the next artifact without drifting into deployment work.

## Execution Loop

1. Run the pre-session readiness gate.
2. Ask for review.
3. Run the synthetic session.
4. Capture live evidence.
5. Fill the scorecard and flow worksheet.
6. Analyze evidence.
7. Write a decision memo.
8. Update governance gates.
9. Only then choose the next artifact.

If any step proposes real patient data, hospital integration, clinical-use claims, or unresolved IP/vendor use, stop and switch to governance review.

## Pre-Session Readiness Gate

Before using reviewer time, start the static product repo server and run:

```bash
cd /home/jnln3799/every_on_git_ubuntu/urology-ai-previsit-demo
npm run phase0:check
```

If the server is already running on a non-default port, point the gate at it:

```bash
UROLOGY_PREVISIT_BASE_URL=http://127.0.0.1:4176 npm run phase0:check
```

This gate verifies the v1 route, five synthetic cases, live capture sheet, scorecard, priority-flow worksheet, safety boundaries, smoke checks, and tests. A failing readiness gate means the session should be delayed or narrowed before asking 許醫師 / 吳老師 to review.

## Reviewer Ask

Ask 許醫師 for:

- one 30-45 minute Phase 0 review slot
- confirmation, replacement, or reordering of the proposed first three complaint flows from the 12 QA categories
- persona preference: named personas or neutral role labels
- exam-prep wording approval/rejection
- patent/vendor boundaries
- one nurse or clinic-staff reviewer if possible

The practical draft lives in:

`/home/jnln3799/every_on_git_ubuntu/urology-ai-previsit-demo/docs/research/v1-phase0-reviewer-ask.md`

## Priority Flow Default

Use this as the starting shortlist unless 許醫師 changes it:

1. `頻尿或夜尿`
2. `小便困難或尿不出來`
3. `血尿或健檢發現潛血`

Runnable synthetic cases now exist for all three:

- `synthetic-frequency-older-adult`
- `synthetic-emptying-difficulty`
- `synthetic-hematuria-occult-blood`

The rationale and substitution rule live in:

`V1_PHASE0_PRIORITY_FLOW_SELECTION.md`

This is not a clinical priority ranking. It is a way to keep Phase 0 narrow enough for line-level review.

## Session Run Standard

Use the run sheet in:

`/home/jnln3799/every_on_git_ubuntu/urology-ai-previsit-demo/docs/research/v1-phase0-review-session-script.md`

Capture live notes in:

`/home/jnln3799/every_on_git_ubuntu/urology-ai-previsit-demo/docs/research/v1-phase0-review-capture.md`

Minimum required evidence:

- boundary clarity judgment
- intake/waiting-room fit comments
- nurse repair usefulness and burden comments
- timed physician summary read
- useful/noisy/unsafe line notes
- confirmed or revised first three complaint flows, or a decision to narrow differently
- export/mock API concerns
- final continue / revise / narrow / pause / governance-review decision

## Analysis Standard

Do not summarize the review as "positive" or "negative" alone.

Classify every important observation as:

- useful: keep or emphasize
- noisy: remove, shorten, or reorder
- unsafe: must change before next review
- missing: add only if it supports the chosen next artifact
- gate: cannot proceed without owner/review

The analysis template lives in:

`/home/jnln3799/every_on_git_ubuntu/urology-ai-previsit-demo/docs/research/v1-phase0-analysis-template.md`

## Decision Memo Standard

The decision memo must choose one:

- continue
- revise
- narrow
- pause
- governance review before next step

The decision memo must name:

- why the decision follows from evidence
- what changed
- what is accepted
- what is rejected or deferred
- the next artifact
- the stop conditions

The memo template lives in:

`/home/jnln3799/every_on_git_ubuntu/urology-ai-previsit-demo/docs/research/v1-phase0-decision-memo-template.md`

## Decision Rules

Continue only if:

- physician would read the summary
- nurse/staff burden is acceptable
- three flows have safe confirmation-only wording direction
- no safety boundary breaks

Revise if:

- the workflow is plausible but wording, fields, or summary order are wrong

Narrow if:

- only one symptom cluster or handoff moment is supported

Pause if:

- summary would not be read
- staff burden is too high
- no workflow slot exists
- safety wording cannot be fixed

Governance review if:

- the next step needs real data, HIS, IP/vendor clearance, regulatory classification, IRB, cloud, or hospital operational approval

## Research Discipline

Do not let Phase 0 become:

- a patient pilot
- a HIS integration meeting
- a patent claim session
- a regulatory conclusion
- a commercial launch plan
- a new broad feature sprint

The output is one decision and one next artifact.
