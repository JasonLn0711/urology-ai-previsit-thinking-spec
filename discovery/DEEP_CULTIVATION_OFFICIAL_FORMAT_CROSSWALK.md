# Deep-Cultivation Official Format Crosswalk

Status: proposal-writing control document

Date: 2026-05-20

Purpose: map the current urology previsit deep-cultivation draft package to the official Health Taiwan proposal format so the next draft can be written as a fundable hospital workflow proposal, not as a research memo or AI demo description.

## Source Basis

Local archived official-format sources:

- `../records/2026-05-19/policy-documents/application/health-taiwan-phase1-proposal-format-114-115-0909.docx`
- `../records/2026-05-19/policy-documents/application/health-taiwan-phase1-application-guidelines.pdf`
- `../records/2026-05-19/policy-documents/execution/category3-smart-healthcare-governance-lazy-guide-1140702.pdf`
- `../records/2026-05-19/policy-documents/budget/budget-preparation-notes-lazy-guide-1140701.pdf`
- `../records/2026-05-19/policy-documents/budget/`
- `../records/2026-05-19/policy-documents/qa/`

Important caveat:

```text
This crosswalk uses the local 114-115 official archive as a drafting scaffold.
Before institutional circulation or submission, the parent proposal owner must confirm the latest live template, application stage, hospital-specific instructions, and internal administrative route.
```

## Official Proposal Order

The archived official proposal format uses this order:

1. Cover page
2. Table of contents
3. `壹、申請單位自我檢核項目表`
4. `貳、計畫概要`
5. `參、申請單位簡介`
6. `肆、計畫規劃`
7. `伍、效益評估`
8. `陸、出國計畫書`
9. `柒、經費規劃`
10. `捌、人力配置表`
11. `玖、其他`
12. `拾、公職人員利益衝突迴避自主檢核表`
13. `拾壹、未有重複申請計畫之聲明切結書`
14. `拾貳、參與計畫同意書`
15. `拾參、審查意見回復表`

## Crosswalk Table

| Official section | What the official format expects | Current material | Gap | Next writing action |
| --- | --- | --- | --- | --- |
| Cover page | project name, county/city, application mode, categories, applicant/co-applicant institutions, institution codes, budget, execution period, PI, contact | `DEEP_CULTIVATION_APPLICATION_DRAFT_V0_3.md` cover fields | applicant, mode, budget, period, institution codes, parent proposal name not confirmed | keep placeholders; ask hospital owner before Word transfer |
| TOC | official auto-generated section order | none needed in Markdown | final Word/PDF step | do not maintain by hand in this repo |
| `壹、自我檢核` | eligibility, official format, COI forms, no duplicate funding, participation consent, only one application mode | v0.2 preflight, MOHW compliance rubric | legal/administrative facts are pending | add explicit applicant-owner checklist and leave institutional blanks |
| `貳、計畫概要` | concise plan summary and problem framing | v0.2 summary, clinical friction analysis, system positioning | summary needs more official/workforce language | write 200-300 word Chinese summary centered on staff-burden reduction |
| `參、申請單位簡介` | applicant/co-applicant institutional background | role table only | institutional text pending | provide role-specific placeholder, not invented institution prose |
| `肆、計畫規劃` | four-scope plan content; workflow, work packages, deliverables | proposal writing guide, intended-use freeze, demo-scope freeze | must look like service implementation plan, not design essay | structure as workflow slot -> modules -> work packages -> governance |
| `伍、效益評估` | KPI table by category, baseline/current data, target, annual checkpoints | KPI-to-budget table, annual checkpoint table | targets and baselines still draft | add integrated KPI-budget-checkpoint table and label all current targets as draft |
| `陸、出國計畫書` | only if scope 2 training-related overseas activity is budgeted | not applicable | must explicitly mark not applicable | write N/A unless training overseas plan is added |
| `柒、經費規劃` |分年經費總表, budget category details, scope allocation, capital/personnel/business categories | KPI-to-budget table | no hospital budget ceiling or allowed category details | add budget narrative map, no fake numbers |
| `捌、人力配置表` | subsidized-unit personnel, current post, work role | role table | named personnel pending | keep role-based table and mark names pending |
| `玖、其他` | attachments, quotations, cooperation materials, figure/table list | repo inclusion recommendation, governance checklist, demo/reviewer artifacts | attachment packet not selected | list recommended appendices and do-not-attach items |
| `拾、利衝自主檢核` | official signed form | none | must be institution-owned | mark parent owner action |
| `拾壹、未重複補助切結` | signed statement | none | must be institution-owned | mark parent owner action |
| `拾貳、參與計畫同意書` | partner consent forms | MOU/partner questions in meeting notes | partner list pending | create partner decision question, no invented partner commitment |
| `拾參、審查意見回復` | reviewer comments, response, revision location | scoring rubric and review response style | only needed after review | prepare empty response table for later |

