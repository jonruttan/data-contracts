# Governance Cases

## SRGOV-CONF-LIB-CONTRACT-001

```yaml spec-test
id: SRGOV-CONF-LIB-CONTRACT-001
title: conformance library contract coverage cases are present
purpose: Ensures conformance includes executable evaluate-based coverage for flat spec_lang.library
  defines contract behavior.
type: governance.check
check: conformance.library_contract_cases_present
harness:
  root: .
  conformance_library_contract_cases_present:
    path: /docs/spec/conformance/cases/core/spec_lang_library_contract.spec.md
    required_case_ids:
    - SRCONF-LIB-CONTRACT-001
    - SRCONF-LIB-CONTRACT-002
    - SRCONF-LIB-CONTRACT-003
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
- target: summary_json
  must:
  - evaluate:
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - conformance.library_contract_cases_present
```
