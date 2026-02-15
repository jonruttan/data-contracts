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
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  policy_evaluate:
  - {call: [{var: policy.pass_when_no_violations}, {var: subject}]}
assert:
- target: violation_count
  must:
  - evaluate:
    - {eq: [{var: subject}, 0]}
- target: summary_json
  must:
  - evaluate:
    - eq:
      - {get: [{var: subject}, passed]}
      - true
    - eq:
      - {get: [{var: subject}, check_id]}
      - conformance.type_contract_field_sync
```
