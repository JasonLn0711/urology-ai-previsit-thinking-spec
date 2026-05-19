# Deep-Cultivation Repo Routing Decision

Status: synthesized
Date: 2026-05-19

## Trigger
The 2026-05-19 北市聯醫 / 吳老師 meeting expanded the urology previsit demo
from a standalone ASR / adaptive-intake demonstration into a possible work
package inside the `健康台灣深耕計畫` proposal discussion.

The immediate question was whether the proposal workflow should include both:

- `urology-ai-previsit-demo`
- `urology-ai-previsit-thinking-spec`

## Decision
Include both repos, but keep their ownership separate.

- `urology-ai-previsit-demo` should be used as the product / runnable evidence
  repo.
- `urology-ai-previsit-thinking-spec` should be used as the governance /
  reasoning repo.
- The official `健康台灣深耕計畫` source archive should remain in
  `planning-everything-track`, not copied here.

## First-Principles Reasoning
The scarce resource is reviewer trust.

Reviewer trust does not come from showing more files. It comes from showing that:

1. the demo is real and bounded;
2. the clinical-question logic is governed;
3. the official policy evidence is traceable;
4. the team is not confusing previsit support with diagnosis, triage, or
   production hospital integration.

That requires three different evidence layers:

| Layer | Canonical repo | Why |
| --- | --- | --- |
| Official policy evidence | `planning-everything-track` | Holds downloaded official pages, plan files, governance forms, budget / procurement references, source manifest, and checksums. |
| Runnable product evidence | `urology-ai-previsit-demo` | Shows the actual ASR-ready adaptive-intake workflow, synthetic cases, UI, tests, and proposal-facing product docs. |
| Governance reasoning | `urology-ai-previsit-thinking-spec` | Explains why the system asks bounded previsit questions, preserves clinician authority, avoids clinical claims, and gates real patient data. |

## Proposal Role For This Repo
This repo should contribute:

- safety boundary language;
- clinical-question governance;
- previsit workflow reasoning;
- assumptions and constraints;
- dated decision records;
- reviewer-facing explanation of why the system is a previsit support tool.

It should not contribute:

- official downloaded PDF / DOCX / HTML archive;
- runnable app code;
- screenshots and generated demo artifacts;
- budget binder;
- final hospital submission package.

## Boundary For The Deep-Cultivation Proposal
The urology previsit system may be framed as:

> A governed smart-healthcare workflow module that collects, repairs, and
> summarizes patient-reported urology information before clinician review, and
> can support future PSA / community-screening follow-up and CRM-ready fields.

It must not be framed as:

- AI triage;
- vital-sign risk scoring;
- autonomous diagnosis;
- treatment recommendation;
- medication or exam ordering;
- production HIS / EMR writeback;
- real patient-data deployment.

## Link Back To Planning Archive
Official-source archive:

`../planning-everything-track/data/knowledge/healthcare/policy/assets/health-taiwan-deep-cultivation-2026/`

Planning repo routing record:

`../planning-everything-track/data/projects/2026-05-lianyi-deep-cultivation-plan/source-archive-and-repo-routing.md`

## Next Use
Before the 2026-06-02 follow-up discussion, use this record to keep the proposal
story clean:

1. planning repo for official policy and meeting evidence;
2. demo repo for runnable `UroPrevisit Navigator` evidence;
3. thinking-spec repo for safety and clinical-question governance;
4. future proposal workspace, if created, for integrated writing and budget
   worksheets.
