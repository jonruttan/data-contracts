# Governance Cases

## SRGOV-LIB-SURFACE-001

```yaml contract-spec
id: SRGOV-LIB-SURFACE-001
title: library public/private surface model is enforced
purpose: Ensures spec_lang.export cases use defines.public/defines.private scopes
  and do not use legacy export shape.
type: governance.check
check: library.public_surface_model
harness:
  root: .
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
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
    - std.object.get:
      - var: subject
      - check_id
    - library.public_surface_model
  target: summary_json
```
