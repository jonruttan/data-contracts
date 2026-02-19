# Governance Cases

## SRGOV-CONTRACT-001

```yaml contract-spec
id: SRGOV-CONTRACT-001
title: contract governance rules pass via governance harness
purpose: Ensures contract policy and traceability integrity checks are enforced through the
  governance spec pipeline.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: contract.governance_check
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
      - contract.governance_check
    imports:
      subject:
        from: artifact
        key: summary_json
```
