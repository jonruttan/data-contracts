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
      check: conformance.type_contract_docs
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - {var: subject}
    - 0
  target: violation_count
- id: assert_2
  class: MUST
  asserts:
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
  target: summary_json
```
