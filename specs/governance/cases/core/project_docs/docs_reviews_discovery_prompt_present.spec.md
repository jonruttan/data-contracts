# Governance Cases

## DCGOV-DOCS-REF-016

```yaml contract-spec
id: DCGOV-DOCS-REF-016
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: discovery review prompt is present
purpose: Ensures the discovery-fit self-heal review prompt exists in the canonical active review prompt set.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: docs.reviews_discovery_prompt_present
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
      - docs.reviews_discovery_prompt_present
    - call:
      - {var: policy.assert.summary_passed}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
```
