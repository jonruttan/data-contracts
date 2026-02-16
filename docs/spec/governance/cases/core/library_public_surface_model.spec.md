# Governance Cases

## SRGOV-LIB-SURFACE-001

```yaml spec-test
id: SRGOV-LIB-SURFACE-001
title: library public/private surface model is enforced
purpose: Ensures spec_lang.library cases use definitions.public/definitions.private scopes
  and do not use legacy export shape.
type: governance.check
check: library.public_surface_model
harness:
  root: .
  spec_lang:
    includes:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
assert:
- target: summary_json
  must:
  - evaluate:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - library.public_surface_model
```
