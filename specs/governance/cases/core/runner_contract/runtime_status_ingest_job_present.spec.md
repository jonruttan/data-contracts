```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-RUNTIME-CI-002
    title: status ingest job present in ci
    purpose: Ensures CI includes a status-ingest control-plane job.
    harness:
      root: .
      ci_ingest_job:
        path: /.github/workflows/ci.yml
        required_tokens:
        - runner-status-ingest:
        - ./scripts/runner_status_ingest.sh --max-age-hours 72 --enforce-freshness
      check:
        profile: governance.scan
        config:
          check: runtime.status_ingest_job_present
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
