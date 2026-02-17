# Governance Cases

## SRGOV-LIB-SURFACE-001

```yaml spec-test
id: SRGOV-LIB-SURFACE-001
title: library public/private surface model is enforced
purpose: Ensures spec_lang.library cases use defines.public/defines.private scopes and do
  not use legacy export shape.
type: governance.check
check: library.public_surface_model
harness:
  root: .
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- id: assert_1
  class: must
  checks:
  - std.logic.eq:
    - std.object.get:
      - var: subject
      - check_id
    - library.public_surface_model
  target: summary_json
```
