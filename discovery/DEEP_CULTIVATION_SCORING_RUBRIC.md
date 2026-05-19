# Deep-Cultivation Proposal Scoring Rubric

Status: working rubric

## Purpose

This rubric defines a four-layer, evidence-required scoring system for Health Taiwan Deep-Cultivation proposals.

It is designed to reduce impression-based review. A reviewer should not give points because a proposal "sounds innovative"; points should be tied to visible evidence in the proposal, official document requirements, workflow diagrams, KPI tables, governance artifacts, or executable prototype evidence.

## Source Basis

Use this rubric with the local official archive:

- `../records/2026-05-19/policy-documents/README.md`
- `../records/2026-05-19/policy-documents/manifest.md`

Core official files behind this rubric:

- `application/health-taiwan-phase1-application-guidelines.pdf`
- `application/health-taiwan-phase1-proposal-format-114-115-0909.docx`
- `application/health-taiwan-deep-cultivation-approved-plan-1140227.pdf`
- `execution/category3-smart-healthcare-governance-lazy-guide-1140702.pdf`
- `execution/ai-governance-self-checklist.docx`
- `execution/cybersecurity-governance-self-checklist.docx`
- `execution/data-governance-self-checklist.docx`
- `budget/funding-use-principles-1140922.pdf`
- `budget/funding-standards-second-revision-1150413.pdf`
- `qa/health-taiwan-qa-1140710.pdf`
- `qa/health-taiwan-procurement-qa-updated.pdf`

Program-case pattern references:

- `../records/2026-05-19/health-taiwan-related-examples.md`
- `../records/2026-05-19/health-taiwan-deep-cultivation-policy-reference.md`

Live source spot-check, 2026-05-19:

| Live source | What it confirms | Rubric use |
| --- | --- | --- |
| MOHW Health Taiwan Deep-Cultivation special page, `https://dep.mohw.gov.tw/tdu/cp-1567-82709-121.html` | Four program scopes, 18 goals, and scope 3 goals including AI-assisted clinical care, workflow efficiency, medical data sharing/security, and smart hospitals. | Supports A2, A8, B11, C1-C3, C7, and D-source refresh. |
| HTSprout plan page, `https://htsprout.nhri.org.tw/dhplan.html` | The plan asks applicants to deep-dig system problems, propose concrete strategies, define performance indicators, and keep a long-term deep-cultivation view. | Supports evidence-required scoring instead of idea-only scoring. |
| MOHW 2026-04-27 outcome news, `https://mohw.gov.tw/cp-2704-86226-1.html` | Public examples include nursing voice AI, e-paper bedside cards, smart medication cabinets, mobile/field services, FHIR data exchange, and AI imaging centers. | Calibrates workflow, burden reduction, deployment, interoperability, and sustainability patterns. |
| Health Taiwan scope-3 smart-healthcare guide, `https://htsprout.nhri.org.tw/UploadFile/HDPlan_fund_1140702_17.pdf` | Scope 3 writing should explicitly address cybersecurity governance, data governance, AI governance, and FHIR/TW Core IG integration. | Supports C1, C2, C3, C7, D9, and cross-layer caps. |

For formal submission, refresh these live pages and the HTSprout download page again. The local archive is the working evidence base, not a substitute for the latest official template.

## Case-Derived Calibration

The score weights are calibrated from public Health Taiwan / deep-cultivation examples and official smart-healthcare guidance. The goal is not to copy another hospital's project. The goal is to extract what reviewers and program designers repeatedly reward: workflow value, staff-burden reduction, service deployment, governance, interoperability, and measurable outcomes.

| Public pattern | What it shows | Rubric impact |
| --- | --- | --- |
| MOHW-reported nursing voice AI assistant, e-paper bedside card, and smart medication cabinet | AI and digital tools are strongest when they reduce clinical documentation, handoff, medication, or nursing burden. | Raises the weight of A4 staff-burden reduction, A8 KPI, B5 summary/handoff quality, and C3 AI governance. |
| Official plan guidance on voice AI, clinical-record drafting, workflow efficiency, data sharing/security, and smart hospitals | Official direction favors workflow automation and governed smart-healthcare infrastructure rather than standalone model novelty. | Justifies the A/B/C split and the rule that AI methods cannot substitute for workflow mapping. |
| Tainan Municipal Hospital ALL-IN-ONE mobile smart-healthcare service pattern | Strong cases combine field deployment, community care, telecare, chronic-disease management, data exchange, and service tracking. | Raises the weight of A3 workflow, A10 stakeholder value, B11 interoperability readiness, C8 deployment plan, and C10 scale. |
| Jen-Ai / Mercy Hospital AI imaging + HIS + health app + green-hospital pattern | AI is paired with information-system modernization, patient-facing app support, operational integration, and measurable sustainability outcomes. | Supports scoring AI together with integration, KPI, hospital-management value, and ESG/sustainability alignment. |
| MOHW AI Center guidance on cybersecurity governance, data governance, AI governance, FHIR, and TW Core IG | Governance is a core requirement for smart-healthcare maturity, not an appendix. | Raises the weight of C1, C2, C3, C7, and D9. |

Scoring implication:

```text
High scores require evidence that the proposal improves a real healthcare workflow.
An AI model, demo screen, or technical architecture without workflow, governance, KPI,
and official-format compliance must be capped even if the technology looks impressive.
```

## Four Independent 100-Point Layers

| Layer | Name | Core Question |
| --- | --- | --- |
| A | Clinical Value And Workflow Integration | Does the hospital or clinical workflow truly need this? |
| B | Technical System And AI Engineering | Can this system be built, tested, and maintained realistically? |
| C | Governance, Security, Regulation, And Sustainability | Can this safely move toward real deployment? |
| D | MOHW Format Compliance And Application Completeness | Will it satisfy official submission rules, format, attachments, budget, and reporting requirements? |

Do not average away failure. Use gate-based review:

| Condition | Recommendation |
| --- | --- |
| Any layer below 60 | Do not pass. |
| Any layer 60-69 | Revise and resubmit. |
| All layers >=70 | Eligible for PoC-level review. |
| All layers >=80 | Eligible for pilot planning. |
| All layers >=90 | High-maturity demonstration candidate. |
| D below 70 | Do not submit yet, even if A/B/C are strong; administrative risk is too high. |

## Evidence Requirement

Every scored item should cite one of:

