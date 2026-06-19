# Urology AI Previsit Thinking Spec

<img src="http://estruyf-github.azurewebsites.net/api/VisitorHit?user=JasonLn0711&repo=urology-ai-previsit-thinking-spec&countColor=%237B1E7B" alt="Visitor count"/>
This repository is the thinking and governance layer for a urology previsit interview system.

It deliberately owns system reasoning, clinical-workflow boundaries, proposal framing, and review evidence. Code, demo implementation, real patient data, hospital integration, clinical protocol writing, and regulatory submission work belong to separately governed repositories or institutional processes.

## First-Principles Role

The repository exists to answer one question:

Can a guided previsit interview collect useful patient-reported information before a urology visit while keeping diagnosis, triage, treatment, and final judgment with clinicians?

Every file should serve one of four purposes:

1. Define the system logic.
2. Govern which questions are clinically appropriate.
3. Prepare or capture clinician/nurse discovery.
4. Record assumptions, constraints, open questions, and dated review evidence.

If a file does not serve one of those purposes, it should not live here.

## Repository Map

```text
urology-ai-previsit-thinking-spec/
├── README.md
├── VERSION
├── VERSIONING.md
├── CHANGELOG.md
├── scripts/
│   └── bump_version.py
├── core/
│   ├── README.md
│   ├── THINKING_SPEC.md
│   ├── DEEP_CULTIVATION_SYSTEM_POSITIONING.md
│   ├── ASSERTIVE_WRITING_POLICY.md
│   ├── DESIGN_PHILOSOPHY.md
│   ├── WORKFLOW_LOGIC.md
│   ├── SAFETY_BOUNDARY.md
│   ├── EVALUATION.md
│   ├── TRADEOFF_ANALYSIS.md
│   ├── FAILURE_ANALYSIS.md
│   └── EVOLUTION_PATH.md
├── clinical-question-governance/
│   ├── README.md
│   ├── clinical_question_governance.md
│   ├── question_candidates_matrix.md
│   ├── doctor_needs.md
│   ├── nurse_needs.md
│   ├── mvp_question_set_recommendation.md
│   └── source_evidence_map.md
├── discovery/
│   ├── README.md
│   ├── NEXT_STEP.md
│   ├── DEEP_CULTIVATION_PROPOSAL_WRITING_GUIDE.md
│   ├── DISCOVERY_PROTOCOL.md
│   ├── MEETING_CAPTURE_TEMPLATE.md
│   ├── DECISION_RECORD_TEMPLATE.md
│   └── PAPER_PATENT_PRODUCT_EXTRACTION.md
├── subprojects/
│   ├── README.md
│   └── subproject-3-wu-chiang-sarcopenia-ai-robot/
├── records/
│   ├── README.md
│   ├── 2026-04-23/
│   ├── 2026-05-03/
│   ├── 2026-05-12/
│   └── 2026-05-19/
└── meta/
    ├── assumptions.md
    ├── constraints.md
    ├── open_questions.md
    └── repo_architecture_review.md
```

## Folder Responsibilities

- `core/`: stable system logic. Use this when checking product intent, workflow boundaries, safety philosophy, evaluation logic, and evolution rules.
- `clinical-question-governance/`: evidence-based question governance. Use this when deciding which urology previsit questions belong in MVP, conditional modules, family/source-labeled support, nurse repair, or clinician-only workflows.
- `discovery/`: meeting and review operating pack. Use this before and after physician/nurse conversations.
- `subprojects/`: parent-proposal companion subproject routing. Use this to keep non-urology deep-cultivation lanes separate while preserving source context and coordination questions.
- `records/`: dated evidence trail. Use this for specific meeting briefs, captures, decision records, and extraction notes.
- `meta/`: assumptions, constraints, open questions, and repository-level architecture review.

## Source Relationship

This repository is a sibling of `planning-everything-track`.

It may read planning context as background, but it does not move, rename, rewrite, or replace files in `planning-everything-track`.