## Current Draft Package Routing

Use these as the official-format writing package:

- Current v0.3 application draft: `DEEP_CULTIVATION_APPLICATION_DRAFT_V0_3.md`
- Official-format crosswalk: `DEEP_CULTIVATION_OFFICIAL_FORMAT_CROSSWALK.md`
- KPI / budget / annual checkpoint integration: `DEEP_CULTIVATION_KPI_BUDGET_ANNUAL_INTEGRATION_TABLE.md`
- Intended-use freeze: `INTENDED_USE_FREEZE.md`
- Demo-scope freeze: `DEMO_SCOPE_FREEZE.md`
- Clinical friction reduction analysis: `CLINICAL_FRICTION_REDUCTION_ANALYSIS.md`
- Governance checklist: `DEEP_CULTIVATION_GOVERNANCE_CHECKLIST.md`
- Scoring rubric: `DEEP_CULTIVATION_SCORING_RUBRIC.md`
- MOHW compliance rubric: `DEEP_CULTIVATION_MOHW_COMPLIANCE_RUBRIC.md`

Older useful but superseded source drafts:

- `DEEP_CULTIVATION_APPLICATION_DRAFT_V0_2.md`
- `DEEP_CULTIVATION_SUBPROJECT_UROLOGY_PREVISIT_V0_1.md`

## Writing Principles For v0.3

### 1. Write as a hospital workflow proposal

Use:

```text
門診前問診與醫師覆核摘要支持
降低重複問診與文書準備負擔
低摩擦導入既有門診流程
```

Avoid:

```text
AI triage
AI diagnosis
自動風險分級
自動寫入 EMR
全院 chatbot
```

### 2. Make staff burden the central benefit

Every major paragraph should answer:

```text
這會減少哪一類醫療人員負擔？
醫師、護理師、櫃台或行政人員需要多做什麼？
新增負擔是否小於被移除的舊負擔？
```

### 3. Keep technology subordinate to workflow

Correct order:

```text
clinical workflow problem
-> low-friction process insertion
-> clinician-reviewable artifact
-> measurable KPI
-> governance and budget
-> AI / ASR / implementation method
```

Wrong order:

```text
AI model
-> possible use cases
-> later find a hospital process
```

### 4. Mark administrative unknowns explicitly

Do not invent:

- applicant identity
- application mode
- budget ceiling
- matching-fund ratio
- exact execution period
- institution codes
- signatories
- procurement route
- real-patient pilot approval

Use `Pending parent proposal owner` until the hospital confirms.

## Immediate Questions For Hospital / PI Owner

| Question | Why it matters |
| --- | --- |
| Is this a continuation, internal supplement, or future second-stage / new proposal package? | determines template, period, and section wording |
| Who is the formal applicant and PI? | required cover page and self-check |
| What is the official parent proposal name? | determines whether this is 子計畫二 or an appendix |
| Is the first workflow slot `報到後 / 候診中 / QR code or tablet` acceptable? | determines plan feasibility |
| Are staff allowed to help patients complete intake? | determines staffing and burden KPI |
| Should the v0.3 draft go into the Word template now? | determines next artifact format |
| What budget ceiling is realistic? | prevents fake budget lines |
| Who owns AI, cybersecurity, data governance, and privacy sign-off? | required for Scope 3 credibility |
| Is CRM follow-up reopened or parked? | prevents scope drift |
| Does `醫師覆核用 SOAP 架構參考摘要` sound safe? | avoids EMR automation overclaim |

## Ready / Not Ready Gate

The proposal is ready for internal clinical/admin review when:

- v0.3 application draft exists
- official-format crosswalk exists
- KPI-budget-checkpoint integration table exists
- intended use and demo scope are frozen
- governance checklist names required owners
- open administrative fields are visible
- all unsafe claims are removed

The proposal is not ready for external or formal submission until:

- latest official template is confirmed
- institutional applicant and mode are confirmed
- budget is itemized by official category
- COI / duplicate funding / consent forms are handled by the institution
- governance self-checks have owner review
- parent proposal owner confirms wording and attachments
