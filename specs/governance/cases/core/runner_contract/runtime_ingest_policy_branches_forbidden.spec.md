```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-PIPE-INGEST-002
    title: ingest policy branch exits are forbidden
    purpose: Ensures ingest script does not hard-fail on freshness policy branches.
    harness:
      root: .
      ingest_script:
        path: /scripts/runner_status_ingest.sh
        must_not_contain:
          - ERROR: compatibility status freshness policy violation
          - exit 1
      check:
        profile: governance.scan
        config:
          check: runtime.ingest_policy_branches_forbidden
    clauses:
      defaults: {}
      imports:
        - from: artifact
          names: [violation_count]
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
