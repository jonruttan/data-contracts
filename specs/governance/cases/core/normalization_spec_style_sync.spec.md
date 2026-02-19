# Governance Cases

## SRGOV-NORM-004

```yaml contract-spec
id: SRGOV-NORM-004
title: normalization spec style policy stays profile-driven
purpose: Ensures conformance style limits and wording remain synchronized with the normalization
  profile and governance scanner constants.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: normalization.spec_style_sync
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
    assert:
      std.logic.eq:
      - {var: subject}
      - 0
    imports:
      subject:
        from: artifact
        key: violation_count
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
      - normalization.spec_style_sync
    imports:
      subject:
        from: artifact
        key: summary_json
```
