# Governance Cases

## DCGOV-DOCS-REF-009

```yaml contract-spec
id: DCGOV-DOCS-REF-009
spec_version: 1
schema_ref: /specs/schema/schema_v1.md
title: core and full adoption profile docs stay synchronized
purpose: Keeps contributor-facing docs aligned on core-check and full-check adoption profile
  wording.
type: contract.check
harness:
  root: .
  adoption_profiles:
    files:
    - README.md
    - docs/development.md
    required_tokens:
    - Core profile
    - Full profile
    - make core-check
    - make check
  check:
    profile: governance.scan
    config:
      check: docs.adoption_profiles_sync
  use:
  - ref: /specs/libraries/policy/policy_assertions.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.assert.no_violations
    - policy.assert.summary_passed
    - policy.assert.summary_check_id
    - policy.assert.scan_pass
contract:
  defaults:
    class: MUST
  imports:
  - from: artifact
    names:
    - violation_count
  steps:
  - id: assert_1
    assert:
      call:
      - {var: policy.assert.no_violations}
      - std.object.assoc:
        - violation_count
        - {var: violation_count}
        - lit: {}
  - id: assert_2
    assert:
    - call:
      - {var: policy.assert.summary_passed}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
    - call:
      - {var: policy.assert.summary_check_id}
      - std.object.assoc:
        - summary_json
        - {var: summary_json}
        - lit: {}
      - docs.adoption_profiles_sync
    imports:
    - from: artifact
      names:
      - summary_json
```
