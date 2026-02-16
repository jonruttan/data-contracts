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
  spec_lang:
    includes:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
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
assert:
- target: violation_count
  must:
  - evaluate:
    - eq:
      - {var: subject}
      - 0
- target: summary_json
  must:
  - evaluate:
    - eq:
      - get:
        - {var: subject}
        - passed
      - true
    - eq:
      - get:
        - {var: subject}
        - check_id
      - runtime.rust_adapter_no_delegate
```
