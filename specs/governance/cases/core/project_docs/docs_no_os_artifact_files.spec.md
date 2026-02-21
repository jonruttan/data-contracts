# Governance Cases

## DCGOV-DOCS-LAYOUT-005

```yaml contract-spec
id: DCGOV-DOCS-LAYOUT-005
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: docs tree excludes OS/editor artifact files
purpose: Prevents tracked filesystem artifacts (for example .DS_Store) in docs surfaces.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.no_os_artifact_files
  use:
  - ref: /specs/libraries/policy/policy_assertions.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.assert.no_violations
    - policy.assert.summary_passed
    - policy.assert.summary_check_id
    - policy.assert.scan_pass
contract:
  defaults: {}
  imports:
  - from: artifact
    names:
    - summary_json
  steps:
  - id: assert_1
    assert:
    - call:
      - {var: policy.assert.summary_check_id}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
      - docs.no_os_artifact_files
    - call:
      - {var: policy.assert.summary_passed}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
```
