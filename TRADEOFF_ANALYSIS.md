# Trade-Off Analysis

## Core Trade-Off

The system trades autonomy for safety and auditability.

It does not try to be a smart medical interviewer. It tries to be a reliable previsit preparation aid. That choice makes the system less impressive at first glance, but easier to review, trust, and improve.

## What Was Sacrificed

## Conversational Naturalness

Structured questions are less flexible than open conversation.

Why sacrificed: structured answers are easier for patients to review and easier for clinicians to scan. They also reduce the risk that open language will be over-interpreted.

## Diagnostic Power

The system intentionally avoids diagnosis.

Why sacrificed: diagnosis belongs to the clinician. Adding diagnostic language would change the safety, trust, and governance profile of the whole concept.

## Broad Medical Coverage

The system does not try to collect a complete medical history.

Why sacrificed: the target problem is repeated previsit information, not total patient modeling. Broad capture would increase burden and reduce clarity.

## Real-World Data Realism

The discovery phase avoids real patient data.

Why sacrificed: early learning should not create privacy exposure before workflow value is proven.

## Integration Ambition

The system does not begin by connecting to hospital record workflows.

Why sacrificed: integration can make a weak workflow look serious. Workflow value should be proven first.

## Voice-First Convenience

Voice is not treated as the main first path.

Why sacrificed: noise, accents, mixed language, older-adult speech, and privacy concerns can shift attention away from the core workflow question.

## Rejected Alternatives

| Alternative | Why It Was Rejected |
| --- | --- |
| Autonomous medical interviewer | Blurs responsibility and may create unsafe trust |
| Voice-first main workflow | Speech capture risk may dominate early discovery |
| Full medical-history intake | Too burdensome and too far from the repeated-question problem |
| Hospital integration first | Solves operational routing before usefulness is proven |
| Transcript output | Gives clinicians more reading rather than a concise starting point |
| Real patient pilot first | Creates governance burden before the concept earns it |

## Counterfactual Design

If the system were autonomous, the key question would become "Can it safely decide?" That is the wrong first question. The right first question is "Does this help the clinician prepare?"

If the system were voice-first, a failed test might reflect speech capture problems rather than workflow value.

If the system collected real patient data immediately, review would focus on privacy and consent before anyone knows whether the workflow helps.

If the system integrated first, effort could be spent on routing information that clinicians do not actually want.

If the system produced transcripts, clinicians might receive more text and less clarity.

## Generalization

The same trade-off pattern applies to other expert-preparation contexts:

- collect only repeated, useful pre-encounter facts
- avoid pretending to make expert judgment
- show missing information before handoff
- keep outputs short and reviewable
- evaluate workflow value before expanding

This can apply to healthcare, legal consultations, insurance claims, education advising, support escalation, and other settings where better preparation helps but final judgment must stay with a human expert.
