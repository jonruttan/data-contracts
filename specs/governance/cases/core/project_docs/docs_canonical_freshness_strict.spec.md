```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-DOCS-CANON-003
  title: docs freshness strict checker passes
  purpose: Ensures specs freshness checks are strict, deterministic, and currently clean.
  harness:
    root: "."
    check:
      profile: governance.scan
      config:
        check: docs.canonical_freshness_strict
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
