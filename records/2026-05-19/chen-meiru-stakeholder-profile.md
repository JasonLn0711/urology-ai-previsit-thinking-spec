# Stakeholder Profile: 陳美如主任

Date: 2026-05-19
Status: working stakeholder-introduction and proposal-review lens

## Purpose

This note records how to introduce 陳美如主任 and how to interpret her likely review priorities for the 北市聯醫 Health Taiwan deep-cultivation proposal.

This is not a personnel file or official title record. Before formal submission, the current title, appointment, and proposal role must be confirmed with 北市聯醫.

## Public Background Summary

陳美如主任 should be introduced as a Taipei City Hospital physician-administrator with a family medicine, community medicine, preventive health, chronic-care, older-adult care, and healthcare operations background.

Publicly visible or cited background includes:

- 臺北市立聯合醫院和平婦幼院區副院長 / 行政副院長 or related administrative role, depending on source and date.
- 家庭醫學科 and 社區醫學 background.
- 中國醫藥學院醫學系 background, according to the public physician-profile link supplied in the working material.
- Prior roles reported in project material: 北市聯醫社區醫學部主任、健康管理處處長、信義區衛生所主任、中興院區醫務秘書.
- Community-health and preventive-care work, including remote / telephone / video health follow-up and case-management style service models.
- Older-adult, home-care, whole-person care, and hospital-at-home adjacent interests.

Important source-backed signals:

- A public Health News report described her as 臺北市立聯合醫院社區醫學科主任 and described the `市民健康生活照護客服中心` as providing abnormal-blood-pressure reminders, health consultation, education, referral, and life-care follow-up by phone or video.
- A PGY training-program document lists 陳美如 as 家醫科 / 行政副院長 with professional background in 社區醫學、全人醫療、老人醫學.
- Public reporting around hospital violence identified her as 北市聯醫和平婦幼院區副院長 and emphasized staff safety, administrative handling, and colleague support.

Proposal implication:

```text
She is best understood as a public-hospital service-system leader, not only as an individual clinician or academic reviewer.
```

## Project-Context Role

In the 2026-05-19 北市聯醫 deep-cultivation meeting context, 陳美如主任 should be treated as a high-value proposal stakeholder because she is evaluating whether the idea can become a real hospital service workflow.

Her likely decision frame is not:

- Which LLM is newest?
- Which model has the best benchmark?
- Is the architecture technically impressive?
- Can this become a paper?

Her likely decision frame is:

```text
Can this enter 北市聯醫's real healthcare workflow, reduce burden, stay governable, and produce measurable service value without creating operational confusion?
```

## First-Principles Interpretation

The scarce resource for 陳美如主任 is not technical novelty. It is institutional execution capacity.

That means she will likely care most about:

1. Whether the proposed workflow is real.
2. Whether the system reduces work instead of adding another screen, form, or support burden.
3. Whether the service can connect across hospital, community, outpatient, and follow-up settings.
4. Whether patient safety, staff safety, privacy, cybersecurity, and responsibility are controlled.
5. Whether each claim can become a KPI, annual checkpoint, owner, budget line, and governance document.

For this reason, the correct framing is:

```text
AI-enabled healthcare workflow and service-system support.
```

Not:

```text
AI medical model / AI diagnosis system / AI triage product.
```

## Likely Highest-Priority Concerns

### 1. 醫護減壓

This is probably the first review lens.

She will likely ask:

- Does this reduce repeated history-taking?
- Does it reduce nursing or administrative phone burden?
- Does it reduce missing-information repair during clinic?
- Does it avoid shifting work from physicians to nurses?
- Does it avoid requiring staff to babysit a new app?

For the urology subproject, this means:

- The system should be written as previsit symptom collection and clinician-review summary support.
- Nursing involvement must stay limited to incomplete, conflicting, or red-flag-observation cases.
- The proposal should measure staff burden explicitly.

### 2. Real Workflow Landing

