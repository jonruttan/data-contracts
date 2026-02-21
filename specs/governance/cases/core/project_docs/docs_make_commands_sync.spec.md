```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-DOCS-REF-007
  title: docs use canonical make command entrypoints
  purpose: Keeps contributor docs aligned on the canonical make-based command entrypoints for verification and gate execution.
  harness:
    root: "."
    make_commands:
      files:
      - README.md
      - docs/development.md
      - ".github/pull_request_template.md"
      required_tokens:
      - make verify-docs
      - make core-check
      - make check
      - make prepush
      - make prepush-fast
      - make ci-cleanroom
      forbidden_tokens:
      - make prepush-parity
    check:
      profile: governance.scan
      config:
        check: docs.make_commands_sync
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
    - id: assert_2
      assert:
      - call:
        - var: policy.assert.summary_passed
        - std.object.assoc:
          - summary_json
          - var: summary_json
          - lit: {}
      - call:
        - var: policy.assert.summary_check_id
        - std.object.assoc:
          - summary_json
          - var: summary_json
          - lit: {}
        - docs.make_commands_sync
      imports:
      - from: artifact
        names:
        - summary_json
```
