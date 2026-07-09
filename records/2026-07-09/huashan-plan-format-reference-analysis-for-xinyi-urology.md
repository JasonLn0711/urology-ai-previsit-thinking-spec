# 華山深耕計畫格式參考分析：供信義 / 泌尿 AI-only 包借鏡

Status: source preserved / analyzed reference

Prepared date: 2026-07-09

## FIRST PRINCIPLE

- Scarce resource: proposal-writing attention and claim-scope fidelity.
- Canonical home: `records/2026-07-09/` in this execution repo.
- Planning role: none in this step; this is a writing reference, not a schedule
  or capacity change.
- Evidence path:
  `sources/huashan-deep-cultivation-ai-agent-readable-verified-notes-2026-07-09.md`.
- Next gate: use this as a format and review-discipline reference when revising
  the 信義 / 泌尿 AI-only package; do not import 華山院區 service content into
  Jason / 陽明交大 scope.

## Source Context

| Source | Copied repo path | Use |
| --- | --- | --- |
| 華山深耕計畫 AI-agent-readable 查核註記版 | `sources/huashan-deep-cultivation-ai-agent-readable-verified-notes-2026-07-09.md` | External reference packet for structure, writing rhythm, KPI / budget / governance linkage, issue labeling, and 60%核刪版 design. |

The file identifies itself as an AI-readable Markdown conversion of
`華山深耕計畫_整合完整版_3750萬_含60_調整版.docx`. It separates agent notes,
external verification notes, and the original plan body. That separation is the
most valuable reusable pattern.

## Research Baseline

These checks support the analysis without turning the 華山 plan into our scope:

| Research point | Current use in this analysis | Source |
| --- | --- | --- |
| Health Taiwan plans need goal, strategy, KPI, checkpoint, and budget linkage across execution years. | Confirms that the 華山 quarterly-checkpoint and budget-link style is worth borrowing. | 健康台灣深耕計畫 application guidance / local `records/2026-07-01/health-taiwan-stage2-application-guidance-record.md`; official Health Taiwan application guidance archive. |
| 114 年起癌症篩檢 policy expanded. | Confirms the 華山 issue-label pattern for policy freshness; for our package, use the same freshness discipline for PSA / 三高 / governance claims. | 國民健康署 114 年起擴大癌症篩檢 announcement. |
| Power BI Gateway is a bridge between on-premises data and Microsoft cloud services. | Confirms the need to write data-residency claims as architecture conditions, not slogans. | Microsoft Learn: On-premises data gateway. |
| Pseudonymisation needs technique, parameters, and policy fit; plain hashing is not enough as a full governance claim. | Confirms that our governance wording should name controls such as HMAC / salt / key separation only when those controls are actually planned. | ENISA pseudonymisation guidance. |

## What The 華山 Packet Does Well

### 1. It starts with agent-readable control notes

The file tells future agents what may be changed and what must remain source
material. This is useful for us because our repo has many source layers,
analysis layers, and proposal layers. A future 信義 draft should keep the same
three-layer discipline:

1. source conversion,
2. verification / issue notes,
3. proposal-facing revised text.

Do not merge reviewer notes into proposal prose until the owner has accepted the
revision.

### 2. It gives the whole proposal a clear service loop

華山 uses a single closed-loop story:

```text
CRM 招募 -> QR / 電子表單 / 健康量測 -> AI 風險分層
-> 工單追蹤 -> 3/6/12 個月追蹤 -> 次年再篩
```

Our transferable version should be narrower:

```text
符合資格者 / 候診填答 -> 問卷缺漏提醒 -> PSA / IPSS / 症狀資料整理
-> 醫師覆核摘要 -> 現場人員確認與追蹤紀錄 -> 年度 KPI / 報表 evidence
```

The writing lesson is the loop shape, not the 華山 service content.

### 3. It assigns shared resources to one owner

華山 explicitly marks shared resources such as cloud/security, Power BI,
health-kiosk nodes, LINE/LIFF, and CRM incremental modules. That is useful
because reviewers dislike duplicate budget lines.

For the 信義 / 泌尿 package, the borrowed pattern is:

| Shared or adjacent item | Our scope-control treatment |
| --- | --- |
| CRM | Parent / other-team workstream; not Jason / 陽明交大 AI-only scope. |
| HIS / EMR / LIS writeback | Activation gate after hospital IT, security, data-governance, and procurement review. |
| Health-check station or capital equipment | Budget-owner work package unless explicitly tied to PSA / 三高 workflow evidence. |
| AI questionnaire / physician-review summary | Jason / 陽明交大 AI-only scope when owner-confirmed. |
| Reports / KPI evidence | In scope when generated from approved workflow logs or synthetic / reviewer evidence. |

### 4. It links quarterly checkpoints to measurable indicators

The 華山 plan uses year and quarter tables with a work item, checkpoint, and
indicator. This is a strong pattern to borrow because it prevents empty annual
milestones.

For our package, convert the format like this:

| Year / quarter | Work item | Checkpoint | Indicator |
| --- | --- | --- | --- |
| 116 Q1 | Workflow and source-field freeze | PSA / IPSS / symptom-field dictionary accepted by 廖醫師 | accepted field list and summary schema |
| 116 Q2 | Prototype review-support flow | QR / tablet questionnaire and missing-field reminder reviewed with synthetic cases | completion rate in rehearsal cases; unsafe wording = 0 |
| 116 Q3 | Staff-review packet | one-page physician-review summary and report fields accepted for pilot-readiness review | clinician usefulness score; read-time target |
| 116 Q4 | Annual evidence package | KPI / budget / governance evidence bundled for owner review | report archive and governance checklist |

Use real owner decisions before moving these into a formal proposal table.

### 5. It includes a 60%核刪版

This is the highest-value budget-writing pattern. The 華山 packet does not only
list a budget; it shows what remains if funding is reduced. For our package, a
proposal-facing budget should include:

| Tier | Retained capability |
| --- | --- |
| Full version | questionnaire, missing-field reminder, physician-review summary, report generation, governance evidence, and owner-confirmed integration support. |
| Reduced version | questionnaire + summary + evidence reports first; defer ASR, deeper integration, and nonessential dashboard polish. |
| Deferred activation | CRM, HIS/EMR/LIS writeback, real patient-data research, procurement-heavy equipment, and vendor-specific modules. |

### 6. It turns risks into fix queues

華山's `ISSUE-*` table and pre-submission fix queue are strong because they give
the proposal team a way to repair the draft without weakening the main thesis.
For our package, use the same form for:

- PSA / 三高 policy freshness,
- AI-only versus CRM scope,
- governance documents,
- budget category and capital-cap treatment,
- real-data / QI / IRB activation,
- owner-confirmed KPI evidence.

## What Not To Copy

| 華山 element | Why not copy into our package | Our replacement |
| --- | --- | --- |
| AI gait / sarcopenia model claims | Different clinical domain and validation path. | AI 問診 / physician-review summary support only. |
| Health-CRM as central loop | CRM is outside Jason / 陽明交大 current scope. | Report and tracking evidence with parent/other-team CRM boundary. |
| Four/five cancer screening operations | Not our direct service content. | PSA 精準篩檢 and health-lifestyle-prescription owner-confirmed fields. |
| High-budget integrated platform language | Our package must stay narrower and claim-gated. | Minimal workflow-support system with governance and owner gates. |
| Vendor/platform-specific cloud claims | Requires architecture confirmation. | Conditional data-flow and governance language. |

## Proposed Writing Upgrade For Our Draft

Use this structure when revising the 信義 / 泌尿 section:

1. `Agent control notes`: source layer, verification layer, proposal layer.
2. `Executive summary`: one service loop, one owner boundary, one budget frame.
3. `Key machine-readable facts`: project name, scope, execution years, budget,
   work packages, owner gates.
4. `Issue / fix queue`: policy, budget, governance, owner, evidence.
5. `Original / current source stack`: links to 6/23, 6/30, 7/1, 7/2, and 7/9
   records.
6. `Proposal body`: problem, workflow, work packages, KPI, budget, governance,
   reduced-budget version.
7. `Scope controls`: CRM, real data, HIS/EMR, procurement, and research routes
   as activation gates.

## Connection Map

- `records/2026-07-02/xinyi-july14-complete-download-package-index.md`: active
  7/14 control index; this 華山 packet is now a format reference for the same
  merged-plan review cycle.
- `records/2026-07-02/xinyi-july14-pre-integration-expert-task-packet.md`:
  keep 廖醫師 questions and PSA / healthy-lifestyle-prescription gates as the
  content source; use 華山 only for form and review discipline.
- `records/2026-07-09/xinyi-capital-budget-liao-subproject-integration-checklist.md`:
  capital-budget source gate that should use the same owner-confirmation and
  issue-queue discipline.
- `discovery/DEEP_CULTIVATION_PROPOSAL_WRITING_GUIDE.md`: should route future
  proposal writing to this analysis as a format reference.
- `discovery/DEEP_CULTIVATION_OFFICIAL_FORMAT_CROSSWALK.md`: remains the formal
  Health Taiwan section-order control; this 華山 note is a peer-example
  reference, not a replacement.

## Action Register

| Action | Status | Owner / trigger |
| --- | --- | --- |
| Preserve copied 華山 source in repo. | confirmed | completed 2026-07-09 |
| Use 華山 issue-table and 60%核刪版 pattern in next 信義 / 泌尿 writing pass. | adopted reference | next formal draft revision |
| Confirm whether parent proposal owner wants our draft to include a reduced-budget version. | pending confirmation | before formal circulation |
| Keep 華山 clinical content out of Jason / 陽明交大 AI-only scope. | confirmed scope control | all future drafting |

## External Research References

- Health Taiwan application guidance:
  `https://htsprout.nhri.org.tw/UploadFile/DHPlan_level1.pdf`
- 國民健康署 114 年起擴大癌症篩檢:
  `https://www.hpa.gov.tw/Pages/Detail.aspx?nodeid=4809&pid=18712`
- Microsoft Learn on-premises data gateway:
  `https://learn.microsoft.com/en-us/power-bi/connect-data/service-gateway-onprem`
- ENISA pseudonymisation healthcare guidance:
  `https://www.enisa.europa.eu/sites/default/files/publications/WP2021%20-%20O.2.3%20Pseudonymisation%20Healthcare%20.pdf`
