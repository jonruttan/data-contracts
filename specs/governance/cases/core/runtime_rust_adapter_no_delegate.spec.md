# Governance Cases

## SRGOV-RUNTIME-CONFIG-006

```yaml contract-spec
id: SRGOV-RUNTIME-CONFIG-006
title: rust adapter does not delegate to python shell adapter
purpose: Ensures runners/rust/runner_adapter.sh invokes the Rust CLI directly and does not
  call runners/public/runner_adapter.sh.
type: contract.check
harness:
  root: .
  rust_adapter:
    path: /runners/rust/runner_adapter.sh
    required_tokens:
    - spec_runner_cli
    - cargo run --quiet
    forbidden_tokens:
    - runners/public/runner_adapter.sh
  check:
    profile: governance.scan
    config:
      check: runtime.rust_adapter_no_delegate
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
    imports:
      subject:
        from: artifact
        key: violation_count
  - id: assert_2
    assert:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - runtime.rust_adapter_no_delegate
    imports:
      subject:
        from: artifact
        key: summary_json
```
