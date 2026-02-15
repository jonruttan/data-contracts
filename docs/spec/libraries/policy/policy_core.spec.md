# Spec-Lang Policy Core Library

## LIB-POLICY-001

```yaml spec-test
id: LIB-POLICY-001
title: policy-core reusable governance predicates
type: spec_lang.library
imports:
- /docs/spec/libraries/path/path_core.spec.md
functions:
  policy.pass_when_no_violations:
    fn:
    - [subject]
    - is_empty:
      - {get: [{var: subject}, violations]}
  policy.fail_when_has_violations:
    fn:
    - [subject]
    - not:
      - {call: [{var: policy.pass_when_no_violations}, {var: subject}]}
  policy.check_id_is:
    fn:
    - [subject, expected]
    - eq:
      - {get: [{var: subject}, check_id]}
      - {var: expected}
  policy.violation_count_is:
    fn:
    - [subject, expected]
    - eq:
      - {get: [{var: subject}, violation_count]}
      - {var: expected}
exports:
- policy.pass_when_no_violations
- policy.fail_when_has_violations
- policy.check_id_is
- policy.violation_count_is
```