The separate demo repository, `urology-ai-previsit-demo`, owns implementation, UI, synthetic cases, tests, and demo artifacts. This repository owns the reasoning and governance that should constrain that demo.

Current architecture decision: keep the thinking/governance repo and demo repo separate. The rationale and revisit criteria are recorded in `meta/repo_architecture_review.md`.

## Current Useful Reading Paths

- For the current repository version: `VERSION`
- For version update rules and release criteria: `VERSIONING.md`
- For version history: `CHANGELOG.md`
- For a full non-technical system spec: `core/THINKING_SPEC.md`
- For the Health Taiwan deep-cultivation system positioning: `core/DEEP_CULTIVATION_SYSTEM_POSITIONING.md`
- For the repo-wide confident / non-defensive writing policy: `core/ASSERTIVE_WRITING_POLICY.md`
- For writing the Health Taiwan deep-cultivation proposal: `discovery/DEEP_CULTIVATION_PROPOSAL_WRITING_GUIDE.md`
- For the 2026-05-21 A2-0048 precedent proposal capture and postdoctoral lessons: `records/2026-05-21/a2-0048-smart-healthcare-center-precedent/README.md`
- For the 2026-05-29 Prof. Wu proposal update and reference-proposal analysis: `records/2026-05-29/README.md`
- For the historical 2026-06-02 信義 integrated PSA / AI 智慧問診 / CRM responsibility clarification, superseded for current scope by the 2026-06-19 owner update: `records/2026-06-02/README.md`
- For the 2026-06-12 吳岳霖主任 LINE conversation and 美如主任 group screenshot, now updated by the 2026-06-19 owner decision that CRM is completely out of scope for Jason / 陽明交大: `records/2026-06-12/README.md`
- For the 吳育德 + 江慧珣 `深耕子計畫三` companion lane on 高齡 AI 步態、肌少症、數位復健與陪伴機器人: `subprojects/subproject-3-wu-chiang-sarcopenia-ai-robot/README.md`
- For the full source-based 子計畫三 content analysis and cross-lane connection map: `subprojects/subproject-3-wu-chiang-sarcopenia-ai-robot/full-content-analysis-and-connection-map.md`
- For the 2026-06-11 子計畫三 verified corrected meeting analysis, KPI/Robot/budget refinement, and cross-lane connection update: `subprojects/subproject-3-wu-chiang-sarcopenia-ai-robot/meeting-analysis-2026-06-11.md`
- For the 2026-06-02 to 2026-06-11 LINE group capture for `深耕子計劃三-吳育德+江慧珣團隊`: `records/2026-06-11/README.md`
- For the pre-circulation assertive writing gate: `discovery/ASSERTIVE_WRITING_GATE.md`
- For the current 2026-06-19 AI-only expert-review packet: `discovery/exports/nycu-ai-previsit-expert-review-packet-2026-06-19.md`
- For the current proposal item definitions based on 廖醫師 PSA format: `discovery/exports/nycu-ai-previsit-proposal-item-definitions-2026-06-19.md`
- For the current KPI-to-budget table: `discovery/DEEP_CULTIVATION_KPI_TO_BUDGET_TABLE.md`
- For the historical v0.7 Word-export source and docx package: `discovery/exports/deep-cultivation-urology-previsit-v0.7-working-discussion-proposal.md` and `discovery/exports/deep-cultivation-urology-previsit-v0.7-working-discussion-proposal.docx`
- For the prior v0.6 fill-out discussion draft with category design, KPI targets, formal budget columns, and front-loaded governance: `discovery/DEEP_CULTIVATION_APPLICATION_DRAFT_V0_6.md`
- For the prior 2026-06-02 discussion draft with NT$10,000,000 three-year budget control: `discovery/DEEP_CULTIVATION_APPLICATION_DRAFT_V0_5.md`
- For the prior precedent-integrated official-package application draft v0.4: `discovery/DEEP_CULTIVATION_APPLICATION_DRAFT_V0_4.md`
- For the prior official-format application draft v0.3: `discovery/DEEP_CULTIVATION_APPLICATION_DRAFT_V0_3.md`
- For the dated implementation record of the assertive writing update: `records/2026-05-20/assertive-writing-implementation-record.md`
- For mapping the official Health Taiwan format to our draft package: `discovery/DEEP_CULTIVATION_OFFICIAL_FORMAT_CROSSWALK.md`
- For the intended-use freeze: `discovery/INTENDED_USE_FREEZE.md`
- For the demo scope freeze: `discovery/DEMO_SCOPE_FREEZE.md`
- For the postdoctoral next-step strategy review for Health Taiwan proposal design: `discovery/DEEP_CULTIVATION_POSTDOC_NEXT_STEP_REVIEW.md`
- For the clinical friction and workforce-burden reduction analysis: `discovery/CLINICAL_FRICTION_REDUCTION_ANALYSIS.md`
- For the prior official-format subproject draft v0.1: `discovery/DEEP_CULTIVATION_SUBPROJECT_UROLOGY_PREVISIT_V0_1.md`
- For KPI-to-budget mapping: `discovery/DEEP_CULTIVATION_KPI_TO_BUDGET_TABLE.md`
- For the integrated KPI / budget / annual-checkpoint proposal table: `discovery/DEEP_CULTIVATION_KPI_BUDGET_ANNUAL_INTEGRATION_TABLE.md`
- For AI / cybersecurity / data governance prep: `discovery/DEEP_CULTIVATION_GOVERNANCE_CHECKLIST.md`
- For annual checkpoint planning: `discovery/DEEP_CULTIVATION_ANNUAL_CHECKPOINT_TABLE.md`
- For scoring a Health Taiwan deep-cultivation draft objectively: `discovery/DEEP_CULTIVATION_SCORING_RUBRIC.md`
- For the expanded MOHW format/application-compliance score: `discovery/DEEP_CULTIVATION_MOHW_COMPLIANCE_RUBRIC.md`
- For safety boundaries: `core/SAFETY_BOUNDARY.md`
- For clinical question governance: `clinical-question-governance/clinical_question_governance.md`
- For the candidate question matrix: `clinical-question-governance/question_candidates_matrix.md`
- For the recommended MVP question set: `clinical-question-governance/mvp_question_set_recommendation.md`
- For the next physician/nurse discovery conversation: `discovery/NEXT_STEP.md`
- For the 2026-05-03 urgent-care AI triage future-direction signal: `records/2026-05-03/yu-urgent-care-ai-triage-reference.md`
- For the 2026-05-19 local ASR-ready adaptive demo readiness record: `records/2026-05-19/demo-asr-readiness-record.md`
- For the 2026-05-19 北市聯醫 deep-cultivation meeting transcript: `records/2026-05-19/taipei-city-hospital-deep-cultivation-meeting-transcript.md`
- For the 2026-05-19 北市聯醫 concise summary and strategic signal: `records/2026-05-19/deep-cultivation-summary-and-signals.md`
- For the official Health Taiwan Deep-Cultivation policy reference: `records/2026-05-19/health-taiwan-deep-cultivation-policy-reference.md`
- For the downloaded official Health Taiwan policy document archive: `records/2026-05-19/policy-documents/README.md`
- For related Health Taiwan examples and proposal patterns: `records/2026-05-19/health-taiwan-related-examples.md`
- For the external `萬小芳` smart-hospital assistant benchmark and postdoctoral clinical AI governance addendum: `records/2026-05-19/wanxiaofang-benchmark-note.md`
- For whether to include this repo and the demo repo in the proposal: `records/2026-05-19/repo-inclusion-recommendation.md`
- For the imported 北市聯醫 deep-cultivation working note: `records/2026-05-19/taipei-city-hospital-deep-cultivation-working-note.md`
- For the 2026-05-19 deep-cultivation decision and CRM/service-flow framing: `records/2026-05-19/deep-cultivation-decision-record.md`
- For the standalone CRM / PRM / HIS / EMR concept note, not linked to current scope: `records/2026-05-19/crm-prm-concept-note.md`
- For the 2026-05-19 expert-review narrowing decision: `records/2026-05-19/expert-review-revise-and-narrow.md`
- For 陳美如主任's stakeholder introduction and likely proposal-review priorities: `records/2026-05-19/chen-meiru-stakeholder-profile.md`
- For repository architecture decisions: `meta/repo_architecture_review.md`
- For the 2026-05-19 deep-cultivation repo-routing decision:
  `records/2026-05-19/deep-cultivation-repo-routing.md`

