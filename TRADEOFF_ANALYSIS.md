# Trade-Off Analysis

## Core Trade-Off

The system trades autonomy for safety.

It does not try to be a smart medical interviewer. It tries to be a reliable previsit preparation aid.

## What Was Sacrificed

### Conversational Naturalness

Structured questions are less flexible than open conversation.

Reason: structure makes answers easier to review and safer to summarize.

### Diagnostic Power

The system intentionally does not diagnose.

Reason: diagnosis belongs to the clinician.

### Integration Ambition

The MVP does not begin with hospital system integration.

Reason: integration would add complexity before proving workflow value.

### Realism From Real Patient Data

The MVP avoids real patient data.

Reason: synthetic data enables faster, safer discovery.

### Voice-First Experience

Voice is not the main path.

Reason: accent, noise, elderly speech, mixed language, and transcription uncertainty create early risk.

## Rejected Alternatives

| Alternative | Why Rejected |
| --- | --- |
| Voice-first AI interviewer | Too much early risk from speech errors, privacy, and overclaiming |
| Autonomous triage | Crosses into clinical decision-making |
| Full medical-history intake | Too burdensome and privacy-heavy for discovery |
| EHR/HIS integration first | Solves technical routing before proving value |
| Free-text transcript output | Gives clinicians more reading instead of a useful summary |
| Real patient pilot first | Governance burden is too high before workflow value is proven |

## Counterfactuals

If the system were voice-first, the meeting would focus on speech accuracy instead of workflow value.

If the system diagnosed, safety and trust would become the central objections.

If the system stored real patient data, privacy governance would dominate discovery.

If the system integrated first, the team might build a technically impressive but clinically unused tool.

## Design Choice

The chosen MVP is deliberately modest:

```text
guided questions
-> missing information
-> patient review
-> clinician-review summary
```

This is the smallest structure that can test workflow usefulness without pretending to be clinical intelligence.
