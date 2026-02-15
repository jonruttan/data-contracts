# Governance Cases

## SRGOV-CONF-LIB-EXPR-001

```yaml spec-test
id: SRGOV-CONF-LIB-EXPR-001
title: spec_lang conformance fixture uses shared helper library calls
purpose: Ensures spec_lang conformance fixtures reuse shared conformance helper library functions
  for repeated expression patterns.
type: governance.check
check: conformance.spec_lang_fixture_library_usage
harness:
  root: .
  spec_lang:
    library_paths:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  spec_lang_fixture_library_usage:
    path: /docs/spec/conformance/cases/core/spec_lang.spec.md
    required_library_path: /docs/spec/libraries/conformance/assertion_core.spec.md
    required_call_prefix: conf.
    min_call_count: 4
    required_case_ids:
    - SRCONF-EXPR-001
    - SRCONF-EXPR-002
    - SRCONF-EXPR-008
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
assert:
- target: violation_count
  must:
  - evaluate:
    - eq:
      - {var: subject}
      - 0
- target: summary_json
  must:
  - evaluate:
    - eq:
      - get:
        - {var: subject}
        - passed
      - true
    - eq:
      - get:
        - {var: subject}
        - check_id
      - conformance.spec_lang_fixture_library_usage
```
