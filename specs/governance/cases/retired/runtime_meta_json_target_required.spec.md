```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-RUNTIME-META-TARGET-001
    title: executable harnesses expose meta_json assertion target
    purpose: Ensures all core executable harness adapters project meta_json.
    harness:
      root: .
      meta_json_targets:
        files:
        - /dc-runner-python
        - /dc-runner-python
        - /dc-runner-python
        - /dc-runner-python
        - /dc-runner-python
        required_tokens:
        - meta_json
      check:
        profile: governance.scan
        config:
          check: runtime.meta_json_target_required
    clauses:
      defaults: {}
      imports:
      - from: artifact
        names:
        - violation_count
      predicates:
      - id: assert_1
        assert:
          std.logic.eq:
          - {var: violation_count}
          - 0
```
