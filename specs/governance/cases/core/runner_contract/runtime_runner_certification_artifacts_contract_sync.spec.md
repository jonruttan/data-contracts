```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-RUNTIME-CERT-003
    title: runner certification artifacts follow contract shape
    purpose: Ensures runner-certify generates contract-shaped JSON and markdown artifacts.
    harness:
      root: .
      check:
        profile: governance.scan
        config:
          check: runtime.runner_certification_artifacts_contract_sync
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
