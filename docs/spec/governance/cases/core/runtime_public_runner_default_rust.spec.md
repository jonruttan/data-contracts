# Governance Cases

## SRGOV-RUNTIME-ENTRY-002

```yaml spec-test
id: SRGOV-RUNTIME-ENTRY-002
title: public runner defaults to rust mode
purpose: Ensures the canonical public adapter defaults to rust and dispatches both supported
  impl modes.
type: governance.check
check: runtime.public_runner_default_rust
harness:
  root: .
  public_runner_default:
    path: /scripts/runner_adapter.sh
    required_tokens:
    - impl="${SPEC_RUNNER_IMPL:-rust}"
    - scripts/rust/runner_adapter.sh
    - scripts/python/runner_adapter.sh
    - --impl
    forbidden_tokens:
    - SPEC_RUNNER_IMPL:-python
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
    - from_step: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- target: violation_count
  must:
  - evaluate:
    - std.logic.eq:
      - {var: subject}
      - 0
- target: summary_json
  must:
  - evaluate:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - runtime.public_runner_default_rust
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
```
