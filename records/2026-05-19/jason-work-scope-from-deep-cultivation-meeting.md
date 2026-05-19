# Jason Work Scope From 2026-05-19 Deep-Cultivation Meeting

Status: synthesized

## Purpose

This note answers:

```text
這篇錄音檔裡面，Jason 的詳細工作是什麼？
```

Source:

- Corrected transcript: `taipei-city-hospital-deep-cultivation-meeting-transcript.md`
- Meeting capture: `deep-cultivation-meeting-capture.md`
- Decision record: `deep-cultivation-decision-record.md`

## Attribution Boundary

The recording does not consistently name `Jason` directly. It assigns work to:

- `吳老師`
- `老師的弟子`
- `學生團隊`
- `吳老師與學生團隊`
- in one research segment, `冠宇`

Therefore, this note treats Jason's work as the actionable work package for Jason as a member of 吳老師團隊 / student side. It separates explicit team assignments from inferred Jason follow-up.

## Short Answer

Jason's main job is not to build a production system immediately.

Jason's meeting-derived job is to help turn the 智慧醫療 / AI / CRM direction into a fundable, governed subproject draft for the deep-cultivation proposal.

The practical work is:

```text
write 子計畫二 -> map PSA/community screening into guided intake and CRM -> define KPI -> map budget -> flag IRB/security/procurement gates -> keep AI inside clinician-reviewed service workflow
```

用中文說，Jason 在這次會議後的角色比較像：

```text
技術研發與計畫落地的轉譯者
```

也就是把臨床端提出的 PSA 篩檢、回診追蹤、CRM、APP、AI 問診、kiosk、智慧藥局等想法，整理成可以放進正式深耕計畫書的子計畫二內容，並且讓內容符合 KPI、預算、IRB、資安、委外與招標邏輯。

## 中文詳細工作整理

## 1. 撰寫智慧醫療子計畫

會議中最明確落到吳老師團隊 / 學生團隊的工作，是協助撰寫第二個範疇，也就是智慧醫療相關子計畫。

Jason 需要把子計畫二寫成一個能被審查者理解的服務計畫，而不是單純技術展示。

內容應包含：

- APP / guided intake
- AI-assisted 問診或小幫手
- CRM / 病人管理
- API 或訊息通知串接
- 回診提醒
- 抽血提醒
- 用藥提醒
- clinician-review summary
- 與 PSA / 社區篩檢後續追蹤的銜接

Jason 也需要替這個子計畫整理第一年、第二年、第三年的 KPI。KPI 必須同時有量化與質化邏輯，並且每個預算項目都要能回扣到 KPI。

## 2. 補齊 IRB 訓練與資料治理前提

會議中反覆提醒，只要進入研究計畫、處理人體資料、病人資料、PSA 資料、biomarker 資料，或參與後續 paper / research workflow，就需要 IRB 訓練。

因此，若 Jason 會進入這些資料或研究流程，Jason 的工作之一就是補齊九小時 IRB 訓練，或至少在計畫書中把這個要求列成團隊進場條件。

這不是行政附註，而是進入計畫、資料與結案流程的基本門檻。

## 3. 規劃智慧醫療系統架構，但先停在 proposal / governance 層

錄音裡討論了許多系統架構方向，包括：

- 將既有 kiosk / 慢性病管理 / 衛教或前端互動系統改成泌尿科或 PSA 相關版本
- 建立 CRM，補足醫院目前病人管理不足的問題
- 串接前端問診、抽血提醒、回診提醒、用藥提醒與後端病人追蹤
- 評估 API、LINE / APP notification、平台或資料串接
- 評估智慧藥局、餐包、包藥機、檢視機等是否能成為智慧醫療的一部分

Jason 的責任不是直接承諾要把這些系統全部做出來，而是把它們整理成 proposal 可審查的架構：

```text
clinical need -> service workflow -> system component -> KPI -> budget -> governance gate
```

例如：

- 如果寫 CRM，就要說明 CRM 解決哪個病人管理問題。
- 如果寫 APP，就要說明 APP 支援哪個回診或問診流程。
- 如果寫 API，就要說明 API 串接哪個通知、資料或 CRM 功能。
- 如果寫智慧藥局，就要說明它是否真的是本案必要服務環節，而不是額外願望清單。

## 4. 把委外、招標與預算寫成可審查邏輯

會議中很明確提到，CRM、APP、平台、問卷、API 或其他系統外包，可能會碰到招標與行政程序。

Jason 要處理的是：

- 哪些工作內部做？
- 哪些工作需要委外？
- 哪些工作可能需要招標？
- 估價是否要乘以 1.2-1.3 作為通膨與未來成本緩衝？
- 外包交付物是什麼？
- 驗收標準是什麼？
- 預算如何對應 KPI？

這表示 Jason 的工作不是只寫「要做 CRM」，而是要寫成：

```text
為了達成某 KPI，需要某 CRM 功能，因此需要某預算 / 外包 / 人力 / 資安文件。
```

## 5. 把 AI 控制在工具角色

這場會議的重要訊號是：北市聯醫要的不是 pure AI model research，而是可以落地的醫療服務系統。

因此 Jason 要避免把子計畫二寫成：

```text
我們要做一個 AI 醫生 / AI 診斷 / AI triage 系統。
```

比較安全且符合會議方向的寫法是：

```text
AI / APP / ASR / API 是輔助病人資料蒐集、提醒、CRM 追蹤與 clinician review 的工具。
```

Jason 要守住：

