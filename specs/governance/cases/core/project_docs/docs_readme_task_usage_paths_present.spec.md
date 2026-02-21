```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  type: contract.check
contracts:
- id: DCGOV-DOCS-REF-025
  title: readme includes task-based usage paths
  purpose: Ensures README is user-oriented and includes concrete task navigation.
  harness:
    root: "."
    readme_usage_paths:
      path: "/README.md"
      required_tokens:
      - How Users Use This Project
      - Author a spec change
      - Validate docs and contract coherence
      - Read compatibility and status telemetry
      - Debug governance or documentation drift
    check:
      profile: governance.scan
      config:
        check: docs.readme_task_usage_paths_present
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
```
