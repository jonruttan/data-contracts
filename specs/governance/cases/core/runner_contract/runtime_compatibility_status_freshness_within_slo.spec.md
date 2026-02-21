```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-RUNTIME-STATUS-004
  title: compatibility status freshness is bounded by SLO
  purpose: Ensures compatibility status telemetry enforces the 72-hour freshness budget.
  harness:
    root: "."
    freshness_policy:
      files:
      - "/scripts/runner_status_ingest.sh"
      - "/scripts/ci_gate.sh"
      required_tokens:
      - "--max-age-hours"
      - '72'
      - "--enforce-freshness"
      - compatibility_stale_or_missing_count
    check:
      profile: governance.scan
      config:
        check: runtime.compatibility_status_freshness_within_slo
  clauses:
    imports:
    - from: artifact
      names:
      - violation_count
    predicates:
    - id: assert_1
      assert:
        call:
        - var: policy.assert.no_violations
        - std.object.assoc:
          - violation_count
          - var: violation_count
          - lit: {}
```

