# MOHW Deep-Cultivation Compliance Rubric

Status: working compliance rubric

2026-06-02 official minutes and 2026-06-19 owner update: the parent 信義 AI
智慧問診 allocation is about NT$15M and includes CRM, while Jason / 陽明交大
current package is the NT$10M AI-only workstream. Compliance review for this
package should exclude CRM budget, CRM KPI, CRM procurement, CRM handoff, and
patient messaging. Use the AI-only expert-review packet and proposal item
definitions as the current working materials.

## Purpose

This file expands the fourth 100-point layer from `DEEP_CULTIVATION_SCORING_RUBRIC.md`.

It scores whether a Health Taiwan Deep-Cultivation proposal follows the official MOHW / Health Taiwan application format, required attachments, budget rules, online submission expectations, governance self-checks, and later execution-control documents.

This layer does not judge whether the proposal idea is good. It judges whether the proposal is formally submit-ready, reviewable, contractable, monitorable, and closeable under the official rules.

## Official Reference Set

Live official source refresh:

- Last checked for this rubric update: `2026-05-19`.
- Current primary source: `https://htsprout.nhri.org.tw/download.html`.
- Current smart-healthcare governance source:
  `https://aicenter.mohw.gov.tw/AC/cp-7200-82982-208.html`.
- Current MOHW policy source:
  `https://dep.mohw.gov.tw/TDU/cp-1567-82247-121.html`.

Observed current-source facts on `2026-05-19`:

- The HTSprout download page still groups official files into application,
  execution, funding, and meeting-QA sections.
- The application section lists the `0909` first-stage proposal format, the
  first-stage application guidelines, the online platform manual, the official
  `114-118` plan page, and the official QA.
- The execution section lists the Scope 3 execution information file, AI
  governance self-check, cybersecurity governance self-check, data governance
  self-check, management/control-point documents, checkpoint record, final
  report templates, site-visit form, and Scope 3 smart-healthcare governance
  guide.
- The funding section lists funding standards, funding-use principles,
  negative-list / restricted-item documents, receipt format, and budget
  preparation notes.
- The meeting-QA section includes checkpoint reporting QA, procurement QA, and
  business briefing QA.
- The AI Center source emphasizes that Scope 3 smart-healthcare drafting should
  handle cybersecurity governance, data governance, AI governance, and
  FHIR / TW Core IG readiness as core requirements.
- The MOHW policy page continues to frame `健康台灣深耕計畫(114-118年)` around four
  categories: improving medical working conditions, cultivating diverse talent,
  introducing smart healthcare technology, and sustainable / socially
  responsible healthcare.

Source spot-check on `2026-05-20`:

- The HTSprout plan page still frames the plan as a five-year `114-118` effort,
  with long-term deep-cultivation planning, concrete strategies, and performance
  indicators across the four official categories.
- The HTSprout application-flow page states first-stage execution runs from the
  114 approved-plan date to the end of 115, the second stage runs 116-118, and
  a second-stage solicitation for new applicants is expected in 115 Q4.
- The AI Center governance page still emphasizes cybersecurity governance, data
  governance, AI governance, and FHIR / TW Core IG readiness for Scope 3
  smart-healthcare drafting.
- The MOHW 115-04-27 first-stage results page emphasizes workflow improvement,
  technology reducing ineffective labor, cross-institution collaboration, FHIR
  exchange, and smart-healthcare services rather than model novelty alone.

Reference hierarchy for formal submission:

1. Latest live HTSprout / MOHW / AI Center pages.
2. Latest downloaded official files from those pages.
3. Hospital or applicant-specific written instructions, if they are stricter or
   later than the public files.
4. This rubric as an internal scoring and preflight tool.

Refresh these sources before formal submission:

```text
https://htsprout.nhri.org.tw/download.html
https://aicenter.mohw.gov.tw/AC/cp-7200-82982-208.html
```

Use the local archive as the current working copy:

```text
../records/2026-05-19/policy-documents/
```

Use the current proposal-prep package as the internal working draft set:

```text
INTENDED_USE_FREEZE.md
DEMO_SCOPE_FREEZE.md
ASSERTIVE_WRITING_GATE.md
../core/ASSERTIVE_WRITING_POLICY.md
DEEP_CULTIVATION_OFFICIAL_FORMAT_CROSSWALK.md
DEEP_CULTIVATION_APPLICATION_DRAFT_V0_3.md
DEEP_CULTIVATION_APPLICATION_DRAFT_V0_2.md
DEEP_CULTIVATION_KPI_TO_BUDGET_TABLE.md
DEEP_CULTIVATION_KPI_BUDGET_ANNUAL_INTEGRATION_TABLE.md
DEEP_CULTIVATION_GOVERNANCE_CHECKLIST.md
DEEP_CULTIVATION_ANNUAL_CHECKPOINT_TABLE.md
```

| Official document group | Local file | Use in D layer |
| --- | --- | --- |
| First-stage application guidelines | `../records/2026-05-19/policy-documents/application/health-taiwan-phase1-application-guidelines.pdf` | Eligibility, application mode, submission flow, page / PDF / paper-copy rules, correction risk. |
| First-stage proposal format | `../records/2026-05-19/policy-documents/application/health-taiwan-phase1-proposal-format-114-115-0909.docx` | Official chapter order, cover fields, self-check table, KPI table, budget table, personnel table, declarations. |
| Online platform manual | `../records/2026-05-19/policy-documents/application/health-taiwan-online-platform-user-guide.pdf` | Platform entry, export, upload, version consistency. |
| Official QA | `../records/2026-05-19/policy-documents/qa/health-taiwan-qa-1140710.pdf` | Interpretation of scope, application, governance, and execution questions. |
| Scope 3 smart-healthcare governance guide | `../records/2026-05-19/policy-documents/execution/category3-smart-healthcare-governance-lazy-guide-1140702.pdf` | Cybersecurity governance, data governance, AI governance, FHIR, TW Core IG, SMART on FHIR. |
| AI governance self-check | `../records/2026-05-19/policy-documents/execution/ai-governance-self-checklist.docx` | Scope 3 AI governance attachment and internal review evidence. |
| Cybersecurity governance self-check | `../records/2026-05-19/policy-documents/execution/cybersecurity-governance-self-checklist.docx` | Security-governance attachment and internal review evidence. |
| Data governance self-check | `../records/2026-05-19/policy-documents/execution/data-governance-self-checklist.docx` | Data-governance attachment and internal review evidence. |
| Management and monitoring points | `../records/2026-05-19/policy-documents/execution/management-and-monitoring-points.pdf` | Later execution, monitoring, checkpoint, and closeout readiness. |
| Checkpoint record template | `../records/2026-05-19/policy-documents/execution/checkpoint-reporting-record-114-115.docx` | Annual / stage checkpoint planning and evidence format. |
| Final results report template | `../records/2026-05-19/policy-documents/execution/final-results-report-114-115.docx` | Closeout and outcome reporting readiness. |
| Funding-use principles | `../records/2026-05-19/policy-documents/budget/funding-use-principles-1140922.pdf` | Budget-use limits, capital ratio, dedicated account, approved-use principle. |
| Negative list / restricted items | `../records/2026-05-19/policy-documents/budget/negative-list-and-restricted-items-1140922.pdf` | Prohibited / restricted expense screening. |
| Funding standards | `../records/2026-05-19/policy-documents/budget/funding-standards-second-revision-1150413.pdf` | Personnel, operating, travel, equipment, reimbursement, and itemized cost standards. |
| Procurement QA | `../records/2026-05-19/policy-documents/qa/health-taiwan-procurement-qa-updated.pdf` | Vendor, outsourcing, procurement, and contract risk interpretation. |

## D-Layer Gate Rules

Apply these gates before calculating a polished score:

| Gate | Result |
| --- | --- |
| Latest official source list not checked before formal submission | Maximum D score: 89 |
| A newer official template/guideline is found but the draft still uses an older structure | Maximum D score: 69 |
| Proposal cites official requirements but cannot point to the exact current source file or URL | Maximum D score: 79 |
| No official proposal format used | Maximum D score: 49 |
| Required self-check / declaration set missing | Maximum D score: 59 |
| Budget table missing or not tied to work packages | Maximum D score: 59 |
| Scope 3 smart-healthcare proposal lacks AI / cybersecurity / data-governance checks | Maximum D score: 69 |
| Platform version and paper/PDF version conflict | Maximum D score: 69 |
| Outward-facing narrative opens with defensive limitation language instead of contribution and workflow value | Maximum D score: 89 |
| Any legal eligibility problem unresolved | Do not submit until resolved. |
| Any hospital-specific instruction conflicts with this local archive | Follow the latest official / hospital instruction and update this file. |

## Narrative Confidence Preflight

This is a D-layer reviewability gate, not a style preference.

Before Word transfer or external circulation, confirm:

| Check | Pass condition |
| --- | --- |
| Contribution-first summary | The project summary starts with the workflow contribution and Health Taiwan value. |
| Boundary-as-design wording | Diagnosis, treatment, triage, EMR, real-data, and deployment boundaries are written as governed design choices. |
| Staff-burden value | The summary names physician/nurse/staff burden reduction before technical novelty. |
| Evidence route | KPI, budget, governance, and annual checkpoint evidence are visible. |
| No apologetic framing | The draft avoids self-weakening phrases such as `只是`, `僅僅`, `just a demo`, and `we only` except in source quotes. |

Use:

```text
contribution -> workflow value -> deliberate scope -> governance boundary -> next evidence gate
```

See `ASSERTIVE_WRITING_GATE.md`.

## D Score Summary

| Section | Points | Core question |
| --- | ---: | --- |
| D1. Applicant eligibility and application mode | 10 | Can this applicant/team legally and procedurally apply under the selected mode? |
| D2. Proposal format and page/layout compliance | 12 | Does the document satisfy the official format rules? |
| D3. Cover, basic data, and institution fields | 8 | Are the platform, PDF, paper, and official-letter identities consistent? |
| D4. Self-check forms and required declarations | 10 | Are all required signed/sealed self-check and declaration forms present? |
| D5. Official chapter order and required content fields | 12 | Does the content follow the official chapter structure and field expectations? |
| D6. Performance indicators and annual checkpoints | 12 | Are KPI, baseline, targets, checkpoints, progress, spending, and dates auditable? |
| D7. Budget planning and funding-rule compliance | 14 | Is each budget item lawful, itemized, justified, and tied to KPI/work package? |
| D8. Personnel allocation and partner workshare | 6 | Are roles, subproject owners, partners, and personnel budget consistent? |
| D9. AI / cybersecurity / data governance alignment | 8 | Does scope 3 smart healthcare include required governance documents and standards? |
| D10. Submission flow, correction risk, and version consistency | 8 | Can the team submit, correct, and preserve identical versions without administrative failure? |
| Total | 100 |  |

## Evidence-Capped Rule For D

Use the same evidence cap from the main rubric:

| Evidence level | Maximum credit |
| --- | ---: |
| No evidence | 0% |
| Claim only | 40% |
| Draft artifact | 70% |
| Internally checked artifact | 90% |
| Signed / submitted / officially confirmed artifact | 100% |

Example:

```text
If the proposal says "合作機構同意參與" but has no signed participation consent,
D4-5 is capped at 40%.
```

# D0. Source Freshness And Official-Document Crosswalk: Non-Scored Gate

D0 is not part of the 100 points. It is the precondition that makes the 100-point
D score meaningful.

If D0 is weak, reviewers may still fill D1-D10 for internal learning, but the
proposal should not be treated as formally submission-ready.

