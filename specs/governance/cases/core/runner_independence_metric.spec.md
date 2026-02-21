```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-STUB-RUNNER_INDEPENDENCE_METRIC
    title: stub case for runner_independence_metric
    purpose: Maintains traceability reference integrity for runner_independence_metric.
    harness:
      root: .
      check:
        profile: governance.scan
        config:
          check: governance.structured_assertions_required
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
