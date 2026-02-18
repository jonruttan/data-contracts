# Governance Cases

## SRGOV-RUNTIME-CONTRACT-SPEC-002

```yaml contract-spec
id: SRGOV-RUNTIME-CONTRACT-SPEC-002
title: legacy executable fence token is forbidden
purpose: Enforces hard-cut removal of legacy executable fence token on canonical surfaces.
type: governance.check
check: runtime.legacy_spec_test_fence_forbidden
contract:
- id: assert_1
  class: MUST
  target: violation_count
  asserts:
  - std.logic.eq:
    - var: subject
    - 0
```