## Current Planning Signal

The latest effective planning decision is the 2026-06-19 owner update: CRM is
completely out of scope for Jason / 陽明交大. The 2026-06-12 LINE conversation and
美如主任 group screenshot remain source evidence for why CRM was removed.

Current active gate:

```text
v0.8 AI 問診與醫師覆核摘要 package planning
```

Current project definition:

```text
泌尿科門診前問診與醫師覆核摘要支持系統
```

The active assignment is now AI-only:

- Jason / 陽明交大 owns AI 智慧問診, one-page physician-review summary, governance, KPI, and budget planning for this package.
- 忠孝院區泌尿科 PSA 主動篩檢 can remain clinical context or parent-proposal sibling content, but its SOP and clinical responsibility are not Jason-owned.
- CRM is out of scope: no CRM planning, no CRM data handoff, no CRM budget, no CRM KPI, no CRM team coordination.

Current source records:

- `records/2026-06-11/wu-chiang-subproject-three-line-record.md`
- `records/2026-06-12/wu-yuelin-line-crm-888-record.md`
- `records/2026-06-02/xinyi-integrated-psa-ai-crm-responsibility-record.md`
- `records/2026-06-02/xinyi-integrated-psa-ai-crm-v0.8-next-step-plan.md`

The latest prior proposal-package evidence is the 2026-05-29 Prof. Wu follow-up
meeting and the v0.7 discussion package.

