# 2026-05-19 Demo ASR Readiness Record

Status: captured

## Purpose

Record the governance meaning of the 2026-05-19 local demo readiness check.

This is not an implementation runbook. The runnable UI, ASR launcher, tests,
and synthetic demo artifacts remain in the sibling `urology-ai-previsit-demo`
repository.

## Observed Demo State

Facts from the local synthetic-data demo check:

- Adaptive intake route was available at
  `http://localhost:4173/app/adaptive-intake/`.
- Clinician summary route was available at
  `http://localhost:4173/app/clinician/`.
- Visit packet route was available at
  `http://localhost:4173/app/clinician/visit-packet/`.
- Local ASR health check returned `ok: true`.
- ASR backend reported `device: cuda`, `computeType: int8`, and
  `noCpuFallback: true`.
- ASR hardware reported `NVIDIA GeForce RTX 4090 Laptop GPU`.
- ASR preprocessing reported fixed `denoise -> normalize` order.
- Demo readiness check passed in the demo repo with:
  - unit tests: 48/48
  - smoke checks: 159/159
  - V2 freeze checks: 257/257

## Governance Interpretation

The useful claim is still narrow:

```text
The system can collect patient-reported previsit information, accept typed or
local ASR input as an input layer, dynamically choose the next governed
previsit question, and prepare role-separated review surfaces for clinician
inspection.
```

The ASR result supports demo readiness only. It does not prove real clinic
microphone reliability, noisy-environment performance, patient usability,
Mandarin/Taiwanese mixed-language robustness, or clinician usefulness.

The adaptive-questioning result supports the current AI-value framing:

```text
AI value = governed next-question selection from current patient state.
Not AI value = chatbot diagnosis or autonomous triage.
```

## Boundaries Preserved

The readiness check does not authorize:

- real patient data
- diagnosis
- triage or urgency labels
- treatment recommendations
- exam ordering
- HIS, EMR, EHR, registration, or queue integration
- production clinical-use claims

The clinician remains the interpreter. The system prepares context and
highlights patient-reported observations for review.

## Next Review Questions

Before treating the ASR-ready adaptive demo as more than a local evidence
artifact, answer:

1. Would the physician actually read the clinician summary or visit packet?
2. Does ASR reduce patient burden, or does microphone setup create a new burden?
3. Which answers must remain click/typed fallback even if ASR is available?
4. Does adaptive next-question selection ask fewer noisy questions than a fixed
   flow while still preserving safety boundaries?
5. What feedback would justify revising the governed question set rather than
   only improving the UI?
