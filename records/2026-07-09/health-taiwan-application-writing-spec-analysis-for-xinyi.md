# 健康台灣深耕計畫申請書撰寫規格分析：信義 / PSA / 智慧問診提報

Status: source copied / live official source spot-checked / proposal-writing control analysis

Prepared date: 2026-07-09

## FIRST PRINCIPLE

- Scarce resource: proposal-writing attention before the 2026-07-14 merged-plan
  review.
- Canonical home: `records/2026-07-09/` in this execution repo.
- Planning role: none in this step unless later mirrored as a locator.
- Evidence path:
  `sources/health-taiwan-application-writing-spec-2026-07-09-ai-agent-readable.md`.
- Next gate: use this specification as the section-order and quality-control
  layer when rewriting the 信義 / PSA / 智慧問診 merged proposal section.

2026-07-13 evidence update: use
`../2026-07-13/README.md` as the latest briefing-level rule layer. This 7/9
analysis continues to own chapter responsibility and traceability; the 7/13
record adds current applicant/category, three-year target, KPI-publication,
block-grant, platform/package, and final-notice validation controls.

## Source Capture

| Source | Copied repo path | SHA-256 |
| --- | --- | --- |
| 健康台灣深耕計畫申請書撰寫規格 AI-agent-readable Markdown | `sources/health-taiwan-application-writing-spec-2026-07-09-ai-agent-readable.md` | `b1505cb979f394094dd992ea85b26776785303eec0e3d6190fb298db2af3b4c7` |

## Live Official Source Spot Check

Checked on 2026-07-09:

- `https://htsprout.nhri.org.tw/download.html`
- `https://htsprout.nhri.org.tw/dhplan.html`
- `https://htsprout.nhri.org.tw/dhplan_11507021633.html`
- `https://dep.mohw.gov.tw/TDU/cp-1567-82709-121.html`

Findings:

- confirmed: the official download page still groups files into application,
  execution, budget, and meeting-QA areas.
- confirmed: official source pages continue to frame the program around four
  scopes: 優化醫療工作條件, 規劃多元人才培訓, 導入智慧科技醫療, and 社會責任醫療永續.
- confirmed: the second-stage 116-118 source currently visible is a
  solicitation briefing notice, not a complete replacement proposal template.
- scope control: this copied specification is a working control layer. Formal
  submission still requires a latest-template check against HTSprout / MOHW and
  any hospital-specific instruction.

## What This Specification Adds

This source is more useful than a generic writing guide because it defines the
job of each application chapter and prevents duplicated content:

| Layer | Practical effect |
| --- | --- |
| Official structure | Keeps the proposal in the expected order: self-check, overview, institution profile, planning, benefit evaluation, overseas plan, budget, staffing, other, legal forms. |
| Chapter responsibility | Assigns one home for each fact type: problem in `貳`, work packages in `肆`, KPI in `伍`, budget in `柒`, governance and risks in `玖`. |
| 20-page compression | Gives a realistic internal compression target while preserving official forms and signature pages. |
| KPI discipline | Requires numerator, denominator, baseline, target, data source, frequency, owner, and verification artifact. |
| Budget discipline | Forces every major expense to connect to a work package, checkpoint, deliverable, KPI, and negative-list screen. |
| Governance discipline | Puts IRB, data governance, AI governance, cybersecurity, human review, model-card, retention, and exit controls into a visible review layer. |

## Impact On The Current Xinyi / PSA Package

The current 信義 package should be written as one executable proposal chain:

```text
policy scope -> local problem -> work package -> annual milestone
-> checkpoint evidence -> KPI -> budget line -> owner -> governance control
```

For the 2026-07-09 廖醫師 PSA package, this means:

| Proposal element | Required treatment |
| --- | --- |
| PSA 篩檢約新臺幣 600 萬元 | Put formal numbers in `柒、經費規劃`; only refer to budget IDs in `肆` and `伍`. |
| PSA / PHI / IPSS workflow | Put operational method in `肆、計畫規劃`; put indicator formulas and report evidence in `伍、效益評估`. |
| 美幸主任資本門內容 | Treat as included in the current PSA package; keep the earlier source record only for traceability. |
| Jason / 陽明交大 AI support | Frame as workflow support: questionnaire completion, missing-field visibility, report consolidation, physician-review summary, governance evidence. |
| CRM and carbon inventory | Keep as companion owner lanes unless the parent proposal owner assigns shared work packages. |
| 華山 plan | Use only as a peer writing and review-discipline reference, not as clinical content for Xinyi. |