- proposal page or section
- table number
- workflow diagram
- KPI table
- budget table
- official form/checklist
- policy document
- prototype screenshot or demo route
- test/readiness result
- governance artifact

Reviewer comment rule:

```text
No comment, no high score.
```

For any subscore above 80% of its maximum, the reviewer should state what evidence supports the score.

## Evidence-Capped Scoring

Each subitem has a maximum score based on the evidence level available. This prevents reviewers from awarding full points because a sentence sounds persuasive.

| Evidence level | Description | Maximum credit for that subitem |
| --- | --- | ---: |
| E0 | No evidence. | 0% |
| E1 | Claim only. The proposal says it will do something but gives no artifact, source, plan, or owner. | 40% |
| E2 | Design artifact. A diagram, table, SOP draft, schema, mockup, role map, or governance draft exists. | 70% |
| E3 | Measured or tested evidence. Baseline, simulation result, prototype test, clinician review, run log, or pilot-like rehearsal exists. | 90% |
| E4 | Governed external evidence. IRB-approved data, hospital-approved workflow, signed partner evidence, procurement-ready spec, or formal governance review exists. | 100% |

Example:

```text
If a proposal claims "SOAP drafting time will decrease" but has no baseline or
measurement plan, A8-2 is capped at E1 even if the wording is strong.
```

## First-Principles Review Model For A/B/C

For every proposal claim, reduce the claim to five questions before assigning points:

| Question | Why it matters | Evidence expected |
| --- | --- | --- |
| What healthcare operation changes? | Prevents scoring a generic AI feature as clinical value. | Before/after workflow, service map, role map, SOP, or visit flow. |
| Who changes behavior? | Prevents assuming adoption without user burden analysis. | Patient, physician, nurse, admin, case manager, IT/security, and management role table. |
| What measurable state improves? | Prevents adjective-only KPI such as "better" or "more efficient". | Baseline, numerator/denominator, target, measurement window, and data owner. |
| What can fail or harm patients/workflow? | Forces review of AI, system, security, data, and clinical-safety risks. | Failure mode table, fallback SOP, escalation rule, audit log, or risk register. |
| Who owns the system after launch? | Separates pilot theater from operational deployment. | Maintenance owner, budget owner, governance committee, update process, and training plan. |

If a proposal cannot answer these five questions with evidence, do not award high A/B/C scores even if the technology is impressive.

## A/B/C Cross-Validation Gates

The three content layers must be scored independently, then cross-checked. A high score in one layer cannot compensate for missing evidence in another layer.

| Gate | Required evidence | Related criteria | Cap if missing |
| --- | --- | --- | --- |
| Clinical workflow gate | Before workflow, after workflow, role interaction, data flow, human review point, and exception flow. | A3, A4, A6, A7, B3, C4 | A capped at 69; B capped at 79 if workflow assumptions drive architecture. |
| KPI gate | Baseline or baseline-collection plan, formula, annual target, owner, and review cadence. | A8, A9, B10, C10, D6 | A capped at 79; D penalties apply if official KPI table is incomplete. |
| Human-in-the-loop gate | Clinician review, edit/reject path, responsibility boundary, and no autonomous diagnosis claim. | A6, A7, B3, B5, C3, C4, C6 | A -10 and C -10; C capped at 79 for any clinical-output system. |
| AI safety gate | Hallucination control, missing-data handling, low-confidence labeling, versioning, and serious-error reporting. | B3, B7, B10, C3, C4, C11 | B capped at 79; C capped at 79. |
| Data/security gate | Consent or IRB path, de-identification, retention, RBAC, access log, incident response, and use limitation. | C1, C2, C5, C7, D9 | C capped at 59 if patient data use is claimed without legal/data-governance path. |
| Interoperability gate | EMR/HIS touchpoint boundary, FHIR/TW Core IG awareness, integration risk, and non-overclaim. | B11, C7, D9 | B -5 and C -5 where data-sharing or cross-site claims are made. |
| Deployment gate | Site, timeline, owner, training, maintenance, budget, and exit/degrade path. | A9, A10, B8, B12, C8, C9, C10 | C capped at 69 if the proposal cannot name a pilot field, owner, or maintenance plan. |

Gate interpretation:

```text
A/B/C are not a weighted average of impressions.
They are three independent maturity tests that must agree with each other.
```

## Layer-Level Score Caps

Use these caps after item-level scoring. The cap is applied to the final layer score, not to a single row.

| Layer | Cap trigger | Maximum score |
| --- | --- | ---: |
| A | No named clinical site, user group, or workflow pain. | 59 |
| A | No before/after workflow map. | 69 |
| A | KPI are only adjectives or slogans. | 79 |
| A | Workflow depends on clinicians or nurses doing significant new work that is not acknowledged. | 79 |
| B | Architecture is only a model, chatbot, or demo screen. | 69 |
| B | No fallback for ASR/model/system failure. | 79 |
| B | No explicit AI task boundary or output schema. | 79 |
| B | Hardware, latency, or integration assumptions are incompatible with a realistic hospital setting. | 69 |
| C | Uses identifiable or real patient data without consent/IRB/de-identification/use-limitation path. | 59 |
| C | Scope 3 smart-healthcare proposal omits cybersecurity, data, or AI governance. | 69 |
| C | Clinical output exists but no physician override/edit/reject/audit path is defined. | 79 |
| C | Claims autonomous diagnosis, treatment, or clinician replacement. | 59, and apply penalty. |

Caps should be documented in the final review. A reviewer may give a lower score than the cap, but cannot exceed it without evidence that removes the trigger.

## Reviewer Micro-Comment Requirement

For every criterion, reviewers should record:

```text
Criterion:
Raw score:
Evidence level: E0 / E1 / E2 / E3 / E4
Evidence pointer:
Cap trigger, if any:
Why the score is not higher:
Specific artifact needed to raise the score:
```

This forces the review to name artifacts, not impressions.

## Urology Previsit / CRM-Screening Interpretation

For this repository's likely proposal direction, do not score the system as an autonomous triage or diagnosis system unless that scope is explicitly added and governed. Score the urology proposal as a governed service-flow and visit-readiness system:

