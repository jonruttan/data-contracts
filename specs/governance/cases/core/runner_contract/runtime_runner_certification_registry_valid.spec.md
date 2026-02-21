```yaml contract-spec
spec_version: 2
schema_ref: /specs/schema/schema_v2.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-RUNTIME-CERT-001
    title: runner certification registry shape is valid
    purpose: Ensures runner certification registry entries are complete and deterministic.
    harness:
      root: .
      runner_certification:
        path: /specs/schema/runner_certification_registry_v2.yaml
        required_runner_ids:
        - rust
        - python
        - php
        - node
        - c
      check:
        profile: governance.scan
        config:
          check: runtime.runner_certification_registry_valid
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
