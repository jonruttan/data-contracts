# Governance Cases

## SRGOV-DOCS-LAYOUT-005

```yaml contract-spec
id: SRGOV-DOCS-LAYOUT-005
title: docs tree excludes OS/editor artifact files
purpose: Prevents tracked filesystem artifacts (for example .DS_Store) in docs surfaces.
type: contract.check
harness:
  root: .
  chain:
    steps:
    - id: lib_policy_core_spec
      class: MUST
      ref: /docs/spec/libraries/policy/policy_core.spec.md
    imports:
    - from: lib_policy_core_spec
      names:
      - policy.pass_when_no_violations
  check:
    profile: governance.scan
    config:
      check: docs.no_os_artifact_files
contract:
- id: assert_1
  class: MUST
  asserts:
  - evaluate:
      lit:
        lit:
          MUST:
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
  target: summary_json
```
