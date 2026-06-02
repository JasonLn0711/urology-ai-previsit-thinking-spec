# Open Questions

## 2026-06-02 信義 Integrated PSA / AI / CRM Questions

These are the active v0.8 planning questions after the 2026-06-02 LINE minutes
and Jason responsibility clarification.

1. Who is final applicant / PI for the integrated 信義 package?
2. Who owns 忠孝院區泌尿科 PSA clinical SOP and Taiwan Urological Association guideline compliance?
3. Which PSA fields must be included in the AI / CRM workflow: eligibility, PSA value, abnormal flag, return appointment, contact status, or follow-up outcome?
4. What exact CRM output supports the abnormal-case return / tracking KPI `>= 70%`?
5. Is CRM an internal follow-up queue, patient messaging system, staff dashboard, vendor platform, or a phased combination?
6. Who owns CRM outsourcing, procurement, vendor acceptance criteria, maintenance, and exit / handoff after the project period?
7. What data route is planned for PSA + AI + CRM: no real data, QI/service improvement, IRB research, or mixed?
8. What privacy / consent wording is needed if CRM contacts patients or stores follow-up status?
9. What security review is required if CRM, AI 問診, ASR, APP, API, or vendor-hosted services are included?
10. Which budget lines are operating expense, outsourcing, personnel, software/service, or capital equipment, and how will the `30%` capital cap be checked?
11. Does AI 智慧問診 need ASR in v0.8, or should typed / QR / tablet intake remain the baseline?
12. Which owner validates the one-page summary `<= 60 秒` KPI?
13. Which owner validates CRM follow-up evidence for the `>= 70%` abnormal-case follow-up KPI?
14. Which sections of v0.7 can be reused directly, and which must be rewritten because CRM is now explicit outsourced scope?
15. Should v0.8 be written as a new full proposal body, an integration skeleton first, or a work-package insert for a parent proposal?
16. How finely should KPI be split so the NT$15,000,000 AI 智慧問診 / CRM allocation is reviewable by主管單位 and審查機關?
17. Which sub-KPIs support each budgetable line: proposal coordination, clinical workflow, AI summary, CRM outsourcing, data quality, staff burden, governance, procurement, maintenance, and annual reporting?
18. Which KPI evidence can be produced before real patient-data approval, and which must wait for QI/service/IRB/governance approval?

## Active Post-Meeting Questions

These are the highest-priority questions after the 2026-04-23 meeting and 許醫師 LINE follow-up materials.

1. Should the proposed first-three Phase 0 flows be accepted, revised, or replaced: `頻尿或夜尿`, `小便困難或尿不出來`, and `血尿或健檢發現潛血`?
2. Should v1 use named personas such as `小許醫師` and `Annie專科護理師`, or neutral `醫師 / 護理師` labels for hospital review?
3. Which exam-prep reminders can be shown before physician confirmation, and which must be hidden until nurse/physician review?
4. Who can join Phase 0 as a nurse or clinic-staff reviewer to judge burden and waiting-room fit?
5. What does 許醫師's patent filing or planned filing already cover, and what implementation space is safe for the team?
6. Does the current vendor relationship create exclusivity, data ownership, derivative-work, or confidentiality limits?
7. Who at 聯醫 owns privacy/security/HIS review before any real patient data, cloud storage, messaging, or writeback is discussed?
8. What metric would make 吳老師 and 許醫師 say v1 is worth moving from synthetic review to pilot-readiness review?
9. Which functions from the current `聯醫小幫手` and `陽明小幫手` must v1 match, and which must it intentionally omit?
10. Is `初步建議` / `檢查方向` wording acceptable only as physician-review context, or should v1 avoid that wording entirely?
11. Is local/on-prem deployment a Phase 1 requirement, or a later architecture experiment after workflow value is proven?

Do not treat these as product backlog items. They are gates that decide whether the next artifact should continue, revise, narrow, pause, or go to governance review.

## 2026-05-19 Expert Review Result

Current decision:

```text
Revise + Narrow.
```

Accepted near-term narrowing:

