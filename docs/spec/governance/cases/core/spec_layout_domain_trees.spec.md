# Governance Cases

## SRGOV-SPECLAYOUT-DOMAIN-001

```yaml spec-test
id: SRGOV-SPECLAYOUT-DOMAIN-001
title: spec layout uses domain tree directories
purpose: Ensures conformance, governance, and library specs are organized under domain subdirectories
  with index files.
type: governance.check
check: spec.layout_domain_trees
harness:
  root: .
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
assert:
- id: assert_1
  class: must
  checks:
  - std.logic.eq:
    - std.object.get:
      - var: subject
      - check_id
    - spec.layout_domain_trees
  target: summary_json
```
