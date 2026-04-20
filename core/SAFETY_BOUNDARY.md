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