- Use `泌尿科門診前問診與醫師覆核摘要支持系統` as the proposal-facing name.
- Use `泌尿科門診前症狀蒐集與醫師覆核摘要輔助流程` as the safe descriptive boundary.
- Lead with Health Taiwan `範疇三：導入智慧科技醫療`; use `範疇一：優化醫療工作條件` as secondary support.
- Do not write the work as an `AI medical system`.
- Park CRM follow-up until a future confirmed next step.
- Superseded by 2026-06-02 responsibility clarification for the 信義 proposal lane:
  CRM outsourcing is now an explicit proposal-writing scope assigned by 美如主任,
  while procurement, privacy, security, data route, and maintenance ownership
  remain open gates.
- Treat ASR as an optional multilingual input layer only.
- Start with non-acute LUTS / OAB-like outpatients: nocturia, frequency, urgency, leakage, voiding difficulty, or weak stream.
- Treat visible blood, retention/current inability to urinate, fever/chills, and flank pain as patient-reported red-flag observations, not triage or risk judgments.
- Use `醫師覆核用 SOAP 架構參考摘要`, not `SOAP 病歷草稿`, `自動病歷`, or `自動產生 EMR`.

Resolved or parked items from the 2026-05-19 / v0.7 baseline:

- CRM execution was parked for v0.7. For the 2026-06-02 信義 lane, this is superseded: CRM outsourcing is now active proposal-writing scope, with activation still gated by procurement, privacy, security, data, and maintenance owners.
- First workflow hypothesis is after registration / while waiting, completed by patient or family with QR code or tablet.
- Partial summary is acceptable if the patient does not complete every field.
- Do not require nurses to complete all missing fields in the first version; nursing should only handle incomplete, conflicting, or red-flag-observation cases.

Still requires clinical confirmation:

- Whether the after-registration / waiting-room workflow slot is accepted by Duobao and clinical stakeholders.
- Whether physicians will read a one-page or 60-second summary.
- Whether the first version should show red-flag observations to nurses first, physicians first, or both.
- Which five fields must appear at the top of the clinician summary.
- Which summary fields are noise and should be hidden in a governance/reviewer view only.
- Whether `SOAP 架構之醫師覆核參考摘要` is safe wording for the hospital audience.

## 2026-05-19 Deep-Cultivation Grant Questions

1. For the 信義 integrated package, what is the exact service workflow from PSA screening to AI 問診, physician-review summary, CRM outsourced follow-up, and KPI evidence?
2. Which CRM functions are funded outsourced scope, and which remain later activation gates after procurement / privacy / security owner confirmation?
3. Will APP / ASR / API work be outsourced, staffed internally, or split into a hybrid plan if it moves beyond documentation?
4. What procurement threshold applies to APP, questionnaire, platform, API, or ASR-related outsourcing?
5. Which MOUs are required: community, clinics, 忠孝院區, 衛生局, university team, or vendors?
6. Who must complete nine-hour IRB training before touching research or patient data?
7. What security-governance documents or self-check forms are required for AI, APP, CRM, API, or patient-data flows?
8. Which KPI justify each budget line in the smart-healthcare previsit-summary subproject?
9. Should Aging Clock be excluded, included as a research appendix, or reframed as a biomarker follow-up service workflow?
10. Before 2026-06-02, what draft content is needed for the 20-23 page smart-healthcare / AI previsit-summary subproject section?
11. What portion of 子計畫二 is Jason personally drafting versus coordinating with 吳老師團隊, vendors, or hospital stakeholders?
12. Which Aging Clock items, if any, are Jason's responsibility rather than 冠宇's research responsibility?
13. Does Jason need to complete nine-hour IRB training before the next data-facing phase, or only before actual patient/research-data access?
14. Are kiosk / chronic-disease-system adaptation and smart-pharmacy components part of Jason's June 2 draft, or should they be parked as optional expansions?
15. Which official Health Taiwan category should lead 子計畫二: 導入智慧科技醫療 alone, or a combined 智慧科技醫療 + 優化醫療工作條件 framing?
16. Should the proposal explicitly include a 多元人才培訓 component for 吳老師團隊 / student cross-domain AI-healthcare work?
17. Which KPI demonstrate alignment with official deep-cultivation performance logic rather than only local project ambition?
18. Which external example is the closest comparison for 子計畫二: nursing voice AI, clinical documentation support, mobile service vehicle, integrated HIS/app, or AI governance/FHIR readiness?
19. Which example patterns should be explicitly cited in the June 2 draft, and which should remain background inspiration only?
20. When updating the sibling `urology-ai-previsit-demo` repo, which surfaces should say "deep-cultivation visit-readiness support" and which should remain demo-only?
21. What wording best separates `SOAP-like draft support for clinician review` from formal medical-record documentation?
22. Which integration language is acceptable for June 2: CRM readiness, API readiness, FHIR/TW Core IG readiness, mock export, or direct hospital-system connection?
23. Which KPI targets are realistic enough to include in the draft, and which should remain placeholders until hospital workflow review?
24. Which sections of `discovery/DEEP_CULTIVATION_PROPOSAL_WRITING_GUIDE.md` are required by the official blank proposal form, and which should be compressed into appendices?
25. Which KPI can be measured during synthetic walkthrough versus only after IRB/security-approved pilot use?
26. Which budget lines can Jason estimate now, and which require hospital procurement or vendor quotes?
27. If repository evidence is included, should reviewers receive GitHub URLs, a curated zip snapshot, selected PDFs/screenshots, or all three?
28. Which exact commit IDs from `urology-ai-previsit-thinking-spec` and `urology-ai-previsit-demo` should be cited in the proposal evidence package?

