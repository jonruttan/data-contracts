# Governance Cases

## SRGOV-CONF-API-001

```yaml spec-test
id: SRGOV-CONF-API-001
title: api.http portable conformance cases use canonical shape
purpose: Ensures api.http portable fixtures keep setup under harness and use only canonical behavior assertion targets.
type: governance.check
check: conformance.api_http_portable_shape
harness:
  root: .
assert:
  - target: text
    must:
      - contain: ["PASS: conformance.api_http_portable_shape"]
```
