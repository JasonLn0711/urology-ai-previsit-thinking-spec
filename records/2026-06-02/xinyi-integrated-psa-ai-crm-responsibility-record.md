# 2026-06-02 信義整合 PSA / AI 智慧問診 / CRM 責任澄清紀錄

Status: captured

## Source

This record is synchronized from the planning repo after the user supplied the
2026-06-02 LINE group minutes and then clarified the team's actual assignment.

Planning-side source record:

```text
/home/jnln3799/every_on_git_ubuntu/planning-everything-track/data/knowledge/healthcare/urology/previsit-interview/meeting-record-2026-06-02-lianyi-outpatient-deep-cultivation.md
```

## User Clarification Preserved

```text
Our project is: 信義 is the integrated PSA 主動篩檢 + AI 智慧問診 + CRM route, with PSA about NT$15M。

我們負責的深耕計畫的部分，是合併忠孝院區泌尿科自行提報的PSA 篩檢以及美如主任交待我後續進行的 CRM 外包（美如主任交待我，把 CRM 外包寫進深耕計畫的案子裡面，然後我還要彙整合併泌尿科自行提報的PSA篩檢，到我們原本設計的計畫內），把三個部份（我原本的部份 + 泌尿科PSA篩檢 + CRM 外包）合併成一個大專案.
```

## Current Project Definition

Our active 信義 deep-cultivation project is one integrated proposal package:

```text
信義門診部攝護腺癌主動篩檢、AI 智慧問診與 CRM 追蹤支持整合計畫
```

The package merges three components:

1. Jason's original AI 智慧問診 / one-page physician-review summary plan.
2. 忠孝院區泌尿科自行提報的 PSA 主動篩檢 plan.
3. 美如主任交辦要寫進深耕計畫的 CRM 外包 scope.

## Budget Signal

| Component | Current budget signal | Status |
| --- | ---: | --- |
| PSA 主動篩檢 | about NT$15,000,000 | official meeting signal; clinical owner and SOP owner pending |
| AI 智慧問診 including CRM | about NT$15,000,000 | official meeting signal; CRM outsourcing details pending |
| 信義碳盤查 | about NT$7,500,000 | parallel parent-proposal workstream, not Jason's core writing package unless assigned |

## Operational Interpretation

- The PSA work has its own clinical proposer and 忠孝院區 urology ownership.
  Jason's task is to merge its target population, annual screening volume,
  abnormal-case follow-up KPI, and guideline boundary into the original AI
  智慧問診 proposal logic.
- CRM is no longer only a future `CRM-ready` phrase for this proposal lane.
  美如主任 has assigned Jason to write CRM outsourcing into the deep-cultivation
  case.
- The proposal should describe CRM as a funded outsourced service / system
  workstream, while still marking procurement, data route, security, privacy,
  KPI ownership, and maintenance as governance-confirmation fields.
- The three parts should read as one service route, not three disconnected
  appendices:

```text
PSA 主動篩檢
-> abnormal / follow-up candidate identification
-> AI 智慧問診 symptom and context collection
-> one-page physician-review summary
-> CRM outsourced follow-up workflow
-> KPI evidence and annual checkpoint
```

## Scope Control

The stronger project definition does not authorize clinical overclaiming.

The proposal can claim:

- PSA screening and follow-up workflow integration, pending clinical SOP owner;
- AI-supported previsit symptom collection and one-page clinician-review
  summary;
- CRM outsourcing as a service-system component for reminders, follow-up queue,
  case-management support, and KPI evidence, pending procurement and governance;
- staff-burden reduction through a governed service flow.

The proposal should keep these as validation gates:

- diagnosis remains clinician-owned;
- treatment decisions remain clinician-owned;
- triage and queue priority remain governed hospital workflow decisions;
- real patient data requires QI/service/IRB/data-governance route;
- HIS/EMR/EHR writeback remains a later governed integration step;
- CRM vendor work requires procurement, security, privacy, data-retention, and
  maintenance ownership.

## Proposal-Writing Implication

The v0.7 proposal package is now a prior discussion baseline.

The next package should be planned as v0.8:

```text
v0.8 = 信義 integrated PSA + AI 智慧問診 + CRM outsourcing package
```

v0.8 should preserve the useful v0.7 elements:

- one-page physician-review summary within 60 seconds;
- source labels and missing-field visibility;
- unsafe wording count = 0;
- governance before KPI and budget;
- KPI-to-budget traceability;
- confident, positive-scope proposal language.

v0.8 must add:

- PSA target population: men aged 50+; 45+ with family history;
- annual screening volume: 3,500 to 5,000;
- abnormal-case follow-up target: >= 70%;
- Taiwan Urological Association guideline compliance statement;
- CRM outsourcing work package;
- CRM-to-KPI mapping for abnormal follow-up;
- owner split across 忠孝院區, 智慧健康醫療中心, IT/security, procurement,
  data governance, and evaluation;
- budget transition from the old NT$10,000,000 discussion slice to the 信義
  NT$15,000,000 AI/CRM allocation plus the separate NT$15,000,000 PSA allocation.

## KPI / Budget Discipline Clarification

The v0.8 proposal should split KPI more finely than the v0.7 discussion draft.

Reason:

```text
The NT$15,000,000 AI 智慧問診 / CRM allocation must be explainable to the supervising unit and review agency.
```

Required writing posture:

- do not use only broad outcome KPIs;
- do not rely only on `60 秒摘要` and `70% 追蹤率`;
- break the allocation into work-package-level KPIs;
- make every KPI traceable to owner, evidence, annual checkpoint, and budget
  category;
- use the detailed KPI stack to show that the budget supports workflow design,
  system outsourcing, data governance, staff-burden reduction, KPI capture, and
  review-ready evidence.

Minimum KPI families for v0.8:

| KPI family | What it explains |
| --- | --- |
| PSA handoff KPI | how PSA screening output enters AI / CRM workflow |
| AI 問診 KPI | how the summary is created, timed, source-labeled, and reviewed |
| CRM 外包 KPI | how follow-up queue, contact attempt, status tracking, and dashboard evidence support abnormal follow-up |
| Data-quality KPI | how missing fields, source labels, audit logs, and exception handling are measured |
| Staff-burden KPI | how the workflow avoids shifting work to physicians, nurses, or front desk staff |
| Governance KPI | how AI, data, cybersecurity, privacy, IRB/QI, and procurement owners are named |
| Vendor / procurement KPI | how outsourced CRM deliverables are accepted and maintained |
| Annual evidence KPI | how the project reports progress each year to the主管單位 and審查機關 |

## Decision

Treat this as an accepted responsibility clarification and a v0.8 planning gate.

Do not directly overwrite v0.7 as if all CRM procurement and clinical SOP
questions are settled. Use the next-step plan to prepare the integrated v0.8
draft once owner and governance questions are mapped.
