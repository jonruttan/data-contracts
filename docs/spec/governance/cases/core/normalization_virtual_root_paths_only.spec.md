# Governance Cases

## SRGOV-NORM-PATHS-001

```yaml spec-test
id: SRGOV-NORM-PATHS-001
title: scoped spec paths use canonical virtual-root form
purpose: Ensures path-bearing spec fields use canonical virtual-root `/...` form.
type: governance.check
check: normalization.virtual_root_paths_only
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
      exports:
        policy.pass_when_no_violations:
          from: library.symbol
          path: /policy.pass_when_no_violations
          required: true
    imports:
    - from_step: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- target: summary_json
  must:
  - evaluate:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - normalization.virtual_root_paths_only
```
