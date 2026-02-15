# Spec-Lang Conformance Assertion Helpers

## LIB-CONF-ASSERT-001

```yaml spec-test
id: LIB-CONF-ASSERT-001
title: reusable conformance assertion helper functions
type: spec_lang.library
functions:
  conf.pass_when_text_contains:
    fn:
    - [subject, token]
    - {contains: [{var: subject}, {var: token}]}
  conf.pass_when_text_regex:
    fn:
    - [subject, pattern]
    - {regex_match: [{var: subject}, {var: pattern}]}
  conf.eq:
    fn:
    - [subject, value]
    - {eq: [{var: subject}, {var: value}]}
  conf.has_error_category:
    fn:
    - [subject, category]
    - {contains: [{var: subject}, {var: category}]}
  conf.json_type_is:
    fn:
    - [subject, type_name]
    - {json_type: [{var: subject}, {var: type_name}]}
exports:
- conf.pass_when_text_contains
- conf.pass_when_text_regex
- conf.eq
- conf.has_error_category
- conf.json_type_is
```
