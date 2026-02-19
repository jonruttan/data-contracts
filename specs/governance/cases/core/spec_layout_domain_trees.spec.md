# Governance Cases

## SRGOV-SPECLAYOUT-DOMAIN-001

```yaml contract-spec
id: SRGOV-SPECLAYOUT-DOMAIN-001
title: spec layout uses domain tree directories
purpose: Ensures conformance, governance, and library specs are organized under domain subdirectories
  with index files.
type: contract.check
harness:
  root: .
  check:
    profile: governance.scan
    config:
      check: spec.layout_domain_trees
  use:
  - ref: /specs/libraries/policy/policy_core.spec.md
    as: lib_policy_core_spec
    symbols:
    - policy.pass_when_no_violations
contract:
  defaults:
    class: MUST
  imports:
    subject:
      from: artifact
      key: summary_json
  steps:
  - id: assert_1
    assert:
      std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - spec.layout_domain_trees
```
