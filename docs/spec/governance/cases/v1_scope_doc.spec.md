# Governance Cases

## SRGOV-DOC-V1-001

```yaml spec-test
id: SRGOV-DOC-V1-001
title: v1 scope contract doc exists and includes required sections
purpose: Ensures v1 scope and compatibility commitments remain explicit and discoverable.
type: governance.check
check: docs.v1_scope_contract
harness:
  root: .
assert:
  - target: text
    must:
      - contain: ["PASS: docs.v1_scope_contract"]
```
