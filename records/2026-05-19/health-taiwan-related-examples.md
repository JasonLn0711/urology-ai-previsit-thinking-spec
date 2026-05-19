# Health Taiwan Deep-Cultivation Related Examples

Status: source-reference

## Purpose

This note answers:

```text
你在網路上找得到深耕計畫的相關計畫實例嗎？
```

It records example patterns that can help shape the 北市聯醫 / urology smart-previsit proposal.

Use this as a proposal-pattern note, not as proof that the urology project has already been validated.

## Source Confidence

| Confidence | Meaning |
| --- | --- |
| Official outcome | Published by MOHW as Health Taiwan Deep-Cultivation result or official plan material. |
| Official guidance | Published by MOHW / Health Taiwan / AI Center as rules, examples, or writing guidance. |
| Reported hospital case | Public media or industry-platform report about a hospital's Health Taiwan / deep-cultivation case. Useful for pattern learning, but verify before formal citation. |

## Example 1: Nursing Voice AI Assistant / E-Paper Bedside Card / Smart Medication Cabinet

Source type: official outcome.

Source:

- MOHW news, `健康臺灣深耕計畫展現豐碩成果：四大核心驅動，部立醫院攜手打造智慧永續新醫療`
  `https://www.mohw.gov.tw/cp-7398-86226-1.html`

What was reported:

- nursing voice AI assistant
- e-paper bedside card
- smart medication cabinet
- technology used to replace ineffective time and reduce clinical documentation burden

Why it matters for this repo:

- This is the closest public official pattern to `ASR + clinical workflow + workload reduction`.
- It supports positioning ASR and summary generation as staff-burden reduction, not as patient-facing diagnosis.
- It directly supports this repo's `clinician-review summary` and `voice as input layer` framing.

Proposal lesson:

```text
ASR is strongest when framed as reducing repeated documentation and handoff burden.
```

## Example 2: Voice AI For Clinical Note Drafting / Handoff Summary

Source type: official guidance.

Source:

- `健康台灣深耕計畫（114-118 年度）` official plan PDF
  `https://htsprout.nhri.org.tw/UploadFile/DHPlan_1140227.pdf`

What the official plan says:

- under smart-healthcare execution strategies, it includes voice AI assisting clinical-record drafting and handoff-summary style documentation work
- it also names AI, workflow efficiency, medical data sharing/security, and smart hospital development

Why it matters for this repo:

- It supports `previsit summary`, `SOAP-like draft`, and `handoff summary` as policy-aligned directions, as long as they remain clinician-reviewed.
- It does not authorize autonomous diagnosis or treatment advice.

Proposal lesson:

```text
Summary generation should be written as draft support for clinician review, not as final clinical documentation.
```

## Example 3: Smart Medical ALL-IN-ONE Mobile Service Vehicle

Source type: reported hospital case via HST / Joint Commission of Taiwan industry platform.

Source:

- `台南市立醫院通過「健康台灣深耕計畫」核定以智慧醫療打造行動式5星級健康服務`
  `https://www.hst.org.tw/tw/story/content/5806`

What was reported:

- Tainan Municipal Hospital received Health Taiwan Deep-Cultivation approval.
- Direction: smart healthcare and community care upgrade.
- Elements included digital governance, clinical AI, cross-hospital data exchange, telemedicine, rural medical-care integration, chronic-disease management, community health promotion.
- The case described an `ALL IN ONE` mobile medical vehicle with 5G, ultrasound, EKG, X-ray, vital-sign tools, ENT scope, HIS, and service tracking.
- The report also described an intelligent health service platform linking clinics, long-term-care institutions, home integrated care, community health units, AI health-risk prediction, telecare, smart whiteboards, and AI voice records.

Why it matters for this repo:

- This is a strong example of `workflow + deployment + integration`, not single-model AI.
- It is close to the meeting direction of kiosk, vital signs, community outreach, CRM, and follow-up.
- It shows how a proposal can combine hospital, community, long-term care, mobile service, AI, and HIS-adjacent tools under one service package.

Proposal lesson:

```text
A strong proposal is a service system with field deployment, not a standalone model.
```

