```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-RUNTIME-CERT-004
    title: required rust runner certification lane passes
    purpose: Ensures rust required lane certification passes and remains blocking.
    harness:
      root: .
      check:
        profile: governance.scan
        config:
          check: runtime.runner_certification_required_lane_passes
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