| Proposal component | Strong scoring interpretation | Weak scoring interpretation |
| --- | --- | --- |
| PSA / community screening | Entry point into a governed follow-up and return-to-hospital workflow. | A disconnected screening activity with no CRM or clinician-review loop. |
| Adaptive intake | Reduces repeated history-taking and captures missing fields before the visit. | A chatbot framed as a diagnosis engine. |
| ASR / voice input | Low-friction input and staff-burden reduction, especially for older adults or assisted workflows. | Voice interface novelty with no workflow slot. |
| Summary / SOAP-like draft | Clinician-reviewed draft support with visible missing fields and uncertainty. | Final medical record or plan generated by AI. |
| CRM follow-up | Service backbone for reminders, case management, return visit, and completion tracking. | Marketing-style CRM wording without patient-flow accountability. |
| FHIR / TW Core IG | Future interoperability readiness and data-governance design. | Overclaimed live HIS/EMR integration without permission, security, or owner. |

## Reviewer Evidence Card

For each high score, reviewers should be able to fill this card:

```text
Criterion:
Score:
Evidence level: E0 / E1 / E2 / E3 / E4
Evidence pointer: page / section / table / figure / file / source
Why this score is justified:
What would raise the score:
What would lower or cap the score:
```

## Not-Applicable Handling

Some proposals are intentionally bounded. For example, the current urology previsit system is not an AI triage system and should not be penalized for lacking autonomous triage. If a criterion is not applicable because the proposal explicitly excludes that scope, score the related item by boundary clarity and safe exclusion.

Example:

```text
If triage is not in scope, evaluate whether the proposal avoids triage claims and defines clinician escalation boundaries.
```

Do not reward a proposal for adding unsafe scope just to satisfy a rubric item.

# A. Clinical Value And Workflow Integration: 100

## A1. Clinical Pain Definition: 10

Scoring intent: A1 should answer why this clinical service problem exists before any AI method is introduced. A proposal that starts from a model capability and then searches for a clinical use case should be scored low here.

| Item | Points | Standard |
| --- | ---: | --- |
| A1-1 Specific clinical field / site / patient group | 2 | Names the department, setting, and target users. |
| A1-2 Specific workflow pain | 2 | Describes concrete pain, not generic efficiency language. |
| A1-3 Affected roles | 2 | Identifies patient, physician, nurse, admin, and/or management impact. |
| A1-4 Quantified or semi-quantified evidence | 2 | Uses baseline volume, time, workload, waiting, error, or follow-up data. |
| A1-5 Urgency / consequence | 2 | Explains why delay matters. |

Low-score signal: "AI can improve healthcare" without a local workflow problem.

## A2. Policy And Clinical Need Alignment: 8

Scoring intent: A2 is not a citation-counting item. The proposal must show how the project operationalizes the official direction: smarter clinical care, reduced workload, workflow efficiency, data safety, and sustainable service improvement.

| Item | Points | Standard |
| --- | ---: | --- |
| A2-1 Smart healthcare alignment | 2 | Maps to `導入智慧科技醫療`. |
| A2-2 Working-condition improvement | 2 | Shows workload reduction or work-environment improvement. |
| A2-3 Workflow efficiency | 2 | Shows improved clinical process, not only software use. |
| A2-4 Medical data sharing / safety awareness | 2 | Addresses data security and governed sharing. |

## A3. Before / After Workflow: 12

Scoring intent: A3 is the main anti-impression criterion. If the reviewer cannot trace patient, staff, clinician, system, and data movement through the proposed workflow, the proposal is not yet deployment-ready.

| Item | Points | Standard |
| --- | ---: | --- |
| A3-1 Before workflow | 2 | Current process is clearly mapped. |
| A3-2 After workflow | 2 | Proposed process is clearly mapped. |
| A3-3 Role interaction | 2 | Shows who does what and when. |
| A3-4 Data flow | 2 | Shows what data is collected, transformed, reviewed, and stored. |
| A3-5 Human review point | 2 | Shows where clinician or staff review occurs. |
| A3-6 Exception flow | 2 | Handles patient inability, missing data, ASR failure, system failure, or high-risk uncertainty. |

High-score standard: hospital staff can understand the workflow without an engineering explanation.

## A4. Staff Burden Reduction Design: 10

Scoring intent: Staff-burden reduction must be scored as net burden, not feature count. A tool that generates summaries but adds extra logins, correction work, or duplicate data entry should lose points.

| Item | Points | Standard |
| --- | ---: | --- |
| A4-1 Reduces repeated questions | 2 | Collects repeated, safe previsit information earlier. |
| A4-2 Reduces documentation preparation | 2 | Produces summary or SOAP-like draft support for review. |
| A4-3 Reduces nursing/admin duplication | 2 | Avoids making staff re-enter the same data. |
| A4-4 Reduces information search cost | 2 | Presents structured context. |
| A4-5 Avoids hidden new burden | 2 | Does not add another tool with no workflow slot. |

## A5. Patient Usability: 8

Scoring intent: Patient usability is part of clinical feasibility. A previsit system that frail, older, anxious, low-literacy, or assisted patients cannot complete will not deliver the promised workflow value.

| Item | Points | Standard |
| --- | ---: | --- |
| A5-1 Plain-language questions | 2 | Patient-facing wording is understandable. |
| A5-2 Low-friction input | 1 | Supports reasonable text, click, voice, or assisted mode. |
| A5-3 Completion design | 2 | Uses bounded question count, progress, skip/unknown, or stopping logic. |
| A5-4 Older-adult / accessibility support | 2 | Accounts for font, language, helper, or staff-assisted mode. |
| A5-5 Privacy notice | 1 | Explains use and limits of data. |

## A6. Clinician Usability: 8

Scoring intent: Clinician usability is scored by fit with visit rhythm. The best evidence is not a pretty screen; it is a reviewer-facing summary that a clinician can quickly accept, correct, ignore, or escalate.

| Item | Points | Standard |
| --- | ---: | --- |
| A6-1 Rapid review | 2 | Summary readable in 30-60 seconds. |
| A6-2 Clinically useful ordering | 2 | Chief concern, missing fields, red-flag observations, and context are easy to find. |
| A6-3 Editable/rejectable output | 2 | Clinician can accept, modify, ignore, or reject. |
| A6-4 Visit rhythm fit | 2 | Does not force clinicians into an impractical tool path. |

## A7. Safety Flag / Escalation Boundary: 8

Scoring intent: This criterion rewards safe boundary design, not aggressive automation. A conservative escalation rule is stronger than an unsupported diagnosis or triage claim.

