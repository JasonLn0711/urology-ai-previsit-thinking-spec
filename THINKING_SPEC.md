# Thinking Spec: Urology Smart-Previsit MVP

## 1. Problem Framing

Urology visits often begin with repeated information gathering. The same patient may be asked similar questions by front-desk staff, nurses, and the physician.

The core problem is not lack of artificial intelligence. The core problem is workflow friction before the clinician enters the formal visit.

The system exists to test whether a guided previsit interview can collect useful, repeated information earlier, reduce duplicated questioning, and produce a short summary that helps the clinician start faster.

The problem must be framed as workflow discovery, not product deployment.

## 2. Design Philosophy

The system starts with guidance, not autonomy.

It should help patients explain their situation in a structured way, while preserving clinician judgment. The safest first version is a guided question flow with clear choices, large interaction targets, plain language, and a final review step.

The design prefers:

- structured questions over open-ended conversation
- patient review before clinician review
- summary over diagnosis
- missing-information prompts over medical conclusions
- human confirmation over automated decision-making
- low-friction workflow learning over full hospital integration

## 3. User Model

Primary users are urology patients preparing for a visit. Some may be older adults, unfamiliar with phones, visually impaired, anxious, or more comfortable using Taiwanese, Mandarin, mixed language, or staff assistance.

Secondary users are nurses, clinic staff, and physicians. Their need is not more raw text. Their need is a short, reviewable previsit summary that identifies the chief concern, symptom pattern, missing information, and review flags.

The system assumes user ability varies widely. Therefore, self-filled, nurse-assisted, and family-assisted paths must all remain conceptually valid.

## 4. Workflow Logic

The workflow begins before the physician-led encounter.

The intended flow is:

```text
patient arrives or checks in
-> patient or helper opens guided previsit flow
-> patient identifies main concern
-> patient answers structured questions
-> system notices missing key information
-> patient or nurse reviews answers
-> system produces clinician-review summary
-> clinician confirms, edits, ignores, or asks follow-up questions
```

The system does not attempt to close the clinical loop. It only prepares the encounter.

The workflow is successful only if it fits the clinic's real sequence of check-in, waiting, nursing, physician review, and documentation.

## 5. Information Strategy

The system should collect only information that is useful before the physician enters.

High-value information includes:

- main urinary concern
- duration
- bother or severity
- daytime bathroom frequency
- nighttime urination
- leakage
- pain or burning
- blood in urine
- fever or chills
- inability to urinate
- current medicines or medicine uncertainty
- preferred language
- accessibility or phone-use needs
- optional patient context

The system should avoid collecting identity details, sensitive identifiers, exact birth dates, real medical record numbers, or anything unnecessary for the discovery demo.

Information strategy is based on minimal useful information, not maximum capture.

## 6. Output Design Logic

The output is a clinician-review summary.

It should be readable quickly and should separate:

- safety notice
- chief concern
- symptom pattern
- duration and severity
- clinician-review flags
- missing information
- patient constraints
- medicine context
- optional patient note

The summary must not sound like a diagnosis. It must preserve uncertainty and keep the clinician in charge.

A useful output is not a complete medical record. It is a short prepared context layer.

## 7. Safety And Boundary Design

The system must never diagnose, triage, or recommend treatment.

Red-flag statements should be presented as observations only, such as:

- Reports blood in urine.
- Reports fever or chills.
- Reports being unable to urinate.

The system should not say:

- likely infection
- probable cancer
- needs catheter
- take medication

The boundary is clinician review, not clinical judgment.

The system should also avoid real patient-data storage in the MVP. Privacy risk is reduced by using synthetic data and by keeping answers temporary during discovery.

## 8. Trust And Adoption Strategy

Trust comes from restraint.

Patients should trust the system because it is simple, clear, and does not overclaim. Clinicians should trust it because it produces reviewable information and does not interfere with judgment.

Adoption depends on whether the summary saves time, reduces repeated questions, and improves completeness without adding staff burden.

The system should invite clinician correction. Ignoring or editing the summary is an acceptable workflow outcome.

## 9. Cognitive Load Design

The system must reduce cognitive load for patients and clinicians.

For patients:

- use short questions
- use familiar choices
- avoid medical jargon
- provide large, clear controls
- allow help from nurse or family
- ask only the minimum useful follow-up questions

