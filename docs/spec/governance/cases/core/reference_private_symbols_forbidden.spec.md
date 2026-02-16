# Governance Cases

## SRGOV-REF-SYMBOLS-004

```yaml spec-test
id: SRGOV-REF-SYMBOLS-004
title: private library symbols are not referenced externally
purpose: Ensures conformance/governance/impl cases do not reference defines.private symbols
  from library docs.
type: governance.check
check: reference.private_symbols_forbidden
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
      - reference.private_symbols_forbidden
```
