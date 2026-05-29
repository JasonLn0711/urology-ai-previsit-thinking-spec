# Next Step: Meeting-To-Decision Pack

## Purpose

The next step is to use the thinking spec as a disciplined discovery tool.

The question is not "Can we build more?" The question is:

Does the urology smart-previsit concept solve a real workflow problem strongly enough to justify the next small experiment?

## Target Outcome

After the physician conversation and same-day synthesis, the project should have:

- a clear statement of the real clinic workflow problem
- a list of repeated questions worth collecting before the physician-led visit
- a list of topics that must remain physician-led
- a judgment on whether the summary is useful
- a continue, revise, narrow, or pause decision
- separate implications for paper framing, patent reasoning, and product decision-making

## Current Active Follow-Up: 2026-06-02 Deep-Cultivation Draft Review

The latest active follow-up comes from the 2026-05-29 Prof. Wu meeting. The working instruction is now:

```text
三年期
總經費新臺幣 1,000 萬元整
每一項經費對應 KPI
討論版控制在 20 頁以內
2026-06-02 前準備好討論版本
```

Current v0.5 discussion artifacts:

- Meeting capture: `../records/2026-05-29/prof-wu-xinyi-proposal-meeting-capture.md`
- Decision record: `../records/2026-05-29/deep-cultivation-v0.5-decision-record.md`
- Reference proposal analysis: `../records/2026-05-29/xinyi-outpatient-proposal-reference/README.md`
- Current application draft v0.5: `DEEP_CULTIVATION_APPLICATION_DRAFT_V0_5.md`

The attached subproject-three PDF is useful as a proposal-structure, KPI, budget, and section-completeness precedent. It should not expand the urology scope into autonomous risk routing, direct HIS/EMR writeback, or unsupported production integration claims.

The latest active follow-up comes from the 2026-05-19 北市聯醫 deep-cultivation meeting:

- Transcript: `../records/2026-05-19/taipei-city-hospital-deep-cultivation-meeting-transcript.md`
- Summary and signals: `../records/2026-05-19/deep-cultivation-summary-and-signals.md`
- Policy reference: `../records/2026-05-19/health-taiwan-deep-cultivation-policy-reference.md`
- Downloaded policy archive: `../records/2026-05-19/policy-documents/README.md`
- Related examples: `../records/2026-05-19/health-taiwan-related-examples.md`
- Intended-use freeze: `INTENDED_USE_FREEZE.md`
- Demo-scope freeze: `DEMO_SCOPE_FREEZE.md`
- Official-format crosswalk: `DEEP_CULTIVATION_OFFICIAL_FORMAT_CROSSWALK.md`
- Current application draft v0.5: `DEEP_CULTIVATION_APPLICATION_DRAFT_V0_5.md`
- Prior application draft v0.4: `DEEP_CULTIVATION_APPLICATION_DRAFT_V0_4.md`
- Application draft v0.3: `DEEP_CULTIVATION_APPLICATION_DRAFT_V0_3.md`
- Prior application skeleton v0.2: `DEEP_CULTIVATION_APPLICATION_DRAFT_V0_2.md`
- KPI-to-budget table: `DEEP_CULTIVATION_KPI_TO_BUDGET_TABLE.md`
- KPI / budget / annual checkpoint integration: `DEEP_CULTIVATION_KPI_BUDGET_ANNUAL_INTEGRATION_TABLE.md`
- Governance checklist: `DEEP_CULTIVATION_GOVERNANCE_CHECKLIST.md`
- Annual checkpoint table: `DEEP_CULTIVATION_ANNUAL_CHECKPOINT_TABLE.md`
- Postdoctoral next-step review: `DEEP_CULTIVATION_POSTDOC_NEXT_STEP_REVIEW.md`
- Capture: `../records/2026-05-19/deep-cultivation-meeting-capture.md`
- Decision record: `../records/2026-05-19/deep-cultivation-decision-record.md`
- Extraction notes: `../records/2026-05-19/deep-cultivation-extraction-notes.md`
- System positioning: `../core/DEEP_CULTIVATION_SYSTEM_POSITIONING.md`
- Proposal writing guide: `DEEP_CULTIVATION_PROPOSAL_WRITING_GUIDE.md`
- Assertive writing gate: `ASSERTIVE_WRITING_GATE.md`
- Scoring rubric: `DEEP_CULTIVATION_SCORING_RUBRIC.md`
- MOHW compliance rubric: `DEEP_CULTIVATION_MOHW_COMPLIANCE_RUBRIC.md`
- Assertive writing policy: `../core/ASSERTIVE_WRITING_POLICY.md`
- Repo inclusion recommendation: `../records/2026-05-19/repo-inclusion-recommendation.md`

