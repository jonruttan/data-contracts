```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-RUNTIME-TRIAGE-011
    title: governance triage selects prefixes from changed paths
    purpose: Ensures triage auto mode derives targeted check prefixes from changed paths before
      fallback prefixes.
    harness:
      root: .
      triage_prefix_selection:
        path: /scripts/governance_triage.sh
        required_tokens:
        - collect_changed_paths
        - select_prefixes_from_changed_paths
        - selection_source="changed_paths"
        - CHECK_PREFIXES
      check:
        profile: governance.scan
        config:
          check: runtime.governance_prefix_selection_from_changed_paths
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
```
