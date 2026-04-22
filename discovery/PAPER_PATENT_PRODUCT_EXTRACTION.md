# Paper, Patent, And Product Extraction

## Purpose

This document keeps three kinds of reasoning separate:

- paper framing: what argument can be studied or written
- patent reasoning: what system logic may be worth prior-art review
- product decision: what a real clinic might adopt or reject

Do not blend these into one story. A useful paper angle is not automatically a product opportunity. A possible patent angle is not automatically novel. A product decision is not automatically publishable.

## Separation Rule

Every post-meeting insight should be sorted into one or more of these categories:

| Category | Question It Answers | Evidence Needed |
| --- | --- | --- |
| Paper | What can be argued, studied, or explained? | workflow evidence, safety logic, reviewer feedback |
| Patent reasoning | What system logic may be distinct enough to investigate? | clear mechanism, boundary, and prior-art questions |
| Product | Would anyone adopt this in practice? | user pain, workflow slot, burden, value, decision maker |

## Paper Framing

## Strong Paper Claim

The strongest paper claim is not:

"Artificial intelligence interviews patients."

The stronger claim is:

"A bounded clinician-review workflow can collect repeated previsit information, repair missing context, and preserve clinical authority through neutral summary design."

## Paper Contribution Areas

Potential contribution areas:

- human-centered clinical workflow design
- safety-boundary design for previsit tools
- clinician-review summary design
- low-risk discovery before clinical integration
- patient and staff burden analysis
- separation of information capture from clinical judgment

## Paper Evidence Template

| Claim | Evidence | Limitation | Next evidence needed |
| --- | --- | --- | --- |
| Repeated previsit questions create friction |  |  |  |
| Some information can be collected safely before physician entry |  |  |  |
| Clinician-review summaries may reduce repeated questioning |  |  |  |
| Safety improves when red flags are phrased as observations |  |  |  |
| Assisted use may be necessary for some patients |  |  |  |

## Paper Quality Gate

Do not write a strong paper claim unless there is:

- workflow evidence
- reviewer feedback
- safety boundary explanation
- limitation statement
- clear decision about what the system does not do

## Patent Reasoning

## Caution

This repository does not assert patentability. It only clarifies system logic that may deserve prior-art review.

## Possible Invention Logic

The strongest reasoning is not "a questionnaire for urology."

The stronger reasoning is:

"A guided previsit workflow that separates patient-facing symptom capture, missing-information repair, neutral clinician-review flagging, and final clinician interpretation."

## Candidate Reasoning Areas

| Area | What to clarify | Prior-art question |
| --- | --- | --- |
| Patient input separated from clinician interpretation | how the system prevents patient answers from becoming conclusions | is this separation already standard? |
| Missing-information repair before handoff | how the system identifies gaps without diagnosing | is this ordinary form validation or a distinct workflow rule? |
| Neutral review flags | how red flags are displayed without urgency labels | how do existing intake systems phrase red flags? |
| Assisted-use modes | how patient self-entry, family-assisted operation, source labeling, and nurse repair remain governed | do existing systems handle this distinction? |
| Short clinician-review summary | how summary design supports rapid review without overclaiming | how common are similar clinician summaries? |

## Patent Reasoning Gate

Before any patent claim is drafted, answer:

1. What is the specific system logic?
2. What problem does that logic solve?
3. What is excluded by design?
4. What prior systems already do something similar?
5. What part is workflow logic rather than ordinary questioning?
6. What evidence shows the logic matters?

## Product Decision

## Product Question

Would a real clinic adopt this because it improves readiness or saves time without adding unacceptable burden?

## Adoption Hypotheses

| Hypothesis | Evidence needed | Decision impact |
| --- | --- | --- |
| Physicians will read a one-minute summary | physician feedback | continue or revise summary |
| Staff can support patients without added burden | workflow feedback | continue, narrow, or pause |
| Patients can answer core questions reliably | usability feedback | revise wording or assisted mode |
| Repeated questions are common enough to matter | workflow evidence | continue or pause |
| Safety wording is acceptable | clinician feedback | continue or revise boundary |

## Product Decision Matrix

| Decision | Evidence Pattern | Next Action |
| --- | --- | --- |
| Continue | clear pain, useful summary, acceptable burden | refine question tree and summary |
| Revise | useful problem, wrong format or wording | redesign the artifact |
| Narrow | value only for one symptom or patient group | focus the scope |
| Pause | no workflow slot, no adoption, or unsafe burden | preserve learning and stop product work |

## Product Anti-Goals

Do not let product planning become:

- a full roadmap
- hospital record integration planning
- autonomous medical advice
- voice-first exploration
- real patient-data collection
- broad platform strategy

## Extraction Output

After the next reviewer conversation, produce three short sections:

## Paper

- strongest claim:
- evidence:
- limitation:
- next evidence:

## Patent Reasoning

- system logic clarified:
- prior-art question:
- what not to claim:

## Product

- adoption signal:
- rejection signal:
- next smallest artifact:
