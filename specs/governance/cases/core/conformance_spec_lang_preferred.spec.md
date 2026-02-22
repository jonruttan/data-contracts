```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
contracts:
  defaults:
    type: contract.check
  clauses:
  - id: DCGOV-STUB-CONFORMANCE_SPEC_LANG_PREFERRED
    title: stub case for conformance_spec_lang_preferred
    purpose: Maintains traceability reference integrity for conformance_spec_lang_preferred.
    harness:
      root: .
      check:
        profile: governance.scan
        config:
          check: governance.structured_assertions_required
    asserts:
      imports:
        - from: artifact
          names: [violation_count]
      checks:
        - id: assert_1
          assert:
            call:
            - {var: policy.assert.no_violations}
            - std.object.assoc:
              - violation_count
              - {var: violation_count}
              - lit: {}
```
