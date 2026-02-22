```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
contracts:
  clauses:
  - id: DCGOV-STUB-RUNTIME_PYTHON_DEPENDENCY_METRIC
    title: stub case for runtime_python_dependency_metric
    purpose: Maintains traceability reference integrity for runtime_python_dependency_metric.
    harness:
      root: "."
      check:
        profile: governance.scan
        config:
          check: governance.structured_assertions_required
    asserts:
      imports:
      - from: artifact
        names:
        - violation_count
      checks:
      - id: assert_1
        assert:
          call:
          - var: policy.assert.no_violations
          - std.object.assoc:
            - violation_count
            - var: violation_count
            - lit: {}
```
