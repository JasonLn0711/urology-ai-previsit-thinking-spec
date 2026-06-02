# Assumptions

## System Assumptions

- The first useful version is a guided previsit workflow, not an autonomous medical interviewer.
- The main value is reducing repeated questions and improving visit readiness.
- After the 2026-05-19 deep-cultivation meeting, the stronger near-term value frame is visit readiness plus patient-management / CRM follow-up, not AI model novelty.
- The deep-cultivation upgrade should be described as `urology previsit / visit-readiness / clinician-review summary / CRM follow-up support`, not AI triage.
- After the 2026-06-02 responsibility clarification, the 信義 proposal lane should be treated as one integrated package: original AI 智慧問診 / one-page summary + 忠孝院區泌尿科 PSA 主動篩檢 + 美如主任交辦 CRM 外包.
- CRM outsourcing is now an active proposal-writing scope for the 信義 package, while real operation, patient messaging, data retention, vendor hosting, and maintenance remain governance and procurement gates.
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
- The next grant-facing artifact should map PSA/community screening, SOP, CRM, APP/AI support, KPI, budget, procurement, and security/IRB gates before adding implementation detail.
- The next v0.8 grant-facing artifact should first be an integration skeleton that maps PSA, AI 智慧問診, CRM outsourcing, KPI, owner, budget, and governance before producing a new full proposal body.
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
