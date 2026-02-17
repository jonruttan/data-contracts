# Spec-Lang Policy Core Library

## LIB-POLICY-001

```yaml spec-test
id: LIB-POLICY-001
title: policy-core reusable governance predicates
type: spec_lang.export
imports:
- /docs/spec/libraries/path/path_core.spec.md
defines:
  public:
    policy.pass_when_no_violations:
      fn:
      - [subject]
      - std.collection.is_empty:
        - std.object.get:
          - {var: subject}
          - violations
  private:
    policy.fail_when_has_violations:
      fn:
      - [subject]
      - std.logic.not:
        - call:
          - {var: policy.pass_when_no_violations}
          - {var: subject}
    policy.check_id_is:
      fn:
      - [subject, expected]
      - std.logic.eq:
        - std.object.get:
          - {var: subject}
          - check_id
        - {var: expected}
    policy.violation_count_is:
      fn:
      - [subject, expected]
      - std.logic.eq:
        - std.object.get:
          - {var: subject}
          - violation_count
        - {var: expected}
```
