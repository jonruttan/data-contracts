# library.single_public_symbol_per_case_required

```yaml spec-test
id: SRGOV-LIB-SINGLE-001
title: library cases use single public symbol granularity
purpose: Ensures each spec_lang.library case defines exactly one symbol under defines.public.
type: governance.check
check: library.single_public_symbol_per_case_required
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
  - evaluate:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
  target: summary_json
```
