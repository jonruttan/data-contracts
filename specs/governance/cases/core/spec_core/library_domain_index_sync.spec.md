```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-LIB-INDEX-001
  title: library domain indexes are synchronized
  purpose: Ensures each library domain index lists all library files and exported symbols without stale entries.
  harness:
    root: "."
    check:
      profile: governance.scan
      config:
        check: library.domain_index_sync
    use:
    - ref: "/specs/libraries/policy/policy_assertions.spec.md"
      as: lib_policy_core_spec
      symbols:
      - policy.assert.no_violations
      - policy.assert.summary_passed
      - policy.assert.summary_check_id
      - policy.assert.scan_pass
  clauses:
    imports:
    - from: artifact
      names:
      - summary_json
    predicates:
    - id: assert_1
      assert:
        call:
        - var: policy.assert.summary_check_id
        - std.object.assoc:
          - summary_json
          - var: summary_json
          - lit: {}
        - library.domain_index_sync
```
