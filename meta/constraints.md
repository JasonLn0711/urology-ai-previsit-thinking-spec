# Constraints

## Repository Constraints

- This repository is independent.
- It is a sibling of `planning-everything-track`.
- It must not live inside the planning repository.
- It must not move, rename, or rewrite existing planning files.
- It must not break existing Markdown links.
- It should remain plain Markdown for easy review and versioning.

## Content Constraints

- No code.
- No programming language discussion.
- No system connection plan.
- No hidden assumptions.
- No real patient data.
- No diagnosis or treatment advice.
- No claims that the concept is clinically complete.
- No vague "AI magic" explanations.
- No AI-first grant framing when the evidence supports visit-readiness workflow and clinician-reviewed summary instead.
- No deep-cultivation wording that upgrades the current urology previsit design into AI triage, autonomous risk scoring, or direct HIS/EMR/EHR writeback.
- No proposal budget line without a matching objective, KPI, owner, and governance path.
- No high proposal score without traceable evidence for the scored item.
- No scoring credit for autonomous triage, diagnosis, treatment recommendation, or direct HIS/EMR/EHR writeback unless a future separately governed scope explicitly authorizes it.
- No defensive, apologetic, or self-weakening article/proposal tone. Boundaries must be written as deliberate design choices, not as retreat. Use `../core/ASSERTIVE_WRITING_POLICY.md` for all outward-facing writing.

## Clinical Constraints

- Clinician review remains mandatory.
- The system may prepare information but must not interpret disease meaning.
- Patient-reported red flags must remain neutral observations.
- The summary must make missing information visible.
- Any patient-facing wording must avoid false reassurance.

## Privacy Constraints

- Discovery materials should use non-real examples only.
- Real patient identifiers are not allowed.
- Any future real patient-data use requires consent, retention, access, deletion, and responsibility rules.

## 2026-05-19 Deep-Cultivation Constraints

- Participants who handle research, papers, human-subject content, or patient data need IRB training before entering that workstream.
- Cross-unit cooperation should be backed by appropriate MOU or written collaboration records.
- KPI and budget must match; no budget line should appear without a corresponding plan objective and KPI.
- APP, platform, API, questionnaire, or vendor work may require procurement / tender review before execution.
- AI, APP, API, and patient-data flows require security-governance review before real deployment or real patient-data use.
- After the 2026-06-19 owner update, CRM is out of scope for Jason / 陽明交大. Do not write CRM outsourcing, CRM-ready handoff, patient messaging, LINE/SMS integration, vendor hosting, production follow-up, CRM KPI, CRM budget, or CRM maintenance into the current AI 問診 package.
- After the 2026-06-23 official meeting minutes and 2026-07-01 北市聯醫 LINE
  update, the proposed 2026-07-14 same-time parent-proposal gate requires one
  merged Huashan / Xinyi plan with KPI, budget, partner route, owner, evidence,
  and procurement / asset-category controls.
- Each parent project should treat NT$37,500,000 per year as the current expected cap until the budget owner confirms otherwise.
- Budget writing must include a 50-60% review-cut scenario while preserving claim-evidence aligned KPI service capacity.
- Hardware equipment and intangible assets, including self-built systems, must remain inside the 30% budget-control rule.
- Software systems should be framed as rental / service / license paths when appropriate; Health Cabin is currently framed as a direct-purchase asset subject to procurement and 30% controls.
- 忠孝院區泌尿科 PSA screening can be integrated into the proposal architecture, but clinical SOP, guideline compliance, abnormal-case handling, and clinical responsibility must remain owned or confirmed by the clinical unit.
- Aging Clock must not be treated as an accepted service claim until data source, aging definition, biomarker scope, intervention, and governance are defined.
- Health Taiwan policy alignment should be explicit: claims should map to smart healthcare, working-condition improvement, talent training, or sustainable/social-responsibility healthcare instead of using generic `AI innovation` language.
- External examples are pattern evidence only. Do not imply the urology proposal has the same approval status, outcomes, or clinical validation unless separately verified.

## Use Constraints

This repository may support:

- product decision-making
- paper framing
- patent reasoning
- workflow analysis
- governance review
- meeting preparation

This repository must not be used as:

- a clinical protocol
- a patient-facing medical instruction set
- a regulatory submission
- a production deployment specification
- proof that the system is safe for real-world use
