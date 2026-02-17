# Spec-Lang Conformance Assertion Helpers

## LIB-CONF-ASSERT-001

```yaml spec-test
id: LIB-CONF-ASSERT-001
title: reusable conformance assertion helper functions
type: spec_lang.library
defines:
  public:
    conf.pass_when_text_contains:
      fn:
      - [subject, token]
      - std.string.contains:
        - {var: subject}
        - {var: token}
  private:
    conf.pass_when_text_regex:
      fn:
      - [subject, pattern]
      - std.string.regex_match:
        - {var: subject}
        - {var: pattern}
    conf.eq:
      fn:
      - [subject, value]
      - std.logic.eq:
        - {var: subject}
        - {var: value}
    conf.has_error_category:
      fn:
      - [subject, category]
      - std.string.contains:
        - {var: subject}
        - {var: category}
    conf.json_type_is:
      fn:
      - [subject, type_name]
      - std.type.json_type:
        - {var: subject}
        - {var: type_name}
harness:
  chain:
    exports:
    - as: conf.pass_when_text_contains
      from: assert.function
      path: /conf.pass_when_text_contains
      required: true
```
