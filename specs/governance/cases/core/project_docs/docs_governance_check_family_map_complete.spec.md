```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
harness:
  type: unit.test
  profile: check
  config:
    legacy_contract_harnesses:
    - "{'root': '.', 'check': {'profile': 'governance.scan', 'config': {'check': 'docs.governance_check_family_map_complete'}}}"
services:
  actions:
  - id: svc.root_check_profile_governance_scan_config_check_docs_governance_check_family_map_complete.default.1
    type: legacy.root_check_profile_governance_scan_config_check_docs_governance_check_family_map_complete
    io: io
    profile: default
contracts:
- id: DCGOV-DOCS-CANON-002
  title: governance check family map covers all registered checks
  purpose: Ensures each governance check id is mapped to a canonical check family prefix.
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
