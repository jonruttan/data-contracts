# Governance Cases

## SRGOV-CONF-PORT-004

```yaml spec-test
id: SRGOV-CONF-PORT-004
title: conformance case fields stay aligned with type contract docs
purpose: Ensures portable fixture top-level keys are declared by each type contract plus common schema keys.
type: governance.check
check: conformance.type_contract_field_sync
harness:
  root: .
  spec_lang:
    library_paths:
    - ../../libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  policy_evaluate:
  - {call: [{var: [policy.pass_when_no_violations]}, {subject: []}]}
assert:
- target: violation_count
  must:
  - evaluate:
    - {eq: [{subject: []}, 0]}
- target: summary_json
  must:
  - evaluate:
    - eq:
      - {get: [{subject: []}, passed]}
      - true
    - eq:
      - {get: [{subject: []}, check_id]}
      - conformance.type_contract_field_sync
```