- no diagnosis
- no treatment recommendation
- no autonomous triage
- no risk scoring
- no direct HIS / EMR / EHR integration as current scope
- clinician remains responsible for interpretation

## Explicit Work Assigned To 吳老師團隊 / Students

## 1. Write The Smart-Healthcare Subproject

The transcript says the second scope, 智慧醫療, needs help from 吳老師 and the student team.

For Jason, this means preparing the 子計畫二 draft around:

- smart healthcare
- APP or guided intake
- AI-assisted previsit workflow
- CRM / patient management
- API or messaging integration
- reminders for visit, lab draw, medication, and follow-up
- clinician-review summary and safe handoff

This is a writing and planning task first. It should not become an implementation spec before the proposal frame is accepted.

## 2. Turn CRM Into The Core Operational Logic

The meeting repeatedly emphasized that the hospital weakness is patient management, not AI.

Jason should frame the system as:

```text
PSA/community screening -> guided intake -> lab/visit reminder -> return visit -> case management -> CRM tracking -> clinician review
```

The previsit AI system should be positioned as a governed input and readiness layer inside CRM, not as a standalone chatbot.

## 3. Define KPI Before Budget

Jason needs to draft KPI before writing budget lines.

Possible KPI categories:

- number of PSA/community participants reached
- percentage of screened participants with completed follow-up workflow
- return-visit completion rate
- reminder delivery / response rate
- CRM enrollment or tracking completeness
- guided-intake completion rate
- missing-information reduction before visit
- clinician-review summary completion rate
- staff / patient usability feedback
- IRB, security, and procurement gates completed

Budget cannot be justified unless it maps to these KPI.

## 4. Draft Budget Categories And Outsourcing Questions

The meeting emphasized that CRM, APP, API, platform, and questionnaire work may require outsourcing and tender / procurement procedures.

Jason should identify, not finalize:

- which work is internal
- which work is outsourced
- which work is hybrid
- rough cost categories
- whether estimates need a 1.2-1.3 multiplier
- what vendor questions need to be answered before June 2
- what procurement threshold applies
- what the acceptance / deliverable criteria would be

Candidate budget categories:

- research assistant or project coordinator
- CRM platform customization
- APP / guided-intake development
- API or messaging integration
- kiosk or front-end device only if justified
- adaptation of existing chronic-disease / CKD-style patient-management tools into a urology or PSA-follow-up version, if the team can justify fit
- pharmacy or medication-packaging integration only if it maps to a clear KPI and service path
- security-governance documentation
- vendor / procurement cost

## 5. Surface IRB, Privacy, MOU, And Security Gates

Jason should not treat governance as paperwork after the fact.

The draft must make these gates visible:

- nine-hour IRB training for people entering research or patient-data work
- IRB path if PSA, biomarker, medical record, or private patient data are collected
- MOU needs for hospital units, clinics, community partners, university team, or government units
- security-governance review for APP, CRM, AI, API, platform, or patient-data flows
- no real patient data during discovery
- clinician remains responsible for interpretation

## 6. Coordinate 子計畫二 With 子計畫一

Jason's smart-healthcare draft cannot float separately.

It should explicitly connect with 子計畫一:

```text
PSA screening event -> abnormal or follow-up-needed case -> return-to-hospital SOP -> CRM tracking -> reminder / guided intake -> clinician review
```

This makes 子計畫二 useful to the clinical mainline instead of a disconnected AI add-on.

## 7. Keep AI As A Tool, Not The Claim

Jason should avoid writing the proposal as:

```text
AI model project
```

The safer meeting-aligned framing is:

```text
service workflow + CRM + guided intake + clinician review
```

AI / ASR / adaptive questioning / APP can appear as supporting mechanisms.

They should not imply:

- diagnosis
- treatment advice
- autonomous triage
- risk scoring
- queue reprioritization
- direct HIS / EMR / EHR integration

## 8. Handle Aging Clock Carefully

Aging Clock was presented by 冠宇, not clearly assigned to Jason as the main owner.

Jason's likely role is to record the boundary and help decide whether it belongs in the proposal.

Current state:

- research-adjacent
- not yet core deep-cultivation work
- needs definition before inclusion

Open issues Jason should preserve:

- data source: NHI database, community cohort, PSA workflow, or new collection
- aging definition
- biomarker list
- intervention plan
- follow-up interval
- IRB and data governance
- whether it can be reframed as a service workflow

If included, it should be a bounded appendix or later sub-study, not the center of 子計畫二.

## Immediate Jason Deliverables Before 2026-06-02

1. Draft 子計畫二 smart-healthcare / AI / CRM outline.
2. Write the service workflow from PSA/community screening to CRM follow-up.
3. List first-year, second-year, and third-year KPI.
4. Map each KPI to budget categories.
5. Mark internal vs outsourced work.
6. Prepare procurement and security-governance questions.
7. Identify IRB/MOU dependencies.
8. Decide how to mention Aging Clock: exclude, appendix, or service-reframed sub-study.
9. Keep all wording inside the clinician-reviewed, non-diagnostic boundary.
10. Confirm whether Jason personally needs to complete the nine-hour IRB training before joining any research-data or patient-data workflow.
11. Decide whether kiosk / chronic-disease-system adaptation and smart-pharmacy ideas are core scope, optional expansion, or out of scope for the June 2 draft.

## One-Sentence Role Definition

Jason is responsible for translating the meeting's 智慧醫療 / AI / CRM discussion into a concrete, governed, KPI-budget-linked 子計畫二 draft that can support PSA/community screening and hospital CRM follow-up without overstating AI or research claims.
