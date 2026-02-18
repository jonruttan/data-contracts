# Governance Cases

## SRGOV-LIB-SURFACE-001

```yaml contract-spec
id: SRGOV-LIB-SURFACE-001
title: library public/private surface model is enforced
purpose: Ensures spec_lang.export cases use defines.public/defines.private scopes and do not
  use non-canonical export shape.
type: contract.check
harness:
  root: .
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: library.public_surface_model
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
    - lit:
        std.logic.eq:
        - std.object.get:
          - {var: subject}
          - check_id
        - library.public_surface_model
  target: summary_json
```
