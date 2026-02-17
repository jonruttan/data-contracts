# Governance Cases

## SRGOV-RUST-PRIMARY-008

```yaml spec-test
id: SRGOV-RUST-PRIMARY-008
title: rust runner interface avoids direct python execution tokens
purpose: Ensures the Rust runner interface implementation does not hardcode direct python
  executable invocation.
type: governance.check
check: runtime.rust_adapter_no_python_exec
harness:
  root: .
  rust_no_python_exec:
    path: /scripts/rust/spec_runner_cli/src/main.rs
    forbidden_tokens:
    - python3
    - PYTHON_BIN
    - resolve_python_bin
    - scripts/run_governance_specs.py
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
      - runtime.rust_adapter_no_python_exec
  target: summary_json
```
