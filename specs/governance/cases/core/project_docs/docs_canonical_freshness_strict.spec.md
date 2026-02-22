```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'check': {'profile': 'governance.scan', 'config': {'check': 'docs.canonical_freshness_strict'}}}"
services:
- type: legacy.root_check_profile_governance_scan_config_check_docs_canonical_freshness_strict
  operations:
  - id: svc.root_check_profile_governance_scan_config_check_docs_canonical_freshness_strict.default.1
    mode: default
    direction: bidirectional
contracts:
  defaults:
    type: contract.check
  clauses:
  - id: DCGOV-DOCS-CANON-003
    title: docs freshness strict checker passes
    purpose: Ensures specs freshness checks are strict, deterministic, and currently
      clean.
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
