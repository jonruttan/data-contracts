```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-RUNTIME-STATUS-003
    title: compatibility status ingestion is configured
    purpose: Ensures status exchange ingestion is wired to release assets and matrix artifacts.
    harness:
      root: .
      status_ingestion:
        files:
        - /scripts/runner_status_ingest.sh
        - /specs/schema/runner_certification_registry_v1.yaml
        required_tokens:
        - release_api_url
        - report_asset_name
        - runner-status-matrix.json
        - runner-status-ingest-log.json
      check:
        profile: governance.scan
        config:
          check: runtime.compatibility_status_ingestion_configured
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

