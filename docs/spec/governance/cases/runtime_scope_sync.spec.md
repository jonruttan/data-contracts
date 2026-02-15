# Governance Cases

## SRGOV-RUNTIME-SCOPE-001

```yaml spec-test
id: SRGOV-RUNTIME-SCOPE-001
title: runtime support scope remains bounded for v1
purpose: Prevents uncontrolled cross-runtime expansion by enforcing explicit v1 runtime scope tokens in contract docs.
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
  - is_empty:
    - {get: [{subject: []}, violations]}
assert:
- target: violation_count
  must:
  - evaluate:
    - {eq: [{subject: []}, 0]}
- target: summary_json
  must:
  - evaluate:
    - eq:
      - {get: [{subject: []}, passed]}
      - true
    - eq:
      - {get: [{subject: []}, check_id]}
      - runtime.scope_sync
```
