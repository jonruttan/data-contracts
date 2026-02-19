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
  check:
    profile: governance.scan
    config:
      check: library.domain_index_sync
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    target: summary_json
    assert:
      std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - library.domain_index_sync
```
