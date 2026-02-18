# Governance Cases

## SRGOV-RUNTIME-CONFIG-006

```yaml contract-spec
id: SRGOV-RUNTIME-CONFIG-006
title: rust adapter does not delegate to python shell adapter
purpose: Ensures scripts/rust/runner_adapter.sh invokes the Rust CLI directly and does not
  call scripts/runner_adapter.sh.
type: contract.check
harness:
  root: .
  rust_adapter:
    path: /scripts/rust/runner_adapter.sh
    required_tokens:
    - spec_runner_cli
    - cargo run --quiet
    forbidden_tokens:
    - scripts/runner_adapter.sh
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: runtime.rust_adapter_no_delegate
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
      lit:
        lit:
          std.logic.eq:
          - {var: subject}
          - 0
  target: violation_count
- id: assert_2
  class: MUST
  asserts:
  - evaluate:
      lit:
        lit:
          MUST:
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
  target: summary_json
```
