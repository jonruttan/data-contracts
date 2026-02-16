# Spec-Lang PHP Domain Library

## LIB-DOMAIN-PHP-001

```yaml spec-test
id: LIB-DOMAIN-PHP-001
title: php projection helper functions
type: spec_lang.library
definitions:
  public:
    php.is_assoc_projection:
      fn:
      - [subject]
      - std.logic.eq:
        - std.object.get:
          - std.object.get:
            - {var: subject}
            - meta
          - php_array_kind
        - assoc
```
