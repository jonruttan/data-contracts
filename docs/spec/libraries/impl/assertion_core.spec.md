# Spec-Lang Impl Assertion Helpers

## LIB-IMPL-ASSERT-001

```yaml spec-test
id: LIB-IMPL-ASSERT-001
title: reusable impl assertion helper functions
type: spec_lang.library
definitions:
  public:
    impl.assert.contains:
      fn:
      - [subject, token]
      - contains:
        - {var: subject}
        - {var: token}
    impl.assert.regex:
      fn:
      - [subject, pattern]
      - regex_match:
        - {var: subject}
        - {var: pattern}
    impl.assert.json_type:
      fn:
      - [subject, type_name]
      - json_type:
        - {var: subject}
        - {var: type_name}
```
