```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-CONF-LIB-CONTRACT-001
    title: conformance library contract coverage cases are present
    purpose: Ensures conformance includes executable evaluate-based coverage for flat spec_lang.export
      defines contract behavior.
    harness:
      root: .
      conformance_library_contract_cases_present:
        path: /specs/conformance/cases/core/spec_lang_library_contract.spec.md
        required_case_ids:
        - DCCONF-LIB-CONTRACT-001
        - DCCONF-LIB-CONTRACT-002
        - DCCONF-LIB-CONTRACT-003
      check:
        profile: governance.scan
        config:
          check: conformance.library_contract_cases_present
      use:
      - ref: /specs/libraries/policy/policy_assertions.spec.md
        as: lib_policy_core_spec
        symbols:
        - policy.assert.no_violations
        - policy.assert.summary_passed
        - policy.assert.summary_check_id
        - policy.assert.scan_pass
    clauses:
      defaults: {}
      imports:
      - from: artifact
        names:
        - summary_json
      predicates:
      - id: assert_1
        assert:
          call:
          - {var: policy.assert.summary_check_id}
          - std.object.assoc:
            - summary_json
            - {var: summary_json}
            - lit: {}
          - conformance.library_contract_cases_present
```
