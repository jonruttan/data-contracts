```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-RUNTIME-DOCS-001
    title: docs use control-plane language
    purpose: Ensures active docs describe this repository as implementation-agnostic control-plane.
    harness:
      root: .
      docs_language:
        files:
        - /README.md
        - /docs/development.md
        - /docs/book/index.md
        - /docs/book/60_runner_and_gates.md
        required_tokens:
        - implementation-agnostic control plane
        - runtime execution ownership lives in runner repositories
      check:
        profile: governance.scan
        config:
          check: runtime.docs_no_required_lane_language
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