Prepare for the tentative 2026-06-02 10:00 follow-up by drafting the smart-healthcare / AI / CRM subproject around service deployment, not model novelty.

All draft language for this follow-up should use the assertive writing policy:

```text
confident contribution first -> scope discipline second -> next review gate third
```

Do not open with defensive disclaimers.

The 2026-05-20 postdoctoral review keeps that direction but narrows the immediate next step:

```text
freeze intended use -> freeze demo scope -> prepare reviewer evidence
-> define governance gates -> map KPI to budget
```

Do not add new AI features until the intended-use and demo-scope freeze are explicit.

The current application-writing execution artifacts are now:

```text
INTENDED_USE_FREEZE.md
DEMO_SCOPE_FREEZE.md
DEEP_CULTIVATION_OFFICIAL_FORMAT_CROSSWALK.md
DEEP_CULTIVATION_APPLICATION_DRAFT_V0_5.md
DEEP_CULTIVATION_APPLICATION_DRAFT_V0_4.md
DEEP_CULTIVATION_KPI_TO_BUDGET_TABLE.md
DEEP_CULTIVATION_KPI_BUDGET_ANNUAL_INTEGRATION_TABLE.md
DEEP_CULTIVATION_GOVERNANCE_CHECKLIST.md
DEEP_CULTIVATION_ANNUAL_CHECKPOINT_TABLE.md
```

Use these as the next drafting package before expanding technical features.

Before sending any section to a teacher, hospital reviewer, or proposal owner, run `ASSERTIVE_WRITING_GATE.md`:

```text
contribution -> workflow value -> deliberate scope -> governance boundary -> next evidence gate
```

The additional clinical-friction insight from the same meeting should be treated as a hard review question:

```text
Will this reduce physician, nurse, or clinic-staff burden without making them do extra AI research, labeling, system switching, or exception handling?
```

Use `CLINICAL_FRICTION_REDUCTION_ANALYSIS.md` before writing KPI, budget, or workflow claims.

Strategic label for the draft:

```text
AI Systems Engineering for Healthcare Deployment
```

The next draft should answer:

- How does PSA/community screening route into SOP, return flow, case management, and CRM?
- Which parts belong to APP, guided intake, ASR, reminders, API, or CRM?
- How should the existing urology previsit demo be described as visit-readiness and clinician-review support, not AI triage?
- Which KPI justify each budget line?
- How does the draft score under the four independent 100-point layers: clinical workflow value, technical engineering, governance, and MOHW format compliance?
- Which work is internal, outsourced, or hybrid?
- What IRB, MOU, procurement, and security-governance gates apply?
- Is Aging Clock excluded, appended as research, or reframed as a biomarker follow-up service?
- Which repository evidence should be attached or referenced, and which should remain internal?

Jason-specific work scope:

- `../records/2026-05-19/jason-work-scope-from-deep-cultivation-meeting.md`

For Jason's June 2 preparation, prioritize:

- 子計畫二 narrative
- proposal skeleton and section order from `DEEP_CULTIVATION_PROPOSAL_WRITING_GUIDE.md`
- objective scoring and format-compliance checks from `DEEP_CULTIVATION_SCORING_RUBRIC.md`
- detailed D-layer compliance checks from `DEEP_CULTIVATION_MOHW_COMPLIANCE_RUBRIC.md`
- first-year / second-year / third-year KPI
- KPI-to-budget mapping
- IRB and privacy prerequisites
- internal vs outsourced system components
- proposal evidence package: thinking spec repo vs demo repo, selected appendices, and exact boundary wording
- whether kiosk / chronic-disease-system adaptation and smart-pharmacy ideas are core scope or optional expansion
- confident and non-defensive tone from `../core/ASSERTIVE_WRITING_POLICY.md`

Policy-alignment paragraph to prepare:

- How 子計畫二 maps to `導入智慧科技醫療`
- How CRM / reminders / summary workflow reduce repeated work and support `優化醫療工作條件`
- How community PSA screening and MOU support `社會責任醫療永續`
- Whether student / cross-domain work should be explicitly framed under `規劃多元人才培訓`
- Why `urology previsit / visit-readiness / clinician-review summary / CRM follow-up support` is the correct current scope

