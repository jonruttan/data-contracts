# runtime.executable_spec_lang_includes_forbidden

```yaml contract-spec
id: SRGOV-CHAIN-FROM-004
title: executable cases forbid spec_lang includes
purpose: Ensures executable case types do not use harness.spec_lang.includes and load
  symbols through harness.chain.
type: governance.check
check: runtime.executable_spec_lang_includes_forbidden
harness:
  root: .
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - std.object.get:
      - var: subject
      - passed
    - true
  target: summary_json
```
