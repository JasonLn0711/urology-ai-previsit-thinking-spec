# Repository Inclusion Recommendation For Deep-Cultivation Proposal

Status: recommendation

## Question

Should the deep-cultivation proposal include the following repositories?

- `urology-ai-previsit-thinking-spec`
- `urology-ai-previsit-demo`

The user's phrase `urology-provisit-demo` is interpreted as the existing sibling repo:

```text
/home/jnclaw/every_on_git_jnclaw/phd-life-system/urology-ai-previsit-demo
```

## Recommendation

Yes. Include both repositories, but with different roles and different levels of exposure.

Do not attach them as undifferentiated raw repo dumps in the main proposal. Use them as a curated evidence package:

```text
proposal main text
-> short repo evidence paragraph
-> appendix / URL / selected file package
-> full repository only if reviewers request reproducibility evidence
```

## Recommended Role Split

| Repository | Include? | Role | How To Describe |
| --- | --- | --- | --- |
| `urology-ai-previsit-thinking-spec` | Yes | Governance, reasoning, policy alignment, safety boundary, proposal-writing logic | The thinking and governance layer for the deep-cultivation smart-healthcare subproject. |
| `urology-ai-previsit-demo` | Yes | Synthetic-data prototype, role-separated workflow, screenshots, demo evidence, testable artifact | A prototype evidence system showing visit-readiness intake, missing-field repair, clinician-review summary, and CRM-ready follow-up fields. |

## Why Include The Thinking Spec Repo

The thinking spec repo is useful because it shows the proposal is not just a software demo.

It contains:

- corrected 2026-05-19 meeting transcript and synthesis
- official Health Taiwan policy archive
- deep-cultivation system positioning
- proposal-writing guide
- safety boundary
- KPI and evaluation logic
- governance assumptions and constraints
- open questions for June 2

Recommended included files:

- `core/DEEP_CULTIVATION_SYSTEM_POSITIONING.md`
- `discovery/DEEP_CULTIVATION_PROPOSAL_WRITING_GUIDE.md`
- `records/2026-05-19/policy-documents/README.md`
- `records/2026-05-19/policy-documents/manifest.md`
- `records/2026-05-19/deep-cultivation-decision-record.md`
- `records/2026-05-19/jason-work-scope-from-deep-cultivation-meeting.md`
- `core/SAFETY_BOUNDARY.md`
- `core/EVALUATION.md`
- `meta/constraints.md`
- `meta/open_questions.md`

Proposal wording:

```text
本團隊已建立 urology-ai-previsit-thinking-spec 作為治理與提案設計層，保存深耕計畫政策文件、會議決策、系統定位、安全邊界、KPI 與治理檢核邏輯，確保智慧醫療子系統不偏離臨床流程改善與醫師覆核原則。
```

## Why Include The Demo Repo

The demo repo is useful because it shows the proposal has an executable artifact and not only written intent.

It contains:

- synthetic urology previsit cases
- adaptive question navigation
- optional local ASR path
- patient confirmation
- nurse missing-field repair
- clinician summary
- visit packet / reviewer packet
- SOAP-like draft support for physician reference
- screenshots and demo script
- tests and readiness checks
- a deep-cultivation positioning note

Recommended included files from `urology-ai-previsit-demo`:

- `README.md`
- `docs/deep-cultivation-positioning.md`
- `docs/demo-script-5min.md`
- `docs/safety-boundary.md`
- `docs/v2-first-principles-readiness-audit.md`
- `docs/product/README.md`
- `docs/product/screenshots/`
- `docs/clinician-demo-report-v1.md`
- `docs/soap-example-case-reports.md`
- `experiments/phase1/scorecard.md`
- `experiments/phase1/decision-memo.md`
- `tests/`

Proposal wording:

```text
另建置 urology-ai-previsit-demo 作為合成資料原型與展示證據，呈現病人端問診、缺漏資訊修補、醫師覆核摘要、角色分離與安全邊界檢核流程。該原型僅用於流程驗證與展示，不連接 HIS/EMR，不使用真實病患資料，也不提供診斷、治療或自動分流。
```

## What Not To Include

Do not include:

- raw chat logs
- local secrets or credentials
- real patient data
- personal machine paths except when used as internal working references
- unrelated branches
- local browser artifacts
- model weights or large ASR runtime artifacts
- speculative AI-triage future documents as current-scope evidence
- full Git history unless requested for audit or reproducibility

## Main Proposal Placement

Use one concise paragraph in the main proposal:

```text
本案已有兩層支持材料：一為 urology-ai-previsit-thinking-spec，作為政策、治理、安全邊界與 KPI 設計之文件層；二為 urology-ai-previsit-demo，作為合成資料原型與流程展示層。兩者共同支援本案之智慧科技醫療導入、醫護減負、CRM 追蹤與負責任 AI 治理，但皆不構成正式臨床系統、診斷工具、自動分流工具或 HIS/EMR 整合系統。
```

## Appendix Placement

Recommended appendix package:

| Appendix | Contents |
| --- | --- |
| Appendix A: Policy and governance evidence | Health Taiwan downloaded policy documents, manifest, proposal guide, safety boundary |
| Appendix B: System positioning | deep-cultivation system positioning and KPI/budget logic |
| Appendix C: Prototype evidence | demo README, screenshots, demo script, synthetic-case outputs, tests/readiness summary |
| Appendix D: Open governance questions | IRB, privacy, MOU, procurement, CRM scope, vendor/internal split |

## Boundary Statement

When including both repos, the boundary must be repeated:

```text
The repositories support proposal preparation and synthetic workflow demonstration. They do not contain a deployed clinical product, real patient data, autonomous diagnosis, treatment recommendation, AI triage, or direct HIS/EMR integration.
```

## Final Recommendation

Include both repos.

Use `urology-ai-previsit-thinking-spec` to prove proposal maturity and governance discipline.

Use `urology-ai-previsit-demo` to prove there is a concrete synthetic-data workflow artifact.

Keep the full proposal self-contained so reviewers understand the project without reading the repositories end to end.