| Item | Points | Standard |
| --- | ---: | --- |
| A7-1 Safety flags are defined | 2 | Red-flag observations or escalation triggers have clear wording. |
| A7-2 Safety observations are visible | 2 | Important patient-reported findings are not buried. |
| A7-3 No autonomous diagnosis | 2 | The proposal does not convert observations into final medical conclusions. |
| A7-4 Conservative uncertainty handling | 2 | Unclear or concerning cases route to human review. |

For urology previsit scope, this replaces autonomous triage scoring.

## A8. Clinical KPI Design: 12

Scoring intent: A8 prevents vague value claims. Each KPI should have an owner, baseline or baseline-collection plan, formula, target, and review cadence.

| Item | Points | Standard |
| --- | ---: | --- |
| A8-1 Time metric | 2 | Measures previsit, review, or documentation time. |
| A8-2 Documentation metric | 2 | Measures summary/SOAP-like draft usefulness or preparation burden. |
| A8-3 Completion metric | 2 | Measures completion, abandonment, or assisted-use rate. |
| A8-4 Clinician satisfaction/usefulness | 2 | Uses Likert, SUS, adoption, or structured feedback. |
| A8-5 Output-use metric | 2 | Tracks accepted, edited, ignored, or rejected summaries. |
| A8-6 Safety KPI | 2 | Tracks unsafe claims, escalation misses, or mandatory human-review compliance. |

## A9. Clinical Evaluation Design: 12

Scoring intent: A9 asks whether the proposal can learn from deployment. High scores require a comparison structure and an error/improvement loop, not only a one-time demo.

| Item | Points | Standard |
| --- | ---: | --- |
| A9-1 Baseline | 2 | Has pre-intervention data or explicit baseline collection plan. |
| A9-2 Before/after comparison | 2 | Defines comparison design. |
| A9-3 User study | 2 | Includes clinician, nurse/staff, and/or patient feedback. |
| A9-4 Pilot setting | 2 | Names department/site, target users, and expected sample or encounter type. |
| A9-5 Error analysis | 2 | Defines error taxonomy and review owner. |
| A9-6 Improvement cycle | 2 | Has monthly/quarterly review and update mechanism. |

## A10. Cross-Stakeholder Value: 12

Scoring intent: High-maturity deep-cultivation proposals should create value for more than one role. A patient-only app or physician-only dashboard is weaker unless it explains why the broader workflow still improves.

| Item | Points | Standard |
| --- | ---: | --- |
| A10-1 Patient value | 3 | Less repetition, clearer preparation, better follow-up continuity. |
| A10-2 Physician value | 3 | Faster context review, less repeated history-taking. |
| A10-3 Nurse/staff value | 2 | Less repair/re-entry burden. |
| A10-4 Hospital management value | 2 | Better capacity, follow-up, or resource management. |
| A10-5 Policy value | 2 | Creates a smart-healthcare or service-flow model that can inform broader policy. |

# B. Technical System And AI Engineering: 100

## B1. Architecture Completeness: 10

Scoring intent: B1 checks whether the proposal is a system, not only an AI component. Architecture should expose enough surfaces for security, audit, monitoring, and maintenance to be assessed.

| Item | Points | Standard |
| --- | ---: | --- |
| B1-1 Patient-facing interface | 1 | Patient/helper entry point defined. |
| B1-2 Clinician/staff interface | 1 | Review or repair surfaces defined. |
| B1-3 Backend/API plan | 1 | Data and service boundary defined, if in scope. |
| B1-4 ASR/NLP/LLM module boundaries | 1 | Model tasks separated. |
| B1-5 Data store / record boundary | 1 | Storage or non-storage decision is explicit. |
| B1-6 Rules / question engine | 1 | Governed logic is explicit. |
| B1-7 Logging | 1 | Event/output logging defined. |
| B1-8 Monitoring | 1 | Error, latency, uptime, or adoption monitoring defined. |
| B1-9 Access control | 1 | Role boundary exists. |
| B1-10 Deployment environment | 1 | Local/server/cloud/edge assumptions stated. |

## B2. Technical Justification: 10

Scoring intent: Technical choices should be justified by clinical workflow, safety, privacy, latency, cost, and maintainability. "Latest model" is not a justification.

| Item | Points | Standard |
| --- | ---: | --- |
| B2-1 ASR justification | 2 | Tied to patient/staff burden, not novelty. |
| B2-2 LLM justification | 2 | Tied to summary or structure, not hype. |
| B2-3 RAG/rule justification | 2 | Tied to safety and source grounding. |
| B2-4 Embedding/question-selection justification | 2 | Tied to bounded adaptive questioning. |
| B2-5 Deployment justification | 2 | Tied to privacy, latency, cost, or hardware constraints. |

## B3. AI Task Boundary: 8

Scoring intent: B3 separates useful clinical-support automation from unsafe medical automation. The output boundary should be visible in product copy, workflow diagrams, and system schema.

| Item | Points | Standard |
| --- | ---: | --- |
| B3-1 AI responsibilities | 2 | Clear task list. |
| B3-2 AI non-responsibilities | 2 | No diagnosis, treatment, or autonomous triage unless separately governed. |
| B3-3 Human intervention points | 2 | Review and override are explicit. |
| B3-4 Output schema | 2 | Summary, JSON, SOAP-like draft, or other fixed output format is defined. |

## B4. Dynamic Questioning / Guided Intake: 8

Scoring intent: Dynamic questioning earns points only when it is bounded, explainable, and safer than a fixed questionnaire. It should stop when useful information is collected and escalate when risk or ambiguity appears.

| Item | Points | Standard |
| --- | ---: | --- |
| B4-1 Question-bank source | 2 | Based on clinician input, guideline, workflow, or governance source. |
| B4-2 Selection logic | 2 | Uses chief concern, answer state, missing fields, or safety observations. |
| B4-3 Stopping condition | 2 | Stops after enough useful information. |
| B4-4 Safety stop/escalation | 2 | Concerning or unclear answers route to human review. |

## B5. Summary / SOAP-Like Draft Quality: 8

Scoring intent: Summary quality is scored by clinical reviewability and boundary safety, not by length or fluency. Missing data and uncertainty should remain visible.

| Item | Points | Standard |
| --- | ---: | --- |
| B5-1 Subjective context | 2 | Chief concern, history, symptom timeline included. |
| B5-2 Objective context | 2 | Vitals/labs/PSA only included if governed and available. |
| B5-3 No over-diagnosis | 2 | Assessment language remains tentative or omitted when outside scope. |
| B5-4 Physician-editable plan | 2 | Plan is draft/reference only; no automatic orders. |