| Item | Evidence required | Full-credit standard | Cap if missing |
| --- | --- | --- | ---: |
| D0-1 Latest source refresh | Refresh log with date, URLs, and reviewer. | HTSprout download page, MOHW policy page, and AI Center governance page checked before formal submission. | 89 |
| D0-2 Official file inventory | Source manifest or proposal appendix table. | Proposal team knows which official application, execution, funding, QA, and governance files control the draft. | 79 |
| D0-3 Template version check | Template filename and date in working notes. | Draft uses the latest proposal format or records why a hospital-provided version controls. | 69 |
| D0-4 Local archive vs live source check | Diff or manual checklist. | Local archive filenames match the live source list; missing or newer files are downloaded or flagged. | 79 |
| D0-5 Hospital instruction override check | Meeting note, email, or admin instruction. | Any hospital-specific rule is recorded and reconciled with public MOHW rules. | 79 |
| D0-6 Source-to-score mapping | D-layer scoring sheet. | Each D1-D10 score points to a source file, official URL, form field, or submission artifact. | 79 |
| D0-7 Submission-stage distinction | Draft label. | Draft distinguishes first-stage application, revised approved plan, execution report, checkpoint report, and final report requirements. | 79 |
| D0-8 Urology proposal boundary | Proposal evidence map. | Demo / synthetic evidence, future pilot, and real clinical deployment are not mixed. | 69 |

Required D0 source groups:

| Source group | Must answer |
| --- | --- |
| Application guidelines | Who may apply, how many cases/modes are allowed, what must be submitted, what correction window applies, and what review route applies. |
| Proposal format | What fields, section order, tables, signatures, and page/layout rules the proposal must follow. |
| Online platform manual | How platform entry, upload, PDF export, and version consistency are controlled. |
| QA set | Which ambiguous rules have official clarifications. |
| Funding standards and principles | What can be budgeted, how capital/current categories work, what the negative list forbids, and what evidence is needed for reimbursement. |
| Scope 3 governance guide | What AI, cybersecurity, data governance, FHIR, TW Core IG, and SMART on FHIR readiness should mean. |
| AI/cybersecurity/data governance self-checks | Which official self-check artifacts must exist for smart-healthcare software/data work. |
| Monitoring/checkpoint/final-report templates | Whether proposed KPI and deliverables can survive execution monitoring and closeout. |

# D1. Applicant Eligibility And Application Mode: 10

| Item | Points | Evidence required | Full-credit standard | Low / zero-score signal |
| --- | ---: | --- | --- | --- |
| D1-1 Applicant type eligibility | 2 | Applicant type and proof. | Applicant is identified as an eligible medical institution, community medical group, MOHW-recognized specialty society, professional association, or other accepted applicant type. | Applicant type is vague or outside allowed categories. |
| D1-2 Eligibility proof attached | 2 | Institution code, registration number, tax ID, or equivalent. | Required proof is included and matches cover/platform data. | Proof omitted or inconsistent. |
| D1-3 One application mode selected | 2 | Official form / cover / platform mode. | Applicant and partner group select one valid mode/category without duplication. | Multiple modes selected without explanation. |
| D1-4 Main applicant and partner relationship | 2 | Partner table, MOU / consent route, system/alliance note. | Same-system, alliance, cross-hospital, community, university, vendor, or clinic roles are clear. | Partner list is a name dump without relationship. |
| D1-5 Scope/category fit | 2 | Selected scope list and content map. | Selected categories one to four are backed by real content and KPI. | Category selected only to look comprehensive. |

Urology proposal note:

```text
If 北市聯醫 or a specific院區 is the formal applicant, the proposal must match
that applicant's legal name, code, responsible person, and internal submission route.
```

# D2. Proposal Format And Page/Layout Compliance: 12

