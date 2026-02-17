# runtime.chain_exports_list_only_required

```yaml spec-test
id: SRGOV-CHAIN-FORM-001
title: chain exports use list-only canonical form
purpose: Ensures harness.chain step exports reject legacy mapping form and require list-form
  entries.
type: governance.check
check: runtime.chain_exports_list_only_required
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
      - as: policy.pass_when_no_violations
        from: library.symbol
        required: true
        path: /policy.pass_when_no_violations
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
      - passed
    - true
  target: summary_json
```