## Example 4: AI Imaging / LUNG CAD + Integrated HIS + Health App

Source type: reported hospital case via UDN.

Source:

- `仁慈醫院響應「健康台灣」成果 AI診斷、科技整合打造韌性醫療`
  `https://udn.com/news/story/7266/9490558`

What was reported:

- Jen-Ai / Mercy hospital presented Health Taiwan Deep-Cultivation results.
- The report mentioned AI lung imaging assistance, an integrated medical information system covering outpatient, emergency, and ward operations, and a digital health-management app for blood sugar, blood pressure, and cholesterol uploads.
- The same report also mentioned green-hospital waste reduction.

Why it matters for this repo:

- It shows a common Health Taiwan pattern: AI assistance plus information-system integration plus patient-facing health-management app plus green-hospital metrics.
- The risk is that imaging AI can be too model-centric if not tied to workflow. This repo's stronger angle is workflow integration from intake to clinician review.

Proposal lesson:

```text
If using AI examples, pair them with workflow efficiency, operational integration, and measurable hospital outcomes.
```

## Example 5: FHIR / TW Core IG / AI Governance / Security Governance

Source type: official guidance.

Sources:

- Taiwan Smart Healthcare AI Centers announcement: `重要公告｜健康台灣深耕計畫智慧醫療規範更新上線`
  `https://aicenter.mohw.gov.tw/AC/cp-7200-82982-208.html`
- Official plan PDF: `健康台灣深耕計畫（114-118 年度）`
  `https://htsprout.nhri.org.tw/UploadFile/DHPlan_1140227.pdf`

What official guidance says:

- For 範疇三 `導入智慧科技醫療`, proposal writing should account for three governance cores: cybersecurity governance, data governance, and AI governance.
- Data should use FHIR and TW Core IG integration.
- AI applications should follow ethical principles including autonomy, transparency, accountability, safety, fairness, sustainability, and privacy protection.
- The official plan also references responsible AI implementation, clinical AI validation / evidence, AI impact evaluation, SMART on FHIR patterns, and international terminology standards such as LOINC, SNOMED CT, and RxNorm.

Why it matters for this repo:

- Governance is not optional. It is part of the proposal's maturity.
- This repo already has a strong boundary around clinician review, no real patient data during discovery, no diagnosis, no autonomous triage, and no direct HIS/EMR integration.
- A June 2 draft should include governance as a first-class work package.

Proposal lesson:

```text
FHIR / TW Core IG / responsible AI / auditability / human-in-the-loop should be included as planning and governance readiness, not premature integration promises.
```

## Pattern Summary

Successful or policy-aligned examples usually combine:

- workflow improvement
- staff workload reduction
- AI as a tool, not the whole claim
- system integration
- measurable KPI
- governance
- cross-unit or community collaboration
- sustainability / ESG when relevant

Less persuasive framing:

```text
We have a strong AI model.
```

More persuasive framing:

```text
We use AI, ASR, APP, CRM, and governed data flow to improve a real healthcare workflow and reduce avoidable burden while preserving clinician authority.
```

## Direct Implications For Urology Smart-Previsit

The current urology direction is closest to:

```text
intelligent clinical intake and visit-readiness infrastructure
```

Useful components to borrow from the examples:

- ASR / voice input as documentation-burden reduction
- structured previsit summary as clinician-reviewed draft support
- kiosk or front-end intake only if it fits a real waiting-room or community workflow
- vital-sign / biomarker / PSA data only with governance and clear workflow
- CRM follow-up as the service backbone
- FHIR/TW Core IG as future governed integration readiness
- AI governance, auditability, lifecycle management, and physician override as proposal differentiators

## Missing Pieces For The June 2 Draft

The examples suggest that this repo's June 2 draft still needs:

1. KPI with measurable targets.
2. Clinical workflow map: when the patient starts, who helps, where the summary appears, and how the clinician reviews.
3. Governance package: cybersecurity, data governance, AI governance, human-in-the-loop, logging, and failure handling.
4. System boundary: no autonomous diagnosis, treatment, triage, or direct HIS/EMR integration.
5. Deployment story: how PSA screening, guided intake, reminders, and CRM become one service path.
