# runtime.chain_exports_from_key_required

```yaml spec-test
id: SRGOV-CHAIN-FROM-001
title: chain exports use canonical from key
purpose: Ensures harness.chain step exports declare the required from field and do not rely
  on legacy key forms.
type: governance.check
check: runtime.chain_exports_from_key_required
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
      - passed
    - true
  target: summary_json
```
