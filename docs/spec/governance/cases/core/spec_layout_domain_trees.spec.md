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
  spec_lang:
    includes:
    - /docs/spec/libraries/policy/policy_core.spec.md
    exports:
    - policy.pass_when_no_violations
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
assert:
- target: summary_json
  must:
  - evaluate:
    - eq:
      - get:
        - {var: subject}
        - check_id
      - spec.layout_domain_trees
```
