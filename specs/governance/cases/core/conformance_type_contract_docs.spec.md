# Governance Cases

## SRGOV-CONF-TYPE-001

```yaml contract-spec
id: SRGOV-CONF-TYPE-001
title: conformance case types have matching type contract docs
purpose: Ensures each type used by portable conformance fixtures is documented under the type-contract
  index.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: conformance.type_contract_docs
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
      - conformance.type_contract_docs
    imports:
      subject:
        from: artifact
        key: summary_json
```
