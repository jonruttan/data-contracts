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
    - "{'root': '.', 'check': {'profile': 'governance.scan', 'config': {'check': 'docs.spec_index_reachability'}}}"
services:
  actions:
  - id: svc.root_check_profile_governance_scan_config_check_docs_spec_index_reachability.default.1
    type: legacy.root_check_profile_governance_scan_config_check_docs_spec_index_reachability
    io: io
    profile: default
contracts:
- id: DCGOV-DOCS-CANON-001
  title: specs index links all canonical spec entrypoints
  purpose: Ensures /specs/index.md links every canonical spec subtree and current
    snapshot.
  clauses:
    imports:
    - artifact:
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
