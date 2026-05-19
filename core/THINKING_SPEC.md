# Thinking Spec: Urology Smart-Previsit System Logic

## 1. Problem Framing

The starting problem is repeated and poorly timed information gathering before a urology visit. A patient may explain similar symptoms to clinic staff, nursing staff, and the physician, while key details can still be missing when the formal visit begins.

The system is not motivated by a need to use artificial intelligence. It is motivated by a workflow question: can common previsit information be collected earlier, checked for completeness, and handed to the clinician in a form that saves time without weakening clinical judgment?

The problem must be framed as discovery before deployment. A useful answer may be "continue", "revise", or "pause". The thinking system is successful if it makes that decision clearer.

## 2. 2026-05-19 Deep-Cultivation Positioning

After the 2026-05-19 北市聯醫 deep-cultivation meeting, the system should also be read as a candidate smart-healthcare component under `健康台灣深耕計畫(114-118年)`.

The accepted positioning is:

```text
urology previsit / visit-readiness / clinician-review summary / CRM follow-up support
```

This positioning expands the grant-facing context, not the clinical authority of the system. It connects the existing urology previsit design to PSA/community screening, SOP, return-to-hospital flow, case management, reminders, and CRM, while preserving the same safety boundary.

It is not:

- AI triage
- diagnosis
- treatment recommendation
- autonomous risk scoring
- direct HIS / EMR / EHR writeback
- production clinical use

The detailed positioning and KPI logic live in `DEEP_CULTIVATION_SYSTEM_POSITIONING.md`.

## 3. Design Philosophy

The system should start with guidance, not autonomy.

The safest early design is a structured previsit conversation that asks plain questions, repairs missing information, supports assisted use, and produces a short reviewable summary. It should not appear to know what disease the patient has or what treatment the patient needs.

The design favors:

- restraint over impressive claims
- structured answers over open-ended guessing
- patient review before clinician review
- neutral observations over medical conclusions
- missing-information repair over diagnosis
- workflow learning before expansion
- explicit boundaries over hidden ambition

This philosophy exists because a previsit tool can become unsafe if it sounds more authoritative than it is.

## 4. User Model

The primary user is a urology patient preparing for a visit. The patient may be older, anxious, visually impaired, unfamiliar with phones, unsure how to describe symptoms, or more comfortable with Mandarin, Taiwanese, mixed language, or help from another person.

The secondary users are clinic staff and clinicians. They do not need a long transcript. Nurses need a missing-information repair surface. Clinicians need a short, trustworthy context layer that helps them see the chief concern, symptom pattern, missing information, source attribution, and review flags before or during the visit.

The system should assume uneven ability from the start. Self-filled, family-assisted, and nurse-repaired use are all valid. A design that works only for young, confident, digitally fluent patients is not adequate for this domain. Patient/family screens should not expose nurse or physician work screens.

## 5. Workflow Logic

The workflow begins before physician-led questioning and ends before clinical interpretation.

The intended sequence is:

1. patient arrives or prepares for the visit
2. patient or helper starts the patient-facing guided previsit flow
3. patient identifies the main concern
4. patient answers structured symptom and context questions
5. missing key information is surfaced
6. patient or helper reviews a patient-facing confirmation page
7. nurse or clinic staff sees a separate missing-information repair workbench when needed
8. nurse supplements missing answers without erasing the original answer source
9. a clinician-review summary is prepared
10. clinician confirms, edits, ignores, or asks follow-up questions

The system does not close the clinical loop. It prepares the encounter. Its value depends on whether this sequence fits the clinic's real check-in, waiting, nursing, and physician workflow.

## 6. Information Strategy

The system should collect the smallest set of information that is useful before the physician enters.

Potentially useful information includes:

- main urinary concern
- duration of symptoms
- patient-rated bother or severity
- daytime bathroom frequency
- nighttime urination
- leakage
- pain or burning
- blood in urine
- fever or chills
- inability to urinate
- current medicines or uncertainty about medicines
- preferred language
- accessibility or help needs
- optional patient context