| Item | Points | Evidence required | Full-credit standard | Low / zero-score signal |
| --- | ---: | --- | --- | --- |
| D2-1 Single merged PDF | 2 | Final exported PDF inventory. | One merged PDF contains proposal and required signed materials. | Multiple loose files without official merged version. |
| D2-2 File size | 1 | File size check. | PDF is within official limit; downloaded guideline currently indicates 25 MB for upload. | Oversized PDF with no compression plan. |
| D2-3 Font | 2 | Word/PDF style check. | Chinese uses official Chinese font; English/numbers use official English font unless latest template changes. | Mixed fonts from copy-paste. |
| D2-4 Font size | 1 | Style check. | Main body follows official 12 pt rule except headings, tables, TOC, or allowed template parts. | Body text shrunk to force page limit. |
| D2-5 Line spacing | 1 | Style check. | Fixed line height follows official rule; current archive indicates 15 pt. | Random spacing or compressed lines. |
| D2-6 Margins | 1 | Page setup check. | Margins follow official rule; current archive indicates 1.5 cm. | Modified margins to fit content. |
| D2-7 Header/footer | 1 | Page setup check. | Header/footer follow official rule; current archive indicates 0.5 cm. | Header/footer omitted or inconsistent. |
| D2-8 Page numbers | 1 | PDF visual check. | Page numbers are complete and match TOC. | TOC page references wrong after PDF export. |
| D2-9 Page limit | 1 | Page count check. | Body stays within official page limit; current archive indicates 40 pages excluding specified materials. | Main content exceeds limit or hides core text in appendix. |
| D2-10 Paper copy / binding | 1 | Submission checklist. | Paper copies and binding follow official instruction; current archive indicates double-sided glue-bound 1 set x 6 copies. | Paper copy requirement ignored. |

# D3. Cover, Basic Data, And Institution Fields: 8

| Item | Points | Evidence required | Full-credit standard | Low / zero-score signal |
| --- | ---: | --- | --- | --- |
| D3-1 Project title consistency | 1 | Platform, PDF, paper copy, official letter. | Same project title everywhere. | Different title versions across files. |
| D3-2 City/county correctness | 1 | Cover and applicant address. | County/city reflects main applicant. | City selected by project site but not applicant rule. |
| D3-3 Application mode correctness | 1 | Cover/platform/category. | Official mode and subcategory match D1. | Cover and platform disagree. |
| D3-4 Scope categories | 1 | Cover and chapter content. | Scope one to four selections match actual work. | ESG/smart-healthcare boxes checked without sections. |
| D3-5 Main institution data | 1 | Name, code, registration, tax ID. | Main institution data complete. | Abbreviated hospital name only. |
| D3-6 Partner institution data | 1 | Partner table and consent/MOU plan. | Partners have names, codes or registration info, and relationship. | Partner names in prose only. |
| D3-7 Funding and period | 1 | Cover and budget table. | Amount, matching funds, period, and annual table agree. | Cover total differs from budget. |
| D3-8 PI/contact data | 1 | Cover and platform. | PI/contact title, phone, email complete and current. | Missing direct contact or old email. |

# D4. Self-Check Forms And Required Declarations: 10

| Item | Points | Evidence required | Full-credit standard | Low / zero-score signal |
| --- | ---: | --- | --- | --- |
| D4-1 Applicant self-check table | 2 | Completed official self-check table. | Every required row checked with consistent notes. | Blank self-check or unchecked critical rows. |
| D4-2 Conflict-of-interest self-check | 2 | Public official conflict-of-interest self-check. | Required form is signed/sealed by the appropriate party. | Form omitted because team assumes it is irrelevant. |
| D4-3 Relationship disclosure decision | 1 | Disclosure form or not-applicable basis. | Relationship disclosure is included when needed or correctly marked not applicable. | No evidence of decision. |
| D4-4 No-duplicate-application declaration | 2 | Signed/sealed declaration. | PI and institution sign/seal statement that no duplicate subsidy is requested. | Similar government funding not addressed. |
| D4-5 Partner participation consent | 2 | Signed partner consent forms. | Partner responsible persons sign/seal consent where required. | Partner listed but no consent route. |
| D4-6 Scanned signatures merged | 1 | Final PDF check. | Signed materials are scanned and merged into the proposal PDF. | Signature pages stored separately and forgotten. |

# D5. Official Chapter Order And Required Content Fields: 12

