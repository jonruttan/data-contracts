# Governance Cases

## SRGOV-RUNTIME-ENTRY-003

```yaml spec-test
id: SRGOV-RUNTIME-ENTRY-003
title: runner adapter hard-fails python impl selection
purpose: Ensures `scripts/runner_adapter.sh` rejects `--impl python` with migration guidance.
type: governance.check
check: runtime.runner_adapter_python_impl_forbidden
harness:
  root: .
  runner_adapter_python_impl:
    path: /scripts/runner_adapter.sh
    required_tokens:
    - python runner impl is no longer supported on the runtime path
    - Use rust impl instead
    forbidden_tokens:
    - exec "${ROOT_DIR}/scripts/python/runner_adapter.sh" "$@"
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
```