The system should avoid collecting identity details, account details, exact birth dates, real medical record numbers, addresses, phone numbers, or anything not needed for the discovery decision.

The information strategy is "minimum useful context", not "maximum capture". Collecting more information can make the system slower, more invasive, harder to review, and harder to govern.

## 7. Output Design Logic

The output should be a clinician-review summary, not a medical conclusion.

The summary should separate:

- safety notice
- chief concern
- symptom pattern
- duration and patient-rated burden
- neutral clinician-review flags
- missing information
- medicine uncertainty
- field-level answer source when patient, family, or nurse input differs
- language or accessibility needs
- optional patient note

The summary should be short enough to review quickly. It should not require the clinician to read a long transcript. It should preserve uncertainty and make it clear that the information came from the patient or helper.

The output is useful only if it helps the clinician begin the visit with better context while still leaving room to confirm, correct, or ignore it.

## 8. Safety And Boundary Design

The core safety boundary is simple: the system may prepare information, but it must not make clinical decisions.

It must not:

- diagnose
- triage
- recommend treatment
- imply the patient is safe or unsafe
- replace clinician questioning
- hide uncertainty
- claim clinical completeness

Patient-reported red flags should be written as observations, not conclusions. For example:

- "Reports blood in urine."
- "Reports fever or chills."
- "Reports being unable to urinate."

The system should not convert these into disease labels, urgency levels, or treatment suggestions.

Privacy boundaries are also part of safety. During discovery, real patient data should not be used. Any future use of real patient data requires a separate consent, retention, access, responsibility, and review plan.

## 9. Trust And Adoption Strategy

Trust comes from restraint, clarity, and clinician control.

Patients are more likely to trust a system that asks understandable questions, allows review, and does not pretend to be a doctor. Clinicians are more likely to trust a system that produces short, neutral, editable summaries and clearly leaves interpretation to them.

Adoption depends on whether the system reduces repeated questions or missing context without adding work. A summary that clinicians ignore is evidence. A workflow that burdens nurses is evidence. A patient confusion point is evidence.

The system should invite correction. Editing or ignoring the summary is not failure by itself; it is part of discovering whether the summary format is useful.

## 10. Cognitive Load Design

The system should lower cognitive load for both patients and clinicians.

For patients, this means:

- short questions
- plain language
- familiar answer choices
- visible progress
- review before handoff
- help from family when needed, with source labeling
- staff repair through a separate workbench when needed
- no pressure to interpret medical meaning

For clinicians, this means:

- short summary
- grouped information
- clear missing fields
- neutral review flags
- no long transcript by default
- no diagnostic tone

Cognitive load is not just a usability issue. In this domain, excessive load can cause skipped answers, misunderstood symptoms, unsafe confidence, or clinician rejection.

## 11. Evaluation Metrics

The system should be evaluated by workflow usefulness and safety, not novelty.

Usefulness metrics:

- completion rate
- time needed to complete the previsit flow
- number of repeated questions reduced
- number of missing key fields reduced
- clinician readability within one minute
- clinician usefulness rating
- staff burden rating
- patient confusion points
- proportion of summaries used, edited, ignored, or rejected

Safety metrics:

- diagnostic claims made by the summary
- treatment suggestions made by the summary
- unclear red-flag wording
- privacy-boundary violations
- patient misunderstanding of system role
- clinician concern that the summary overstates certainty

Decision metrics:

- continue if workflow value is clear and safety boundaries hold
- revise if value exists but the question tree, assisted mode, or summary format is wrong
- pause if workflow fit, safety, privacy, or staff burden is unacceptable

## 12. Scope Control

The first discovery version should remain narrow.

In scope:

- guided previsit questions
- patient/family-facing self-filled or assisted completion
- missing-information repair
- patient or helper confirmation
- nurse missing-information workbench
- clinician-review summary
- explicit safety and privacy boundaries
- meeting and decision support

Out of scope:

- diagnosis
- triage
- treatment advice
- real patient data
- production use
- hospital record integration
- voice-first use as the main path
- complete medical-history capture
- claims of clinical completeness

