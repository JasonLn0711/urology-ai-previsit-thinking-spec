# 北市聯醫深耕計畫會議摘要與重要訊號

Status: synthesized

## Purpose

This note preserves the concise meeting summary and strategic interpretation from the 2026-05-19 北市聯醫 deep-cultivation discussion.

Use this file when a reader needs the meeting's practical meaning quickly. Use `taipei-city-hospital-deep-cultivation-meeting-transcript.md` for the corrected detailed transcript.

## Meeting Core Themes

The meeting centered on:

1. 北市聯醫深耕計畫申請架構
2. 子計畫拆分與定位
3. PSA 社區篩檢與泌尿科應用
4. CRM / 智慧醫療 / APP 整合
5. ESG 與碳盤查可能納入方向
6. IRB、MOU、招標程序
7. KPI 與預算連動邏輯
8. Aging Clock 研究構想
9. AI 與智慧醫療場域整合
10. 分工與 2026-06-02 下一次會議安排

## Corrected Summary

## 1. Plan Structure And IRB

If the proposal goes out under 信義院外門診部, the formal owner will likely follow the relevant 健保代碼 responsible person.

Any participant involved in research planning, papers, human-subject content, patient records, PSA data, biomarker data, or patient privacy needs IRB training. The meeting repeatedly used nine hours as the required training target.

This applies beyond the PI. Collaborators, students, assistants, and anyone entering the data or research workflow need to be covered.

## 2. Three-Subproject Structure

The meeting converged on a three-part plan.

## 子計畫一: PSA / Community Screening

Core components:

- PSA screening
- 信義區 / community outreach
- possible male community screening route
- urology return flow
- SOP
- CRM
- case follow-up

Important nuance: screening is not enough. PSA screening must connect to return-to-hospital flow, case management, and follow-up.

The meeting also raised whether PSA blood draw could support additional biomarker collection. That possibility is not yet accepted as core scope.

## 子計畫二: Smart Healthcare / AI / CRM

Core components:

- APP
- CRM
- AI-assisted intake
- patient management
- API integration
- kiosk or front-end intake
- reminder systems
- possible smart-pharmacy or medication-reminder layer

The strongest statement from the meeting is that the hospital's immediate weakness is CRM / patient management, not AI model capability.

The useful claim is:

```text
front-end guided intake / reminders -> back-end CRM -> managed follow-up -> clinician review
```

AI, APP, ASR, kiosk, and API are support tools inside this service workflow.

## 子計畫三: ESG / Carbon Accounting / Sustainability

This is likely a policy and completeness layer:

- ESG
- carbon accounting
- green building / new-site management
- sustainable healthcare

It should support the deep-cultivation package but should not replace the clinical service mainline.

## 3. Smart Pharmacy And Medication Packaging

The meeting discussed the gap between hospital medication bags and outside-clinic medication packaging.

Possible smart-healthcare elements:

- medication reminders
- package-by-dose / meal-pack style medication support
- packaging machine
- inspection machine
- APP or LINE reminder
- CRM follow-up

Figures such as roughly one million for a packaging machine and around 1.7 million for an inspection machine were discussed as rough meeting-level references, not final budget.

## 4. MOU And Cross-Unit Cooperation

Potential MOU or collaboration targets include:

- 衛生局
- community clinics
- 聯合診所
- 忠孝院區
- university team
- community leaders or local units

Cross-unit cooperation matters for review. Partners should be selected deliberately and matched to the actual service workflow.

## 5. KPI And Budget Logic

The strongest administrative rule from the meeting:

```text
KPI must justify budget.
```

If the plan includes hardware, outsourced software, APP development, CRM, API integration, assistants, or biomarker testing, the corresponding plan content and KPI must already exist.

Budget should not appear as a disconnected wish list.

## 6. Tender / Outsourcing

The meeting repeatedly warned that outsourced CRM, APP, API, platform, questionnaire, or system work may trigger procurement or tender procedures.

Thresholds such as 200,000 NTD were discussed, but exact rules still need confirmation.

The practical implication is that the June 2 draft should mark:

- internal work
- outsourced work
- hybrid work
- procurement questions
- vendor deliverables
- rough budget categories

## 7. Aging Clock Research Direction

冠宇's Aging Clock direction is research-adjacent.

The concept:

```text
baseline blood/biomarker data -> biological-age estimate -> targeted intervention -> three-month follow-up -> compare biomarker or aging-speed change
```

Candidate markers mentioned:

- CBC / DBC
- inflammatory markers
- CRP
- oxidative stress
- ROS
- SOD
- MDA
- kidney function
- liver function
- hormone-related markers
- other accessible biomarkers

The proposed distinction from traditional Aging Clock work is to avoid relying only on expensive DNA methylation and instead explore accessible biomarkers suitable for a Taiwanese / Asian cohort.

## 8. 美如主任's Key Feedback

美如主任's feedback should be treated as a reviewer-risk map:

- This sounds like a research project.
- What is the data source: NHI database, community cohort, or new collection?
- What is the definition of aging?
- How many biomarkers are required?
- What is the intervention?
- How does this become an executable service workflow?

Until those are answered, Aging Clock should not be the center of the deep-cultivation proposal.

## Final Direction

The most coherent structure is:

```text
子計畫一: PSA + community screening + CRM + SOP
子計畫二: smart healthcare + AI + APP + guided intake + patient management + CRM/API
子計畫三: ESG + carbon accounting + sustainable healthcare
```

Expected workload:

- each group drafts its section
- total proposal likely around 70 real content pages after forms and attachments
- each subproject roughly 20-23 pages
- next discussion tentatively 2026-06-02 10:00

## True Strategic Signal

This meeting shows that 北市聯醫 is not asking for a pure research project or paper-only AI model.

The stronger direction is:

```text
AI Systems Engineering for Healthcare Deployment
```

In practical terms:

- CRM is central.
- AI is a tool.
- APP / ASR / kiosk / API are workflow supports.
- PSA screening is the clinical entry point.
- SOP and follow-up make it a service system.
- KPI, budget, procurement, IRB, MOU, and security governance determine whether it is fundable and executable.

The repo should therefore keep framing the urology smart-previsit system as a clinician-reviewed service and patient-management aid, not as an autonomous medical AI.

## Policy Context: Health Taiwan Deep-Cultivation Plan

The relevant policy context is `健康台灣深耕計畫(114-118年)`.

Official program materials frame it around four categories:

- 優化醫療工作條件
- 規劃多元人才培訓
- 導入智慧科技醫療
- 社會責任醫療永續

This meeting's strongest fit is:

```text
子計畫二 -> 導入智慧科技醫療
子計畫一 -> 社會責任醫療永續 / community-based integrated care
子計畫三 -> 社會責任醫療永續 / ESG / carbon footprint
CRM + reminders + workflow efficiency -> 優化醫療工作條件 + 智慧科技醫療
student / cross-domain work -> 規劃多元人才培訓, if explicitly designed
```

See `health-taiwan-deep-cultivation-policy-reference.md` for the source-backed policy reference.
