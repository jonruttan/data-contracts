# Spec-Lang Conformance Assertion Helpers

## LIB-CONF-ASSERT-001

```yaml spec-test
id: LIB-CONF-ASSERT-001
title: reusable conformance assertion helper functions
type: spec_lang.library
functions:
  conf.pass_when_text_contains:
    fn:
    - {lit: [subject, token]}
    - contains:
      - {var: subject}
      - {var: token}
  conf.pass_when_text_regex:
    fn:
    - {lit: [subject, pattern]}
    - regex_match:
      - {var: subject}
      - {var: pattern}
  conf.eq:
    fn:
    - {lit: [subject, value]}
    - eq:
      - {var: subject}
      - {var: value}
  conf.has_error_category:
    fn:
    - {lit: [subject, category]}
    - contains:
      - {var: subject}
      - {var: category}
  conf.json_type_is:
    fn:
    - {lit: [subject, type_name]}
    - json_type:
      - {var: subject}
      - {var: type_name}
exports:
- conf.pass_when_text_contains
- conf.pass_when_text_regex
- conf.eq
- conf.has_error_category
- conf.json_type_is
```
