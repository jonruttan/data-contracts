# Governance Cases

## SRGOV-CONF-PORT-004

```yaml contract-spec
id: SRGOV-CONF-PORT-004
title: conformance case fields stay aligned with type contract docs
purpose: Ensures portable fixture top-level keys are declared by each type contract
  plus common schema keys.
type: governance.check
check: conformance.type_contract_field_sync
harness:
  root: .
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
  target: violation_count
- id: assert_2
  class: MUST
  asserts:
  - MUST:
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - passed
      - true
    - std.logic.eq:
      - std.object.get:
        - var: subject
        - check_id
      - conformance.type_contract_field_sync
  target: summary_json
```
