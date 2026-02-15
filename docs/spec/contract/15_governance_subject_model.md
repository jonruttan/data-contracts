# Governance Subject Model Contract (v1)

## Purpose

Enable governance checks to run decision logic in spec-lang by separating:

1. deterministic repository-data extraction (adapter/substrate), and
2. pure expression evaluation (`evaluate`).

## Model

Governance checks MUST expose typed, deterministic subject payloads to
spec-lang expressions instead of embedding decision logic in Python scanners.

Subject payload examples:

- list of conformance case rows with leaf-op summaries
- list of string fields for ambient-pattern scanning
- normalized docs token tables for sync checks

## Constraints

- Subject extraction MUST be deterministic for the same repository state.
- Subject extraction MUST avoid network/ambient time/random dependencies.
- Spec-lang expressions remain pure and side-effect free.

## Migration Policy

When migrating a governance check:

- keep extraction in adapter code
- move pass/fail decision into spec-lang `policy_evaluate`
- preserve error category and stable message expectations
- keep behavior parity with previous scanner logic
- avoid per-check policy verdict branching text in extractor functions

Naming rule:

- Assertion trees use `evaluate`.
- Governance/orchestration policy fields use `policy_evaluate`.

Hard requirement:

- Governance decision checks MUST declare and evaluate `policy_evaluate`.
- Extractor outputs and central policy evaluation contract are defined in:
  `docs/spec/contract/18_governance_subject_extractors.md`.

## Initial Migration Scope

First checks targeted by this model:

- `conformance.spec_lang_preferred`
- `conformance.no_ambient_assumptions`
- `conformance.portable_determinism_guard`
