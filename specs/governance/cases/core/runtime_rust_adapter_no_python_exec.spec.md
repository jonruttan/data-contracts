# Governance Cases

## SRGOV-RUST-PRIMARY-008

```yaml contract-spec
id: SRGOV-RUST-PRIMARY-008
title: rust runner interface avoids direct python execution tokens
purpose: Ensures the Rust runner interface implementation does not hardcode direct python
  executable invocation.
type: contract.check
harness:
  root: .
  rust_no_python_exec:
    path: /runners/rust/spec_runner_cli/src/main.rs
    forbidden_tokens:
    - python3
    - PYTHON_BIN
    - resolve_python_bin
    - scripts/run_governance_specs.py
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /specs/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: runtime.rust_adapter_no_python_exec
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - {var: subject}
    - 0
  target: violation_count
- id: assert_2
  class: MUST
  asserts:
  - std.logic.eq:
    - std.object.get:
      - {var: subject}
      - passed
    - true
  - std.logic.eq:
    - std.object.get:
      - {var: subject}
      - check_id
    - runtime.rust_adapter_no_python_exec
  target: summary_json
```