She will likely care whether the system has a concrete clinical slot.

Acceptable framing:

```text
報到後 -> 候診期間 -> 病人/家屬 QR code or tablet 填寫 -> partial or complete summary -> human review -> physician reads one-page summary
```

Weak framing:

```text
Patients use our AI platform someday before clinic.
```

The proposal should avoid claiming the workflow is already validated. Write it as a hypothesis to be confirmed by clinical stakeholders.

### 3. System Integration And Non-Island Design

Because her background is service-system and public-hospital operations, she will likely be skeptical of standalone demos.

She will likely ask:

- Where does this sit relative to HIS / EMR / registration / outpatient workflow?
- Who receives the output?
- Who owns follow-up?
- Can this connect to health management, CRM, case management, or community service later?
- If it stays standalone, what value survives after the demo?

For this project:

- Do not promise current HIS/EMR integration.
- Do write future interoperability readiness and governance conditions.
- Keep CRM follow-up parked for the current urology slice, but describe it as a future governed patient-management layer if the hospital reopens that scope.

### 4. Sustainable Operations

She will likely care about what happens after the project year.

Questions she may ask:

- Who maintains the system?
- Who updates the question bank?
- Who answers when staff report an error?
- Who pays for ASR, API, tablets, or vendor support?
- Can hospital IT or an approved vendor take over?
- What is the audit trail?

Proposal implication:

- Every technical feature should map to owner, governance, budget, and maintenance.
- Avoid demo-only language unless the phase is explicitly demo-only.

### 5. Executive Readability

She likely needs the proposal to be explainable to hospital executives, health-bureau stakeholders, and reviewers.

The one-sentence version should be:

```text
本子計畫先在非急性泌尿科門診導入受治理的門診前症狀蒐集與醫師覆核摘要流程，評估是否能減少重複問診、提升資料完整性，並建立未來智慧醫療與病人管理延伸所需的治理基礎。
```

Avoid:

```text
我們用 LLM / RAG / ASR / multi-agent 架構解決醫療問題。
```

### 6. Safety, Responsibility, And Governance

Given the hospital-administration context, she will likely care about:

- human-in-the-loop
- no AI diagnosis
- no autonomous triage
- no treatment or exam-order recommendations
- no automatic EMR writeback
- patient data boundary
- IRB / privacy / cybersecurity ownership
- auditability
- error reporting
- staff safety and escalation SOP

The current urology wording should therefore remain:

```text
醫師覆核用 SOAP 架構參考摘要
```

Not:

```text
自動病歷 / AI SOAP / AI EMR generation
```

### 7. Public-Hospital And Community Value

Her background points toward community medicine, health management, older-adult care, home care, and prevention.

For a 北市聯醫 deep-cultivation proposal, she may value:

- community screening and return-to-hospital flow
- chronic-care and preventive-care follow-up
- older-adult usability
- digital access for family helpers
- cross-site workflows across 聯醫院區, clinics, health centers, and community partners
- service equity and sustainability

For the current urology slice, do not over-expand into full CRM. Instead, preserve:

```text
future governed continuity-of-care / patient-management readiness
```

## How This Should Change Our Proposal

### Keep

- `泌尿科門診前問診與醫師覆核摘要支持系統`
- non-acute LUTS / OAB-like first scope
- after-registration / waiting-room intake hypothesis
- patient / family self-entry
- one-page clinician-review summary
- source labels
- missing-field display
- red-flag observations as patient reports only
- optional multilingual ASR
- no automatic EMR writeback

### Strengthen

- Add a short stakeholder-facing rationale: this is a workflow and governance project, not a model project.
- Add staff-burden KPI explicitly.
- Add maintenance owner and governance owner placeholders.
- Add pilot-readiness checkpoints before any real deployment claim.
- Add a future path for patient-management / CRM only as a governed later phase.

### Avoid

