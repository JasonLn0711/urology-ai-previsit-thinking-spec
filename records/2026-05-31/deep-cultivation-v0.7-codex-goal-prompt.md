# Deep Cultivation v0.7 Codex Goal Prompt

狀態：Codex goal prompt record

日期：2026-05-31

用途：保存可直接貼給 Codex 的 v0.7 工作提示，用於將目前 `v0.6` 健康台灣深耕計畫泌尿科門診前問診草稿，推進成 2026-06-02 討論用的 Word-ready 官方格式填報討論稿。

## Codex Goal Prompt

```text
Repo: /home/jnln3799/every_on_git_ubuntu/urology-ai-previsit-thinking-spec

Goal:
Create a v0.7「健康台灣深耕計畫」Word-ready discussion draft for 2026-06-02 review. The draft should convert the current urology previsit v0.6 package into an official-format fill-out discussion稿. Produce a traceable Markdown source and, if tooling allows, a .docx export.

Use AGENTS.md tone:
Taiwan Traditional Chinese. Confident, evidence-led, positive-scope writing. Lead with contribution -> evidence -> supported scope -> next implication. Treat limitations as governance layers, claim-evidence alignment, scoped evidence, or planned extensions.

Read first:
- AGENTS.md
- discovery/NEXT_STEP.md
- discovery/DEEP_CULTIVATION_APPLICATION_DRAFT_V0_6.md
- discovery/DEEP_CULTIVATION_OFFICIAL_FORMAT_CROSSWALK.md
- discovery/DEEP_CULTIVATION_MOHW_COMPLIANCE_RUBRIC.md
- discovery/DEEP_CULTIVATION_KPI_BUDGET_ANNUAL_INTEGRATION_TABLE.md
- discovery/DEEP_CULTIVATION_GOVERNANCE_CHECKLIST.md
- discovery/ASSERTIVE_WRITING_GATE.md
- core/ASSERTIVE_WRITING_POLICY.md
- records/2026-05-29/prof-wu-xinyi-proposal-meeting-capture.md
- records/2026-05-29/xinyi-outpatient-proposal-reference/README.md
- records/2026-05-19/policy-documents/README.md

Official working sources:
- records/2026-05-19/policy-documents/application/health-taiwan-phase1-proposal-format-114-115-0909.docx
- records/2026-05-19/policy-documents/application/health-taiwan-phase1-application-guidelines.pdf
- records/2026-05-19/policy-documents/execution/category3-smart-healthcare-governance-lazy-guide-1140702.pdf
- records/2026-05-19/policy-documents/execution/ai-governance-self-checklist.docx
- records/2026-05-19/policy-documents/execution/cybersecurity-governance-self-checklist.docx
- records/2026-05-19/policy-documents/execution/data-governance-self-checklist.docx
- records/2026-05-19/policy-documents/budget/
- records/2026-05-19/policy-documents/qa/

Key decision:
Use official MOHW/Health Taiwan 0909 Word format as the hard outer structure. Use「子計畫三：數位化肌肉骨骼功能評估與居家追蹤計畫」only as an internal composition reference for service-system framing, three-year matrix, organization, governance, KPI, and budget. Do not copy its clinical content or risky claims.

Deliverables:
1. Create:
   discovery/DEEP_CULTIVATION_APPLICATION_DRAFT_V0_7_DOCX_SOURCE.md
2. Create:
   discovery/DEEP_CULTIVATION_DOCX_TRANSFER_CHECKLIST.md
3. If feasible, create:
   exports/deep-cultivation-urology-previsit-v0.7-discussion.docx
   Use pandoc or available repo tooling. If conversion is blocked, document why and provide the exact command to run.
4. Lightly update discovery/NEXT_STEP.md or records/2026-05-31/README.md to record v0.7 docx-source status and next review step. Keep this update minimal.

v0.7 document title:
健康台灣深耕計畫申請討論稿 v0.7
工作題名：泌尿科門診前問診與醫師覆核摘要支持系統
狀態：2026-06-02 討論用 Word 轉換來源稿
定位：官方格式填報討論稿，不是正式送件版

Required official section order:
1. 封面欄位 / Cover page
2. 目錄 placeholder
3. 壹、申請單位自我檢核項目表
4. 貳、計畫概要
5. 參、申請單位簡介
6. 肆、計畫規劃
7. 伍、效益評估
8. 陸、出國計畫書
9. 柒、經費規劃
10. 捌、人力配置表
11. 玖、其他
12. 拾、公職人員利益衝突迴避自主檢核表
13. 拾壹、未有重複申請計畫之聲明切結書
14. 拾貳、參與計畫同意書
15. 拾參、審查意見回復表

Core content:
- Main category: 範疇三：導入智慧科技醫療
- Supporting category: 範疇一：優化醫療工作條件
- Contribution: in urology outpatient or approved screening follow-up context, build low-friction previsit intake, source label, missing-field visibility, one-page clinician-review summary, staff-review / CRM-ready field design, and governance records to reduce repeated questioning, missing-field follow-up, summary preparation, and follow-up organization burden.
- Workflow: 門診/篩檢追蹤入口 -> 低摩擦症狀蒐集 -> patient/family/staff-assisted input -> optional ASR with confirmation -> source label/missing fields -> one-page clinician-review summary -> clinician confirm/edit/ignore/return -> staff-review or CRM-ready queue only if approved -> KPI evaluation/checkpoint.
- Governance before KPI and budget: AI governance, cybersecurity governance, data governance, IRB/QI, procurement governance, FHIR/TW Core IG readiness.
- Scope control: no automatic diagnosis, treatment advice, automatic triage/queue priority, orders, medication, procedure, automatic HIS/EMR writeback, production clinical-use approval, or broad citywide scale before site ownership and governance approval.
- KPI: summary read time <= 60 sec; source label 100%; unsafe wording = 0; missing-field visibility >= 90%; clinician usefulness median >= 4/5; governance owner named or pending explicit; KPI-to-budget traceability 100%.
- Budget: NT$10,000,000 discussion allocation. Year 1 NT$4,000,000; Year 2 NT$3,200,000; Year 3 NT$2,800,000. Every line needs KPI, owner, evidence, procurement note. Formal accounting category, unit price, quantity, procurement threshold remain pending.
- Personnel: role-based table only. Do not invent names. Include parent proposal owner, budget owner, subproject PI/owner, urology clinical lead, outpatient workflow owner, nursing/care-team reviewer, IT/security owner, AI/data governance owner, IRB/QI owner, engineering owner, evaluation owner, proposal coordinator.
- Attachments: recommend governance checklist, KPI-budget table, annual checkpoint table, intended-use freeze, demo-scope freeze, clinical question governance, reviewer scorecard template. Exclude unapproved real patient data or unconfirmed partner/production claims.

Quality gates:
- Every major section must connect to workflow value, KPI, governance, owner, or budget.
- Keep within a 20-page discussion稿 logic.
- Mark pending fields explicitly; do not fabricate applicant, PI, hospital owner, accounting category, unit price, quantity, procurement, IRB/QI approval, security approval, or partner commitment.
- Avoid defensive language like「只是 demo」「僅能」as framing. Use positive-scope wording.
- Do not expand clinical scope or add new AI features.

Validation:
- Run rg checks for risky terms: 自動診斷, 自動分流, 直接寫入, production, HIS writeback, EMR writeback.
- Run rg checks for required terms: AI治理, 資安治理, 資料治理, FHIR, TW Core IG, KPI, owner, evidence, procurement.
- If docx is created, verify file exists and has reasonable size.

Do not commit or push unless explicitly asked.
Final response: list files created/updated, docx status, validation run, pending owner/admin questions, and next step.
```