Example-pattern paragraph to prepare:

- Compare 子計畫二 to MOHW examples of AI voice assistant / documentation burden reduction.
- Use the Tainan mobile-service pattern as evidence that deep-cultivation proposals can be service-system and deployment oriented.
- Use AI Center guidance to add cybersecurity governance, data governance, AI governance, FHIR/TW Core IG, and human-in-the-loop language.
- Avoid claiming direct equivalence to AI triage or diagnosis examples.

## Detailed Artifacts

Use these documents to run the next step:

- `DEEP_CULTIVATION_PROPOSAL_WRITING_GUIDE.md`: proposal section structure, story line, KPI/budget logic, and June 2 draft package
- `DEEP_CULTIVATION_SCORING_RUBRIC.md`: A/B/C/D 100-point scoring system, evidence requirements, penalties, and MOHW format-compliance checklist
- `DEEP_CULTIVATION_MOHW_COMPLIANCE_RUBRIC.md`: expanded D-layer official-format, attachment, budget, governance-checklist, submission, and reporting preflight
- `DISCOVERY_PROTOCOL.md`: meeting runbook, question sequence, capture rules, and decision standard
- `MEETING_CAPTURE_TEMPLATE.md`: structured note template for workflow facts, repeated questions, boundaries, and decision signals
- `DECISION_RECORD_TEMPLATE.md`: post-meeting decision record for continue, revise, narrow, or pause
- `PAPER_PATENT_PRODUCT_EXTRACTION.md`: separate extraction logic for paper framing, patent reasoning, and product adoption

Recommended order:

1. Read `DISCOVERY_PROTOCOL.md` before the meeting.
2. Fill `MEETING_CAPTURE_TEMPLATE.md` during or immediately after the meeting.
3. Write one copy of `DECISION_RECORD_TEMPLATE.md` after synthesis.
4. Use `PAPER_PATENT_PRODUCT_EXTRACTION.md` to keep research, patent, and product conclusions separate.

For the planned 2026-04-23 urology conversation, use the dated working packet:

- `../records/2026-04-23/pre-meeting-brief.md`
- `../records/2026-04-23/meeting-capture.md`
- `../records/2026-04-23/decision-record.md`
- `../records/2026-04-23/extraction-notes.md`

After the 2026-04-23 meeting and 許醫師 LINE follow-up materials, the active next research step is no longer a generic discovery conversation. Use:

- `V1_PHASE0_CLINICIAN_REVIEW_PROTOCOL.md`
- `V1_PHASE0_EXECUTION_AND_ANALYSIS_PLAN.md`
- `V1_PHASE0_PRIORITY_FLOW_SELECTION.md`

This keeps the next work synthetic-only and asks clinician/nurse reviewers to judge v1 usefulness, unsafe wording, first three complaint flows, and governance gates before any real-data pilot.

Before asking for reviewer time, run the demo repo readiness gate:

```bash
cd /home/jnln3799/every_on_git_ubuntu/urology-ai-previsit-demo
UROLOGY_PREVISIT_BASE_URL=http://127.0.0.1:4176 npm run phase0:check
```

The gate must pass for the active local server, five synthetic cases, live capture sheet, priority-flow worksheet, scorecard, safety boundaries, smoke checks, and tests.

Current proposed first-three default, pending 許醫師 confirmation:

- `頻尿或夜尿`
- `小便困難或尿不出來`
- `血尿或健檢發現潛血`

This default is a review scaffold, not a clinical priority claim.

## Step 1: Pre-Meeting Readiness

Enter the meeting with a discovery frame, not a product pitch.

Bring:

- core problem statement
- workflow sequence
- physician question list
- safety boundary
- evaluation criteria
- stop boundary

Opening frame:

"The goal is not to replace physician judgment. The goal is to understand whether a guided previsit flow can collect repeated, high-value information before the formal visit and give the clinician a short reviewable summary."

Do not promise:

- diagnosis
- triage
- treatment suggestions
- hospital integration
- voice-first interaction
- production use
- real patient-data use

## Step 2: Meeting Capture

Capture observations in four categories:

| Category | What To Capture | Why It Matters |
| --- | --- | --- |
| Workflow facts | current check-in, waiting, nursing, and physician sequence | prevents imagined workflow design |
| Repeated questions | questions asked more than once | defines where previsit collection may help |
| Boundaries | physician-only topics, safety concerns, privacy concerns | prevents unsafe expansion |
| Decision signals | useful, noisy, unacceptable, next artifact | supports continue, revise, narrow, or pause |