For clinicians:

- provide a compact summary
- highlight missing information
- flag patient-reported review items neutrally
- avoid long transcripts unless specifically requested later

The system should make the next action obvious at every step.

## 10. Evaluation Metrics

The system should be evaluated by workflow usefulness, not technical novelty.

Core evaluation metrics:

- completion rate
- time required to complete
- summary readability under 60 seconds
- number of repeated questions reduced
- amount of missing information reduced
- clinician usefulness rating
- patient or staff usability rating
- proportion of summaries clinicians edit, ignore, or use
- number of unsafe or misleading output cases
- number of privacy-boundary violations

A successful MVP proves whether the workflow is worth deeper prototyping.

## 11. Scope Control

The MVP must remain narrow.

In scope:

- guided previsit questions
- patient or helper mode
- missing-information prompts
- patient review
- clinician-review summary
- synthetic cases
- safety and privacy boundaries
- meeting discussion support

Out of scope:

- diagnosis
- triage
- treatment recommendation
- real patient data
- hospital system integration
- autonomous interview
- voice-first workflow
- production deployment
- complete medical history capture

Scope control protects the project from becoming unsafe or untestable too early.

## 12. System Identity

The system identity is:

A guided previsit reasoning and summary aid for urology workflow discovery.

It is not:

- a doctor
- a chatbot doctor
- a diagnosis engine
- a hospital system replacement
- a medical decision system

The system's role is to make repeated previsit information easier to collect and easier for clinicians to review.

## 13. Failure Analysis

The system fails if it creates false confidence, increases workload, confuses patients, produces misleading summaries, violates privacy expectations, or distracts from physician-led judgment.

Major failure modes:

- patient misunderstands a question
- patient skips key details
- older adult cannot operate the interface
- summary is too long
- clinician does not trust the summary
- staff workflow has no place to use it
- red-flag language sounds diagnostic
- privacy boundary is unclear
- the system tries to integrate too early
- the system solves a demo problem but not a clinic problem

Failure should be treated as design evidence, not embarrassment.

## 14. Evolution Path

The system should evolve only after workflow value is proven.

Possible stages:

1. Thinking spec and meeting pack.
2. Synthetic guided-flow demo.
3. Clinician feedback on summary usefulness.
4. Revised question tree.
5. Nurse-assisted workflow test.
6. Printable or exportable summary format.
7. Limited real-world pilot only with explicit governance.
8. Integration discussion only after clinical workflow and privacy rules are clear.

Evolution should remain evidence-driven. The project should not move from summary aid to clinical decision system without a separate safety, regulatory, and governance review.

## Advanced Module: Trade-Off Analysis

The system sacrifices conversational flexibility in order to gain safety, clarity, and auditability.

Rejected alternatives:

- voice-first AI interview: rejected because accent, noise, elderly speech, privacy, and transcription errors create early risk
- autonomous triage: rejected because it crosses into clinical judgment
- hospital integration first: rejected because integration complexity would hide whether the workflow itself is useful
- full medical-history intake: rejected because excessive capture increases burden and privacy risk
- free-form transcript output: rejected because clinicians need summary, not another long document

The chosen design favors modest usefulness over impressive claims.

## Advanced Module: Counterfactual Design

If the system were reversed into a voice-first autonomous interviewer, the project would likely break in several ways:

- patients with accents, mixed language, or quiet speech may be misunderstood
- the system could appear to make clinical decisions
- clinicians may distrust or ignore opaque summaries
- privacy risk increases if audio is captured
- implementation difficulty would distract from workflow learning

If the system stored real patient data from the beginning, governance burden would rise before workflow value is proven.

If the system integrated with hospital systems first, the team might solve technical routing before confirming whether the summary is useful.

## Advanced Module: Generalization

This thinking structure can be reused in other domains where repeated pre-encounter information gathering creates friction.

Reusable domains include:

- dermatology previsit symptom intake
- orthopedic injury history capture
- chronic disease follow-up preparation
- dental visit preparation
- mental-health screening support
- elder-care intake
- insurance claim preparation
- legal consultation intake
- customer-support escalation summaries
- education advising pre-meeting forms

The general pattern is:

```text
before expert encounter
-> collect repeated information
-> detect missing context
-> let user review
-> generate expert-review summary
-> expert remains final decision-maker
```
