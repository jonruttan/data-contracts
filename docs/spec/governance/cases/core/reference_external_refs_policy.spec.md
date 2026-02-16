# Governance Cases

## SRGOV-REF-EXTERNAL-001

```yaml spec-test
id: SRGOV-REF-EXTERNAL-001
title: external refs require explicit policy and capability
purpose: Ensures external:// references are deny-by-default and must declare allow policy.
type: governance.check
check: reference.external_refs_policy
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
    - from: lib_policy_core_spec
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
      - reference.external_refs_policy
```
