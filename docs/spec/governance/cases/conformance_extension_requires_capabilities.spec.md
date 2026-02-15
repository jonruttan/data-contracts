# Governance Cases

## SRGOV-CONF-PORT-003

```yaml spec-test
id: SRGOV-CONF-PORT-003
title: extension type conformance cases declare requires.capabilities
purpose: Ensures non-core type fixtures explicitly declare required capabilities for portable parity.
type: governance.check
check: conformance.extension_requires_capabilities
harness:
  root: .
  policy_evaluate:
  - is_empty:
    - get:
      - subject: []
      - violations
assert:
- target: text
  must:
  - contain:
    - 'PASS: conformance.extension_requires_capabilities'
```
