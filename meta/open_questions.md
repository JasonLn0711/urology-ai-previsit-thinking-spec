# Open Questions

## 2026-05-19 Deep-Cultivation Grant Questions

1. For 子計畫二, what is the exact service workflow from guided intake to CRM follow-up?
2. Which CRM functions are required for the first proposal: reminders, lab-draw prompts, return-visit tracking, case-management status, medication reminders, or all of these?
3. Will CRM / APP / API work be outsourced, staffed internally, or split into a hybrid plan?
4. What procurement threshold applies to CRM, APP, questionnaire, platform, or API outsourcing?
5. Which MOUs are required: community, clinics, 忠孝院區, 衛生局, university team, or vendors?
6. Who must complete nine-hour IRB training before touching research or patient data?
7. What security-governance documents or self-check forms are required for AI, APP, CRM, API, or patient-data flows?
8. Which KPI justify each budget line in the smart-healthcare / CRM subproject?
9. Should Aging Clock be excluded, included as a research appendix, or reframed as a biomarker follow-up service workflow?
10. Before 2026-06-02, what draft content is needed for the 20-23 page smart-healthcare / AI / CRM subproject section?
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
6. Does optional ASR reduce patient burden in practice, or does microphone setup and correction create a new workflow burden?

## Safety Questions

1. What wording is acceptable for red-flag observations?
2. What privacy model would be needed before real patient data?
3. What consent language would be required?
4. What failure reporting process would be needed in any future pilot?
5. What misunderstanding would be most dangerous for patients?
6. Which ASR errors would be most dangerous if they were silently converted into structured answers?

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
