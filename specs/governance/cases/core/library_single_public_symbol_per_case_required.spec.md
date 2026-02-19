# library.single_public_symbol_per_case_required

```yaml contract-spec
id: SRGOV-LIB-SINGLE-001
title: library cases use single public symbol granularity
purpose: Ensures each spec_lang.export case defines exactly one symbol under defines.public.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: library.single_public_symbol_per_case_required
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  steps:
  - id: assert_1
    'on': summary_json
    assert:
      std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
```
