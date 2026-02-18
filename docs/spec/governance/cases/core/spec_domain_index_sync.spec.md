# Governance Cases

## SRGOV-SPECLAYOUT-INDEX-001

```yaml contract-spec
id: SRGOV-SPECLAYOUT-INDEX-001
title: spec domain indexes are synchronized
purpose: Ensures each domain index tracks all spec files in its subtree and has no
  stale paths.
type: governance.check
check: spec.domain_index_sync
harness:
  root: .
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - std.object.get:
      - var: subject
      - check_id
    - spec.domain_index_sync
  target: summary_json
```
