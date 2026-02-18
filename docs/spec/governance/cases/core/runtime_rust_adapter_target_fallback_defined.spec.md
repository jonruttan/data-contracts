# Governance Cases

## SRGOV-RUNTIME-PREPUSH-004

```yaml contract-spec
id: SRGOV-RUNTIME-PREPUSH-004
title: rust adapter defines preferred-target fallback and strict mode
purpose: Ensures local rust adapter can fallback to host target while supporting strict target
  enforcement.
type: governance.check
check: runtime.rust_adapter_target_fallback_defined
harness:
  root: .
  rust_target_fallback:
    path: /scripts/rust/runner_adapter.sh
    required_tokens:
    - resolve_rust_target_mode
    - preferred target missing; using host target
    - SPEC_RUNNER_RUST_TARGET_STRICT
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
contract:
- id: assert_1
  class: must
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
```
