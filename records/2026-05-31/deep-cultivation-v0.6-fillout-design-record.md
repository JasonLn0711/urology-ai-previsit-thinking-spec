# Decision Record: Deep-Cultivation Proposal Package v0.6

Status: synthesized

## Decision Identity

| Field | Notes |
| --- | --- |
| Decision record ID | DR-2026-05-31-001 |
| Date | 2026-05-31 |
| Source request | User confirmed the v0.5 update should become v0.6 |
| Related v0.5 decision | `../2026-05-29/deep-cultivation-v0.5-decision-record.md` |
| Related reference analysis | `../2026-05-29/xinyi-outpatient-proposal-reference/README.md` |
| Active draft | `../../discovery/DEEP_CULTIVATION_APPLICATION_DRAFT_V0_6.md` |

## Decision

Promote the active 2026-06-02 discussion package from v0.5 to v0.6.

v0.6 is the fill-out design version. It keeps the v0.5 budget and page controls, then adds the proposal-facing choices needed before moving toward a parent Word template.

## v0.6 Adds

- Primary category: `範疇三：導入智慧科技醫療`.
- Secondary support category: `範疇一：優化醫療工作條件`.
- Subproject-three reference used as a fill-out skeleton, not as clinical content.
- Service flow:

```text
門診 / 篩檢追蹤入口
-> 低摩擦症狀蒐集
-> source label / 缺漏欄位
-> 一頁式醫師覆核摘要
-> staff-review / CRM-ready queue
-> KPI 評估
```

- Verifiable KPI targets:
  - summary read time `<= 60 秒`
  - source label `100%`
  - unsafe wording `= 0`
  - missing-field visibility `>= 90%`
  - clinician usefulness `>= 4/5`
  - governance owner named
- Formal budget fill-out columns before submission:

```text
正式會計科目 / 單價 / 數量 / 年度 / KPI / owner / evidence / procurement note
```

- Governance section moved before KPI and budget:
  - AI governance
  - 資安治理
  - 資料治理
  - IRB/QI
  - 採購
  - FHIR/TW Core IG readiness
- Proposal-facing language rule: use Taiwan Traditional Chinese except necessary English technical terms.

## v0.6 Preserves

- Working title: `泌尿科門診前問診與醫師覆核摘要支持系統`.
- Three-year discussion allocation: NT$10,000,000.
- Discussion draft page control: 20 pages.
- Narrow urology previsit / clinician-review summary scope.
- No automatic diagnosis, treatment advice, autonomous triage, queue priority, automatic HIS/EMR/EHR writeback, production clinical-use claim, or real patient-data use before governance approval.

## Reference Handling

Use the attached subproject-three PDF for:

- cover identity and budget placement
- service-system writing structure
- three-year matrix
- organization and manpower table
- governance-before-KPI structure
- KPI and budget table discipline

Do not use it for:

- musculoskeletal clinical content
- automatic risk routing
- direct production HIS / FHIR claims
- unsupported clinical-effectiveness claims
- broad scale numbers before site ownership exists

## Immediate Next Actions

| Action | Done definition |
| --- | --- |
| Create v0.6 discussion draft | `../../discovery/DEEP_CULTIVATION_APPLICATION_DRAFT_V0_6.md` exists. |
| Update package pointers | README, discovery index, NEXT_STEP, KPI/budget tables, crosswalk, annual checkpoint table, and planning tracker point to v0.6 as current. |
| Bump repo version | `VERSION` and `meta/version.json` show `v0.6.0`; `CHANGELOG.md` records the release. |
| Verify consistency | Search confirms no current-entrypoint text still points to v0.5. |

## Review Boundary

v0.6 is proposal-prep material. It is not a signed institutional application, official budget, procurement specification, IRB protocol, clinical deployment plan, or production integration approval.
