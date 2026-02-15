# Spec-Lang HTTP Domain Library

## LIB-DOMAIN-HTTP-001

```yaml spec-test
id: LIB-DOMAIN-HTTP-001
title: http projection helper functions
type: spec_lang.library
definitions:
  public:
    http.status_in:
      fn:
      - [subject, allowed]
      - in:
        - get:
          - {get: [{var: subject}, value]}
          - status
        - {var: allowed}
```
