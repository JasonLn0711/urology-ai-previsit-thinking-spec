# Versioning Rules

Status: active governance rule

Current version source: `VERSION`

This repository uses project-governance semantic versioning:

```text
vMAJOR.MINOR.PATCH
```

Example:

```text
v1.1.3
```

The version tracks the stability of the thinking spec, proposal package, clinical boundary and governance evidence in this repository. It does not replace Git commits. Git records every change; the version number marks meaningful proposal/governance states.

## Version Files

The source of truth is:

```text
VERSION
```

Machine-readable metadata is stored in:

```text
meta/version.json
```

Human-readable release history is stored in:

```text
CHANGELOG.md
```

Use the automated script:

```bash
python3 scripts/bump_version.py --part patch --summary "Short update summary"
```

Supported bump types:

```bash
python3 scripts/bump_version.py --part patch --summary "Fix wording and indexes"
python3 scripts/bump_version.py --part minor --summary "Add proposal checkpoint package"
python3 scripts/bump_version.py --part major --summary "Freeze first submission-ready package"
```

Dry run:

```bash
python3 scripts/bump_version.py --part patch --summary "Preview only" --dry-run
```

## Version Meaning

### v0.x.y

`v0.x.y` means the repository is still in governed discovery, drafting and proposal-preparation mode.

Use `v0.x.y` before the first complete external proposal package is frozen.

Examples:

- source capture
- meeting records
- deep-cultivation draft refinement
- KPI/budget/governance table improvement
- internal reviewer pack preparation
- precedent analysis

### v1.0.0

Use `v1.0.0` only when the first complete proposal package is ready for external circulation or formal parent-proposal integration.

Minimum conditions:

1. Current proposal draft is frozen.
2. Intended use is frozen.
3. Demo scope is frozen.
4. KPI, budget and annual checkpoints are mapped.
5. Clinical safety boundary is unchanged and explicit.
6. Governance checklist has named owners or clear pending owner fields.
7. Review-response table exists.
8. Changelog records the release.

### v1.x.y

Use `v1.x.y` for compatible updates after the first proposal-ready baseline.

Examples:

- new supporting record
- reviewer feedback integration that does not change intended use
- better KPI wording without changing the evaluation architecture
- budget table refinement within the same approved scope
- additional appendices for the same proposal package

### v2.0.0 and above

Use a new major version when the project identity changes in a way that would require reviewers, clinicians or proposal owners to re-evaluate the system boundary.

Examples:

- expanding from urology previsit support to another specialty as an equal core scope
- reopening CRM follow-up as a funded first-version module
- moving from synthetic/expert review into real patient-data workflow
- adding production HIS/EMR writeback as a core claim
- changing from clinician-review summary to clinical decision support
- changing diagnosis, treatment, triage or queue-priority boundaries

## Bump Rules

### PATCH

Use `PATCH` for changes that improve clarity, evidence traceability or repository navigation without changing proposal scope.

Patch examples:

- typo fixes
- README index updates
- link fixes
- source archive checksum or metadata updates
- adding a dated record that does not change the proposal boundary
- adding notes from a meeting without changing the accepted decision
- improving wording while preserving the same meaning

Command:

```bash
python3 scripts/bump_version.py --part patch --summary "Update record index and source metadata"
```

### MINOR

Use `MINOR` for new proposal, governance or evaluation capability that is compatible with the existing boundary.

Minor examples:

- adding a new official-format draft package
- adding a new KPI-to-budget integration table
- adding a new governance checklist
- adding a new clinician-review protocol
- adding a new mermaid architecture package
- adding a new accepted stakeholder decision that changes execution order but not intended use
- adding a new future-phase spec while keeping it parked

Command:

```bash
python3 scripts/bump_version.py --part minor --summary "Add official-format proposal package"
```

### MAJOR

Use `MAJOR` for changes that alter the clinical, governance or proposal identity of the project.

Major examples:

- first formal proposal-ready freeze from `v0.x.y` to `v1.0.0`
- changing intended use
- changing target users
- changing target clinical workflow
- allowing real patient data after governance approval
- adding formal integration with HIS/EMR/EHR as a core deliverable
- changing the system from previsit workflow support to clinical decision support
- reopening diagnosis, treatment, autonomous triage, queue-priority or prescription-related functions

Command:

```bash
python3 scripts/bump_version.py --part major --summary "Freeze first proposal-ready package"
```

## Required Release Checklist

Before updating a version number:

1. Confirm the current working tree changes belong to this repo.
2. Confirm unrelated user edits are not being rewritten.
3. Decide whether the change is `patch`, `minor` or `major`.
4. Run the bump script.
5. Inspect `VERSION`, `meta/version.json` and `CHANGELOG.md`.
6. Run `git diff --check`.
7. Commit the version bump together with the files that justify it, unless the user asks for separate commits.

## Clinical Boundary Rule

The versioning system must preserve the safety boundary:

```text
Clinical authority remains with clinicians by design.
```

Any change that affects diagnosis, treatment, triage, queue priority, EMR writeback, real patient data, or clinician authority is at least a `MAJOR` candidate and must be reviewed explicitly.

## Proposal Writing Rule

Version notes must be confident and direct.

Use:

```text
Added the official-format checkpoint package.
```

Avoid:

```text
Maybe added some files that might be useful later.
```

Safety boundaries should be written as design architecture, not defensive apology.