Scope control protects the project from becoming unsafe, expensive, or impossible to evaluate before the basic workflow question is answered.

## 13. System Identity

The system identity is:

A guided previsit reasoning and summary aid for urology workflow discovery.

It is not:

- a doctor
- a medical advice agent
- a diagnosis engine
- a triage desk
- a hospital record system
- a replacement for nurse or physician judgment

The system's legitimate role is to help collect repeated, high-value context and make that context easier for clinicians to review.

## 14. Failure Analysis

The system fails if it increases burden, creates false confidence, misleads patients, loses clinician trust, or hides risk behind polished output.

Major failure modes include:

- patient misunderstands a question
- patient skips key information
- older adult cannot complete the flow
- assisted use consumes too much staff time
- summary is too long
- summary sounds diagnostic
- clinician finds the output irrelevant
- no real clinic workflow slot exists
- privacy expectations are unclear
- the project expands before proof of value

Failure should be treated as design evidence. A pause decision is acceptable if the workflow problem is weaker than expected or if the safety boundary cannot be preserved.

## 15. Evolution Path

The system should evolve only after each prior stage proves useful.

The staged path is:

1. thinking specification and meeting pack
2. synthetic discovery walkthrough
3. clinician feedback on workflow fit and summary usefulness
4. revised question tree and summary format
5. assisted-use workflow test
6. standard one-page clinician-review summary
7. governance review before any real patient data
8. limited real-world pilot only under explicit approval
9. integration discussion only after workflow value, safety, privacy, and responsibility are clear

The system must not evolve from summary aid into clinical decision system without a separate governance review.

## Advanced Module: Trade-Off Analysis

The system sacrifices flexibility, automation, and early realism in order to gain safety, clarity, and auditability.

What was sacrificed:

- conversational naturalness, because structured answers are safer and easier to review
- diagnostic ambition, because diagnosis belongs to clinicians
- broad intake coverage, because excessive scope burdens patients and clinicians
- real patient realism, because early discovery should not create privacy risk
- integration ambition, because workflow value should be proven before operational complexity
- voice-first convenience, because speech errors, noise, mixed language, and privacy concerns can distort early learning

Rejected alternatives:

- autonomous medical interviewer, rejected because it blurs clinical responsibility
- voice-first interaction as the main path, rejected because the first risk is miscapture, not lack of novelty
- full medical-history intake, rejected because it expands burden beyond the repeated-question problem
- hospital integration first, rejected because it solves routing before proving usefulness
- transcript output, rejected because clinicians need concise review, not more reading
- real patient pilot first, rejected because governance should follow evidence, not precede the basic workflow test

The chosen design favors modest usefulness over impressive claims.

## Advanced Module: Counterfactual Design

If the design were reversed into an autonomous interviewer, the main failure would be responsibility confusion: patients might treat the system as medical judgment, and clinicians might reject summaries that appear to make hidden decisions.

If the design were voice-first from the start, the meeting could become a debate about speech capture instead of a test of whether previsit information is useful.

If the design collected real patient data immediately, privacy and consent concerns would dominate before the workflow problem is proven.

If the design began with hospital-system integration, the team could spend effort on operational routing while never learning whether the summary helps the visit.

If the design produced a full transcript, clinicians would receive more text rather than a clearer starting point.

These counterfactuals show why the chosen system is intentionally smaller than the most ambitious version.

## Advanced Module: Generalization

This structure can be reused wherever repeated information is gathered before an expert encounter.

Reusable domains include:

- dermatology visit preparation
- orthopedic injury history intake
- chronic disease follow-up
- dental visit preparation
- elder-care intake
- mental-health screening support with strict boundaries
- insurance claim preparation
- legal consultation intake
- customer-support escalation summaries
- education advising pre-meeting forms

The reusable pattern is:

1. identify repeated pre-encounter information
2. collect only the minimum useful context
3. repair missing information before handoff
4. let the user review
5. produce an expert-review summary
6. keep final judgment with the expert
7. evaluate usefulness before expanding scope