## B6. Optional Device / Vitals / PSA Integration: 8

Scoring intent: Device, vitals, PSA, or lab data should improve workflow meaning. Raw values without ownership, normal/abnormal handling, and missing-value treatment should not receive high points.

| Item | Points | Standard |
| --- | ---: | --- |
| B6-1 Field definition | 2 | Defines PSA, lab, vital sign, or device fields if in scope. |
| B6-2 Abnormal value handling | 2 | Uses governed thresholds or clinician review. |
| B6-3 Symptom/context linkage | 2 | Does not paste numbers without clinical workflow meaning. |
| B6-4 Missing value handling | 2 | Marks unknown; does not fabricate. |

If not in current scope, score based on explicit future-boundary clarity.

## B7. Failure Handling And Fallback: 10

Scoring intent: B7 is a realism check. A healthcare system proposal should say what happens when speech recognition fails, the model times out, fields are missing, or output confidence is low.

| Item | Points | Standard |
| --- | ---: | --- |
| B7-1 ASR error | 2 | Review/correction or fallback path. |
| B7-2 LLM hallucination | 2 | Constrained output, source attribution, rule checks. |
| B7-3 Timeout/system failure | 2 | Manual/degraded workflow. |
| B7-4 Insufficient data | 2 | Unknown/missing fields displayed. |
| B7-5 Safety uncertainty | 2 | Conservative human review. |

## B8. Performance And Deployment Feasibility: 8

Scoring intent: Performance targets should match the clinical setting. A system that works only with unrealistic GPU, network, or latency assumptions should be capped even if the demo works.

| Item | Points | Standard |
| --- | ---: | --- |
| B8-1 Latency target | 2 | Reasonable response-time target. |
| B8-2 Hardware realism | 2 | GPU/cloud/edge assumptions realistic. |
| B8-3 Concurrent use | 2 | Anticipates multiple users or explains single-station limit. |
| B8-4 Offline/degraded mode | 2 | Basic flow survives model/network failure where needed. |

## B9. Modularity And Maintainability: 8

Scoring intent: Maintainability matters because deep-cultivation projects are multi-year. Question banks, thresholds, prompts, rules, and interfaces should be replaceable without rewriting the whole system.

| Item | Points | Standard |
| --- | ---: | --- |
| B9-1 Module boundaries | 2 | UI, ASR, question bank, summary, governance separable. |
| B9-2 Configurable rules | 2 | Question bank, thresholds, prompts, and labels maintainable. |
| B9-3 Tests | 2 | Unit/integration/workflow tests or validation plan. |
| B9-4 Documentation | 2 | README, API/operation docs, or user guide. |

## B10. Monitoring And Quality Improvement: 8

Scoring intent: Monitoring converts a demo into an operational system. High scores require metrics that can detect degradation, adoption failure, safety events, and update risk.

| Item | Points | Standard |
| --- | ---: | --- |
| B10-1 Error-rate monitoring | 2 | ASR/model/API/system errors tracked. |
| B10-2 Adoption monitoring | 2 | Accept/edit/reject or usage metrics tracked. |
| B10-3 Safety-event monitoring | 2 | Prompt injection, unsafe output, abnormal input, or privacy events tracked. |
| B10-4 Versioned improvement process | 2 | Updates trigger review and revalidation. |

## B11. Interoperability Readiness: 7

Scoring intent: B11 rewards honest integration design. A proposal should distinguish current export/import, future FHIR/TW Core IG readiness, and unapproved direct EMR/HIS writeback.

| Item | Points | Standard |
| --- | ---: | --- |
| B11-1 Hospital-system touchpoint | 2 | Defines read/export/writeback boundary. |
| B11-2 EMR/HIS non-overclaim | 1 | Does not imply unapproved direct integration. |
| B11-3 FHIR / TW Core IG awareness | 2 | Maps future data readiness to official standards if relevant. |
| B11-4 Integration-risk statement | 2 | Addresses permission, synchronization, format, ownership, and security. |

## B12. Engineering Maturity Evidence: 7

Scoring intent: B12 gives credit for evidence that the system has been made concrete. Screenshots, synthetic runs, test data, logs, and issue lists are stronger than architectural promises.

| Item | Points | Standard |
| --- | ---: | --- |
| B12-1 Prototype exists | 2 | Operable synthetic demo or equivalent. |
| B12-2 Screenshots/video | 1 | Real demo evidence. |
| B12-3 Test data | 1 | Synthetic/de-identified data clearly labeled. |
| B12-4 Deployment/readiness record | 1 | Runbook, command, or deployment log. |
| B12-5 Issue/risk list | 1 | Known problems listed. |
| B12-6 Roadmap | 1 | Next stage clear. |

# C. Governance, Security, Regulation, And Sustainability: 100

## C1. Cybersecurity Governance: 12

Scoring intent: Cybersecurity is scored as operational control, not as a generic statement that data will be secure. The review should be able to identify access rules, logs, and response ownership.

| Item | Points | Standard |
| --- | ---: | --- |
| C1-1 RBAC | 2 | Role-based access model. |
| C1-2 Encryption | 2 | Transmission/storage encryption plan, if data is stored/transmitted. |
| C1-3 Access log | 2 | Who accessed what and when. |
| C1-4 Least privilege | 2 | Minimal necessary access. |
| C1-5 Incident response | 2 | Breach/attack response path. |
| C1-6 Periodic audit | 2 | Routine access/log review. |

## C2. Data Governance: 12

Scoring intent: Data governance must say what data is used, why it is legal to use it, how long it is retained, who may access it, and whether it can be reused for training or evaluation.

| Item | Points | Standard |
| --- | ---: | --- |
| C2-1 Legal data source | 2 | Consent/IRB/institutional basis stated. |
| C2-2 De-identification | 2 | Identifiers removed or protected. |
| C2-3 Retention policy | 2 | Storage duration and deletion. |
| C2-4 Use limitation | 2 | Research, test, training, and clinical use separated. |
| C2-5 Data-quality checks | 2 | Missing/abnormal/duplicate checks. |
| C2-6 Standardized format | 2 | FHIR/TW Core IG readiness when relevant. |

## C3. AI Governance: 15

Scoring intent: AI governance creates traceability from input to model/prompt/rule version to output to clinician action. Without traceability, learning and accountability are weak.

