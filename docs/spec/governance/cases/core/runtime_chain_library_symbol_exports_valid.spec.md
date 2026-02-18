# runtime.chain_library_symbol_exports_valid

```yaml contract-spec
id: SRGOV-CHAIN-FROM-003
title: chain assert function imports are valid
purpose: Ensures from=assert.function step imports include valid symbol path and contract
  shape.
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
      check: runtime.chain_library_symbol_exports_valid
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
    - lit:
        std.logic.eq:
        - std.object.get:
          - {var: subject}
          - passed
        - true
  target: summary_json
```
