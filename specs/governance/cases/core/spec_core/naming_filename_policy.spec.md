```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-DOCS-NAME-001
    title: docs filenames follow lowercase separator policy
    purpose: Enforces deterministic docs filename shape using underscores for words and hyphens
      for section separators.
    harness:
      root: .
      filename_policy:
        paths:
        - docs
        include_extensions:
        - .md
        - .yaml
        - .yml
        - .json
        allow_exact:
        - README.md
        allowed_name_regex: ^[a-z0-9]+(?:_[a-z0-9]+)*(?:-[a-z0-9]+(?:_[a-z0-9]+)*)*(?:\.spec)?\.(?:md|yaml|yml|json)$
      check:
        profile: governance.scan
        config:
          check: naming.filename_policy
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
      - id: assert_2
        assert:
        - call:
          - {var: policy.assert.summary_passed}
          - std.object.assoc:
            - summary_json
            - {var: summary_json}
            - lit: {}
        - call:
          - {var: policy.assert.summary_check_id}
          - std.object.assoc:
            - summary_json
            - {var: summary_json}
            - lit: {}
          - naming.filename_policy
        imports:
        - from: artifact
          names:
          - summary_json
```
