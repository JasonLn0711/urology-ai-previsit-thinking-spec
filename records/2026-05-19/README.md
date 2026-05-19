# 2026-05-19 Records

## Purpose

This folder captures two separate 2026-05-19 signals:

1. local ASR-ready adaptive demo readiness
2. 北市聯醫深耕計畫 meeting evidence from the morning discussion with 吳老師、美如主任、泌尿科團隊, and related collaborators

These records should be read as governance and planning evidence. They do not authorize real patient-data use, clinical deployment, diagnosis, treatment advice, autonomous triage, or HIS/EMR integration.

The evergreen system-design supplement created from this evidence is `../../core/DEEP_CULTIVATION_SYSTEM_POSITIONING.md`.

The evergreen proposal-writing guide created from this evidence is `../../discovery/DEEP_CULTIVATION_PROPOSAL_WRITING_GUIDE.md`.

The deep-cultivation scoring rubric created from this evidence and the downloaded official requirements is `../../discovery/DEEP_CULTIVATION_SCORING_RUBRIC.md`.
It now includes A/B/C micro-scoring controls: live-source spot checks,
first-principles review questions, cross-validation gates, score caps,
reviewer micro-comment requirements, and urology previsit / CRM interpretation
rules.

The expanded MOHW format/application-compliance rubric is `../../discovery/DEEP_CULTIVATION_MOHW_COMPLIANCE_RUBRIC.md`.
It includes the fourth 100-point D layer plus a non-scored D0 source-freshness
gate for live HTSprout / MOHW / AI Center verification before formal
submission.

The local official-policy archive is `policy-documents/`.

The repository inclusion recommendation is `repo-inclusion-recommendation.md`.

## Files

- `demo-asr-readiness-record.md`
  - Local synthetic-data demo readiness and ASR boundary record.
- `taipei-city-hospital-deep-cultivation-meeting-transcript.md`
  - Corrected detailed transcript assembled from ASR and intermediate transcript drafts.
- `deep-cultivation-meeting-capture.md`
  - Structured meeting capture and same-day synthesis.
- `deep-cultivation-summary-and-signals.md`
  - Concise corrected summary and strategic signal note for the meeting.
- `health-taiwan-deep-cultivation-policy-reference.md`
  - Official policy-context reference for the Health Taiwan Deep-Cultivation Plan and how it maps to this repo.
- `health-taiwan-related-examples.md`
  - Source-backed related examples and proposal patterns found online.
- `taipei-city-hospital-deep-cultivation-working-note.md`
  - Imported and normalized working note from the original `北市聯合醫院 深耕計畫 2026 3650ad7cf431807cb930eec129f0d3f5.md` file.
- `policy-documents/`
  - Downloaded official Health Taiwan Deep-Cultivation policy, application, execution, governance, budget, QA, approved-list, and related briefing files.
- `repo-inclusion-recommendation.md`
  - Recommendation for how to include this thinking spec repo and the sibling demo repo in the proposal evidence package.
- `deep-cultivation-decision-record.md`
  - Decision record for how the meeting changes the thinking repo.
- `deep-cultivation-extraction-notes.md`
  - Paper, product, grant, and research-boundary extraction notes.
- `jason-work-scope-from-deep-cultivation-meeting.md`
  - Jason-specific work-scope interpretation from the recording, with attribution boundaries.
- `expert-review-revise-and-narrow.md`
  - Accepted expert-review direction: Revise + Narrow, use `泌尿科門診前問診與醫師覆核摘要支持系統`, park CRM follow-up, keep ASR as optional multilingual input, and start with non-acute LUTS / OAB-like outpatients.
- `chen-meiru-stakeholder-profile.md`
  - Introduction and proposal-review lens for 陳美如主任: public-hospital service-system leadership, community/family-medicine background, likely priorities around workflow landing, staff-burden reduction, governance, KPI, cross-system continuity, and sustainable operations.
- `sources/`
  - Archived ASR and intermediate transcript files.

## Current Interpretation

The deep-cultivation meeting shifts the near-term framing from a demo-only urology previsit aid toward a broader service-improvement package:

```text
PSA / community screening -> SOP -> return-to-hospital flow -> case management -> CRM -> clinician review
```

AI, APP, ASR, and adaptive questioning remain tools inside a governed service workflow. They are not the primary claim by themselves.

Short strategic label:

```text
AI Systems Engineering for Healthcare Deployment
```

Official policy alignment:

```text
健康台灣深耕計畫(114-118年): 優化醫療工作條件 + 多元人才培訓 + 智慧科技醫療 + 社會責任醫療永續
```

Related examples suggest the stronger proposal pattern is:

```text
workflow improvement + staff-burden reduction + AI as tool + system integration + governance + KPI
```

Proposal writing should therefore start from clinical workflow pain, service landing, KPI, governance, and budget mapping. It should introduce AI/ASR/LLM methods only after the workflow and service value are clear.

Before a formal draft is circulated, score it with:

```text
clinical value and workflow integration
technical system and AI engineering
governance, security, regulation, and sustainability
MOHW format compliance and application completeness
```

Do not collapse those four scores into a single impression score. A draft with strong technical content but weak MOHW format compliance still carries submission risk.

## Latest Expert-Review Direction

After the same-day expert review, the current direction is:

```text
Revise + Narrow.
```

The proposal-facing name is:

```text
泌尿科門診前問診與醫師覆核摘要支持系統
```

The safe descriptive boundary is:

```text
泌尿科門診前症狀蒐集與醫師覆核摘要輔助流程
```

Operational implications:

- Do not write this as an `AI medical system`.
- CRM follow-up is parked until a future confirmed step.
- ASR is only an optional multilingual input layer.
- First-version scope should prioritize non-acute LUTS / OAB-like outpatients: nocturia, frequency, urgency, leakage, voiding difficulty, or weak stream.
- Visible blood, retention/current inability to urinate, fever/chills, and flank pain remain patient-reported red-flag observations, not triage or risk judgments.
- The clinician-facing output should be called `醫師覆核用 SOAP 架構參考摘要`, not `SOAP 病歷草稿`, `自動病歷`, or `自動產生 EMR`.
- Health Taiwan positioning should lead with `範疇三：導入智慧科技醫療`, with `範疇一：優化醫療工作條件` as secondary support.

## 陳美如主任 Stakeholder Lens

For proposal writing, treat 陳美如主任 as a public-hospital service-system reviewer rather than as a model-accuracy reviewer.

Likely top priorities:

- real workflow landing in 北市聯醫, not demo-only AI
- measurable reduction of physician, nursing, or administrative burden
- cross-system continuity across outpatient workflow, community health, case management, CRM, and future HIS/EMR readiness
- governance: human-in-the-loop, data boundary, IRB/privacy/security, audit trail, staff safety, and responsibility
- KPI, annual checkpoints, owner, budget, and maintenance plan
- executive-readable service value
