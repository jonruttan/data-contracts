# Governance Cases

## SRGOV-RUNTIME-CONFIG-006

```yaml spec-test
id: SRGOV-RUNTIME-CONFIG-006
title: rust adapter does not delegate to python shell adapter
purpose: Ensures scripts/rust/runner_adapter.sh invokes the Rust CLI directly and does not
  call scripts/runner_adapter.sh.
type: governance.check
check: runtime.rust_adapter_no_delegate
harness:
  root: .
  rust_adapter:
    path: /scripts/rust/runner_adapter.sh
    required_tokens:
    - spec_runner_cli
    - cargo run --quiet
    forbidden_tokens:
    - scripts/runner_adapter.sh
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- id: assert_1
  class: must
  checks:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
- id: assert_2
  class: must
  checks:
  - must:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - runtime.rust_adapter_no_delegate
  target: summary_json
```