The latest expert-review decision after that meeting is `Revise + Narrow`.

Current proposal name:

```text
泌尿科門診前問診與醫師覆核摘要支持系統
```

Safe descriptive boundary:

```text
泌尿科門診前症狀蒐集與醫師覆核摘要輔助流程
```

Near-term framing should emphasize:

- CRM and 三高防治888 / 大公衛 CRM-side policy framing are historical context only
  for this package; do not turn them into Jason / 陽明交大 deliverables
- the 2026-06-19 owner update changes ownership: Jason / 陽明交大 should design
  AI 問診 and physician-review summary only
- a separate `深耕子計劃三-吳育德+江慧珣團隊` lane now has its own routing
  section under `subprojects/`; it appears to focus on high-age AI gait,
  sarcopenia risk screening, digital rehabilitation, and companion/simple robot
  planning, and should not be merged into the urology AI-only package unless
  explicitly assigned by the parent proposal owner
- copied 子計畫三 source attachments now support a stronger connection map:
  use the NT$17.5M/year service-policy draft as the primary proposal-facing
  frame, the NT$18M/year research draft as methods/validation support, and the
  AI Robot deck as smart-terminal / Robot feasibility context
- the 2026-06-11 verified corrected meeting record narrows 子計畫三 execution:
  Robot should start as health-service-center / community-center onsite support,
  KPI should be scenario-based around per-event throughput, high-risk model
  validation may need long-term-care or nursing-home enrichment, and budget
  revision should move room toward personnel, case management, Robot integration,
  and APP / Dashboard follow-up operations