- Model-first explanation.
- Broad AI-transformation language.
- Claiming clinical benefit before workflow validation.
- Saying physicians will definitely read the summary.
- Saying nurses will complete the questionnaire.
- Saying this can already connect to HIS / EMR.
- Making CRM follow-up part of the immediate urology v0.1 scope after it has been parked.

## Suggested Introduction Paragraph

可在給團隊或專家看的文件中這樣介紹：

```text
陳美如主任是臺北市立聯合醫院體系內具家庭醫學、社區醫學、健康管理、預防醫學、高齡與全人照護背景的醫師與醫療行政主管。從其公開經歷與過去參與的市民健康生活照護、社區健康管理、在宅/高齡照護與院區行政工作來看，她看深耕計畫時，重點應不會只放在 AI 模型本身，而會放在服務流程能否落地、是否減少醫護負擔、是否能跨院區/社區/健康管理流程銜接、是否有清楚 KPI、治理、維運與責任歸屬。
```

## Suggested Meeting Framing

Use this when discussing the urology subproject with her or with people preparing materials for her:

```text
主任，我們這個子計畫目前不把它寫成 AI 診斷或 AI 分流，而是先寫成非急性泌尿科門診前的症狀蒐集與醫師覆核摘要流程。第一版只處理夜尿、頻尿、急尿、漏尿、排尿困難等穩定門診常見症狀，目標是確認候診期間是否能先整理病人/家屬可安全提供的資訊，讓醫師看到一頁式 summary，並評估是否減少重複問診與缺漏欄位。

我們想請您幫忙看的不是模型夠不夠炫，而是三件事：第一，這個流程在聯醫門診是否有可落地的 slot；第二，它會不會減輕醫師或護理負擔，還是反而增加一套工作；第三，這種寫法是否符合深耕計畫需要的 KPI、治理、跨單位合作與後續維運邏輯。
```

## Questions To Ask Her

1. 以聯醫實際門診流程，這個 intake 最適合放在報到前、報到後候診、護理站，還是診間內？
2. 她最擔心這個系統增加哪一種醫護負擔？
3. 如果要寫進深耕計畫，她會希望第一年 KPI 是流程設計、pilot 人數、醫師閱讀時間、護理負擔、還是病人完成率？
4. Red-flag observations 應該先給護理站、診間醫師、還是只在 summary 裡顯示？
5. 如果 CRM 暫時不做，是否可以寫成 `future governed patient-management readiness`？
6. 她希望看到哪一種 dashboard 或管考資料，才會覺得這不是 demo？
7. 這個子計畫需要哪些院內單位先同意：泌尿科、護理、資訊、資安、個資、IRB、門診行政、健康管理處、或院區主管？
8. 哪些詞會讓她或審查者覺得我們在做 AI 診斷、AI 分流或自動病歷？

## Sources

- 臺北市立聯合醫院和平婦幼院區 public site and physician-profile link supplied in the working material: `https://websrv01.tpech.gov.tw/drview/home/read?emp_no=DXD41`
- Health News, 2011-11-24, `「市民健康生活照護客服中心」 健康的推手`: `https://www.healthnews.com.tw/article/127`
- PGY community-medicine training-program document surfaced in public search, listing 陳美如 as 家醫科 / 行政副院長 with 社區醫學、全人醫療、老人醫學 background: `https://hlm.tzuchi.com.tw/tch/images/tzuchi3628/2025/03/20240307/PGY_113%E8%A8%88%E5%8A%83%E6%9B%B8%E9%80%81%E5%AF%A9%E9%80%9A%E9%81%8E%E7%89%88_1b132.pdf`
- Taipei Open Data public overseas-report record for 2025 World Hospital at Home Congress context: `https://data.taipei/api/dataset/667d5b10-d09f-4ed3-bef9-309bc09c1221/resource/6903cd70-6e96-4514-a4ca-41e14030688c/download`
- Mirror Media / SETN republication, 2026 hospital-violence administrative response context: `https://www.mirrormedia.mg/external/setn_1590502`