During capture, avoid turning every comment into a feature request. Objections are evidence.

## Step 3: Same-Day Synthesis

Within the same day, compress the meeting into a one-page decision summary.

Use this structure:

| Section | Content |
| --- | --- |
| Clinical need | what problem exists before the physician-led visit |
| User need | what patients, nurses, or physicians need to reduce friction |
| Workflow pain points | where repeated questioning or missing information appears |
| Pre-collectable information | what can be safely asked before the physician enters |
| Physician-led information | what must remain physician-owned |
| Summary format | what the clinician would actually read |
| Safety concerns | what could mislead, overburden, or create privacy risk |
| Recommendation | continue, revise, narrow, or pause |
| Next owner/action | the smallest next artifact and who should review it |

Use cautious wording:

- observed
- reported
- requested
- likely useful
- may be noisy
- needs confirmation
- not yet justified

## Step 4: Decision Gate

Continue only if:

- the repeated-question problem is real
- clinicians can name useful pre-collected information
- the summary can be short enough to read
- safety boundaries remain acceptable
- the next artifact is small and concrete

Revise if:

- the question tree is too broad
- the summary format is wrong
- self-filled use is unrealistic but assisted use is plausible
- the main value is staff workflow rather than patient self-entry
- the clinician wants different grouping or wording

Pause if:

- the clinic has no place to use the workflow
- clinicians would not read the summary
- the concept adds staff burden without clear benefit
- safety or privacy concerns dominate
- existing intake forms already solve the problem well enough

## Step 5: Paper Framing Extraction

The paper framing should not be "artificial intelligence asks medical questions."

The stronger framing is:

"A bounded clinician-review workflow can use guided previsit interaction to reduce repeated information gathering while preserving clinical authority and safety boundaries."

Evidence needed:

- current workflow map
- repeated-question examples
- clinician usefulness judgment
- safety objections
- summary format feedback
- decision rationale

## Step 6: Patent Reasoning Extraction

The patent reasoning should not claim that a questionnaire alone is novel.

The stronger invention logic is:

"A guided previsit workflow that separates patient-facing symptom capture, missing-information repair, safety-boundary preservation, and clinician-review summary generation."

Possible reasoning areas:

- separating patient input from clinician interpretation
- identifying missing previsit information before handoff
- generating neutral review flags rather than diagnostic claims
- supporting patient self-entry, family-assisted operation with source labeling, and nurse repair of missing information
- producing a constrained summary for rapid clinical review

Do not assert patentability without prior-art review.

## Step 7: Product Decision Extraction

The product question is:

Would a real clinic adopt this because it saves time or improves readiness without adding unacceptable burden?

Decision matrix:

| Decision | Use When | Next Action |
| --- | --- | --- |
| Continue | workflow pain is real and summary is useful | refine question tree and summary |
| Revise | concept is useful but current format is wrong | redesign around feedback |
| Narrow | only one patient group or symptom group is valuable | focus the next experiment |
| Pause | no workflow fit or too much burden | stop product work and preserve learning |

## Step 8: Repository Update After Meeting

After the meeting, update this thinking repo with:

- confirmed workflow facts
- rejected assumptions
- revised open questions
- decision gate result
- paper, patent, and product implications

Do not add real patient data.

Do not add technical implementation details.

Do not rewrite the entire thinking spec unless the meeting invalidates a core assumption.

For the 2026-05-19 deep-cultivation meeting, the repo update is complete when:

- the corrected transcript is archived
- source ASR/transcript files are preserved under `records/2026-05-19/sources/`
- the capture, decision record, and extraction notes exist
- `core/DEEP_CULTIVATION_SYSTEM_POSITIONING.md` records the accepted deep-cultivation system-design supplement
- `README.md`, `meta/open_questions.md`, assumptions, constraints, and evolution/safety docs point to the CRM/service-flow framing
- Aging Clock remains explicitly bounded until definition and governance are clarified

## Acceptance Criteria

This next step is complete when:

- the meeting has a one-page summary
- each open question is answered, revised, or marked unknown
- the continue, revise, narrow, or pause decision is explicit
- safety boundaries are unchanged or updated deliberately
- paper, patent, and product implications are separated
- no real patient data is stored
- no technical implementation plan replaces workflow reasoning
