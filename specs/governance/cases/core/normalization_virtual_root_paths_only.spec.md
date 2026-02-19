# Governance Cases

## SRGOV-NORM-PATHS-001

```yaml contract-spec
id: SRGOV-NORM-PATHS-001
title: scoped spec paths use canonical virtual-root form
purpose: Ensures path-bearing spec fields use canonical virtual-root `/...` form.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: normalization.virtual_root_paths_only
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    'on': summary_json
    assert:
      std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - normalization.virtual_root_paths_only
```
