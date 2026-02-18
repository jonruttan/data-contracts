# Governance Cases

## SRGOV-LIB-INDEX-001

```yaml contract-spec
id: SRGOV-LIB-INDEX-001
title: library domain indexes are synchronized
purpose: Ensures each library domain index lists all library files and exported symbols without
  stale entries.
type: contract.check
harness:
  root: .
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /specs/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: library.domain_index_sync
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - std.object.get:
      - {var: subject}
      - check_id
    - library.domain_index_sync
  target: summary_json
```