## Proposed Section Routing For 信義 / PSA / 智慧問診

| Official section | What belongs there for this package | What stays out |
| --- | --- | --- |
| `貳、計畫概要` | 腦心血管疾病防治 / 三高追蹤 as main service story; PSA 精準篩檢與智慧問診 as feature; current gap and expected service value. | Detailed unit prices, full workflow tables, long AI feature lists. |
| `參、申請機構簡介` | 信義門診部, 忠孝院區, health-service-center collaboration capacity, and role boundaries. | Generic history or unsupported claims. |
| `肆、計畫規劃` | Work packages: community screening intake, PSA/IPSS workflow, result notification and tracking, AI-assisted questionnaire / summary / reporting, governance workflow. | KPI formulas and itemized budget. |
| `伍、效益評估` | PSA screening volume, abnormal follow-up completion, IPSS completion, result-notification record, summary-readiness, staff-efficiency, governance evidence. | Narrative method description already covered in `肆`. |
| `柒、經費規劃` | PSA testing, PHI, staffing, materials, capital equipment, software/service, AI workflow support, and annual totals. | Clinical rationale repeated from `貳` or `肆`. |
| `捌、人力配置` | PI, clinical owner, data/report owner, AI workflow owner, budget/procurement owner, governance owner. | Named commitments not confirmed by the owner. |
| `玖、其他` | Risk register, IRB/QI/data route, AI/data/cybersecurity self-check status, procurement notes, external source URLs or QR Code index. | New claims not tied to evidence. |

## Cross-Repo / Existing-File Connections

- `records/2026-07-09/line-xinyi-deep-cultivation-psa-subproject-20260709-record.md`:
  latest 廖醫師 PSA package source and capital-budget inclusion resolution.
- `records/2026-07-09/huashan-plan-format-reference-analysis-for-xinyi-urology.md`:
  peer-format reference for issue queues, checkpoints, KPI / budget linkage,
  and reduced-budget discipline.
- `records/2026-07-02/xinyi-july14-complete-download-package-index.md`:
  current 7/14 merged-plan control index.
- `records/2026-07-02/xinyi-july14-pre-integration-expert-task-packet.md`:
  owner-question and before-review task packet.
- `discovery/DEEP_CULTIVATION_PROPOSAL_WRITING_GUIDE.md`:
  writing entrypoint; should now point to this specification before formal
  section rewriting.
- `discovery/DEEP_CULTIVATION_OFFICIAL_FORMAT_CROSSWALK.md`:
  earlier official-format crosswalk; this new specification should supersede it
  for chapter-role and compression rules, while the crosswalk remains useful
  for historical AI-only package mapping.
- `discovery/DEEP_CULTIVATION_MOHW_COMPLIANCE_RUBRIC.md`:
  compliance scoring layer; use this specification to strengthen D-layer source
  traceability and chapter completeness.

## Owner Review Gates Before Rewriting

| Gate | Owner / trigger | Required evidence |
| --- | --- | --- |
| Latest second-stage template | proposal coordinator before formal circulation | HTSprout / MOHW latest download or written instruction. |
| Application mode and applicant eligibility | parent proposal owner | selected mode, applicant/co-applicant list, institution codes. |
| PSA budget final figure | budget owner | annual totals, subsidy/self-funding split, capital ratio, itemized basis. |
| KPI baselines | 廖醫師 / health-service-center / report owner | baseline data or explicit `TODO` if not yet available. |
| Governance attachments | governance / IT / data owner | AI, cybersecurity, data-governance self-check status; IRB/QI route if applicable. |
| Other materials requested by 美幸主任 | Jason / 岳霖主任 / proposal coordinator | confirmed remaining-material list and destination section. |

## Practical Drafting Rule

For the next merged proposal pass, do not start by polishing prose. Start by
building a compact traceability table:

```text
WP -> milestone -> checkpoint -> KPI -> data source -> budget ID -> owner -> governance control
```

Once that table is coherent, each official chapter can be drafted by slicing the
same facts into its assigned role. This prevents duplicate claims, inconsistent
budget numbers, and KPI rows that cannot be audited.

The 2026-07-13 briefing also requires each work package to show its official
scope/goal, 116/117/118 target, continuation/new-project status, government-
grant interface, public-result handling, and submission-readiness evidence.
