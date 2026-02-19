# Governance Cases

## SRGOV-CONF-LIB-CONTRACT-001

```yaml contract-spec
id: SRGOV-CONF-LIB-CONTRACT-001
title: conformance library contract coverage cases are present
purpose: Ensures conformance includes executable evaluate-based coverage for flat spec_lang.export
  defines contract behavior.
type: contract.check
harness:
  root: .
  conformance_library_contract_cases_present:
    path: /specs/conformance/cases/core/spec_lang_library_contract.spec.md
    required_case_ids:
    - SRCONF-LIB-CONTRACT-001
    - SRCONF-LIB-CONTRACT-002
    - SRCONF-LIB-CONTRACT-003
  check:
    profile: governance.scan
    config:
      check: conformance.library_contract_cases_present
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
        - check_id
      - conformance.library_contract_cases_present
```
