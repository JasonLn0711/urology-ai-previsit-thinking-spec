# Assumptions

## System Assumptions

- The first useful version is a guided previsit workflow, not an autonomous medical interviewer.
- The main value is reducing repeated questions and improving visit readiness.
- After the 2026-06-19 owner update, the active near-term value frame is urology visit readiness through AI 問診 and physician-review summary, not CRM or patient-management system design.
- The deep-cultivation upgrade should be described as `urology previsit / visit-readiness / clinician-review summary support`, not AI triage and not CRM follow-up support.
- CRM is fully out of scope for Jason / 陽明交大 current planning. Do not plan CRM interface, data handoff, KPI, budget, procurement, vendor work, maintenance, or patient follow-up.
- The AI 問診 lane should provide structured intake, source labels, missing-field visibility, physician-review summary, reviewer evidence, and governance notes for its own workflow only.
- The `深耕子計劃三-吳育德+江慧珣團隊` lane should be tracked as a separate parent-proposal companion subproject, currently centered on high-age AI gait, sarcopenia screening, digital rehabilitation, and companion/simple robot planning.
- The 吳 + 江 子計畫三 lane should not change the urology previsit intended use unless a parent-proposal owner explicitly assigns a shared workflow, shared governance artifact, or shared KPI/budget table.
- Clinicians need a short review summary, not a full transcript.
- Patients may need nurse or family assistance.
- Older adults and mixed-language users are normal users, not edge cases.
- Missing-information prompts are safer than medical interpretation.
- Neutral review flags are safer than disease or urgency labels.

## Workflow Assumptions

- A usable moment exists before or during the waiting period, but this must be confirmed.
- Some urology questions are repeated often enough to justify previsit collection.
- Some information can safely be collected before the physician-led visit.
- Some topics must remain physician-led.
- A summary is useful only if clinicians can read it quickly and trust its boundaries.

## Discovery Assumptions

- The first physician conversation should test usefulness, not promise deployment.
- The smallest valid next artifact is a refined question tree plus a summary format.
- The next grant-facing artifact should map AI 問診, physician-review summary, KPI, NT$10,000,000 planning budget, governance, clinical review, and security/IRB gates before adding implementation detail.
- The next v0.8 grant-facing artifact should be an AI-only package; CRM should appear only as historical context if needed.
- The proposal-writing sequence should start from clinical pain, workflow fit, KPI, governance, and budget logic; AI/ASR/LLM method details should come after the service story is clear.
- Proposal scoring should be evidence-based and separated into clinical workflow value, technical engineering, governance, and MOHW format-compliance scores rather than collapsed into a reviewer impression.
- The project should pause if the clinic has no practical workflow slot.
- A negative or narrowing decision is still useful learning.

## Research-Adjacency Assumptions

- Aging Clock is not yet a core deep-cultivation claim.
- Aging Clock becomes proposal-ready only if the team defines its data source, aging definition, biomarker panel, intervention, follow-up interval, and service workflow fit.
- If Aging Clock uses PSA/community blood-draw infrastructure, it needs separate IRB and data-governance framing rather than being implied by the screening workflow.

## Safety Assumptions

- Diagnosis, triage, and treatment recommendations are out of scope.
- Real patient data is out of scope for discovery.
- Clinician review is mandatory.
- Red flags should be presented as observations only.
- Privacy governance must be explicit before any real patient data is considered.

## Audit Note

These assumptions are not facts. They are starting points to test through clinician review and workflow observation.
