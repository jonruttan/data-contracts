# Governance Cases

## DCGOV-RUNTIME-STATUS-004

```yaml contract-spec
id: DCGOV-RUNTIME-STATUS-004
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: compatibility status freshness is bounded by SLO
purpose: Ensures compatibility status telemetry enforces the 72-hour freshness budget.
type: contract.check
harness:
  root: .
  freshness_policy:
    files:
    - /scripts/runner_status_ingest.sh
    - /scripts/ci_gate.sh
    required_tokens:
    - --max-age-hours
    - "72"
    - --enforce-freshness
    - compatibility_stale_or_missing_count
  check:
    profile: governance.scan
    config:
      check: runtime.compatibility_status_freshness_within_slo
contract:
  defaults: {}
  imports:
  - from: artifact
    names:
    - violation_count
  steps:
  - id: assert_1
    assert:
      call:
      - {var: policy.assert.no_violations}
      - std.object.assoc:
        - violation_count
        - {var: violation_count}
        - lit: {}
```

