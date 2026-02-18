# runtime.chain_exports_from_key_required

```yaml contract-spec
id: SRGOV-CHAIN-FROM-001
title: chain exports use canonical from key
purpose: Ensures harness.chain step exports declare the required from field and do not rely
  on non-canonical key forms.
type: contract.check
harness:
  root: .
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /specs/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: runtime.chain_exports_from_key_required
contract:
- id: assert_1
  class: MUST
  asserts:
  - std.logic.eq:
    - std.object.get:
      - {var: subject}
      - passed
    - true
  target: summary_json
```
