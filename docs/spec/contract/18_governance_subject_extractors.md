# Governance Subject Extractor Contract (v1)

## Purpose

Defines the extractor/policy split for governance checks:

1. extractor stage gathers deterministic repository data
2. policy stage evaluates `policy_evaluate` via spec-lang

## Extractor Output Shape

Governance check implementations SHOULD return a structured payload with:

- `subject`: primary policy input (rows/report/object)
- `violations`: candidate violation messages (data-only)
- `symbols` (optional): symbol table values for policy evaluation
- `policy_evaluate`: list-based spec-lang expression
- `policy_path`: source location token for diagnostics

## Determinism Requirements

- Extractors MUST be deterministic for the same repository state.
- Extractors MUST NOT use ambient time/random/network data.
- Extractors MUST NOT decide final pass/fail directly.

## Policy Requirements

- Final verdict MUST be the result of `policy_evaluate`.
- On policy failure, diagnostics MUST include `case_id`, `check_id`, and
  `policy_path`.
- Check-specific branch text like `"<check> policy_evaluate returned false"`
  MUST NOT be embedded in check implementations.

## Migration Notes

For scanner-first checks:

- keep scanner logic as extractor data production
- move boolean gate logic into `policy_evaluate`
- preserve stable violation messages for CI diagnostics
