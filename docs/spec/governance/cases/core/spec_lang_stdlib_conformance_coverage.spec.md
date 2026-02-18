# Governance Cases

## SRGOV-STDLIB-004

```yaml contract-spec
id: SRGOV-STDLIB-004
title: stdlib conformance coverage files are present
purpose: Ensures canonical stdlib conformance fixtures are present and discoverable.
type: contract.check
harness:
  root: .
  stdlib_conformance:
    required_paths:
    - /docs/spec/conformance/cases/core/spec_lang_stdlib.spec.md
    - /docs/spec/conformance/cases/core/spec_lang_schema.spec.md
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
      check: spec_lang.stdlib_conformance_coverage
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
    - lit:
        lit:
          lit:
            std.logic.eq:
            - {var: subject}
            - 0
  target: violation_count
```