| Item | Points | Standard |
| --- | ---: | --- |
| C3-1 Model versioning | 2 | Output traceable to model version. |
| C3-2 Prompt/rule versioning | 2 | Prompt/rule changes tracked. |
| C3-3 Output audit | 2 | Raw AI output separated from accepted final text. |
| C3-4 Clinician edit log | 2 | Corrections/rejections analyzable. |
| C3-5 Uncertainty labeling | 2 | Low confidence and missing data visible. |
| C3-6 Bias monitoring | 2 | Age, language, sex/gender, literacy, or disability impact considered. |
| C3-7 No autonomous diagnosis | 2 | Clinical decision remains human-owned. |
| C3-8 Serious error reporting | 1 | Escalation or reporting pathway. |

## C4. Clinical Safety Design: 10

Scoring intent: C4 ensures that clinical safety is designed into the workflow, not appended as a disclaimer. Safety observations, uncertainty, use limits, and responsibility boundaries should be visible to users.

| Item | Points | Standard |
| --- | ---: | --- |
| C4-1 Safety observation rules | 2 | Red-flag reports shown neutrally. |
| C4-2 Human escalation | 2 | Concerning or uncertain cases routed to human review. |
| C4-3 Error warning | 2 | Clinician sees uncertainty/source limits. |
| C4-4 Use limitation | 2 | Excluded populations or settings stated. |
| C4-5 Responsibility boundary | 2 | Clinician owns final interpretation and action. |

## C5. Legal / Ethics Awareness: 8

Scoring intent: Legal and ethics scoring should match the actual deployment stage. Research, demo, pilot, and clinical use have different IRB, medical-record, data-use, and SaMD/TFDA implications.

| Item | Points | Standard |
| --- | ---: | --- |
| C5-1 IRB decision path | 2 | IRB need and timing stated. |
| C5-2 Medical-record/legal awareness | 2 | Clinical documentation status clear. |
| C5-3 Personal Data Protection Act awareness | 2 | Data collection and use basis stated. |
| C5-4 SaMD/TFDA awareness | 2 | If applicable, software medical-device path acknowledged; if not, demo/research status explicit. |

## C6. Clinical AI Validation Path: 8

Scoring intent: Validation should test usefulness and safety in context. Accuracy alone is insufficient if the system changes clinical workload, documentation, or follow-up behavior.

| Item | Points | Standard |
| --- | ---: | --- |
| C6-1 Validation dataset | 2 | Test sample or validation plan. |
| C6-2 Clinical benefit evaluation | 2 | Measures usefulness, not only accuracy. |
| C6-3 Expert review | 2 | Clinician-labeled or clinician-reviewed outputs. |
| C6-4 Certification/approval boundary | 2 | Clearly states whether it is demo, research, pilot, or certified product. |

## C7. SMART on FHIR / Interoperability Governance: 8

Scoring intent: C7 is about governed interoperability. FHIR/TW Core IG and SMART on FHIR should be treated as a standardization path with data ownership and security, not as buzzwords.

| Item | Points | Standard |
| --- | ---: | --- |
| C7-1 FHIR resource mapping | 2 | Patient, Observation, MedicationRequest, Condition, QuestionnaireResponse, etc. considered when relevant. |
| C7-2 TW Core IG alignment | 2 | Taiwan implementation guide awareness. |
| C7-3 SMART on FHIR scenario | 2 | If relevant, explains app-in-EMR ecosystem path. |
| C7-4 Cross-site scalability | 2 | Avoids single-hospital data lock-in. |

## C8. Deployment And Operation Plan: 10

Scoring intent: Deployment scoring asks whether the proposal can leave the slide deck. Site, role, timeline, training, support, and maintenance responsibility must be concrete.

| Item | Points | Standard |
| --- | ---: | --- |
| C8-1 Site defined | 2 | Department, clinic, or community setting named. |
| C8-2 Timeline defined | 2 | Milestones and deliverables by month/quarter. |
| C8-3 Roles defined | 2 | Clinical, engineering, PM, security, and admin owners. |
| C8-4 Training plan | 2 | Clinician/staff/admin training. |
| C8-5 Maintenance ownership | 2 | Who owns system after pilot. |

## C9. Budget Realism: 5

Scoring intent: Budget realism links resources to operational value. Costs should map to work packages, owners, and maintenance instead of appearing as generic equipment or cloud spend.

| Item | Points | Standard |
| --- | ---: | --- |
| C9-1 Personnel cost | 1 | Engineering, clinical, PM, RA allocation realistic. |
| C9-2 Equipment cost | 1 | No unrelated high-spec purchases. |
| C9-3 Software/API/cloud cost | 1 | ASR/LLM/cloud/API costs considered. |
| C9-4 Maintenance cost | 1 | Ongoing cost included. |
| C9-5 Cost-effectiveness | 1 | Links cost to clinical/service value. |

## C10. Sustainability And Scale: 7

Scoring intent: Sustainability is scored by governed continuation or exit. A strong plan can scale, update, monitor, or stop safely based on evidence.

| Item | Points | Standard |
| --- | ---: | --- |
| C10-1 Specialty expansion | 2 | Clear path beyond initial specialty if evidence supports. |
| C10-2 Site expansion | 2 | Single site to multi-site logic. |
| C10-3 Maintainable question bank | 1 | Clinician-updatable or governed update path. |
| C10-4 Long-term KPI monitoring | 1 | Outcome tracking after pilot. |
| C10-5 Exit/degrade strategy | 1 | Stop or downgrade if ineffective. |

## C11. Risk Register: 5

Scoring intent: The risk register is an audit object. A high-score proposal names risks early and gives owners and mitigation paths instead of hiding uncertainty.

| Item | Points | Standard |
| --- | ---: | --- |
| C11-1 Technical risk | 1 | ASR, model, uptime, integration. |
| C11-2 Clinical risk | 1 | Misleading output, missing data, unsafe confidence. |
| C11-3 Security risk | 1 | Leakage, misuse, access abuse. |
| C11-4 Adoption risk | 1 | Clinician, staff, patient non-use. |
| C11-5 Mitigation | 1 | Each risk has response. |

# D. MOHW Format Compliance And Application Completeness: 100

This layer evaluates whether the proposal follows official MOHW Health Taiwan Deep-Cultivation requirements, proposal format, online submission expectations, attachments, funding rules, governance checklists, and execution/reporting requirements.

It evaluates administrative and document compliance, not whether the idea is clinically good.

Expanded D-layer file:

- `DEEP_CULTIVATION_MOHW_COMPLIANCE_RUBRIC.md`

Use that file when doing official-format, attachment, budget, governance-checklist, submission, and reporting preflight.
It now includes a non-scored `D0` source-freshness and official-document
crosswalk gate. Before a formal submission, refresh the live HTSprout / MOHW /
AI Center source pages and verify that the proposal still uses the current
official template and required forms.

## Required Official References For D

Use these local documents as the working archive, but re-check the live official
download pages before formal submission:

- `../records/2026-05-19/policy-documents/application/health-taiwan-phase1-application-guidelines.pdf`
- `../records/2026-05-19/policy-documents/application/health-taiwan-phase1-proposal-format-114-115-0909.docx`
- `../records/2026-05-19/policy-documents/application/health-taiwan-online-platform-user-guide.pdf`
- `../records/2026-05-19/policy-documents/qa/health-taiwan-qa-1140710.pdf`
- `../records/2026-05-19/policy-documents/budget/funding-use-principles-1140922.pdf`
- `../records/2026-05-19/policy-documents/budget/negative-list-and-restricted-items-1140922.pdf`
- `../records/2026-05-19/policy-documents/budget/funding-standards-second-revision-1150413.pdf`
- `../records/2026-05-19/policy-documents/execution/management-and-monitoring-points.pdf`
- `../records/2026-05-19/policy-documents/execution/checkpoint-reporting-record-114-115.docx`
- `../records/2026-05-19/policy-documents/execution/final-results-report-114-115.docx`
- `../records/2026-05-19/policy-documents/execution/ai-governance-self-checklist.docx`
- `../records/2026-05-19/policy-documents/execution/cybersecurity-governance-self-checklist.docx`
- `../records/2026-05-19/policy-documents/execution/data-governance-self-checklist.docx`

## D1. Applicant Eligibility And Application Mode: 10

| Item | Points | Compliance Standard |
| --- | ---: | --- |
| D1-1 Applicant eligibility stated | 2 | Applicant type is eligible and identified. |
| D1-2 Eligibility proof attached | 2 | Medical institution code, registration, tax ID, or equivalent evidence included. |
| D1-3 One application mode selected | 2 | Application mode/category is not ambiguous or duplicated. |
| D1-4 Main applicant / partner relationship clear | 2 | Same system, alliance, cross-hospital, community, or vendor roles are stated. |
| D1-5 Scope/category selection fits content | 2 | Categories one to four are selected only where supported by content. |

## D2. Proposal Format And Page/Layout Compliance: 12

| Item | Points | Compliance Standard |
| --- | ---: | --- |
| D2-1 Single merged PDF | 2 | Uploaded proposal is one merged PDF. |
| D2-2 File size | 1 | PDF is under official file-size limit, currently 25 MB for proposal upload in guidelines. |
| D2-3 Font | 2 | Chinese uses 標楷體; English/numbers use Times New Roman unless official template says otherwise. |
| D2-4 Font size | 1 | Main text 12 pt except allowed headings, tables, and TOC. |
| D2-5 Line spacing | 1 | Fixed line height follows official rule, currently 15 pt for proposal. |
| D2-6 Margins | 1 | Top/bottom/left/right 1.5 cm unless official template changes. |
| D2-7 Header/footer | 1 | Header/footer 0.5 cm. |
| D2-8 Page numbers | 1 | Page numbers inserted and consistent. |
| D2-9 Page limit | 1 | Exported proposal body stays within official limit, currently 40 pages excluding specified front/appendix materials. |
| D2-10 Printed copies | 1 | Paper copy count and binding match official requirement, currently double-sided glue-bound 1 set x 6 copies. |

Before submission, re-check the latest official template because hospital-provided instructions may supersede the downloaded copy.

## D3. Cover, Basic Data, And Institution Fields: 8

| Item | Points | Compliance Standard |
| --- | ---: | --- |
| D3-1 Project title | 1 | Same across platform, PDF, paper copy, and official letter. |
| D3-2 City/county | 1 | Main applicant location is correct. |
| D3-3 Application mode | 1 | A/B/C/D or subcategory matches official form. |
| D3-4 Scope categories | 1 | Selected scopes match proposal contents. |
| D3-5 Main institution data | 1 | Name, code, registration, tax ID complete. |
| D3-6 Partner institution data | 1 | Partner names/codes/relationship complete. |
| D3-7 Funding and period | 1 | Amount and schedule match budget tables. |
| D3-8 PI/contact data | 1 | Titles, phone, and email complete. |

## D4. Self-Check Forms And Required Declarations: 10

| Item | Points | Compliance Standard |
| --- | ---: | --- |
| D4-1 Applicant self-check table | 2 | All required rows checked and notes are internally consistent. |
| D4-2 Conflict-of-interest self-check | 2 | Public official conflict-of-interest self-check included and signed/sealed if required. |
| D4-3 Relationship disclosure decision | 1 | Disclosure form included or correctly marked not applicable. |
| D4-4 No-duplicate-application declaration | 2 | Signed/sealed by PI and institution as required. |
| D4-5 Partner participation consent | 2 | Partner responsible persons sign/seal where required. |
| D4-6 Scanned signatures merged | 1 | Signed documents merged into final PDF. |

## D5. Official Chapter Order And Required Content Fields: 12

| Item | Points | Compliance Standard |
| --- | ---: | --- |
| D5-1 Official order preserved | 2 | Chapter order follows official template and is not arbitrarily rearranged. |
| D5-2 Table of contents | 1 | TOC and pages correct. |
| D5-3 Project overview | 2 | Basis, current state, and problem analysis complete. |
| D5-4 Existing-government-funding distinction | 2 | Explains distinction or connection with existing government subsidy projects. |
| D5-5 Applicant institution introduction | 1 | Institution capabilities, equipment, and track record included within official limit. |
| D5-6 Project planning | 2 | Annual goals over 114-118 or applicable years by scope. |
| D5-7 Overseas plan handling | 1 | Included only where scope 2 / talent training requires it. |
| D5-8 Attachments / figures / appendix handling | 1 | Uses allowed attachments; does not hide required core content in appendices. |

## D6. Performance Indicators And Annual Checkpoints: 12

