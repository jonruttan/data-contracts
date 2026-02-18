# Governance Cases

## SRGOV-NORM-001

```yaml contract-spec
id: SRGOV-NORM-001
title: normalization profile defines required source-of-truth fields
purpose: Ensures normalization profile exists and includes all required top-level keys and
  path scopes.
type: governance.check
check: normalization.profile_sync
harness:
  root: .
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
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - normalization.profile_sync
  target: summary_json
```
