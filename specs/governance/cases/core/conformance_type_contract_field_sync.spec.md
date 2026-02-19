# Governance Cases

## SRGOV-CONF-PORT-004

```yaml contract-spec
id: SRGOV-CONF-PORT-004
title: conformance case fields stay aligned with type contract docs
purpose: Ensures portable fixture top-level keys are declared by each type contract plus common
  schema keys.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: conformance.type_contract_field_sync
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
      - conformance.type_contract_field_sync
    imports:
      subject:
        from: artifact
        key: summary_json
```
