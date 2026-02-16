# Spec-Lang HTTP Domain Library

## LIB-DOMAIN-HTTP-001

```yaml spec-test
id: LIB-DOMAIN-HTTP-001
title: http projection helper functions
type: spec_lang.library
defines:
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
    domain.http.cors_allow_origin:
      fn:
      - [subject]
      - std.object.get:
        - std.object.get:
          - std.object.get:
            - {var: subject}
            - value
          - cors
        - allow_origin
    domain.http.cors_allows_method:
      fn:
      - [subject, method_name]
      - std.collection.includes:
        - std.object.get:
          - std.object.get:
            - std.object.get:
              - {var: subject}
              - value
            - cors
          - allow_methods
        - {var: method_name}
    domain.http.cors_allows_header:
      fn:
      - [subject, header_name]
      - std.collection.includes:
        - std.object.get:
          - std.object.get:
            - std.object.get:
              - {var: subject}
              - value
            - cors
          - allow_headers
        - {var: header_name}
    domain.http.cors_credentials_enabled:
      fn:
      - [subject]
      - std.logic.eq:
        - std.object.get:
          - std.object.get:
            - std.object.get:
              - {var: subject}
              - value
            - cors
          - allow_credentials
        - true
    domain.http.cors_max_age_gte:
      fn:
      - [subject, min_age]
      - std.logic.gte:
        - std.object.get:
          - std.object.get:
            - std.object.get:
              - {var: subject}
              - value
            - cors
          - max_age
        - {var: min_age}
    domain.http.is_preflight_step:
      fn:
      - [step]
      - std.logic.eq:
        - std.object.get:
          - {var: step}
          - method
        - OPTIONS
    domain.http.step_by_id:
      fn:
      - [steps, step_id]
      - std.collection.find:
        - fn:
          - [row]
          - std.logic.eq:
            - std.object.get:
              - {var: row}
              - id
            - {var: step_id}
        - {var: steps}
    domain.http.step_status_is:
      fn:
      - [steps, step_id, expected]
      - std.logic.eq:
        - std.object.get:
          - call:
            - {var: domain.http.step_by_id}
            - {var: steps}
            - {var: step_id}
          - status
        - {var: expected}
    domain.http.step_body_json_get:
      fn:
      - [steps, step_id, field]
      - std.object.get:
        - std.object.get:
          - call:
            - {var: domain.http.step_by_id}
            - {var: steps}
            - {var: step_id}
          - body_json
        - {var: field}
```
