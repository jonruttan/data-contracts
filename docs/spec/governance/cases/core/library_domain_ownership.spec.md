# Governance Cases

## SRGOV-LIB-DOMAIN-001

```yaml spec-test
id: SRGOV-LIB-DOMAIN-001
title: library paths obey domain ownership
purpose: Ensures conformance cases use conformance libraries and governance cases use policy/path
  libraries.
type: governance.check
check: library.domain_ownership
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
- id: assert_1
  class: must
  checks:
  - std.logic.eq:
    - std.object.get:
      - var: subject
      - check_id
    - library.domain_ownership
  target: summary_json
```
