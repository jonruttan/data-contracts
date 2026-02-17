# Spec-Lang Impl Assertion Helpers

## LIB-IMPL-ASSERT-001

```yaml spec-test
id: LIB-IMPL-ASSERT-001-001-IMPL-ASSERT-CONTAINS
title: 'reusable impl assertion helper functions: impl.assert.contains'
type: spec_lang.export
defines:
  public:
    impl.assert.contains:
      fn:
      - [subject, token]
      - std.string.contains:
        - {var: subject}
        - {var: token}
  private: {}
```

```yaml spec-test
id: LIB-IMPL-ASSERT-001-002-IMPL-ASSERT-REGEX
title: 'reusable impl assertion helper functions: impl.assert.regex'
type: spec_lang.export
defines:
  public:
    impl.assert.regex:
      fn:
      - [subject, pattern]
      - std.string.regex_match:
        - {var: subject}
        - {var: pattern}
  private: {}
```

```yaml spec-test
id: LIB-IMPL-ASSERT-001-003-IMPL-ASSERT-JSON-TYPE
title: 'reusable impl assertion helper functions: impl.assert.json_type'
type: spec_lang.export
defines:
  public:
    impl.assert.json_type:
      fn:
      - [subject, type_name]
      - std.type.json_type:
        - {var: subject}
        - {var: type_name}
  private: {}
```
