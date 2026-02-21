```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-DOCS-REF-016
  title: discovery review prompt is present
  purpose: Ensures the discovery-fit self-heal review prompt exists in the canonical active review prompt set.
  harness:
    root: "."
    check:
      profile: governance.scan
      config:
        check: docs.reviews_discovery_prompt_present
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
      - call:
        - var: policy.assert.summary_check_id
        - std.object.assoc:
          - summary_json
          - var: summary_json
          - lit: {}
        - docs.reviews_discovery_prompt_present
      - call:
        - var: policy.assert.summary_passed
        - std.object.assoc:
          - summary_json
          - var: summary_json
          - lit: {}
```
