# 2026-05-12 imedtac Company AI Triage Sync

## Source

- Date: `2026-05-12`
- Meeting: 慧誠智醫 business / PM sync with Jason about future AI triage collaboration.
- Planning source bundle: `/home/jnclaw/every_on_git_jnclaw/phd-life-system/planning-everything-track/data/knowledge/personal/sources/2026-05-12-imedtac-company-ai-triage-sync/`

## Routing

This is a future-direction record, not a change to the current urology previsit discovery boundary.

Use it to reason about a possible product ladder:

`previsit structured intake -> clinician-review evidence -> urgent-care symptom intake -> vital-sign-aware triage support -> governed kiosk / HIS integration`

Do not treat it as approval to add triage, risk scoring, direct HIS connection, or real patient data to the urology MVP.

## Key Product Facts

- 慧誠 has a self-service vital-sign kiosk currently framed around outpatient / urgent-care style workflows.
- Default vital signs are blood pressure, SpO2, temperature, and for all-in-one SKU height/weight.
- Hardware is Windows-based all-in-one, fanless, no onboard GPU.
- Architecture context includes middleware, RESTful API, FHIR, HIS, and EMR.
- The company-side long-term target is English-first, voice-input, all-specialty symptom triage with vital-sign-aware result generation.
- The near-term ask is a presentable demo that can show 慧誠 / Wu-team collaboration before customer discussions.
- The short-term business pressure is an English AI-triage reference demo before a June US-customer visit, if scope and product/API materials arrive.

## Jason's Demo / Technical Position

- The current urology previsit demo was shown as an analogy: structured intake, dynamic question routing, patient/family support, nurse/clinician handoff, and optional ASR for free-form text.
- Dynamic question selection can use embedding-style semantic matching rather than only a fixed tree.
- CPU-only local execution is feasible for the lightweight structured-intake path.
- Full LLM/cloud/GPU use is an architecture choice, not a v0 requirement.
- English ASR is feasible but needs validation under kiosk noise, microphone quality, accent, and medical-vocabulary constraints.
- Vital-sign-to-triage meaning requires authoritative medical criteria and clinician/company validation.

## Action Items From Post-Meeting Summary

阿聖 side:

- organize an English symptom flow;
- re-check medical wording;
- study vital-sign integration;
- prepare an architecture diagram;
- clarify ASR + embedding-routing division;
- study local deployment feasibility.

慧誠 side:

- provide current kiosk / UI / product information;
- provide API / integration information;
- provide workflow and deployment scenario details;
- continue discussion on possible integration flow.

## Open Questions

1. What exact API or data export can the kiosk provide?
2. Is demo integration expected as iframe/link, shared UI, API handoff, or simulated flow?
3. Which vital-sign fields must influence the result for the demo to be meaningful?
4. Can v0 use simulated vital signs?
5. What source governs all-specialty urgent-care question modules?
6. What output wording is safe: "needs clinician review", "care level suggestion", "call emergency services", or another label?
7. Who signs off vital-sign thresholds and red-flag logic?
8. What is the smallest deliverable before the next meeting?

## Boundary

Current boundary remains:

- no diagnosis,
- no treatment advice,
- no autonomous triage,
- no urgent-care risk score in current MVP,
- no direct HIS / EMR / EHR integration,
- no real patient data in discovery,
- no invented clinical thresholds,
- no public disclosure of patent-sensitive or core ASR + LLM workflow details without explicit approval.
