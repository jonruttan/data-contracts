```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-OBJECTIVE-003
    title: objective tripwires are clean
    purpose: Ensures objective manifest tripwire checks map to valid governance checks and currently
      pass.
    harness:
      root: .
      objective_tripwires:
        manifest_path: /specs/governance/metrics/objective_manifest.yaml
        cases_path: /specs/governance/cases
        case_file_pattern: '*.spec.md'
      check:
        profile: governance.scan
        config:
          check: objective.tripwires_clean
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
          - objective.tripwires_clean
        imports:
        - from: artifact
          names:
          - summary_json
```
