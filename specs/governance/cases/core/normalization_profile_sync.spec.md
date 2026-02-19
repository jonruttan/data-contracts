# Governance Cases

## SRGOV-NORM-001

```yaml contract-spec
id: SRGOV-NORM-001
title: normalization profile defines required source-of-truth fields
purpose: Ensures normalization profile exists and includes all required top-level keys and
  path scopes.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: normalization.profile_sync
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  imports:
    subject:
      from: artifact
      key: violation_count
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
  - id: assert_2
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
      - normalization.profile_sync
    imports:
      subject:
        from: artifact
        key: summary_json
```
