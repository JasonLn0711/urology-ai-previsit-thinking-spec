# Design Philosophy

## Core Belief

The safest first version is not the most autonomous system. It is the clearest system.

The purpose is to support a clinical conversation, not replace it. The system should make a clinician's first few minutes better prepared, not make the patient believe a medical decision has already been made.

## First Principles

The design begins from five first principles:

1. Repeated questions are workflow waste only if the answers are reliable and useful when collected earlier.
2. Previsit collection is valuable only when it reduces burden rather than shifting burden to patients or staff.
3. A summary is safer than a conclusion because it preserves clinician authority.
4. Missing information should be repaired before handoff, but uncertainty should never be hidden.
5. The first experiment should test workflow fit before any larger operational commitment.

## Design Values

## Restraint

The system should do less than it technically could. Restraint prevents premature diagnosis, unclear responsibility, and privacy exposure.

## Plainness

The system should use patient-understandable language and reviewer-understandable reasoning. If a decision cannot be explained plainly, it should not be hidden inside the system.

## Clinician Authority

The clinician remains the final interpreter. The system prepares context; it does not decide what the context means.

## Assisted Access

Older adults, low-literacy patients, mixed-language patients, and patients who need help are normal users. The design must allow patient self-entry, family-assisted operation, and nurse repair. Patient/family screens should stay separate from nurse and physician work screens.

## Low Burden

The system should fit the existing previsit rhythm. A design that saves physician time but consumes more nursing time may fail.

## Auditability

The system should make assumptions, boundaries, and evaluation criteria explicit. This is necessary for product review, paper framing, patent reasoning, and governance.

## Rejected Design Instincts

The project should not begin by asking, "How can artificial intelligence interview the patient?"

The better starting question is, "What repeated information does the clinic wish it already had before the physician-led visit begins?"

The design also rejects the instinct to collect every possible symptom detail. More data is not automatically better. In this workflow, excess detail can make summaries harder to read, privacy harder to govern, and patients more fatigued.

## Design Boundary

The system should feel like preparation, not care delivery. Its tone, output, and evaluation should all reinforce that boundary.