| Item | Points | Evidence required | Full-credit standard | Low / zero-score signal |
| --- | ---: | --- | --- | --- |
| D5-1 Official order preserved | 2 | Proposal outline vs official template. | Chapter order follows official format: self-check, overview, institution intro, planning, benefits/KPI, overseas plan if applicable, budget, personnel, other, declarations, response table. | Custom order replaces official structure. |
| D5-2 Table of contents | 1 | Final PDF TOC. | TOC generated and page references checked after export. | TOC stale or missing. |
| D5-3 Project overview | 2 | Overview section. | Basis, current state, problem analysis, and local need are complete. | Generic policy slogans only. |
| D5-4 Existing-government-funding distinction | 2 | Funding distinction section. | Explains overlap, distinction, or connection with existing MOHW, ministry, city, or hospital subsidies. | Duplicate-funding risk ignored. |
| D5-5 Applicant institution introduction | 1 | Institution intro section. | Institution capability, equipment, track record, and roles fit official limit. | Long brochure text without relevance. |
| D5-6 Project planning | 2 | Planning section by scope/year. | Annual goals and work packages map to selected scopes and 114-118 / applicable years. | Work package list not connected to scope. |
| D5-7 Overseas plan handling | 1 | Overseas plan section. | Included only when scope 2 / talent training requires it; follows official cost and trip rules. | Unneeded travel section inserted. |
| D5-8 Attachments and appendix handling | 1 | Attachment list. | Attachments support core content and do not hide required sections. | Critical KPI/budget/governance content pushed to appendix. |

# D6. Performance Indicators And Annual Checkpoints: 12

| Item | Points | Evidence required | Full-credit standard | Low / zero-score signal |
| --- | ---: | --- | --- | --- |
| D6-1 KPI for each selected scope | 2 | KPI table. | Every selected scope has at least one measurable indicator. | Scope selected but no KPI. |
| D6-2 KPI definition | 2 | Formula / definition column. | Numerator, denominator, method, measurement period, and data owner are clear. | KPI is a slogan such as "improve efficiency". |
| D6-3 Baseline/current data | 2 | Baseline column. | Current data or baseline collection method is supplied. | Baseline blank or "TBD". |
| D6-4 Annual targets | 2 | Annual target columns. | Required annual values are realistic and connected to work packages. | Yearly targets copied across years without logic. |
| D6-5 Checkpoint work content | 1 | Checkpoint table. | Quarterly/annual work content and checkpoint descriptions exist. | Work content only says "continue implementation". |
| D6-6 Cumulative progress | 1 | Cumulative progress %. | Percentage progress is credible and staged. | 90% progress before procurement/IRB gate. |
| D6-7 Cumulative spending | 1 | Spending by checkpoint. | Spending aligns with budget timing and procurement stages. | Spending front-loaded without deliverable. |
| D6-8 Expected result and date | 1 | Expected result/date field. | Each checkpoint has a verifiable output and due date. | No measurable deliverable. |

Urology proposal note:

```text
For 子計畫二, good KPI candidates include previsit completion rate, clinician
summary usefulness score, missing-field reduction, CRM follow-up completion,
security-governance gate completion, and prototype/pilot readiness evidence.
```

# D7. Budget Planning And Funding-Rule Compliance: 14

| Item | Points | Evidence required | Full-credit standard | Low / zero-score signal |
| --- | ---: | --- | --- | --- |
| D7-1 Annual budget table | 2 | Official annual budget table. | Required years, totals, and scope allocation are complete. | Only total amount shown. |
| D7-2 Subsidy vs matching funds | 1 | Budget columns. | Subsidy, matching funds, and totals are separated and consistent. | Matching funds hidden in prose. |
| D7-3 Current vs capital categories | 2 | Itemized budget. | Personnel, operating, equipment, and capital/current categories are correct. | Software service placed under wrong category. |
| D7-4 Capital expense ratio | 2 | Capital-ratio calculation. | Capital expense generally respects the 30% principle unless justified and approved. | Equipment-heavy budget without rationale. |
| D7-5 Personnel budget | 1 | Personnel budget detail. | Salary, labor insurance, health insurance, pension/retirement or equivalent are handled. | RA listed but no salary basis. |
| D7-6 Operating expenses | 1 | Operating-item detail. | Expenses directly tie to tasks, KPI, and work packages. | Generic "miscellaneous" line. |
| D7-7 Equipment expenses | 1 | Equipment justification. | Equipment is necessary, proportionate, and tied to outputs. | Expensive hardware unrelated to KPI. |
| D7-8 Scope-level allocation | 1 | Scope allocation table. | Budget is mapped to scope one to four or selected categories. | Budget cannot be traced to scope. |
| D7-9 Unit price / quantity / explanation | 1 | Itemized unit table. | Unit price, quantity, period, and explanation are auditable. | Lump sum only. |
| D7-10 Negative-list compliance | 1 | Negative-list review. | No prohibited or restricted items are included. | Restricted item included without approval route. |
| D7-11 Dedicated account / actual-use awareness | 1 | Budget narrative. | Proposal recognizes dedicated account, approved-purpose use, and no diversion. | Budget treated as flexible pool. |

