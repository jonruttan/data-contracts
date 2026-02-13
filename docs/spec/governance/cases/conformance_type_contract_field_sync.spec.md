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
assert:
  - target: text
    must:
      - contain: ["PASS: conformance.type_contract_field_sync"]
```
