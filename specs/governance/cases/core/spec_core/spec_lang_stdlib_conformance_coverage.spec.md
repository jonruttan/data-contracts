```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-STDLIB-004
    title: stdlib conformance coverage files are present
    purpose: Ensures canonical stdlib conformance fixtures are present and discoverable.
    harness:
      root: .
      stdlib_conformance:
        required_paths:
        - /specs/conformance/cases/core/spec_lang_stdlib.spec.md
        - /specs/conformance/cases/core/spec_lang_schema.spec.md
      check:
        profile: governance.scan
        config:
          check: spec_lang.stdlib_conformance_coverage
      use:
      - ref: /specs/libraries/policy/policy_assertions.spec.md
        as: lib_policy_core_spec
        symbols:
        - policy.assert.no_violations
        - policy.assert.summary_passed
        - policy.assert.summary_check_id
        - policy.assert.scan_pass
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
