# v0.8 Next-Step Plan: 信義 PSA / AI 智慧問診 / CRM 整合大專案

Status: planning gate

2026-06-19 supersession:

```text
本 next-step plan 保留為 2026-06-02 歷史版本。依 2026-06-02 official minutes and 2026-06-19 owner update，信義母案 AI 智慧問診提報約 NT$15,000,000 且包含 CRM；CRM 由其他團隊處理。Jason / 陽明交大目前有效方向是 AI 問診與醫師覆核摘要 package，三年 NT$10,000,000 作為目前 AI-only 討論額度。
```

Official meeting-minutes source:

```text
records/2026-06-02/outpatient-deep-cultivation-official-meeting-minutes.md
```

Date: 2026-06-02

## Verdict

Current gate: `v0.8 integrated proposal planning`.

The v0.7 discussion package is complete as the pre-6/2 working baseline. The
next valid step is not more AI feature design. The next valid step is to convert
the proposal architecture from a standalone AI 智慧問診 / previsit-summary package
into one 信義 integrated package that merges:

1. original AI 智慧問診 / one-page summary;
2. 忠孝院區泌尿科 PSA 主動篩檢;
3. 美如主任交辦 CRM 外包.

## Evidence

- 2026-06-02 responsibility record:
  `records/2026-06-02/xinyi-integrated-psa-ai-crm-responsibility-record.md`
- Current draft baseline:
  `discovery/DEEP_CULTIVATION_APPLICATION_DRAFT_V0_7.md`
- Current Word-ready export:
  `discovery/exports/deep-cultivation-urology-previsit-v0.7-working-discussion-proposal.docx`
- KPI / budget table:
  `discovery/DEEP_CULTIVATION_KPI_BUDGET_ANNUAL_INTEGRATION_TABLE.md`
- Governance checklist:
  `discovery/DEEP_CULTIVATION_GOVERNANCE_CHECKLIST.md`

## First-Principle Question

The scarce resource is reviewer trust.

Reviewer trust comes from one coherent service route:

```text
screening target -> clinical SOP -> information collection -> physician summary
-> follow-up management -> KPI evidence -> governance ownership
```

The proposal should make the integrated route easy to inspect. It should not ask
reviewers to infer how PSA, AI 問診, and CRM are connected.

## KPI Granularity Rule

User-provided planning note:

```text
要思考，把 KPI 拆分的細一點，要能夠支撐 1500 萬元的經費支出，這樣我們才能向主管單位交待，這樣也才能讓審查機關通過。
```

Operational interpretation:

- The NT$15,000,000 AI 智慧問診 / CRM allocation cannot be justified by only
  one or two headline KPIs.
- The proposal needs a fine-grained KPI stack that maps each budgetable work
  package to measurable outputs, responsible owners, evidence artifacts, and
  annual checkpoints.
- The review logic should be:

```text
NT$15M budget -> work packages -> sub-KPIs -> owner -> evidence artifact
-> annual checkpoint -> reviewer explanation
```

The KPI stack should be detailed enough to answer主管單位 and審查機關:

1. What exactly is being purchased or staffed?
2. What workflow state will change?
3. Who owns the change?
4. What evidence proves completion?
5. Which annual checkpoint verifies progress?
6. Why does this belong in the NT$15,000,000 allocation?

## What To Execute Next

### 1. Build the v0.8 integration skeleton

Expected artifact:

```text
discovery/DEEP_CULTIVATION_APPLICATION_DRAFT_V0_8_INTEGRATION_SKELETON.md
```

Purpose: create the new section order and work-package map before editing the
proposal body.

Required sections:

- one-page integrated thesis;
- workstream map: PSA, AI 智慧問診, CRM 外包;
- service flow;
- owner split;
- KPI map;
- budget transition;
- governance gates;
- 2026-06-23 question list.

Validation: every section must name the owner question, KPI, or governance gate
that controls it.

### 2. Update KPI / budget architecture

Expected artifact:

```text
discovery/DEEP_CULTIVATION_KPI_BUDGET_ANNUAL_INTEGRATION_TABLE.md
```

Add a v0.8 section or table that separates:

- PSA screening KPI: annual `3,500-5,000` screened;
- PSA follow-up KPI: abnormal-case return / tracking `>= 70%`;
- AI summary KPI: one-page physician-reference summary within `60` seconds;
- information-quality KPI: source labels, missing fields, unsafe wording;
- CRM outsourcing KPI: follow-up queue completeness, reminder / contact attempt
  evidence, abnormal-case tracking evidence, owner-reviewed dashboard fields;
- governance KPI: named owners for AI, data, cybersecurity, IRB/QI, procurement,
  and CRM maintenance.

Then split the NT$15,000,000 AI/CRM allocation into budget-support KPI families:

