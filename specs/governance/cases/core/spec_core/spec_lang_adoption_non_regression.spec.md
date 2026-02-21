```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-SPEC-LANG-002
  title: spec-lang adoption metric is non-regressing
  purpose: Enforces monotonic non-regression for spec-lang adoption metrics against checked-in baseline.
  harness:
    root: "."
    spec_lang_adoption_non_regression:
      baseline_path: "/specs/governance/metrics/spec_lang_adoption_baseline.json"
      summary_fields:
        overall_logic_self_contained_ratio: non_decrease
        native_logic_escape_case_ratio: non_increase
        governance_library_backed_policy_ratio: non_decrease
        governance_symbol_resolution_ratio: non_decrease
        library_public_surface_ratio: non_decrease
      segment_fields:
        conformance:
          mean_logic_self_contained_ratio: non_decrease
        governance:
          mean_logic_self_contained_ratio: non_decrease
          library_backed_policy_ratio: non_decrease
          governance_symbol_resolution_ratio: non_decrease
      epsilon: 1.0e-12
      spec_lang_adoption:
        roots:
        - "/specs/conformance/cases"
        - "/specs/governance/cases"
        - runner-owned implementation specs
        segment_rules:
        - prefix: specs/conformance/cases
          segment: conformance
        - prefix: specs/governance/cases
          segment: governance
        - prefix: runner-owned implementation specs
          segment: impl
        recursive: true
    check:
      profile: governance.scan
      config:
        check: spec.spec_lang_adoption_non_regression
    use:
    - ref: "/specs/libraries/policy/policy_assertions.spec.md"
      as: lib_policy_core_spec
      symbols:
      - policy.assert.no_violations
      - policy.assert.summary_passed
      - policy.assert.summary_check_id
      - policy.assert.scan_pass
  clauses:
    imports:
    - from: artifact
      names:
      - violation_count
    predicates:
    - id: assert_1
      assert:
        call:
        - var: policy.assert.no_violations
        - std.object.assoc:
          - violation_count
          - var: violation_count
          - lit: {}
    - id: assert_2
      assert:
      - call:
        - var: policy.assert.summary_passed
        - std.object.assoc:
          - summary_json
          - var: summary_json
          - lit: {}
      - call:
        - var: policy.assert.summary_check_id
        - std.object.assoc:
          - summary_json
          - var: summary_json
          - lit: {}
        - spec.spec_lang_adoption_non_regression
      imports:
      - from: artifact
        names:
        - summary_json
```
