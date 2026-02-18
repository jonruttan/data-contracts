# runtime.chain_exports_list_only_required

```yaml contract-spec
id: SRGOV-CHAIN-FORM-001
title: chain exports use list-only canonical form
purpose: Ensures harness.chain step exports reject legacy mapping form and require
  list-form entries.
type: governance.check
check: runtime.chain_exports_list_only_required
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