- proposal / project management KPI;
- clinical workflow and PSA handoff KPI;
- AI 問診 / one-page summary KPI;
- CRM outsourcing / follow-up management KPI;
- data quality / auditability KPI;
- staff burden / usability KPI;
- governance / security / privacy KPI;
- procurement / vendor acceptance KPI;
- annual reporting / evidence-package KPI.

Stop rule: do not invent formal unit prices before hospital budget/procurement
owner review.

### 3. Update governance checklist for CRM outsourcing

Expected artifact:

```text
discovery/DEEP_CULTIVATION_GOVERNANCE_CHECKLIST.md
```

Add explicit CRM outsourcing governance:

- vendor scope;
- data fields;
- consent / notification route;
- data retention and deletion;
- security review;
- access roles;
- incident and correction route;
- maintenance owner;
- handoff after project period;
- whether CRM sends messages, only tracks internal queue, or both.

Stop rule: no real patient messaging, LINE/SMS claim, or production follow-up
claim until privacy, procurement, and security owners are named.

### 4. Update open questions and owner map

Expected artifacts:

```text
meta/open_questions.md
discovery/DEEP_CULTIVATION_APPLICATION_DRAFT_V0_8_INTEGRATION_SKELETON.md
```

Questions to resolve before the 2026-06-23 信義 slot:

- Who is final applicant / PI?
- Who owns PSA SOP and Taiwan Urological Association guideline compliance?
- Who owns CRM outsourcing and procurement?
- What exact CRM output supports the `>= 70%` abnormal follow-up KPI?
- What data route is planned: no real data, QI/service, IRB research, or mixed?
- Does CRM send patient messages or only maintain an internal follow-up queue?
- What capital expenditure items exist, and how will the `30%` cap be checked?
- Which parts of AI 問診 are internal, outsourced, or hybrid?
- Is ASR funded, demo-only, or excluded from v0.8?

### 5. Draft the v0.8 proposal body only after skeleton review

Expected artifact:

```text
discovery/DEEP_CULTIVATION_APPLICATION_DRAFT_V0_8.md
```

Use v0.7 as a source, but rewrite the project identity:

```text
from: 泌尿科門診前問診與醫師覆核摘要支持系統
to: 信義門診部攝護腺癌主動篩檢、AI 智慧問診與 CRM 追蹤支持整合計畫
```

Preserve:

- clinician authority;
- one-page summary;
- source labels;
- governance-first structure;
- KPI-to-budget traceability;
- positive-scope writing.

Replace:

- standalone NT$10M framing;
- optional `CRM-ready` language;
- PSA as optional follow-up context;
- any wording that leaves the three streams disconnected.

## What To Think Through

### Project architecture

The central architecture question is:

```text
Is CRM the downstream service backbone for PSA abnormal follow-up, AI 問診
follow-up, or both?
```

If both, v0.8 should make CRM the shared service layer.

### Claim-evidence fit

The proposal can claim integration design now. It should reserve outcome claims
until workflow evidence exists.

Good claim:

```text
本計畫建立 PSA 篩檢後追蹤、AI 智慧問診摘要與 CRM 服務管理的一體化流程，使異常個案追蹤、門診前資訊整理與醫師覆核摘要能在同一治理架構下被設計、執行與評估。
```

Evidence still needed:

- clinical SOP owner;
- CRM workflow owner;
- abnormal follow-up baseline;
- procurement route;
- data route;
- staff workflow review.

### Governance posture

CRM outsourcing increases governance load. Treat that as proposal maturity:

```text
CRM 外包不是單純採購系統，而是追蹤責任、資料治理、資安審查、維運交接與 KPI evidence 的服務治理設計。
```

## Stop Rules

- Do not generate a new Word export until v0.8 skeleton, KPI table, and CRM
  governance questions are updated.
- Do not claim production CRM operation before procurement, privacy, security,
  data governance, and maintenance owners are named.
- Do not claim improved cancer detection, diagnosis, treatment quality, or
  medical outcomes from AI 問診.
- Do not collapse 忠孝院區's PSA clinical ownership into Jason's AI/CRM writing
  role. Jason integrates the proposal; the clinical SOP must remain owned by
  the clinical unit.
- Do not reopen HIS/EMR/EHR writeback as first-version scope.

## Validation

Smallest validation commands after the repo edits:

```bash
git diff --check
rg -n "CRM-ready|NT\\$10,000,000|PSA / screening follow-up optional|future activation gate|parked" discovery meta core records README.md
```

The `rg` command should not produce zero results, because historical records
remain valid. Instead, it should identify which current-facing files still need
v0.8 update if they are used for active drafting.

## Definition Of Done For The Next Work Block

The next work block is complete when:

- the 2026-06-02 record exists;
- `discovery/NEXT_STEP.md` points to v0.8 planning;
- `meta/open_questions.md` has the 信義 integration questions;
- `README.md` and `records/README.md` point to the new 2026-06-02 record;
- no current-facing file describes CRM as only parked without also noting the
  2026-06-02 responsibility clarification.
