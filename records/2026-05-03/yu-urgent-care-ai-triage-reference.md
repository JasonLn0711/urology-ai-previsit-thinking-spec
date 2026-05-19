# 2026-05-03 Yu Urgent-Care AI Triage Reference

## Source
- Sender: Ken Yu / 余金樹.
- Date: `2026-05-03`.
- Message: LINE image and text shared to 吳育德老師.
- Planning capture:
  - `/home/jnclaw/every_on_git_jnclaw/phd-life-system/planning-everything-track/weeks/2026-W18/days/2026-05-03.md`
  - `/home/jnclaw/every_on_git_jnclaw/phd-life-system/planning-everything-track/data/projects/2026-04-urology-ai-previsit-interview/2026-05-03-yu-urgent-care-ai-triage-reference.md`
  - `/home/jnclaw/every_on_git_jnclaw/phd-life-system/planning-everything-track/data/knowledge/healthcare/urology/previsit-interview/assets/2026-05-03-yu-urgent-care-ai-triage/README.md`

Follow-up company sync:

- `2026-05-12` 慧誠智醫 business / PM sync about AI triage and vital-sign kiosk integration.
- Planning source bundle: `/home/jnclaw/every_on_git_jnclaw/phd-life-system/planning-everything-track/data/knowledge/personal/sources/2026-05-12-huicheng-company-ai-triage-sync/`
- Thinking record: `../2026-05-12/huicheng-company-ai-triage-sync.md`

## Exact Text

```text
May 3, 2026 Sunday
11:21 Ken Yu 余金樹 Photos
11:25 Ken Yu 余金樹 @吳育德 昨天提到的Urgent care intake kiosk with AI triage, 這應該是終極目標，但可以先從協助醫生問診開始，然後直接連到HIS. 美國資安太嚴格，短期內外國人軟體應該不容易進去，但其他地區應該是趨勢也有機會。請老師參考一下。
```

## Interpretation
This source clarifies the May 2 `台灣版 triage` language:

- The advanced product direction is a Taiwan-local triage-adjacent system.
- The current urology MVP is the start point, because it already supports `協助醫生問診`.
- HIS connection is a later integration target, not current discovery scope.
- US cybersecurity barriers are business-development context, not a reason to lower safety or privacy standards.
- The `2026-05-12` sync further clarifies that the likely commercial path is tied to 慧誠's vital-sign kiosk, Windows all-in-one deployment constraints, RESTful/FHIR/HIS/EMR integration context, English voice input, and broad urgent-care symptom intake.

## Boundary
Current thinking boundary remains unchanged:

- no real patient data during discovery
- no diagnosis
- no treatment advice
- no autonomous triage
- no risk score
- no queue reprioritization
- no direct HIS / EMR / EHR / registration integration

## Governance Questions
Before any urgent-care / AI-triage direction becomes implementation work, answer:

1. Does `triage` mean information readiness, queue prioritization, risk scoring, or formal clinical triage?
2. Who owns clinical responsibility for any urgency label or queue change?
3. What hospital process approves direct HIS connection?
4. What privacy/security review is needed before any patient identifiers or visit data enter the system?
5. What regulatory language distinguishes physician history-taking support from clinical decision support?
6. Which region and deployment context is being discussed: Taiwan, US, Thailand, Malaysia, Central Asia, Middle East, or another market?

## Next Thinking Action
If this direction stays active, draft a product ladder from:

`協助醫生問診 -> visit-readiness summary -> nurse/clinician review triggers -> governed triage discussion -> HIS integration review`

Do not skip from the current MVP directly to risk scores or queue automation.
