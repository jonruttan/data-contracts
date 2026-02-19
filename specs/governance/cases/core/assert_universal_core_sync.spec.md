# Governance Cases

## SRGOV-ASSERT-CORE-001

```yaml contract-spec
id: SRGOV-ASSERT-CORE-001
title: assertion docs define universal evaluate core
purpose: Ensures schema and contract docs consistently define evaluate as the universal assertion
  core and classify other operators as authoring sugar.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: assert.universal_core_sync
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
      - assert.universal_core_sync
    imports:
      subject:
        from: artifact
        key: summary_json
```
