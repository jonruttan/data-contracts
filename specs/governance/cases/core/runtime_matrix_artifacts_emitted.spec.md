```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-RUNTIME-CI-003
    title: matrix artifacts are emitted in ci
    purpose: Ensures CI publishes canonical status matrix artifacts.
    harness:
      root: .
      ci_matrix_artifacts:
        path: /.github/workflows/ci.yml
        required_tokens:
        - .artifacts/runner-status-matrix.json
        - .artifacts/runner-status-matrix.md
        - .artifacts/runner-status-ingest-log.json
      check:
        profile: governance.scan
        config:
          check: runtime.matrix_artifacts_emitted
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
