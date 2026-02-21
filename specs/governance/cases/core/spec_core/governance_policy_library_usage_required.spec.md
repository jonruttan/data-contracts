```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-POLICY-LIB-002
    title: governance policy expressions require shared library wiring
    purpose: Ensures governance decision policies use shared spec-lang libraries and call exported
      library symbols.
    harness:
      root: .
      policy_library_requirements:
        cases_path: /specs/governance/cases
        case_file_pattern: '*.spec.md'
        ignore_checks:
        - governance.policy_library_usage_required
      check:
        profile: governance.scan
        config:
          check: governance.policy_library_usage_required
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
        - violation_count
      predicates:
      - id: assert_1
        assert:
          call:
          - {var: policy.assert.no_violations}
          - std.object.assoc:
            - violation_count
            - {var: violation_count}
            - lit: {}
      - id: assert_2
        assert:
        - call:
          - {var: policy.assert.summary_passed}
          - std.object.assoc:
            - summary_json
            - {var: summary_json}
            - lit: {}
        - call:
          - {var: policy.assert.summary_check_id}
          - std.object.assoc:
            - summary_json
            - {var: summary_json}
            - lit: {}
          - governance.policy_library_usage_required
        imports:
        - from: artifact
          names:
          - summary_json
```
