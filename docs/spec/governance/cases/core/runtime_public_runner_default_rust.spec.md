# Governance Cases

## SRGOV-RUNTIME-ENTRY-002

```yaml contract-spec
id: SRGOV-RUNTIME-ENTRY-002
title: public runner defaults to rust mode
purpose: Ensures the canonical public adapter defaults to rust and forbids python impl runtime
  dispatch.
type: governance.check
check: runtime.public_runner_default_rust
harness:
  root: .
  public_runner_default:
    path: /scripts/runner_adapter.sh
    required_tokens:
    - impl="${SPEC_RUNNER_IMPL:-rust}"
    - scripts/rust/runner_adapter.sh
    - python runner impl is no longer supported on the runtime path
    - --impl
    forbidden_tokens:
    - SPEC_RUNNER_IMPL:-python
    - exec "${ROOT_DIR}/scripts/python/runner_adapter.sh"
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
- id: assert_2
  class: must
  asserts:
  - must:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - runtime.public_runner_default_rust
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
  target: summary_json
```
