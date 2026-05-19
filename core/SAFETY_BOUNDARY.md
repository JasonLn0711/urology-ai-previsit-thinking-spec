# Safety Boundary

## Boundary Statement

The system is a previsit summary aid. It prepares information for clinician review. It does not provide medical judgment.

This boundary is not a legal footnote; it is the organizing rule for the whole system.

## Clinical Boundary

The system may:

- ask patient-friendly previsit questions
- identify missing information
- show patient-reported red flags as neutral observations
- prepare a short clinician-review summary
- make uncertainty visible

The system must not:

- diagnose
- triage
- recommend treatment
- claim that a condition is likely
- tell a patient what action to take
- imply that a clinician is unnecessary
- claim that the summary is clinically complete

## Safe Wording

Allowed wording:

- Reports blood in urine.
- Reports fever or chills.
- Reports being unable to urinate.
- Reports pain or burning with urination.
- Missing information: current medicines.

Disallowed wording:

- Likely infection.
- Probable cancer.
- Needs catheter.
- Take medication.
- Low risk.
- No need to see a doctor.
- Emergency diagnosis.

The rule is simple: describe what was reported; do not infer what it means.

## Privacy Boundary

During discovery, real patient data is out of scope.

The system should not collect:

- names
- phone numbers
- addresses
- national or hospital identifiers
- exact birth dates
- account credentials
- real medical record numbers
- real patient records

If real patient data is ever considered, the project needs a separate governance decision covering consent, retention, deletion, access, responsibility, and review.

## Responsibility Boundary

The clinician is responsible for interpretation. The patient or helper is responsible only for reporting answers as best they can. The system is responsible for preserving those answers clearly and avoiding overstatement.

## Trust Boundary

Every patient-facing or reviewer-facing explanation should make these points clear:

- the system does not diagnose
- the system does not recommend treatment
- a clinician must review all information
- the information may be incomplete or patient-reported
- discovery materials should not contain real patient data

## Governance Boundary

Any expansion beyond previsit summary support requires explicit review. Expansion includes real patient data, clinical recommendations, production claims, automated urgency labels, or connection to hospital record workflows.

## 2026-05-03 Urgent-Care Triage Reference

The 2026-05-03 余總 image/message names `Urgent care intake kiosk with AI triage` as a possible ultimate target and says the practical start can be `協助醫生問診`.

For this thinking repo, that means:

- `協助醫生問診` is aligned with the current previsit summary aid boundary.
- `AI triage`, risk scoring, queue reprioritization, and HIS connection are outside the current boundary.
- A future triage-adjacent version needs a new governance decision before any urgency label, risk score, patient-routing behavior, or HIS data flow is specified.

## 2026-05-19 Deep-Cultivation Meeting Boundary

The 北市聯醫 deep-cultivation meeting supports CRM, APP, AI, reminders, PSA/community screening, and case-management planning only as a governed service workflow.

It does not relax the safety boundary.

The accepted system-positioning supplement is `DEEP_CULTIVATION_SYSTEM_POSITIONING.md`; it should be used when wording grant text or updating the sibling demo repo so that "deep-cultivation upgrade" does not drift into AI triage, autonomous risk scoring, or direct EMR integration.

Before any real patient-data work, the project needs explicit review for:

- IRB training and approval path
- consent and privacy model
- MOU or collaboration records
- security-governance documents
- procurement / vendor responsibility if outsourced
- clinician responsibility and review workflow

Aging Clock and biomarker follow-up must remain research-adjacent until data source, aging definition, biomarker scope, intervention, and review responsibility are defined.
