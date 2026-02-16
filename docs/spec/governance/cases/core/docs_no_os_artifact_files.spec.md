# Governance Cases

## SRGOV-DOCS-LAYOUT-005

```yaml spec-test
id: SRGOV-DOCS-LAYOUT-005
title: docs tree excludes OS/editor artifact files
purpose: Prevents tracked filesystem artifacts (for example .DS_Store) in docs surfaces.
type: governance.check
check: docs.no_os_artifact_files
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
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - check_id
      - docs.no_os_artifact_files
    - std.logic.eq:
      - std.object.get:
        - {var: subject}
        - passed
      - true
```