## Workflow Questions

1. What is the current patient flow from check-in to physician entry?
2. Which questions are repeated most often?
3. Which information can be safely collected before the physician enters?
4. Which topics must remain physician-led?
5. Should the first realistic version be patient self-entry, family-assisted operation with source labels, nurse repair, nurse-led selected cases, or mixed?
6. Where would the workflow fit without slowing staff down?
7. What does the current `陽明小幫手` actually do between registration/check-in and physician entry?
8. Does the current `聯醫小幫手` include patient-facing advice or exam-direction language that v1 must avoid?

## User Questions

1. Which patient groups would benefit most?
2. Which patient groups would struggle most?
3. What language, vision, literacy, or phone-use barriers are common?
4. What help should staff or family provide, and where should that help stop?

## Output Questions

1. What summary format would the physician actually read?
2. Which fields are useful and which are noise?
3. Should missing information, review flags, or both be shown?
4. Is a one-page summary enough?
5. Which wording would make clinicians distrust the output?
6. In the adaptive demo, does the clinician prefer seeing why the next question was selected, or only the final summarized answer?

## Adoption Questions

1. Who benefits most: patient, nurse, physician, or clinic flow?
2. What would make staff reject the workflow?
3. What would make clinicians trust it?
4. What would make clinicians ignore it?
5. What is the smallest useful next artifact?
6. Should the next artifact be a benchmark-difference table before any additional app build?
7. Does optional ASR reduce patient burden in practice, or does microphone setup and correction create a new workflow burden?

## Safety Questions

1. What wording is acceptable for red-flag observations?
2. What privacy model would be needed before real patient data?
3. What consent language would be required?
4. What failure reporting process would be needed in any future pilot?
5. What misunderstanding would be most dangerous for patients?
6. What current-app wording would make a patient think the system is giving advice instead of preparing a physician-reviewed note?
7. Who approves cloud vs local/on-prem deployment, encryption, logging, and maintenance before any hospital-network installation?
8. Which ASR errors would be most dangerous if they were silently converted into structured answers?

## 2026-05-03 Urgent-Care Triage Direction

1. Does `triage` mean previsit information readiness, queue prioritization, risk scoring, urgent-care triage, or another workflow?
2. Is the next artifact a product ladder from `協助醫生問診` to future AI triage, or a company-internal sandbox demo using the current urology MVP?
3. What HIS connection is being imagined: export, copy/paste, mock API, read-only lookup, writeback, or real queue/registration integration?
4. Which region is the first business context: Taiwan, US, Thailand, Malaysia, Central Asia, Middle East, or another market?
5. Who owns privacy/security, clinical responsibility, and regulatory language if the system moves beyond physician history-taking support?

## Decision Questions

1. Should the project continue after the physician conversation?
2. If yes, should the next step be a revised question tree, summary mockup, or assisted workflow test?
3. If no, what wrong assumption did the conversation reveal?
4. What evidence would change the decision later?
