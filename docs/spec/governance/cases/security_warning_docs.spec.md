# Governance Cases

## SRGOV-DOC-SEC-001

```yaml spec-test
id: SRGOV-DOC-SEC-001
title: required trust-model docs declare non-sandboxed trusted-input contract
purpose: Ensures required docs state that spec execution is not sandboxed and untrusted specs are unsafe.
type: governance.check
check: docs.security_warning_contract
harness:
  root: .
  policy_evaluate:
    - ["is_empty", ["get", ["subject"], "violations"]]
assert:
  - target: text
    must:
      - contain: ["PASS: docs.security_warning_contract"]
```
