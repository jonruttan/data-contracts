# Governance Cases

## SRGOV-CONF-LIB-EXPR-001

```yaml contract-spec
id: SRGOV-CONF-LIB-EXPR-001
title: spec_lang conformance fixture uses shared helper library calls
purpose: Ensures spec_lang conformance fixtures reuse shared conformance helper library functions
  for repeated expression patterns.
type: contract.check
harness:
  root: .
  spec_lang_fixture_library_usage:
    path: /docs/spec/conformance/cases/core/spec_lang.spec.md
    required_library_path: /docs/spec/libraries/conformance/assertion_core.spec.md
    required_call_prefix: conf.
    min_call_count: 4
    required_case_ids:
    - SRCONF-EXPR-001
    - SRCONF-EXPR-002
    - SRCONF-EXPR-008
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
      check: conformance.spec_lang_fixture_library_usage
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
      lit:
        lit:
          std.logic.eq:
          - {var: subject}
          - 0
  target: violation_count
- id: assert_2
  class: MUST
  asserts:
  - evaluate:
      lit:
        lit:
          MUST:
          - std.logic.eq:
            - std.object.get:
              - {var: subject}
              - passed
            - true
          - std.logic.eq:
            - std.object.get:
              - {var: subject}
              - check_id
            - conformance.spec_lang_fixture_library_usage
  target: summary_json
```