| Item | Points | Compliance Standard |
| --- | ---: | --- |
| D6-1 KPI for each selected scope | 2 | Each selected scope has measurable indicators. |
| D6-2 KPI formula / measurement definition | 2 | Numerator, denominator, method, or scoring method clear. |
| D6-3 Baseline/current data | 2 | Current value or baseline collection method included. |
| D6-4 Annual targets | 2 | Annual target values for required years included. |
| D6-5 Quarterly/annual checkpoint content | 1 | Work content and checkpoint description included. |
| D6-6 Cumulative progress | 1 | Cumulative expected progress (%) reasonable. |
| D6-7 Cumulative spending | 1 | Cumulative planned spending aligns with budget table. |
| D6-8 Expected result and date | 1 | Checkpoint can be managed and verified. |

Use official guidance that process indicators alone are weak; outcome or mission indicators should be prioritized.

## D7. Budget Planning And Funding-Rule Compliance: 14

| Item | Points | Compliance Standard |
| --- | ---: | --- |
| D7-1 Annual budget table | 2 | Required years listed and totals consistent. |
| D7-2 Subsidy vs matching funds separated | 1 | Fields separated and consistent. |
| D7-3 Current vs capital categories | 2 | Personnel, operating, equipment, and capital/current categories correct. |
| D7-4 Capital expense ratio | 2 | Capital expense generally within 30% unless justified and approved. |
| D7-5 Personnel budget | 1 | Salary, labor/health insurance, pension/retirement items handled. |
| D7-6 Operating expenses | 1 | Directly tied to work packages. |
| D7-7 Equipment expenses | 1 | Equipment is relevant and justified. |
| D7-8 Scope-level budget allocation | 1 | Scope/category budget distribution complete. |
| D7-9 Unit price / quantity / explanation | 1 | Costs can be audited. |
| D7-10 Negative-list compliance | 1 | No prohibited or restricted items included. |
| D7-11 Account and actual-use awareness | 1 | Proposal recognizes dedicated account, approved purpose, and no misuse. |

## D8. Personnel Allocation And Partner Workshare: 6

| Item | Points | Compliance Standard |
| --- | ---: | --- |
| D8-1 PI role | 1 | Overall responsibility clear. |
| D8-2 Co-PI roles | 1 | Clinical, engineering, administrative, and governance roles assigned. |
| D8-3 Subproject owners | 1 | Each subproject has an owner. |
| D8-4 Staff/assistant work | 1 | Work nature, task, and scope are stated. |
| D8-5 Partner division of labor | 1 | Each partner's work is specific. |
| D8-6 Personnel/budget consistency | 1 | Staffing table and personnel budget do not conflict. |

## D9. AI / Cybersecurity / Data Governance Document Alignment: 8

| Item | Points | Compliance Standard |
| --- | ---: | --- |
| D9-1 AI governance self-check | 2 | AI governance checklist used where scope 3 smart healthcare applies. |
| D9-2 Cybersecurity governance self-check | 2 | Cybersecurity checklist used for system/data work. |
| D9-3 Data governance self-check | 2 | Data-governance checklist used for patient data, EMR, FHIR, or data-sharing work. |
| D9-4 Three AI Centers / certification awareness | 1 | If applicable, proposal notes alignment or future certification path. |
| D9-5 SMART on FHIR / FHIR alignment | 1 | Especially for smart-healthcare software or data workflows. |

## D10. Submission Flow, Correction Risk, And Version Consistency: 8

| Item | Points | Compliance Standard |
| --- | ---: | --- |
| D10-1 Platform entry complete | 1 | Online platform data complete. |
| D10-2 Exported PDF checked | 1 | Export matches platform data. |
| D10-3 Paper copies prepared | 1 | Required copies/binding ready. |
| D10-4 Online/paper consistency | 2 | Paper and platform versions match; if not, written copy controls per guideline. |
| D10-5 Correction deadline tracked | 1 | Three-working-day correction window tracked if notified. |
| D10-6 One-correction-limit risk | 1 | Proposal has pre-submission internal check to avoid single-correction failure. |
| D10-7 Official letter / submission identifiers | 1 | Project title, institution, codes, and submission identifiers match. |

## D-Layer Penalties

| Issue | Penalty |
| --- | ---: |
| Not using official proposal format | -20 |
| Arbitrarily changing official chapter order | -10 |
| PDF over official file-size limit | -5 |
| Proposal body over official page limit | -8 |
| Font, spacing, or margin clearly noncompliant | -5 to -10 |
| Missing applicant self-check table | -10 |
| Missing conflict-of-interest check | -10 |
| Missing no-duplicate-application declaration | -10 |
| Missing partner participation consent where required | -8 |
| Budget table inconsistent with work package | -10 |
| Capital budget over ratio without justification | -10 |
| Platform and paper versions inconsistent | -15 |
| Missing annual checkpoints | -10 |
| Missing baseline/current data and annual targets | -10 |
| Scope 3 smart healthcare without AI/cybersecurity/data governance checklists | -10 |

# Cross-Layer Penalty Rules

| Issue | Penalty |
| --- | ---: |
| AI/LLM buzzwords without workflow need | A -15 |
| No human-in-the-loop where clinical output exists | A -10, C -10 |
| No cybersecurity governance for data/system work | C -15 |
| No data governance for patient-data or interoperability claims | C -10 |
| No FHIR/TW Core IG or interoperability discussion where data sharing is claimed | B -5, C -5 |
| KPI are only adjectives | A -10, D -5 |
| Claims to replace clinicians | C -20 |
| Hardware/latency assumptions are unrealistic | B -15 |
| Uses patient data without IRB/consent/de-identification path | C -20, D -5 |
| No pilot or workflow site | A -5, C -5 |

# Final Review Template

```text
A. Clinical Value And Workflow Integration: __/100
Evidence:
Main strengths:
Main gaps:
PoC readiness:

B. Technical System And AI Engineering: __/100
Evidence:
Main strengths:
Main gaps:
Largest engineering risk:

C. Governance, Security, Regulation, And Sustainability: __/100
Evidence:
Main strengths:
Main gaps:
Deployment governance readiness:

D. MOHW Format Compliance And Application Completeness: __/100
Evidence:
Main strengths:
Main gaps:
Submission readiness:

Gate decision:
[ ] Do not pass
[ ] Revise and resubmit
[ ] Eligible for PoC review
[ ] Eligible for pilot planning
[ ] High-maturity demonstration candidate
```

Core principle:

```text
A/B/C decide whether it is a good healthcare system proposal.
D decides whether it can be formally submitted, reviewed, contracted, monitored, and closed without avoidable administrative failure.
```
