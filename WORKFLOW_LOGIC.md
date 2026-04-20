# Workflow Logic

## Workflow Purpose

The workflow exists to prepare the visit, not complete the visit.

## Encounter Sequence

```text
patient arrives
-> previsit support begins
-> patient or helper selects main concern
-> system asks structured questions
-> system identifies missing information
-> patient or helper reviews answers
-> system creates clinician-review summary
-> clinician confirms, edits, ignores, or asks follow-up
```

## Key Workflow Decisions

### Patient Self-Filled vs Assisted

The system must support both self-filled and assisted use because some patients may have difficulty with phones, vision, language, or medical concepts.

### Structured Questions First

Structured questions reduce ambiguity and make summaries easier to review.

### Missing Information Before Summary

The system should ask for missing key fields before producing the final summary.

### Review Before Handoff

The patient or nurse should review answers before the clinician sees the summary.

### Clinician Owns Interpretation

The clinician can use, edit, or ignore the summary.

## Meeting Discovery Questions

The workflow must be tested against real clinic practice:

1. What happens between check-in and physician entry?
2. Which questions are repeated most often?
3. Which answers can be collected early?
4. Which topics must remain physician-led?
5. Who should operate the system?
6. What makes output useful?
7. What makes output unsafe?
8. What metric would prove value?
