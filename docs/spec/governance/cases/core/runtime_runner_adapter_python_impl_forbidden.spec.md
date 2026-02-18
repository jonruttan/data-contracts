# Governance Cases

## SRGOV-RUNTIME-ENTRY-003

```yaml contract-spec
id: SRGOV-RUNTIME-ENTRY-003
title: runner adapter hard-fails python impl selection
purpose: Ensures `scripts/runner_adapter.sh` rejects `--impl python` with migration guidance.
type: contract.check
harness:
  root: .
  runner_adapter_python_impl:
    path: /scripts/runner_adapter.sh
    required_tokens:
    - python runner impl is no longer supported on the runtime path
    - Use rust impl instead
    forbidden_tokens:
    - exec "${ROOT_DIR}/scripts/python/runner_adapter.sh" "$@"
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
      check: runtime.runner_adapter_python_impl_forbidden
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
    - lit:
        std.logic.eq:
        - {var: subject}
        - 0
  target: violation_count
```
