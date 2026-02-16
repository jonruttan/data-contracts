# Spec-Lang HTTP Domain Library

## LIB-DOMAIN-HTTP-001

```yaml spec-test
id: LIB-DOMAIN-HTTP-001
title: http projection helper functions
type: spec_lang.library
definitions:
  public:
    domain.http.status:
      fn:
      - [subject]
      - std.object.get:
        - std.object.get:
          - {var: subject}
          - value
        - status
    domain.http.status_in:
      fn:
      - [subject, allowed]
      - std.collection.in:
        - std.object.get:
          - std.object.get:
            - {var: subject}
            - value
          - status
        - {var: allowed}
    domain.http.status_is:
      fn:
      - [subject, expected]
      - std.logic.eq:
        - std.object.get:
          - std.object.get:
            - {var: subject}
            - value
          - status
        - {var: expected}
    domain.http.status_is_unauthorized:
      fn:
      - [subject]
      - call:
        - {var: domain.http.status_is}
        - {var: subject}
        - 401
    domain.http.status_is_forbidden:
      fn:
      - [subject]
      - call:
        - {var: domain.http.status_is}
        - {var: subject}
        - 403
    domain.http.ok_2xx:
      fn:
      - [subject]
      - std.logic.and:
        - std.logic.gte:
          - std.object.get:
            - std.object.get:
              - {var: subject}
              - value
            - status
          - 200
        - std.logic.lt:
          - std.object.get:
            - std.object.get:
              - {var: subject}
              - value
            - status
          - 300
    domain.http.header_get:
      fn:
      - [subject, key]
      - std.object.get:
        - std.object.get:
          - std.object.get:
            - {var: subject}
            - value
          - headers
        - {var: key}
    domain.http.header_contains:
      fn:
      - [subject, key, token]
      - std.string.contains:
        - std.object.get:
          - std.object.get:
            - std.object.get:
              - {var: subject}
              - value
            - headers
          - {var: key}
        - {var: token}
    domain.http.body_text:
      fn:
      - [subject]
      - std.object.get:
        - std.object.get:
          - {var: subject}
          - value
        - body_text
    domain.http.body_json:
      fn:
      - [subject]
      - std.object.get:
        - std.object.get:
          - {var: subject}
          - value
        - body_json
    domain.http.body_json_type_is:
      fn:
      - [subject, expected_type]
      - std.type.json_type:
        - std.object.get:
          - std.object.get:
            - {var: subject}
            - value
          - body_json
        - {var: expected_type}
    domain.http.body_json_has_key:
      fn:
      - [subject, key]
      - std.object.has_key:
        - std.object.get:
          - std.object.get:
            - {var: subject}
            - value
          - body_json
        - {var: key}
    domain.http.auth_is_oauth:
      fn:
      - [subject]
      - std.logic.eq:
        - std.object.get:
          - std.object.get:
            - {var: subject}
            - meta
          - auth_mode
        - oauth
    domain.http.has_bearer_header:
      fn:
      - [subject]
      - std.string.starts_with:
        - std.object.get:
          - std.object.get:
            - std.object.get:
              - {var: subject}
              - value
            - headers
          - Authorization
        - 'Bearer '
    domain.http.oauth_scope_requested:
      fn:
      - [subject]
      - std.logic.neq:
        - std.object.get:
          - std.object.get:
            - std.object.get:
              - {var: subject}
              - context
            - oauth
          - scope_requested
        - null
```