- the v0.8 package should stand on AI 問診, physician-review summary, workflow fit, governance, and KPI-to-budget traceability
- PSA budget and SOP remain clinical / parent-proposal matters; use PSA only as possible clinical context unless explicitly reassigned
- AI 智慧問診與醫師覆核摘要 uses NT$10,000,000 as the current three-year planning envelope until the parent proposal owner changes it
- v0.7 is now the prior baseline for the AI 智慧問診 / one-page-summary component; v0.8 planning must update the project identity before a new Word export
- the 2026-06-02 discussion version now uses a three-year NT$10,000,000 working budget, maps every budget line to KPI / owner / evidence / checkpoint, and stays within a 20-page discussion cap
- the 2026-05-29 attached subproject-three PDF is archived and analyzed as a formatting / KPI / budget precedent, not as scope-expansion authority
- urology previsit symptom collection and clinician-review summary as the current system role
- primary Health Taiwan fit under `範疇三：導入智慧科技醫療`, with `範疇一：優化醫療工作條件` as secondary support
- first-version narrowing to non-acute LUTS / OAB-like outpatients: nocturia, frequency, urgency, leakage, voiding difficulty, or weak stream
- after-registration / waiting-room QR code or tablet completion by patient or family as the first workflow hypothesis
- partial summary is acceptable if the patient does not finish every field
- CRM follow-up was parked in the v0.7 baseline; after the 2026-06-19 update, CRM is excluded entirely from this package
- ASR remains an optional multilingual input layer, not the core clinical claim
- SOAP / EMR wording must stay as `醫師覆核用 SOAP 架構參考摘要`; no automatic EMR writeback or formal medical-record generation
- blood in urine, fever/chills, flank pain, and currently being unable to urinate are `patient-reported red-flag observations`, not triage or risk judgments
- APP, AI, ASR, kiosk, API, and reminders as workflow tools, not autonomous clinical decision tools
- proposal writing should start from clinical workflow pain, service landing, KPI, governance, and budget mapping, not from model novelty
- clinical friction reduction is a first-class Health Taiwan proposal criterion: the system must reduce physician/nurse/clinic-staff burden and must not turn clinicians into AI labelers or extra-workflow operators
- all article, proposal, paper, lab-brief, and reviewer-facing writing must follow `core/ASSERTIVE_WRITING_POLICY.md`: confident, direct, and non-defensive, with safety boundaries written as deliberate design choices rather than apologies
- the 2026-05-20 postdoctoral next-step review recommends freezing intended use, freezing demo scope, preparing reviewer evidence, defining governance gates, and mapping KPI to budget before adding more AI features
- the 2026-05-20 execution step created application-drafting artifacts: intended-use freeze, demo-scope freeze, application draft v0.2, KPI-to-budget table, governance checklist, and annual checkpoint table
- the 2026-05-20 format-alignment step promoted the proposal-writing package to v0.3 with an official-format crosswalk and KPI / budget / annual-checkpoint integration table
- the 2026-05-21 precedent-integration step promoted the proposal-writing package to v0.4 by learning the A2-0048 proposal's official-format discipline while preserving the narrow urology previsit scope
- the 2026-05-29 Prof. Wu follow-up promoted the discussion package to v0.5 by fixing the working budget at three years / NT$10,000,000, requiring KPI-linked budget lines, and enforcing a 20-page discussion draft
- the 2026-05-31 fill-out design update promoted the discussion package to v0.6 by making `範疇三：導入智慧科技醫療` the primary category, `範疇一：優化醫療工作條件` the secondary support category, using verifiable KPI targets, adding formal budget fill-out columns, and moving governance before KPI and budget
- the 2026-06-01 v0.7 update promotes the active Word-export package by removing subproject-three wording from the delivered proposal text, making the 118-year milestone concrete, and keeping HIS/EMR/EHR writeback for a second-version system-integration and governance-confirmation step
- the official policy/rule archive now lives under `records/2026-05-19/policy-documents/`
- draft scoring should use the four independent 100-point layers in `discovery/DEEP_CULTIVATION_SCORING_RUBRIC.md`, including the MOHW format-compliance layer before formal submission
- the expanded D-layer rubric in `discovery/DEEP_CULTIVATION_MOHW_COMPLIANCE_RUBRIC.md` should be treated as a source-freshness and official-format preflight, not just an administrative checklist
- Aging Clock as research-adjacent until the data source, aging definition, biomarker scope, intervention, and service fit are clarified
- the concise strategic label may remain `AI Systems Engineering for Healthcare Deployment`, but the concrete proposal label should be `泌尿科門診前問診與醫師覆核摘要支持系統`
- policy alignment with `健康台灣深耕計畫(114-118年)`: smart healthcare, working-condition improvement, talent training, and sustainable/social-responsibility healthcare
- related examples support the pattern: workflow improvement, staff-burden reduction, AI as a tool, system integration, governance, and KPI
- 陳美如主任's stakeholder lens should be treated as a service-system review lens: real workflow landing, staff burden, cross-system continuity, governance, KPI, budget-to-owner mapping, and sustainable operations matter more than model novelty

