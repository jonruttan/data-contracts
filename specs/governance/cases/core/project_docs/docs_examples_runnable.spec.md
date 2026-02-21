```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-DOCS-REF-004
    title: reference examples parse or are explicitly opted out
    purpose: Ensures reference examples are trustworthy by requiring parseable or statically valid
      fenced examples unless explicitly opted out.
    harness:
      root: .
      docs_examples:
        files:
        - docs/book/10_getting_started.md
        - docs/book/20_case_model.md
        - docs/book/30_assertion_model.md
        - docs/book/40_spec_lang_authoring.md
        - docs/book/60_runner_and_gates.md
        - docs/book/80_troubleshooting.md
        - docs/book/90_reference_guide.md
        - docs/development.md
      check:
        profile: governance.scan
        config:
          check: docs.examples_runnable
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
          - docs.examples_runnable
        imports:
        - from: artifact
          names:
          - summary_json
```
