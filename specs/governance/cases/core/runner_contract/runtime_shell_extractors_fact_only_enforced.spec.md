```yaml contract-spec
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
defaults:
  type: contract.check
contracts:
  - id: DCGOV-PIPE-SHELL-001
    title: shell extractors are fact emitters only
    purpose: Ensures extractor scripts do not emit direct policy failure exits for governance domains.
    harness:
      root: .
      extractor_script:
        path: /scripts/governance_catalog_validate.sh
        must_not_contain:
          - exit 1
          - blocking_fail
      check:
        profile: governance.scan
        config:
          check: runtime.shell_extractors_fact_only_enforced
    clauses:
      defaults: {}
      imports:
        - from: artifact
          names: [violation_count]
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
