```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-DOCS-CANON-003
  title: docs freshness strict checker passes
  purpose: Ensures specs freshness checks are strict, deterministic, and 
    currently clean.
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
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'check': {'profile': 'governance.scan', 'config': {'check': 'docs.canonical_freshness_strict'}}}"
services:
  entries:
  - id: 
      svc.root_check_profile_governance_scan_config_check_docs_canonical_freshness_strict.default.1
    type: 
      legacy.root_check_profile_governance_scan_config_check_docs_canonical_freshness_strict
    io: io
    profile: default
    config: {}
```
