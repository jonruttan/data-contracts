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
  policy_evaluate:
  - call:
    - {var: policy.pass_when_no_violations}
    - {var: subject}
  chain:
    steps:
    - id: lib_policy_core_spec
      class: must
      ref: /docs/spec/libraries/policy/policy_core.spec.md
      exports:
        policy.pass_when_no_violations:
          from: library.symbol
          path: /policy.pass_when_no_violations
          required: true
    imports:
    - from_step: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
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
