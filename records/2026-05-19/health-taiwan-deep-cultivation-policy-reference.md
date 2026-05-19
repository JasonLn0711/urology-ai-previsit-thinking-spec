# Health Taiwan Deep-Cultivation Policy Reference

Status: source-reference

## Purpose

This note records the official policy context for the `深耕計畫` discussed in the 2026-05-19 北市聯醫 meeting.

Use this note to keep the proposal framing aligned with the Ministry of Health and Welfare / Health Taiwan Deep-Cultivation policy direction.

## Verified Sources

Verified on 2026-05-19 from official/public program sources:

- 衛生福利部科技發展組：「健康台灣深耕計畫」專區
  `https://dep.mohw.gov.tw/TDU/cp-1567-82709-121.html`
- 健康台灣深耕計畫網站：計畫頁
  `https://htsprout.nhri.org.tw/dhplan.html`
- 健康台灣深耕計畫網站：簡介 / 四大範疇
  `https://htsprout.nhri.org.tw/introduce.html`
- 健康台灣深耕計畫網站：下載專區
  `https://htsprout.nhri.org.tw/download.html`
- 臺灣智慧醫療三大中心：健康台灣深耕計畫智慧醫療規範更新
  `https://aicenter.mohw.gov.tw/AC/cp-7200-82982-208.html`

## Local Official Document Archive

Downloaded official materials are stored under:

```text
records/2026-05-19/policy-documents/
```

Key local index files:

- `policy-documents/README.md`
- `policy-documents/manifest.md`

The archive includes the official download-page materials for application, execution, governance checklists, budget rules, QA, approved lists, source-page snapshots, and related briefing files as available on 2026-05-19.

## What The Plan Is

The relevant `深耕計畫` is the `健康台灣深耕計畫(114-118年)`.

It is a five-year national healthcare-system reform and investment program. Official materials describe it as a system-level effort to improve the medical environment, support healthcare workers, train talent, introduce smart medical technology, and strengthen sustainable / socially responsible healthcare.

Key official facts:

- Period: 114-118年, corresponding to 2025-2029.
- Execution period: five years.
- Approved budget: NT$48.9B.
- Planning logic: applicants should propose bottom-up, concrete, diverse, innovative, long-term deep-cultivation strategies and performance indicators.
- Policy frame: systemic reform for healthcare environment improvement, health-system sustainability, and national health benefit.

## Four Official Categories

## 1. 優化醫療工作條件

Officially relevant aims include:

- improve healthcare-worker value and work environment
- optimize hospital resource allocation
- expand technology investment to reduce workload
- retain medical workforce

Meeting relevance:

- CRM, reminders, guided intake, summary generation, and workflow automation should be framed as reducing avoidable workload and repeated work.

## 2. 規劃多元人才培訓

Officially relevant aims include:

- continuing education and professional development
- cross-disciplinary collaboration and learning
- incentives for difficult / critical specialties
- clearer career development paths

Meeting relevance:

- 吳老師團隊, student involvement, IRB training, AI/medical collaboration, and cross-domain proposal writing fit here only if the proposal states a concrete training and collaboration mechanism.

## 3. 導入智慧科技醫療

Officially relevant aims include:

- AI technology assisting clinical care
- internationally connected medical technologies and techniques
- improved care workflow and efficiency
- medical data sharing and security
- smart-hospital development

Meeting relevance:

- This is the strongest official home for 子計畫二.
- Urology previsit intake, ASR, adaptive questioning, APP, CRM, API, reminders, and clinician-review summaries should be written as smart-healthcare tools that improve workflow and efficiency.
- Data sharing and security must be framed as governed, not assumed.

## 4. 社會責任醫療永續

Officially relevant aims include:

- tiered medical care and community-based integrated care
- improved access and equity
- healthy lifestyle support
- carbon-footprint reduction and green hospitals
- ESG management

Meeting relevance:

- 子計畫一's community PSA screening and 子計畫三's ESG / carbon accounting align here.
- The meeting's emphasis on community, clinics, MOU, and new-site sustainability should be mapped to this category.

## Policy-Aligned Interpretation For This Repo

The meeting should not be understood as simply asking for an AI model.

The policy-aligned interpretation is:

```text
PSA/community screening + SOP + CRM + guided intake + reminders + clinician-review summary + governed follow-up
```

This connects to official categories as follows:

| Proposal element | Official category fit |
| --- | --- |
| Guided intake / ASR / adaptive questioning | 導入智慧科技醫療 |
| CRM / reminder / follow-up workflow | 優化醫療工作條件 + 導入智慧科技醫療 |
| KPI-budget linkage | Program execution discipline |
| IRB / privacy / data security | 導入智慧科技醫療: medical data sharing and security |
| Community PSA screening | 社會責任醫療永續 |
| MOU with clinics / hospital units / community partners | 社會責任醫療永續 + vertical integration |
| ESG / carbon accounting | 社會責任醫療永續 |
| Student / cross-domain AI-healthcare work | 規劃多元人才培訓, if explicitly designed |

## Implication For 子計畫二

子計畫二 should be written as:

```text
智慧科技導入以支援泌尿科 PSA / community screening 的 visit-readiness, CRM follow-up, and clinician-reviewed care workflow.
```

It should not be written as:

```text
standalone AI model research
```

The proposal should emphasize:

- workflow efficiency
- reduced repeated work
- patient-management continuity
- data security
- clinician review
- interoperability readiness only at a governed planning level
- measurable KPI

## Boundary

The policy direction supports smart healthcare, but it does not remove this repo's safety boundary.

Still out of scope without separate governance:

- diagnosis
- treatment advice
- autonomous triage
- urgency or risk score
- real patient data during discovery
- direct HIS / EMR / EHR integration
- clinical effectiveness claims

## Next Use

Use this note when drafting:

- 子計畫二 smart-healthcare / AI / CRM section
- KPI and budget mapping
- June 2 follow-up questions
- policy-alignment paragraph in grant text
- `AI Systems Engineering for Healthcare Deployment` framing
