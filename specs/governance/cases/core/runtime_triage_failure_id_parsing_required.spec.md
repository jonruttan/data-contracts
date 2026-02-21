```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-RUNTIME-TRIAGE-005
    title: triage parser derives failing check ids and prefixes
    purpose: Ensures triage script parses governance ERROR lines and maps check ids to check-prefix
      retries.
    harness:
      root: .
      triage_failure_parser:
        path: /scripts/governance_triage.sh
        required_tokens:
        - '^ERROR: ([A-Z0-9-]+):'
        - parse_error_ids_from_output
        - build_prefixes_from_ids
        - specs/governance/check_prefix_map_v1.yaml
      check:
        profile: governance.scan
        config:
          check: runtime.triage_failure_id_parsing_required
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
