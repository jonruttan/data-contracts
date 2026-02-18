# Governance Cases

## SRGOV-NORM-PATHS-001

```yaml contract-spec
id: SRGOV-NORM-PATHS-001
title: scoped spec paths use canonical virtual-root form
purpose: Ensures path-bearing spec fields use canonical virtual-root `/...` form.
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
      check: normalization.virtual_root_paths_only
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
        - normalization.virtual_root_paths_only
  target: summary_json
```
