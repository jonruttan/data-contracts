# Governance Cases

## SRGOV-CONF-INDEX-001

```yaml contract-spec
id: SRGOV-CONF-INDEX-001
title: conformance index stays in sync with fixture ids
purpose: Ensures conformance case index includes all fixture ids and no stale ids.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: conformance.case_index_sync
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
    target: violation_count
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
  - id: assert_2
    target: summary_json
    assert:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - conformance.case_index_sync
```