This does not change the core safety boundary: no diagnosis, no treatment advice, no autonomous triage, no real patient data during discovery, and no HIS/EMR/EHR integration without separate governance.

The accepted system-positioning supplement is `core/DEEP_CULTIVATION_SYSTEM_POSITIONING.md`. Use it when updating the sibling `urology-ai-previsit-demo` repo or drafting the June 2 deep-cultivation subproject, especially to avoid drifting from previsit support into AI triage claims.

## Writing Rule

All outward-facing writing in this repo must be assertive and non-defensive.

Safety boundaries remain mandatory, but they should be framed as mature architecture:

```text
Clinical authority remains with clinicians by design.
```

not:

```text
The system cannot make clinical decisions.
```

Use `core/ASSERTIVE_WRITING_POLICY.md` before drafting articles, proposals, paper framing, reviewer briefs, lab briefs, or project positioning.

Use `discovery/ASSERTIVE_WRITING_GATE.md` before circulating any section to a teacher, hospital reviewer, or proposal owner.

## Versioning Rule

This repository uses governed semantic versioning:

```text
vMAJOR.MINOR.PATCH
```

The current source of truth is `VERSION`. Detailed rules are in `VERSIONING.md`.

Use the automated bump script:

```bash
python3 scripts/bump_version.py --part patch --summary "Short update summary"
```

Use `patch` for wording, index, source-capture and navigation changes; `minor` for compatible proposal/governance/evaluation additions; `major` for first formal proposal freeze or any change to intended use, clinical boundary, real patient data, HIS/EMR integration, diagnosis, treatment, triage or queue-priority scope.

## Operating Rule

The first useful version should be modest, reviewable, and safe:

1. collect repeated, high-value previsit information
2. repair missing information before handoff
3. let the patient or helper review a patient-facing confirmation
4. give clinic staff a separate missing-information repair workbench when needed
5. preserve answer source when family or nurse input is involved
6. produce a short clinician-review summary
7. leave interpretation and action with the clinician

## Redundancy Rule

Some overlap is intentional:

- `core/THINKING_SPEC.md` is the integrated master narrative.
- Files under `core/` split the master narrative into reviewable dimensions.
- Files under `clinical-question-governance/` are not a replacement for `core/`; they apply the safety and workflow logic to concrete clinical questions.
- Files under `discovery/` are operating templates, not source-of-truth clinical evidence.
- `records/` keeps dated evidence and should not be rewritten into evergreen doctrine unless a decision is accepted.

Avoid adding new root-level Markdown files unless they are entrypoints. New substantive documents should go into `core/`, `clinical-question-governance/`, `discovery/`, `records/`, or `meta/`.

## Audit Rule

Any future change should answer four questions:

1. Does this reduce workflow friction without adding hidden burden?
2. Does this preserve clinician authority?
3. Does this avoid real patient data unless governance is explicit?
4. Does this make the next decision clearer?
