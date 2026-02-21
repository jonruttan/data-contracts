```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-DOCS-REF-008
    title: compatibility examples are explicitly labeled
    purpose: Ensures active documentation keeps Rust as canonical and labels Python/PHP examples
      as non-blocking compatibility lanes.
    harness:
      root: .
      compatibility_docs:
        files:
        - /README.md
        - /docs/development.md
        - /specs/contract/12_runner_interface.md
        
        required_tokens:
        - implementation-agnostic
        - compatibility lanes
        - non-blocking
        forbidden_tokens:
        - ./scripts/ci_gate.sh
      check:
        profile: governance.scan
        config:
          check: docs.compatibility_examples_labeled
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