Urology proposal note:

```text
Do not add CRM, APP, API, ASR, kiosk, smart pharmacy, or vendor lines unless
each has a matching objective, KPI, owner, procurement route, and governance gate.
```

# D8. Personnel Allocation And Partner Workshare: 6

| Item | Points | Evidence required | Full-credit standard | Low / zero-score signal |
| --- | ---: | --- | --- | --- |
| D8-1 PI role | 1 | Personnel table. | PI owns total coordination, decision, and reporting responsibility. | PI listed only by name. |
| D8-2 Co-PI roles | 1 | Personnel table. | Clinical, engineering, administrative, and governance roles are explicit. | Co-PIs duplicated without responsibility split. |
| D8-3 Subproject owners | 1 | Subproject map. | Each 子計畫 has an owner and backup/contact. | Subproject ownership unclear. |
| D8-4 Staff/assistant work | 1 | Work-scope column. | Staff and RA work nature, task, and scope are written concretely. | "協助計畫" only. |
| D8-5 Partner workshare | 1 | Partner table / MOU route. | Each partner has concrete tasks, deliverables, and data/permission boundaries. | Partner listed for prestige only. |
| D8-6 Personnel/budget consistency | 1 | Personnel vs budget cross-check. | Human resources match personnel budget and workplan. | Budget hires no one for critical task. |

# D9. AI / Cybersecurity / Data Governance Alignment: 8

| Item | Points | Evidence required | Full-credit standard | Low / zero-score signal |
| --- | ---: | --- | --- | --- |
| D9-1 AI governance self-check | 2 | AI governance checklist and workplan mapping. | AI governance self-check is completed or scheduled with owner and evidence. | AI system described with no governance attachment. |
| D9-2 Cybersecurity governance self-check | 2 | Cybersecurity checklist and architecture/security notes. | Security governance self-check exists for system/data/API/APP work. | "Use hospital network" treated as sufficient. |
| D9-3 Data governance self-check | 2 | Data-governance checklist and data-flow map. | Patient data, EMR, CRM, FHIR, or data-sharing work has data-governance review. | Data use described but source/retention/access omitted. |
| D9-4 Three AI Centers / certification alignment | 1 | Governance narrative. | Proposal acknowledges responsible AI, clinical AI validation, and AI impact evaluation path if applicable. | Certification/validation claims made without path. |
| D9-5 FHIR / TW Core IG / SMART on FHIR | 1 | Interoperability plan. | Proposal uses these as readiness standards where data exchange is claimed. | HIS/EMR integration claimed with no standard. |

Urology proposal note:

```text
If the first version is a synthetic-data demo, D9 should score boundary clarity:
no real patient data, no production writeback, and a future governance gate before
any live CRM/HIS/EMR use.
```

# D10. Submission Flow, Correction Risk, And Version Consistency: 8

| Item | Points | Evidence required | Full-credit standard | Low / zero-score signal |
| --- | ---: | --- | --- | --- |
| D10-1 Platform entry complete | 1 | Platform checklist / screenshots if available. | Required online platform fields are complete. | Platform entry left until final hour. |
| D10-2 Exported PDF checked | 1 | Exported PDF review. | PDF export matches platform and Word source. | PDF export breaks TOC/tables/signature pages. |
| D10-3 Paper copies prepared | 1 | Paper-copy checklist. | Required copies and binding are prepared on time. | Printing left unresolved. |
| D10-4 Online/paper consistency | 2 | Version-control evidence. | Online, PDF, paper copy, and official letter are identical where required. | Different budget totals across versions. |
| D10-5 Correction deadline tracked | 1 | Submission calendar. | Correction window is tracked; current guideline states three working days after notice. | Team misses correction window. |
| D10-6 One-correction-limit risk | 1 | Internal preflight checklist. | Team performs pre-submission checks because correction is limited. | Relies on external correction to catch errors. |
| D10-7 Official letter / identifiers | 1 | Official letter and submission metadata. | Project title, unit, codes, and identifiers match everywhere. | Official letter uses old title or wrong unit. |

