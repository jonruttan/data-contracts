# Governance Cases

## SRGOV-REF-PATHS-001

```yaml spec-test
id: SRGOV-REF-PATHS-001
title: contract paths referenced by specs exist
purpose: Ensures referenced contract-root paths fail fast when missing.
type: governance.check
check: reference.contract_paths_exist
harness:
  root: .
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
      exports:
        policy.pass_when_no_violations:
          from: library.symbol
          path: /policy.pass_when_no_violations
          required: true
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- id: assert_1
  class: must
  checks:
  - std.logic.eq:
    - std.object.get:
      - var: subject
      - check_id
    - reference.contract_paths_exist
  target: summary_json
```
