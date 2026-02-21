```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-RUNTIME-TRIAGE-012
  title: triage artifact includes selection metadata
  purpose: Ensures governance triage artifacts include selection_source and selected_prefixes metadata.
  harness:
    root: "."
    triage_artifact_selection_metadata:
      path: "/scripts/governance_triage.sh"
      required_tokens:
      - selection_source
      - selected_prefixes
      - broad_required
      - governance-triage-summary.md
    check:
      profile: governance.scan
      config:
        check: runtime.governance_triage_artifact_contains_selection_metadata
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
```
