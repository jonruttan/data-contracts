```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-RUNTIME-SHELL-003
    title: infra script boundary enforced
    purpose: Ensures ingest script remains transport/integration oriented and does not import governance policy docs.
    harness:
      root: .
      ingest_script:
        path: /scripts/runner_status_ingest.sh
        required_tokens:
          - require_tool curl
          - require_tool jq
          - require_tool shasum
        forbidden_tokens:
          - specs/contract/policy_v1.yaml
          - check_sets_v1.yaml
      check:
        profile: governance.scan
        config:
          check: runtime.infra_script_boundary_enforced
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
