# library.single_public_symbol_per_case_required

```yaml contract-spec
id: SRGOV-LIB-SINGLE-001
title: library cases use single public symbol granularity
purpose: Ensures each spec_lang.export case defines exactly one symbol under defines.public.
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
      check: library.single_public_symbol_per_case_required
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
      lit:
        lit:
          std.logic.eq:
          - std.object.get:
            - {var: subject}
            - passed
          - true
  target: summary_json
```
