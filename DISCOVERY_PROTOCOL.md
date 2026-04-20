# Discovery Protocol

## Purpose

This protocol turns the thinking spec into a focused physician and workflow discovery session.

The goal is to learn whether the urology smart-previsit concept solves a real clinic problem strongly enough to justify the next small experiment.

The goal is not to pitch a finished product, collect real patient data, or ask for approval to deploy anything.

## Core Discovery Question

Would a guided previsit flow help the clinic collect repeated, high-value information before the physician-led visit, while preserving clinician judgment and avoiding added staff burden?

## Roles

| Role | Responsibility |
| --- | --- |
| Physician reviewer | explains clinical workflow, usefulness, noise, and safety concerns |
| Clinic workflow informant | explains check-in, waiting, nursing, and handoff realities |
| Product thinker | keeps the discussion focused on problem, boundary, and next decision |
| Note taker | records facts, assumptions, objections, and decision signals without real patient data |

One person may hold more than one role, but the responsibilities should remain separate.

## Pre-Meeting Preparation

Before the meeting, read:

- `THINKING_SPEC.md`
- `WORKFLOW_LOGIC.md`
- `SAFETY_BOUNDARY.md`
- `EVALUATION.md`
- `meta/open_questions.md`

Bring only the reasoning frame:

- problem statement
- workflow hypothesis
- safety boundary
- open questions
- evaluation criteria

Do not bring a long feature roadmap. The meeting should test workflow fit, not product ambition.

## Opening Script

Use this opening frame:

"The goal is not to replace physician judgment. The goal is to understand whether a guided previsit flow can collect repeated, high-value information before the formal visit and give the clinician a short reviewable summary. If the workflow does not fit, pausing is an acceptable outcome."

Then state the safety boundary:

"The concept does not diagnose, triage, recommend treatment, or use real patient data during discovery. Any red-flag information would be shown only as patient-reported observations for clinician review."

## Run Of Meeting

## 1. Map The Current Workflow

Ask:

1. What happens from patient arrival to physician entry?
2. Who talks to the patient before the physician?
3. What information is collected at each step?
4. Where do delays, missing details, or repeated questions appear?
5. Which parts are fixed process and which parts vary by patient?

Output:

- current workflow map
- repeated-question points
- handoff points
- staff burden points

## 2. Identify Repeated, High-Value Questions

Ask:

1. Which questions are asked repeatedly by staff or physicians?
2. Which answers would actually help before the physician enters?
3. Which answers are often missing or unclear?
4. Which questions are safe for a patient or helper to answer before the visit?
5. Which questions are not worth asking early?

Output:

- candidate previsit questions
- questions to remove
- missing-information targets
- physician-only topics

## 3. Separate Previsit Collection From Clinical Judgment

Ask:

1. Which information can be collected early but must be interpreted by the physician?
2. Which topics must remain physician-led from the start?
3. What wording would sound too diagnostic?
4. What red-flag observations are useful if phrased neutrally?
5. What would make the summary unsafe?

Output:

- previsit-safe information list
- physician-led information list
- unsafe wording list
- acceptable observation wording

## 4. Test Patient And Staff Reality

Ask:

1. Which patients could self-complete the flow?
2. Which patients would need staff or family assistance?
3. What language, vision, literacy, or phone-use barriers are common?
4. Would staff assistance save time, shift burden, or add burden?
5. Where would this fit without slowing the clinic?

Output:

- user constraint list
- assisted-use recommendation
- likely adoption blockers
- workflow slot hypothesis

## 5. Test Summary Usefulness

Ask:

1. What would the physician want to see first?
2. What information should never be placed at the top?
3. What can be omitted?
4. What must be shown as missing?
5. Could the summary be read in under one minute?
6. Would the physician use, edit, ignore, or reject it?

Output:

- summary section order
- useful fields
- noisy fields
- missing-information display rule
- clinician-readability judgment

## 6. Decide The Next Small Artifact

Ask:

1. Should the project continue, revise, narrow, or pause?
2. What is the smallest useful next artifact?
3. Who should review it?
4. What evidence would change the decision?
5. What must not be built yet?

Output:

- decision gate result
- next artifact
- owner or reviewer
- pause triggers
- explicit non-goals

## Capture Rules

Write down:

- what was directly stated
- what was inferred
- what remains unknown
- what was rejected
- what would make the concept unsafe
- what would make the concept useful

Do not write down:

- real patient identifiers
- real patient stories with identifying detail
- speculative diagnosis
- treatment suggestions
- commitments to build or deploy
- unreviewed claims of clinical usefulness

## Evidence Standard

A claim is strong only if it is linked to at least one of these:

- current workflow fact
- repeated-question example
- clinician usefulness statement
- staff burden statement
- patient constraint
- safety objection
- summary format preference
- explicit decision from the reviewer

If a claim is based only on hope or product intuition, mark it as an assumption.

## Decision Standard

Use this rule:

- continue if the workflow pain is real and the summary would be used
- revise if the problem is real but the current shape is wrong
- narrow if the value exists only for a specific patient group or symptom group
- pause if the workflow does not fit, staff burden rises, or safety concerns dominate

## Closing Script

End with:

"The next step will not be a broad product roadmap. We will write one decision record: what problem was confirmed, what was rejected, what boundary must remain, and what smallest next artifact is justified."

Then confirm:

- decision category
- smallest next artifact
- reviewer for the next artifact
- safety boundary
- unanswered questions

## Done Definition

The discovery step is done when the repository contains:

- completed capture template
- decision record
- updated assumptions
- updated open questions
- separated paper, patent, and product implications
- no real patient data
- no clinical advice
- no hidden product commitment
