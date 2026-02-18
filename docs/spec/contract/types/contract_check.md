# Type Contract: contract.check

## Status

- v1 core type

## Purpose

Execute a typed harness check profile and assert externally visible behavior through
contract assertions.

## Required Fields

- `id` (string)
- `type` (must equal `contract.check`)
- `harness` (mapping with `check.profile` and `check.config`)
- `contract` (list of assertion steps)

## Optional Fields

- common optional fields from schema v1 (`title`, `purpose`, `assert_health`, `expect`, `requires`)

## Targets

- profile-defined subject targets (for example `text`, `stdout`, `stderr`, `summary_json`, `violation_count`)

## Type Rules

- runner-only setup/config keys MUST live under `harness`.
- `harness.check.profile` selects the canonical runtime profile.
- `harness.check.config` carries profile-specific input fields.
- assertions evaluate profile subjects only; they must not depend on internal runtime structures.

## Failure Category Guidance

- schema violations -> `schema`
- assertion mismatches -> `assertion`
- runtime/profile faults -> `runtime`
