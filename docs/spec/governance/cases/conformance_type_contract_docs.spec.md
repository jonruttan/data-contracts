# Governance Cases

## SRGOV-CONF-TYPE-001

```yaml spec-test
id: SRGOV-CONF-TYPE-001
title: conformance case types have matching type contract docs
purpose: Ensures each type used by portable conformance fixtures is documented under the type-contract index.
type: governance.check
check: conformance.type_contract_docs
harness:
  root: .
assert:
  - target: text
    must:
      - contain: ["PASS: conformance.type_contract_docs"]
```
