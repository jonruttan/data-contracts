# Governance Cases

## SRGOV-RUNTIME-SCOPE-001

```yaml spec-test
id: SRGOV-RUNTIME-SCOPE-001
title: runtime support scope remains bounded for v1
purpose: Prevents uncontrolled cross-runtime expansion by enforcing explicit v1 runtime scope
  tokens in contract docs.
type: governance.check
check: runtime.scope_sync
harness:
  root: .
  runtime_scope:
    files:
    - docs/spec/contract/08_v1_scope.md
    - docs/spec/contract/13_runtime_scope.md
    - docs/spec/contract/12_runner_interface.md
    required_tokens:
    - Python runner
    - PHP runner
    - required support targets
    - contract/governance expansion
    forbidden_tokens:
    - Node.js runner
    - Ruby runner
    - Java runner
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
      exports:
        policy.pass_when_no_violations:
          from: library.symbol
          path: /policy.pass_when_no_violations
          required: true
    imports:
    - from_step: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- target: violation_count
  must:
  - evaluate:
    - std.logic.eq:
      - {var: subject}
      - 0
- target: summary_json
  must:
  - evaluate:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - runtime.scope_sync
```
