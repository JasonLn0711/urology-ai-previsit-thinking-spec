# Assertive Writing Policy

Status: canonical writing policy
Date: 2026-05-20

## Purpose

This repository's writing must be confident, direct, and non-defensive.

This applies to:

- article drafts
- proposal drafts
- paper framing
- reviewer briefs
- lab briefs
- grant positioning
- project narrative
- public-facing or stakeholder-facing summaries

The system has deliberate boundaries. Those boundaries should be written as mature architecture, not as apology.

Core rule:

```text
Safety boundaries stay.
Defensive tone goes.
Positive operating scope leads.
```

## Positive-Scope Document Design

Design outward-facing documents around what the work enables, what evidence
supports, what clinical or operational scope it owns, and what the next
validation layer will confirm.

Avoid using denial, apology, or defensive posture as the paragraph's organizing
voice. A proposal should not sound like it is asking forgiveness for having
scope controls. It should show that the scope controls are part of the system's
professional design.

Use direct negative wording only when legal, clinical, safety, or exact-source
precision requires it. When a negative statement is necessary, pair it with the
affirmative operating scope.

Default order:

```text
capability -> workflow value -> evidence -> scope control -> next gate
```

## Non-Negotiable Writing Stance

Write from this stance:

```text
This project is a deliberately scoped clinical workflow-support system.
It reduces previsit information friction, prepares clinician-reviewable summaries,
preserves clinician authority, and creates a governed path for smart-healthcare deployment.
```

Do not write from this stance:

```text
This is only a small demo, not a real medical AI, and we are not sure whether it is useful.
```

The first stance is accurate, confident, and reviewable.
The second stance weakens the work before the reviewer has evaluated it.

## Boundaries Are Design Choices

When describing exclusions, use design logic.

| Defensive wording | Assertive replacement |
| --- | --- |
| The system cannot diagnose. | Clinical diagnosis remains with physicians by design. |
| We do not do triage. | The first version focuses on previsit information readiness, not autonomous urgency assignment. |
| This is only a demo. | The current artifact is a governed workflow prototype for expert review and proposal development. |
| It is not a full HIS/EMR system. | The system is a focused previsit workflow layer designed to coexist with HIS/EMR boundaries. |
| We only summarize. | The system compresses patient-reported previsit narratives into clinician-reviewable handoff artifacts. |
| The AI is not perfect. | All AI-supported outputs remain source-labeled, reviewable, and under clinician authority. |
| We still need more research. | The next stage evaluates measurable workflow value, safety boundaries, and staff-burden reduction under defined governance gates. |

## Forbidden Tone Patterns

Avoid wording that makes the project sound apologetic, uncertain, or self-minimizing:

- `只是`
- `僅僅`
- `小小的 demo`
- `還不成熟`
- `不能算是`
- `不敢說`
- `沒有什麼`
- `初步而已`
- `可能有一點幫助`
- `不是很完整`
- `需要更多研究才能知道有沒有價值`
- `we only`
- `we merely`
- `just a demo`
- `preliminary only`
- `limited prototype`
- `not really`
- `maybe useful`

If a sentence needs caution, use governance language instead of apology.

## Preferred Vocabulary

Use these phrases when they match the evidence:

- deliberately scoped
- governed workflow layer
- clinician-review artifact
- source-labeled summary
- previsit information compression
- clinical handoff support
- workflow friction reduction
- staff-burden reduction
- review-ready evidence package
- governance-ready design
- human-authority preserving
- audit-ready
- bounded implementation path
- measurable workflow value
- low-friction clinical workflow support
- smart-healthcare deployment pathway

## Proposal Writing Rule

A proposal paragraph should start with the contribution, then name the scope, then name the governance boundary.

Preferred:

```text
本子計畫建立泌尿科門診前問診與醫師覆核摘要支持系統，將病人或家屬於候診階段可安全提供的症狀資訊，整理為一頁式、來源可追溯的醫師覆核摘要。系統聚焦降低重複問診、缺漏資訊修補與文書準備負擔；診斷、治療決策與正式病歷紀錄仍由醫師掌握。
```

Avoid:

```text
本系統只是輔助工具，不能診斷，也不能取代醫師，目前只是初步 demo，未來還需要更多研究。
```

## Paper Writing Rule

A paper contribution should be written as a positive research claim.

Preferred:

```text
We present a governed previsit intake and clinician-review summary workflow that compresses patient-reported urology narratives into source-labeled handoff artifacts while preserving clinician authority.
```

Avoid:

```text
We only build a preliminary chatbot and do not provide diagnosis or treatment.
```

## Safety Boundary Language

Safety language must remain precise, but it should not sound defensive.

Use:

```text
The architecture keeps final clinical interpretation with physicians and restricts the system to previsit collection, missing-information visibility, and clinician-review summary preparation.
```

Avoid:

```text
The system is not allowed to make decisions, so it can only collect information.
```

## Review Checklist

Before accepting any outward-facing draft, check:

- Does the first paragraph state the contribution before limitations?
- Are boundaries written as deliberate design choices?
- Is clinical authority preserved without apologetic wording?
- Does the draft lead with workflow value, staff-burden reduction, and deployability?
- Does the document avoid making denial, apology, or defensive posture the organizing voice?
- Does it avoid `only`, `just`, `merely`, `只是`, and `僅僅` unless quoting someone else?
- Does the draft sound like a serious clinical workflow engineering project rather than a defensive AI demo?

If any answer fails, revise the wording before using the draft.