# D-Layer Penalty Table

| Issue | Penalty |
| --- | ---: |
| Not using official proposal format | -20 |
| Arbitrarily changing official chapter order | -10 |
| PDF over official file-size limit | -5 |
| Proposal body over official page limit | -8 |
| Font, spacing, or margin clearly noncompliant | -5 to -10 |
| Missing applicant self-check table | -10 |
| Missing conflict-of-interest self-check | -10 |
| Missing no-duplicate-application declaration | -10 |
| Missing partner participation consent where required | -8 |
| KPI table lacks baseline/current data | -10 |
| Annual checkpoint table missing | -10 |
| Budget table inconsistent with work packages | -10 |
| Capital budget over ratio without explanation / approval route | -10 |
| Negative-list or restricted item unresolved | -10 |
| Scope 3 smart healthcare without AI/cybersecurity/data governance checklists | -10 |
| FHIR / TW Core IG absent while claiming data exchange | -5 |
| Platform/PDF/paper versions inconsistent | -15 |
| Correction-window ownership missing | -5 |

# D-Layer Pre-Submission Evidence Packet

Before circulating a formal draft, collect this packet:

| Evidence | Owner to assign | Required before |
| --- | --- | --- |
| Live official source refresh log | Proposal coordinator | First full draft and final submission |
| Official proposal template version | Proposal coordinator | First full draft |
| Source-to-score crosswalk for D1-D10 | Proposal coordinator | Internal review |
| Applicant eligibility proof | Hospital admin | First full draft |
| Main applicant / partner identity table | PI / admin | First full draft |
| Scope category map | Proposal lead | First full draft |
| KPI table with baseline and annual targets | Subproject owners | Internal review |
| Annual checkpoint table | Project manager | Internal review |
| Budget table with unit price, quantity, category, KPI link | Finance / subproject owners | Internal review |
| Negative-list and capital-ratio check | Finance | Internal review |
| AI governance self-check | AI / engineering owner | Scope 3 review |
| Cybersecurity governance self-check | Security / IT owner | Scope 3 review |
| Data governance self-check | Data / privacy owner | Scope 3 review |
| Partner participation consent / MOU route | PI / hospital admin | Submission draft |
| Conflict-of-interest and relationship disclosure decision | Admin | Submission draft |
| No-duplicate-application declaration | PI / admin | Submission draft |
| Platform/PDF/paper consistency check | Proposal coordinator | Final submission |
| Correction-window owner | Proposal coordinator | Final submission |

# Urology Previsit Draft-Specific D-Layer Checklist

For the 北市聯醫 / urology previsit / CRM-support proposal, score D with these extra checks:

- If `urology previsit` is framed under scope 3, D9 must include AI, cybersecurity, and data-governance self-check routing.
- If CRM, APP, API, or reminders are budgeted, D7 must show KPI and procurement/governance route.
- If PSA/community screening is included, D6 must include follow-up/return-to-care KPI, not only screening count.
- If real patient data is mentioned, D4/D9 must trigger IRB, consent, privacy, retention, access, and deletion questions.
- If the demo repo is cited, D5/D9 must label it as synthetic prototype evidence, not clinical deployment evidence.
- If HIS/EMR/FHIR is mentioned, D9 must distinguish future interoperability readiness from current production writeback.
- If Aging Clock / biomarker work is included, D1/D5/D6/D7/D9 must identify whether it is a research sub-study, service add-on, or separate proposal lane.

Core rule:

```text
D is not a paperwork afterthought.
D is the proof that the proposal can survive official intake, review, budgeting,
contracting, monitoring, governance checks, and final reporting.
```
