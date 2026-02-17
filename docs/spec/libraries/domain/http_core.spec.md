# Spec-Lang HTTP Domain Library

## LIB-DOMAIN-HTTP-001

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-001-DOMAIN-HTTP-STATUS
title: 'http projection helper functions: domain.http.status'
type: spec_lang.export
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
  private: {}
harness:
  chain:
    exports:
    - as: domain.http.cors_allow_origin
      from: assert.function
      path: /domain.http.cors_allow_origin
      required: true
    - as: domain.http.cors_allows_method
      from: assert.function
      path: /domain.http.cors_allows_method
      required: true
    - as: domain.http.cors_allows_header
      from: assert.function
      path: /domain.http.cors_allows_header
      required: true
    - as: domain.http.cors_credentials_enabled
      from: assert.function
      path: /domain.http.cors_credentials_enabled
      required: true
    - as: domain.http.cors_max_age_gte
      from: assert.function
      path: /domain.http.cors_max_age_gte
      required: true
    - as: domain.http.is_preflight_step
      from: assert.function
      path: /domain.http.is_preflight_step
      required: true
    - as: domain.http.step_by_id
      from: assert.function
      path: /domain.http.step_by_id
      required: true
    - as: domain.http.step_status_is
      from: assert.function
      path: /domain.http.step_status_is
      required: true
    - as: domain.http.step_body_json_get
      from: assert.function
      path: /domain.http.step_body_json_get
      required: true
    - as: domain.http.status
      from: assert.function
      path: /domain.http.status
      required: true
    - as: domain.http.status_in
      from: assert.function
      path: /domain.http.status_in
      required: true
    - as: domain.http.status_is
      from: assert.function
      path: /domain.http.status_is
      required: true
    - as: domain.http.status_is_unauthorized
      from: assert.function
      path: /domain.http.status_is_unauthorized
      required: true
    - as: domain.http.status_is_forbidden
      from: assert.function
      path: /domain.http.status_is_forbidden
      required: true
    - as: domain.http.ok_2xx
      from: assert.function
      path: /domain.http.ok_2xx
      required: true
    - as: domain.http.header_get
      from: assert.function
      path: /domain.http.header_get
      required: true
    - as: domain.http.header_contains
      from: assert.function
      path: /domain.http.header_contains
      required: true
    - as: domain.http.body_text
      from: assert.function
      path: /domain.http.body_text
      required: true
    - as: domain.http.body_json
      from: assert.function
      path: /domain.http.body_json
      required: true
    - as: domain.http.body_json_type_is
      from: assert.function
      path: /domain.http.body_json_type_is
      required: true
    - as: domain.http.body_json_has_key
      from: assert.function
      path: /domain.http.body_json_has_key
      required: true
    - as: domain.http.auth_is_oauth
      from: assert.function
      path: /domain.http.auth_is_oauth
      required: true
    - as: domain.http.has_bearer_header
      from: assert.function
      path: /domain.http.has_bearer_header
      required: true
    - as: domain.http.oauth_scope_requested
      from: assert.function
      path: /domain.http.oauth_scope_requested
      required: true
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-002-DOMAIN-HTTP-STATUS-IN
title: 'http projection helper functions: domain.http.status_in'
type: spec_lang.export
defines:
  public:
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
  private: {}
harness:
  chain:
    exports:
    - as: domain.http.cors_allow_origin
      from: assert.function
      path: /domain.http.cors_allow_origin
      required: true
    - as: domain.http.cors_allows_method
      from: assert.function
      path: /domain.http.cors_allows_method
      required: true
    - as: domain.http.cors_allows_header
      from: assert.function
      path: /domain.http.cors_allows_header
      required: true
    - as: domain.http.cors_credentials_enabled
      from: assert.function
      path: /domain.http.cors_credentials_enabled
      required: true
    - as: domain.http.cors_max_age_gte
      from: assert.function
      path: /domain.http.cors_max_age_gte
      required: true
    - as: domain.http.is_preflight_step
      from: assert.function
      path: /domain.http.is_preflight_step
      required: true
    - as: domain.http.step_by_id
      from: assert.function
      path: /domain.http.step_by_id
      required: true
    - as: domain.http.step_status_is
      from: assert.function
      path: /domain.http.step_status_is
      required: true
    - as: domain.http.step_body_json_get
      from: assert.function
      path: /domain.http.step_body_json_get
      required: true
    - as: domain.http.status
      from: assert.function
      path: /domain.http.status
      required: true
    - as: domain.http.status_in
      from: assert.function
      path: /domain.http.status_in
      required: true
    - as: domain.http.status_is
      from: assert.function
      path: /domain.http.status_is
      required: true
    - as: domain.http.status_is_unauthorized
      from: assert.function
      path: /domain.http.status_is_unauthorized
      required: true
    - as: domain.http.status_is_forbidden
      from: assert.function
      path: /domain.http.status_is_forbidden
      required: true
    - as: domain.http.ok_2xx
      from: assert.function
      path: /domain.http.ok_2xx
      required: true
    - as: domain.http.header_get
      from: assert.function
      path: /domain.http.header_get
      required: true
    - as: domain.http.header_contains
      from: assert.function
      path: /domain.http.header_contains
      required: true
    - as: domain.http.body_text
      from: assert.function
      path: /domain.http.body_text
      required: true
    - as: domain.http.body_json
      from: assert.function
      path: /domain.http.body_json
      required: true
    - as: domain.http.body_json_type_is
      from: assert.function
      path: /domain.http.body_json_type_is
      required: true
    - as: domain.http.body_json_has_key
      from: assert.function
      path: /domain.http.body_json_has_key
      required: true
    - as: domain.http.auth_is_oauth
      from: assert.function
      path: /domain.http.auth_is_oauth
      required: true
    - as: domain.http.has_bearer_header
      from: assert.function
      path: /domain.http.has_bearer_header
      required: true
    - as: domain.http.oauth_scope_requested
      from: assert.function
      path: /domain.http.oauth_scope_requested
      required: true
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-003-DOMAIN-HTTP-STATUS-IS
title: 'http projection helper functions: domain.http.status_is'
type: spec_lang.export
defines:
  public:
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
  private: {}
harness:
  chain:
    exports:
    - as: domain.http.cors_allow_origin
      from: assert.function
      path: /domain.http.cors_allow_origin
      required: true
    - as: domain.http.cors_allows_method
      from: assert.function
      path: /domain.http.cors_allows_method
      required: true
    - as: domain.http.cors_allows_header
      from: assert.function
      path: /domain.http.cors_allows_header
      required: true
    - as: domain.http.cors_credentials_enabled
      from: assert.function
      path: /domain.http.cors_credentials_enabled
      required: true
    - as: domain.http.cors_max_age_gte
      from: assert.function
      path: /domain.http.cors_max_age_gte
      required: true
    - as: domain.http.is_preflight_step
      from: assert.function
      path: /domain.http.is_preflight_step
      required: true
    - as: domain.http.step_by_id
      from: assert.function
      path: /domain.http.step_by_id
      required: true
    - as: domain.http.step_status_is
      from: assert.function
      path: /domain.http.step_status_is
      required: true
    - as: domain.http.step_body_json_get
      from: assert.function
      path: /domain.http.step_body_json_get
      required: true
    - as: domain.http.status
      from: assert.function
      path: /domain.http.status
      required: true
    - as: domain.http.status_in
      from: assert.function
      path: /domain.http.status_in
      required: true
    - as: domain.http.status_is
      from: assert.function
      path: /domain.http.status_is
      required: true
    - as: domain.http.status_is_unauthorized
      from: assert.function
      path: /domain.http.status_is_unauthorized
      required: true
    - as: domain.http.status_is_forbidden
      from: assert.function
      path: /domain.http.status_is_forbidden
      required: true
    - as: domain.http.ok_2xx
      from: assert.function
      path: /domain.http.ok_2xx
      required: true
    - as: domain.http.header_get
      from: assert.function
      path: /domain.http.header_get
      required: true
    - as: domain.http.header_contains
      from: assert.function
      path: /domain.http.header_contains
      required: true
    - as: domain.http.body_text
      from: assert.function
      path: /domain.http.body_text
      required: true
    - as: domain.http.body_json
      from: assert.function
      path: /domain.http.body_json
      required: true
    - as: domain.http.body_json_type_is
      from: assert.function
      path: /domain.http.body_json_type_is
      required: true
    - as: domain.http.body_json_has_key
      from: assert.function
      path: /domain.http.body_json_has_key
      required: true
    - as: domain.http.auth_is_oauth
      from: assert.function
      path: /domain.http.auth_is_oauth
      required: true
    - as: domain.http.has_bearer_header
      from: assert.function
      path: /domain.http.has_bearer_header
      required: true
    - as: domain.http.oauth_scope_requested
      from: assert.function
      path: /domain.http.oauth_scope_requested
      required: true
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-004-DOMAIN-HTTP-STATUS-IS-UNAUTHORIZED
title: 'http projection helper functions: domain.http.status_is_unauthorized'
type: spec_lang.export
defines:
  public:
    domain.http.status_is_unauthorized:
      fn:
      - [subject]
      - call:
        - {var: domain.http.status_is}
        - {var: subject}
        - 401
  private: {}
harness:
  chain:
    exports:
    - as: domain.http.cors_allow_origin
      from: assert.function
      path: /domain.http.cors_allow_origin
      required: true
    - as: domain.http.cors_allows_method
      from: assert.function
      path: /domain.http.cors_allows_method
      required: true
    - as: domain.http.cors_allows_header
      from: assert.function
      path: /domain.http.cors_allows_header
      required: true
    - as: domain.http.cors_credentials_enabled
      from: assert.function
      path: /domain.http.cors_credentials_enabled
      required: true
    - as: domain.http.cors_max_age_gte
      from: assert.function
      path: /domain.http.cors_max_age_gte
      required: true
    - as: domain.http.is_preflight_step
      from: assert.function
      path: /domain.http.is_preflight_step
      required: true
    - as: domain.http.step_by_id
      from: assert.function
      path: /domain.http.step_by_id
      required: true
    - as: domain.http.step_status_is
      from: assert.function
      path: /domain.http.step_status_is
      required: true
    - as: domain.http.step_body_json_get
      from: assert.function
      path: /domain.http.step_body_json_get
      required: true
    - as: domain.http.status
      from: assert.function
      path: /domain.http.status
      required: true
    - as: domain.http.status_in
      from: assert.function
      path: /domain.http.status_in
      required: true
    - as: domain.http.status_is
      from: assert.function
      path: /domain.http.status_is
      required: true
    - as: domain.http.status_is_unauthorized
      from: assert.function
      path: /domain.http.status_is_unauthorized
      required: true
    - as: domain.http.status_is_forbidden
      from: assert.function
      path: /domain.http.status_is_forbidden
      required: true
    - as: domain.http.ok_2xx
      from: assert.function
      path: /domain.http.ok_2xx
      required: true
    - as: domain.http.header_get
      from: assert.function
      path: /domain.http.header_get
      required: true
    - as: domain.http.header_contains
      from: assert.function
      path: /domain.http.header_contains
      required: true
    - as: domain.http.body_text
      from: assert.function
      path: /domain.http.body_text
      required: true
    - as: domain.http.body_json
      from: assert.function
      path: /domain.http.body_json
      required: true
    - as: domain.http.body_json_type_is
      from: assert.function
      path: /domain.http.body_json_type_is
      required: true
    - as: domain.http.body_json_has_key
      from: assert.function
      path: /domain.http.body_json_has_key
      required: true
    - as: domain.http.auth_is_oauth
      from: assert.function
      path: /domain.http.auth_is_oauth
      required: true
    - as: domain.http.has_bearer_header
      from: assert.function
      path: /domain.http.has_bearer_header
      required: true
    - as: domain.http.oauth_scope_requested
      from: assert.function
      path: /domain.http.oauth_scope_requested
      required: true
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-005-DOMAIN-HTTP-STATUS-IS-FORBIDDEN
title: 'http projection helper functions: domain.http.status_is_forbidden'
type: spec_lang.export
defines:
  public:
    domain.http.status_is_forbidden:
      fn:
      - [subject]
      - call:
        - {var: domain.http.status_is}
        - {var: subject}
        - 403
  private: {}
harness:
  chain:
    exports:
    - as: domain.http.cors_allow_origin
      from: assert.function
      path: /domain.http.cors_allow_origin
      required: true
    - as: domain.http.cors_allows_method
      from: assert.function
      path: /domain.http.cors_allows_method
      required: true
    - as: domain.http.cors_allows_header
      from: assert.function
      path: /domain.http.cors_allows_header
      required: true
    - as: domain.http.cors_credentials_enabled
      from: assert.function
      path: /domain.http.cors_credentials_enabled
      required: true
    - as: domain.http.cors_max_age_gte
      from: assert.function
      path: /domain.http.cors_max_age_gte
      required: true
    - as: domain.http.is_preflight_step
      from: assert.function
      path: /domain.http.is_preflight_step
      required: true
    - as: domain.http.step_by_id
      from: assert.function
      path: /domain.http.step_by_id
      required: true
    - as: domain.http.step_status_is
      from: assert.function
      path: /domain.http.step_status_is
      required: true
    - as: domain.http.step_body_json_get
      from: assert.function
      path: /domain.http.step_body_json_get
      required: true
    - as: domain.http.status
      from: assert.function
      path: /domain.http.status
      required: true
    - as: domain.http.status_in
      from: assert.function
      path: /domain.http.status_in
      required: true
    - as: domain.http.status_is
      from: assert.function
      path: /domain.http.status_is
      required: true
    - as: domain.http.status_is_unauthorized
      from: assert.function
      path: /domain.http.status_is_unauthorized
      required: true
    - as: domain.http.status_is_forbidden
      from: assert.function
      path: /domain.http.status_is_forbidden
      required: true
    - as: domain.http.ok_2xx
      from: assert.function
      path: /domain.http.ok_2xx
      required: true
    - as: domain.http.header_get
      from: assert.function
      path: /domain.http.header_get
      required: true
    - as: domain.http.header_contains
      from: assert.function
      path: /domain.http.header_contains
      required: true
    - as: domain.http.body_text
      from: assert.function
      path: /domain.http.body_text
      required: true
    - as: domain.http.body_json
      from: assert.function
      path: /domain.http.body_json
      required: true
    - as: domain.http.body_json_type_is
      from: assert.function
      path: /domain.http.body_json_type_is
      required: true
    - as: domain.http.body_json_has_key
      from: assert.function
      path: /domain.http.body_json_has_key
      required: true
    - as: domain.http.auth_is_oauth
      from: assert.function
      path: /domain.http.auth_is_oauth
      required: true
    - as: domain.http.has_bearer_header
      from: assert.function
      path: /domain.http.has_bearer_header
      required: true
    - as: domain.http.oauth_scope_requested
      from: assert.function
      path: /domain.http.oauth_scope_requested
      required: true
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-006-DOMAIN-HTTP-OK-2XX
title: 'http projection helper functions: domain.http.ok_2xx'
type: spec_lang.export
defines:
  public:
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
  private: {}
harness:
  chain:
    exports:
    - as: domain.http.cors_allow_origin
      from: assert.function
      path: /domain.http.cors_allow_origin
      required: true
    - as: domain.http.cors_allows_method
      from: assert.function
      path: /domain.http.cors_allows_method
      required: true
    - as: domain.http.cors_allows_header
      from: assert.function
      path: /domain.http.cors_allows_header
      required: true
    - as: domain.http.cors_credentials_enabled
      from: assert.function
      path: /domain.http.cors_credentials_enabled
      required: true
    - as: domain.http.cors_max_age_gte
      from: assert.function
      path: /domain.http.cors_max_age_gte
      required: true
    - as: domain.http.is_preflight_step
      from: assert.function
      path: /domain.http.is_preflight_step
      required: true
    - as: domain.http.step_by_id
      from: assert.function
      path: /domain.http.step_by_id
      required: true
    - as: domain.http.step_status_is
      from: assert.function
      path: /domain.http.step_status_is
      required: true
    - as: domain.http.step_body_json_get
      from: assert.function
      path: /domain.http.step_body_json_get
      required: true
    - as: domain.http.status
      from: assert.function
      path: /domain.http.status
      required: true
    - as: domain.http.status_in
      from: assert.function
      path: /domain.http.status_in
      required: true
    - as: domain.http.status_is
      from: assert.function
      path: /domain.http.status_is
      required: true
    - as: domain.http.status_is_unauthorized
      from: assert.function
      path: /domain.http.status_is_unauthorized
      required: true
    - as: domain.http.status_is_forbidden
      from: assert.function
      path: /domain.http.status_is_forbidden
      required: true
    - as: domain.http.ok_2xx
      from: assert.function
      path: /domain.http.ok_2xx
      required: true
    - as: domain.http.header_get
      from: assert.function
      path: /domain.http.header_get
      required: true
    - as: domain.http.header_contains
      from: assert.function
      path: /domain.http.header_contains
      required: true
    - as: domain.http.body_text
      from: assert.function
      path: /domain.http.body_text
      required: true
    - as: domain.http.body_json
      from: assert.function
      path: /domain.http.body_json
      required: true
    - as: domain.http.body_json_type_is
      from: assert.function
      path: /domain.http.body_json_type_is
      required: true
    - as: domain.http.body_json_has_key
      from: assert.function
      path: /domain.http.body_json_has_key
      required: true
    - as: domain.http.auth_is_oauth
      from: assert.function
      path: /domain.http.auth_is_oauth
      required: true
    - as: domain.http.has_bearer_header
      from: assert.function
      path: /domain.http.has_bearer_header
      required: true
    - as: domain.http.oauth_scope_requested
      from: assert.function
      path: /domain.http.oauth_scope_requested
      required: true
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-007-DOMAIN-HTTP-HEADER-GET
title: 'http projection helper functions: domain.http.header_get'
type: spec_lang.export
defines:
  public:
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
  private: {}
harness:
  chain:
    exports:
    - as: domain.http.cors_allow_origin
      from: assert.function
      path: /domain.http.cors_allow_origin
      required: true
    - as: domain.http.cors_allows_method
      from: assert.function
      path: /domain.http.cors_allows_method
      required: true
    - as: domain.http.cors_allows_header
      from: assert.function
      path: /domain.http.cors_allows_header
      required: true
    - as: domain.http.cors_credentials_enabled
      from: assert.function
      path: /domain.http.cors_credentials_enabled
      required: true
    - as: domain.http.cors_max_age_gte
      from: assert.function
      path: /domain.http.cors_max_age_gte
      required: true
    - as: domain.http.is_preflight_step
      from: assert.function
      path: /domain.http.is_preflight_step
      required: true
    - as: domain.http.step_by_id
      from: assert.function
      path: /domain.http.step_by_id
      required: true
    - as: domain.http.step_status_is
      from: assert.function
      path: /domain.http.step_status_is
      required: true
    - as: domain.http.step_body_json_get
      from: assert.function
      path: /domain.http.step_body_json_get
      required: true
    - as: domain.http.status
      from: assert.function
      path: /domain.http.status
      required: true
    - as: domain.http.status_in
      from: assert.function
      path: /domain.http.status_in
      required: true
    - as: domain.http.status_is
      from: assert.function
      path: /domain.http.status_is
      required: true
    - as: domain.http.status_is_unauthorized
      from: assert.function
      path: /domain.http.status_is_unauthorized
      required: true
    - as: domain.http.status_is_forbidden
      from: assert.function
      path: /domain.http.status_is_forbidden
      required: true
    - as: domain.http.ok_2xx
      from: assert.function
      path: /domain.http.ok_2xx
      required: true
    - as: domain.http.header_get
      from: assert.function
      path: /domain.http.header_get
      required: true
    - as: domain.http.header_contains
      from: assert.function
      path: /domain.http.header_contains
      required: true
    - as: domain.http.body_text
      from: assert.function
      path: /domain.http.body_text
      required: true
    - as: domain.http.body_json
      from: assert.function
      path: /domain.http.body_json
      required: true
    - as: domain.http.body_json_type_is
      from: assert.function
      path: /domain.http.body_json_type_is
      required: true
    - as: domain.http.body_json_has_key
      from: assert.function
      path: /domain.http.body_json_has_key
      required: true
    - as: domain.http.auth_is_oauth
      from: assert.function
      path: /domain.http.auth_is_oauth
      required: true
    - as: domain.http.has_bearer_header
      from: assert.function
      path: /domain.http.has_bearer_header
      required: true
    - as: domain.http.oauth_scope_requested
      from: assert.function
      path: /domain.http.oauth_scope_requested
      required: true
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-008-DOMAIN-HTTP-HEADER-CONTAINS
title: 'http projection helper functions: domain.http.header_contains'
type: spec_lang.export
defines:
  public:
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
  private: {}
harness:
  chain:
    exports:
    - as: domain.http.cors_allow_origin
      from: assert.function
      path: /domain.http.cors_allow_origin
      required: true
    - as: domain.http.cors_allows_method
      from: assert.function
      path: /domain.http.cors_allows_method
      required: true
    - as: domain.http.cors_allows_header
      from: assert.function
      path: /domain.http.cors_allows_header
      required: true
    - as: domain.http.cors_credentials_enabled
      from: assert.function
      path: /domain.http.cors_credentials_enabled
      required: true
    - as: domain.http.cors_max_age_gte
      from: assert.function
      path: /domain.http.cors_max_age_gte
      required: true
    - as: domain.http.is_preflight_step
      from: assert.function
      path: /domain.http.is_preflight_step
      required: true
    - as: domain.http.step_by_id
      from: assert.function
      path: /domain.http.step_by_id
      required: true
    - as: domain.http.step_status_is
      from: assert.function
      path: /domain.http.step_status_is
      required: true
    - as: domain.http.step_body_json_get
      from: assert.function
      path: /domain.http.step_body_json_get
      required: true
    - as: domain.http.status
      from: assert.function
      path: /domain.http.status
      required: true
    - as: domain.http.status_in
      from: assert.function
      path: /domain.http.status_in
      required: true
    - as: domain.http.status_is
      from: assert.function
      path: /domain.http.status_is
      required: true
    - as: domain.http.status_is_unauthorized
      from: assert.function
      path: /domain.http.status_is_unauthorized
      required: true
    - as: domain.http.status_is_forbidden
      from: assert.function
      path: /domain.http.status_is_forbidden
      required: true
    - as: domain.http.ok_2xx
      from: assert.function
      path: /domain.http.ok_2xx
      required: true
    - as: domain.http.header_get
      from: assert.function
      path: /domain.http.header_get
      required: true
    - as: domain.http.header_contains
      from: assert.function
      path: /domain.http.header_contains
      required: true
    - as: domain.http.body_text
      from: assert.function
      path: /domain.http.body_text
      required: true
    - as: domain.http.body_json
      from: assert.function
      path: /domain.http.body_json
      required: true
    - as: domain.http.body_json_type_is
      from: assert.function
      path: /domain.http.body_json_type_is
      required: true
    - as: domain.http.body_json_has_key
      from: assert.function
      path: /domain.http.body_json_has_key
      required: true
    - as: domain.http.auth_is_oauth
      from: assert.function
      path: /domain.http.auth_is_oauth
      required: true
    - as: domain.http.has_bearer_header
      from: assert.function
      path: /domain.http.has_bearer_header
      required: true
    - as: domain.http.oauth_scope_requested
      from: assert.function
      path: /domain.http.oauth_scope_requested
      required: true
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-009-DOMAIN-HTTP-BODY-TEXT
title: 'http projection helper functions: domain.http.body_text'
type: spec_lang.export
defines:
  public:
    domain.http.body_text:
      fn:
      - [subject]
      - std.object.get:
        - std.object.get:
          - {var: subject}
          - value
        - body_text
  private: {}
harness:
  chain:
    exports:
    - as: domain.http.cors_allow_origin
      from: assert.function
      path: /domain.http.cors_allow_origin
      required: true
    - as: domain.http.cors_allows_method
      from: assert.function
      path: /domain.http.cors_allows_method
      required: true
    - as: domain.http.cors_allows_header
      from: assert.function
      path: /domain.http.cors_allows_header
      required: true
    - as: domain.http.cors_credentials_enabled
      from: assert.function
      path: /domain.http.cors_credentials_enabled
      required: true
    - as: domain.http.cors_max_age_gte
      from: assert.function
      path: /domain.http.cors_max_age_gte
      required: true
    - as: domain.http.is_preflight_step
      from: assert.function
      path: /domain.http.is_preflight_step
      required: true
    - as: domain.http.step_by_id
      from: assert.function
      path: /domain.http.step_by_id
      required: true
    - as: domain.http.step_status_is
      from: assert.function
      path: /domain.http.step_status_is
      required: true
    - as: domain.http.step_body_json_get
      from: assert.function
      path: /domain.http.step_body_json_get
      required: true
    - as: domain.http.status
      from: assert.function
      path: /domain.http.status
      required: true
    - as: domain.http.status_in
      from: assert.function
      path: /domain.http.status_in
      required: true
    - as: domain.http.status_is
      from: assert.function
      path: /domain.http.status_is
      required: true
    - as: domain.http.status_is_unauthorized
      from: assert.function
      path: /domain.http.status_is_unauthorized
      required: true
    - as: domain.http.status_is_forbidden
      from: assert.function
      path: /domain.http.status_is_forbidden
      required: true
    - as: domain.http.ok_2xx
      from: assert.function
      path: /domain.http.ok_2xx
      required: true
    - as: domain.http.header_get
      from: assert.function
      path: /domain.http.header_get
      required: true
    - as: domain.http.header_contains
      from: assert.function
      path: /domain.http.header_contains
      required: true
    - as: domain.http.body_text
      from: assert.function
      path: /domain.http.body_text
      required: true
    - as: domain.http.body_json
      from: assert.function
      path: /domain.http.body_json
      required: true
    - as: domain.http.body_json_type_is
      from: assert.function
      path: /domain.http.body_json_type_is
      required: true
    - as: domain.http.body_json_has_key
      from: assert.function
      path: /domain.http.body_json_has_key
      required: true
    - as: domain.http.auth_is_oauth
      from: assert.function
      path: /domain.http.auth_is_oauth
      required: true
    - as: domain.http.has_bearer_header
      from: assert.function
      path: /domain.http.has_bearer_header
      required: true
    - as: domain.http.oauth_scope_requested
      from: assert.function
      path: /domain.http.oauth_scope_requested
      required: true
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-010-DOMAIN-HTTP-BODY-JSON
title: 'http projection helper functions: domain.http.body_json'
type: spec_lang.export
defines:
  public:
    domain.http.body_json:
      fn:
      - [subject]
      - std.object.get:
        - std.object.get:
          - {var: subject}
          - value
        - body_json
  private: {}
harness:
  chain:
    exports:
    - as: domain.http.cors_allow_origin
      from: assert.function
      path: /domain.http.cors_allow_origin
      required: true
    - as: domain.http.cors_allows_method
      from: assert.function
      path: /domain.http.cors_allows_method
      required: true
    - as: domain.http.cors_allows_header
      from: assert.function
      path: /domain.http.cors_allows_header
      required: true
    - as: domain.http.cors_credentials_enabled
      from: assert.function
      path: /domain.http.cors_credentials_enabled
      required: true
    - as: domain.http.cors_max_age_gte
      from: assert.function
      path: /domain.http.cors_max_age_gte
      required: true
    - as: domain.http.is_preflight_step
      from: assert.function
      path: /domain.http.is_preflight_step
      required: true
    - as: domain.http.step_by_id
      from: assert.function
      path: /domain.http.step_by_id
      required: true
    - as: domain.http.step_status_is
      from: assert.function
      path: /domain.http.step_status_is
      required: true
    - as: domain.http.step_body_json_get
      from: assert.function
      path: /domain.http.step_body_json_get
      required: true
    - as: domain.http.status
      from: assert.function
      path: /domain.http.status
      required: true
    - as: domain.http.status_in
      from: assert.function
      path: /domain.http.status_in
      required: true
    - as: domain.http.status_is
      from: assert.function
      path: /domain.http.status_is
      required: true
    - as: domain.http.status_is_unauthorized
      from: assert.function
      path: /domain.http.status_is_unauthorized
      required: true
    - as: domain.http.status_is_forbidden
      from: assert.function
      path: /domain.http.status_is_forbidden
      required: true
    - as: domain.http.ok_2xx
      from: assert.function
      path: /domain.http.ok_2xx
      required: true
    - as: domain.http.header_get
      from: assert.function
      path: /domain.http.header_get
      required: true
    - as: domain.http.header_contains
      from: assert.function
      path: /domain.http.header_contains
      required: true
    - as: domain.http.body_text
      from: assert.function
      path: /domain.http.body_text
      required: true
    - as: domain.http.body_json
      from: assert.function
      path: /domain.http.body_json
      required: true
    - as: domain.http.body_json_type_is
      from: assert.function
      path: /domain.http.body_json_type_is
      required: true
    - as: domain.http.body_json_has_key
      from: assert.function
      path: /domain.http.body_json_has_key
      required: true
    - as: domain.http.auth_is_oauth
      from: assert.function
      path: /domain.http.auth_is_oauth
      required: true
    - as: domain.http.has_bearer_header
      from: assert.function
      path: /domain.http.has_bearer_header
      required: true
    - as: domain.http.oauth_scope_requested
      from: assert.function
      path: /domain.http.oauth_scope_requested
      required: true
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-011-DOMAIN-HTTP-BODY-JSON-TYPE-IS
title: 'http projection helper functions: domain.http.body_json_type_is'
type: spec_lang.export
defines:
  public:
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
  private: {}
harness:
  chain:
    exports:
    - as: domain.http.cors_allow_origin
      from: assert.function
      path: /domain.http.cors_allow_origin
      required: true
    - as: domain.http.cors_allows_method
      from: assert.function
      path: /domain.http.cors_allows_method
      required: true
    - as: domain.http.cors_allows_header
      from: assert.function
      path: /domain.http.cors_allows_header
      required: true
    - as: domain.http.cors_credentials_enabled
      from: assert.function
      path: /domain.http.cors_credentials_enabled
      required: true
    - as: domain.http.cors_max_age_gte
      from: assert.function
      path: /domain.http.cors_max_age_gte
      required: true
    - as: domain.http.is_preflight_step
      from: assert.function
      path: /domain.http.is_preflight_step
      required: true
    - as: domain.http.step_by_id
      from: assert.function
      path: /domain.http.step_by_id
      required: true
    - as: domain.http.step_status_is
      from: assert.function
      path: /domain.http.step_status_is
      required: true
    - as: domain.http.step_body_json_get
      from: assert.function
      path: /domain.http.step_body_json_get
      required: true
    - as: domain.http.status
      from: assert.function
      path: /domain.http.status
      required: true
    - as: domain.http.status_in
      from: assert.function
      path: /domain.http.status_in
      required: true
    - as: domain.http.status_is
      from: assert.function
      path: /domain.http.status_is
      required: true
    - as: domain.http.status_is_unauthorized
      from: assert.function
      path: /domain.http.status_is_unauthorized
      required: true
    - as: domain.http.status_is_forbidden
      from: assert.function
      path: /domain.http.status_is_forbidden
      required: true
    - as: domain.http.ok_2xx
      from: assert.function
      path: /domain.http.ok_2xx
      required: true
    - as: domain.http.header_get
      from: assert.function
      path: /domain.http.header_get
      required: true
    - as: domain.http.header_contains
      from: assert.function
      path: /domain.http.header_contains
      required: true
    - as: domain.http.body_text
      from: assert.function
      path: /domain.http.body_text
      required: true
    - as: domain.http.body_json
      from: assert.function
      path: /domain.http.body_json
      required: true
    - as: domain.http.body_json_type_is
      from: assert.function
      path: /domain.http.body_json_type_is
      required: true
    - as: domain.http.body_json_has_key
      from: assert.function
      path: /domain.http.body_json_has_key
      required: true
    - as: domain.http.auth_is_oauth
      from: assert.function
      path: /domain.http.auth_is_oauth
      required: true
    - as: domain.http.has_bearer_header
      from: assert.function
      path: /domain.http.has_bearer_header
      required: true
    - as: domain.http.oauth_scope_requested
      from: assert.function
      path: /domain.http.oauth_scope_requested
      required: true
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-012-DOMAIN-HTTP-BODY-JSON-HAS-KEY
title: 'http projection helper functions: domain.http.body_json_has_key'
type: spec_lang.export
defines:
  public:
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
  private: {}
harness:
  chain:
    exports:
    - as: domain.http.cors_allow_origin
      from: assert.function
      path: /domain.http.cors_allow_origin
      required: true
    - as: domain.http.cors_allows_method
      from: assert.function
      path: /domain.http.cors_allows_method
      required: true
    - as: domain.http.cors_allows_header
      from: assert.function
      path: /domain.http.cors_allows_header
      required: true
    - as: domain.http.cors_credentials_enabled
      from: assert.function
      path: /domain.http.cors_credentials_enabled
      required: true
    - as: domain.http.cors_max_age_gte
      from: assert.function
      path: /domain.http.cors_max_age_gte
      required: true
    - as: domain.http.is_preflight_step
      from: assert.function
      path: /domain.http.is_preflight_step
      required: true
    - as: domain.http.step_by_id
      from: assert.function
      path: /domain.http.step_by_id
      required: true
    - as: domain.http.step_status_is
      from: assert.function
      path: /domain.http.step_status_is
      required: true
    - as: domain.http.step_body_json_get
      from: assert.function
      path: /domain.http.step_body_json_get
      required: true
    - as: domain.http.status
      from: assert.function
      path: /domain.http.status
      required: true
    - as: domain.http.status_in
      from: assert.function
      path: /domain.http.status_in
      required: true
    - as: domain.http.status_is
      from: assert.function
      path: /domain.http.status_is
      required: true
    - as: domain.http.status_is_unauthorized
      from: assert.function
      path: /domain.http.status_is_unauthorized
      required: true
    - as: domain.http.status_is_forbidden
      from: assert.function
      path: /domain.http.status_is_forbidden
      required: true
    - as: domain.http.ok_2xx
      from: assert.function
      path: /domain.http.ok_2xx
      required: true
    - as: domain.http.header_get
      from: assert.function
      path: /domain.http.header_get
      required: true
    - as: domain.http.header_contains
      from: assert.function
      path: /domain.http.header_contains
      required: true
    - as: domain.http.body_text
      from: assert.function
      path: /domain.http.body_text
      required: true
    - as: domain.http.body_json
      from: assert.function
      path: /domain.http.body_json
      required: true
    - as: domain.http.body_json_type_is
      from: assert.function
      path: /domain.http.body_json_type_is
      required: true
    - as: domain.http.body_json_has_key
      from: assert.function
      path: /domain.http.body_json_has_key
      required: true
    - as: domain.http.auth_is_oauth
      from: assert.function
      path: /domain.http.auth_is_oauth
      required: true
    - as: domain.http.has_bearer_header
      from: assert.function
      path: /domain.http.has_bearer_header
      required: true
    - as: domain.http.oauth_scope_requested
      from: assert.function
      path: /domain.http.oauth_scope_requested
      required: true
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-013-DOMAIN-HTTP-AUTH-IS-OAUTH
title: 'http projection helper functions: domain.http.auth_is_oauth'
type: spec_lang.export
defines:
  public:
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
  private: {}
harness:
  chain:
    exports:
    - as: domain.http.cors_allow_origin
      from: assert.function
      path: /domain.http.cors_allow_origin
      required: true
    - as: domain.http.cors_allows_method
      from: assert.function
      path: /domain.http.cors_allows_method
      required: true
    - as: domain.http.cors_allows_header
      from: assert.function
      path: /domain.http.cors_allows_header
      required: true
    - as: domain.http.cors_credentials_enabled
      from: assert.function
      path: /domain.http.cors_credentials_enabled
      required: true
    - as: domain.http.cors_max_age_gte
      from: assert.function
      path: /domain.http.cors_max_age_gte
      required: true
    - as: domain.http.is_preflight_step
      from: assert.function
      path: /domain.http.is_preflight_step
      required: true
    - as: domain.http.step_by_id
      from: assert.function
      path: /domain.http.step_by_id
      required: true
    - as: domain.http.step_status_is
      from: assert.function
      path: /domain.http.step_status_is
      required: true
    - as: domain.http.step_body_json_get
      from: assert.function
      path: /domain.http.step_body_json_get
      required: true
    - as: domain.http.status
      from: assert.function
      path: /domain.http.status
      required: true
    - as: domain.http.status_in
      from: assert.function
      path: /domain.http.status_in
      required: true
    - as: domain.http.status_is
      from: assert.function
      path: /domain.http.status_is
      required: true
    - as: domain.http.status_is_unauthorized
      from: assert.function
      path: /domain.http.status_is_unauthorized
      required: true
    - as: domain.http.status_is_forbidden
      from: assert.function
      path: /domain.http.status_is_forbidden
      required: true
    - as: domain.http.ok_2xx
      from: assert.function
      path: /domain.http.ok_2xx
      required: true
    - as: domain.http.header_get
      from: assert.function
      path: /domain.http.header_get
      required: true
    - as: domain.http.header_contains
      from: assert.function
      path: /domain.http.header_contains
      required: true
    - as: domain.http.body_text
      from: assert.function
      path: /domain.http.body_text
      required: true
    - as: domain.http.body_json
      from: assert.function
      path: /domain.http.body_json
      required: true
    - as: domain.http.body_json_type_is
      from: assert.function
      path: /domain.http.body_json_type_is
      required: true
    - as: domain.http.body_json_has_key
      from: assert.function
      path: /domain.http.body_json_has_key
      required: true
    - as: domain.http.auth_is_oauth
      from: assert.function
      path: /domain.http.auth_is_oauth
      required: true
    - as: domain.http.has_bearer_header
      from: assert.function
      path: /domain.http.has_bearer_header
      required: true
    - as: domain.http.oauth_scope_requested
      from: assert.function
      path: /domain.http.oauth_scope_requested
      required: true
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-014-DOMAIN-HTTP-HAS-BEARER-HEADER
title: 'http projection helper functions: domain.http.has_bearer_header'
type: spec_lang.export
defines:
  public:
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
  private: {}
harness:
  chain:
    exports:
    - as: domain.http.cors_allow_origin
      from: assert.function
      path: /domain.http.cors_allow_origin
      required: true
    - as: domain.http.cors_allows_method
      from: assert.function
      path: /domain.http.cors_allows_method
      required: true
    - as: domain.http.cors_allows_header
      from: assert.function
      path: /domain.http.cors_allows_header
      required: true
    - as: domain.http.cors_credentials_enabled
      from: assert.function
      path: /domain.http.cors_credentials_enabled
      required: true
    - as: domain.http.cors_max_age_gte
      from: assert.function
      path: /domain.http.cors_max_age_gte
      required: true
    - as: domain.http.is_preflight_step
      from: assert.function
      path: /domain.http.is_preflight_step
      required: true
    - as: domain.http.step_by_id
      from: assert.function
      path: /domain.http.step_by_id
      required: true
    - as: domain.http.step_status_is
      from: assert.function
      path: /domain.http.step_status_is
      required: true
    - as: domain.http.step_body_json_get
      from: assert.function
      path: /domain.http.step_body_json_get
      required: true
    - as: domain.http.status
      from: assert.function
      path: /domain.http.status
      required: true
    - as: domain.http.status_in
      from: assert.function
      path: /domain.http.status_in
      required: true
    - as: domain.http.status_is
      from: assert.function
      path: /domain.http.status_is
      required: true
    - as: domain.http.status_is_unauthorized
      from: assert.function
      path: /domain.http.status_is_unauthorized
      required: true
    - as: domain.http.status_is_forbidden
      from: assert.function
      path: /domain.http.status_is_forbidden
      required: true
    - as: domain.http.ok_2xx
      from: assert.function
      path: /domain.http.ok_2xx
      required: true
    - as: domain.http.header_get
      from: assert.function
      path: /domain.http.header_get
      required: true
    - as: domain.http.header_contains
      from: assert.function
      path: /domain.http.header_contains
      required: true
    - as: domain.http.body_text
      from: assert.function
      path: /domain.http.body_text
      required: true
    - as: domain.http.body_json
      from: assert.function
      path: /domain.http.body_json
      required: true
    - as: domain.http.body_json_type_is
      from: assert.function
      path: /domain.http.body_json_type_is
      required: true
    - as: domain.http.body_json_has_key
      from: assert.function
      path: /domain.http.body_json_has_key
      required: true
    - as: domain.http.auth_is_oauth
      from: assert.function
      path: /domain.http.auth_is_oauth
      required: true
    - as: domain.http.has_bearer_header
      from: assert.function
      path: /domain.http.has_bearer_header
      required: true
    - as: domain.http.oauth_scope_requested
      from: assert.function
      path: /domain.http.oauth_scope_requested
      required: true
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-015-DOMAIN-HTTP-OAUTH-SCOPE-REQUESTED
title: 'http projection helper functions: domain.http.oauth_scope_requested'
type: spec_lang.export
defines:
  public:
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
  private: {}
harness:
  chain:
    exports:
    - as: domain.http.cors_allow_origin
      from: assert.function
      path: /domain.http.cors_allow_origin
      required: true
    - as: domain.http.cors_allows_method
      from: assert.function
      path: /domain.http.cors_allows_method
      required: true
    - as: domain.http.cors_allows_header
      from: assert.function
      path: /domain.http.cors_allows_header
      required: true
    - as: domain.http.cors_credentials_enabled
      from: assert.function
      path: /domain.http.cors_credentials_enabled
      required: true
    - as: domain.http.cors_max_age_gte
      from: assert.function
      path: /domain.http.cors_max_age_gte
      required: true
    - as: domain.http.is_preflight_step
      from: assert.function
      path: /domain.http.is_preflight_step
      required: true
    - as: domain.http.step_by_id
      from: assert.function
      path: /domain.http.step_by_id
      required: true
    - as: domain.http.step_status_is
      from: assert.function
      path: /domain.http.step_status_is
      required: true
    - as: domain.http.step_body_json_get
      from: assert.function
      path: /domain.http.step_body_json_get
      required: true
    - as: domain.http.status
      from: assert.function
      path: /domain.http.status
      required: true
    - as: domain.http.status_in
      from: assert.function
      path: /domain.http.status_in
      required: true
    - as: domain.http.status_is
      from: assert.function
      path: /domain.http.status_is
      required: true
    - as: domain.http.status_is_unauthorized
      from: assert.function
      path: /domain.http.status_is_unauthorized
      required: true
    - as: domain.http.status_is_forbidden
      from: assert.function
      path: /domain.http.status_is_forbidden
      required: true
    - as: domain.http.ok_2xx
      from: assert.function
      path: /domain.http.ok_2xx
      required: true
    - as: domain.http.header_get
      from: assert.function
      path: /domain.http.header_get
      required: true
    - as: domain.http.header_contains
      from: assert.function
      path: /domain.http.header_contains
      required: true
    - as: domain.http.body_text
      from: assert.function
      path: /domain.http.body_text
      required: true
    - as: domain.http.body_json
      from: assert.function
      path: /domain.http.body_json
      required: true
    - as: domain.http.body_json_type_is
      from: assert.function
      path: /domain.http.body_json_type_is
      required: true
    - as: domain.http.body_json_has_key
      from: assert.function
      path: /domain.http.body_json_has_key
      required: true
    - as: domain.http.auth_is_oauth
      from: assert.function
      path: /domain.http.auth_is_oauth
      required: true
    - as: domain.http.has_bearer_header
      from: assert.function
      path: /domain.http.has_bearer_header
      required: true
    - as: domain.http.oauth_scope_requested
      from: assert.function
      path: /domain.http.oauth_scope_requested
      required: true
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-016-DOMAIN-HTTP-CORS-ALLOW-ORIGIN
title: 'http projection helper functions: domain.http.cors_allow_origin'
type: spec_lang.export
defines:
  public:
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
  private: {}
harness:
  chain:
    exports:
    - as: domain.http.cors_allow_origin
      from: assert.function
      path: /domain.http.cors_allow_origin
      required: true
    - as: domain.http.cors_allows_method
      from: assert.function
      path: /domain.http.cors_allows_method
      required: true
    - as: domain.http.cors_allows_header
      from: assert.function
      path: /domain.http.cors_allows_header
      required: true
    - as: domain.http.cors_credentials_enabled
      from: assert.function
      path: /domain.http.cors_credentials_enabled
      required: true
    - as: domain.http.cors_max_age_gte
      from: assert.function
      path: /domain.http.cors_max_age_gte
      required: true
    - as: domain.http.is_preflight_step
      from: assert.function
      path: /domain.http.is_preflight_step
      required: true
    - as: domain.http.step_by_id
      from: assert.function
      path: /domain.http.step_by_id
      required: true
    - as: domain.http.step_status_is
      from: assert.function
      path: /domain.http.step_status_is
      required: true
    - as: domain.http.step_body_json_get
      from: assert.function
      path: /domain.http.step_body_json_get
      required: true
    - as: domain.http.status
      from: assert.function
      path: /domain.http.status
      required: true
    - as: domain.http.status_in
      from: assert.function
      path: /domain.http.status_in
      required: true
    - as: domain.http.status_is
      from: assert.function
      path: /domain.http.status_is
      required: true
    - as: domain.http.status_is_unauthorized
      from: assert.function
      path: /domain.http.status_is_unauthorized
      required: true
    - as: domain.http.status_is_forbidden
      from: assert.function
      path: /domain.http.status_is_forbidden
      required: true
    - as: domain.http.ok_2xx
      from: assert.function
      path: /domain.http.ok_2xx
      required: true
    - as: domain.http.header_get
      from: assert.function
      path: /domain.http.header_get
      required: true
    - as: domain.http.header_contains
      from: assert.function
      path: /domain.http.header_contains
      required: true
    - as: domain.http.body_text
      from: assert.function
      path: /domain.http.body_text
      required: true
    - as: domain.http.body_json
      from: assert.function
      path: /domain.http.body_json
      required: true
    - as: domain.http.body_json_type_is
      from: assert.function
      path: /domain.http.body_json_type_is
      required: true
    - as: domain.http.body_json_has_key
      from: assert.function
      path: /domain.http.body_json_has_key
      required: true
    - as: domain.http.auth_is_oauth
      from: assert.function
      path: /domain.http.auth_is_oauth
      required: true
    - as: domain.http.has_bearer_header
      from: assert.function
      path: /domain.http.has_bearer_header
      required: true
    - as: domain.http.oauth_scope_requested
      from: assert.function
      path: /domain.http.oauth_scope_requested
      required: true
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-017-DOMAIN-HTTP-CORS-ALLOWS-METHOD
title: 'http projection helper functions: domain.http.cors_allows_method'
type: spec_lang.export
defines:
  public:
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
  private: {}
harness:
  chain:
    exports:
    - as: domain.http.cors_allow_origin
      from: assert.function
      path: /domain.http.cors_allow_origin
      required: true
    - as: domain.http.cors_allows_method
      from: assert.function
      path: /domain.http.cors_allows_method
      required: true
    - as: domain.http.cors_allows_header
      from: assert.function
      path: /domain.http.cors_allows_header
      required: true
    - as: domain.http.cors_credentials_enabled
      from: assert.function
      path: /domain.http.cors_credentials_enabled
      required: true
    - as: domain.http.cors_max_age_gte
      from: assert.function
      path: /domain.http.cors_max_age_gte
      required: true
    - as: domain.http.is_preflight_step
      from: assert.function
      path: /domain.http.is_preflight_step
      required: true
    - as: domain.http.step_by_id
      from: assert.function
      path: /domain.http.step_by_id
      required: true
    - as: domain.http.step_status_is
      from: assert.function
      path: /domain.http.step_status_is
      required: true
    - as: domain.http.step_body_json_get
      from: assert.function
      path: /domain.http.step_body_json_get
      required: true
    - as: domain.http.status
      from: assert.function
      path: /domain.http.status
      required: true
    - as: domain.http.status_in
      from: assert.function
      path: /domain.http.status_in
      required: true
    - as: domain.http.status_is
      from: assert.function
      path: /domain.http.status_is
      required: true
    - as: domain.http.status_is_unauthorized
      from: assert.function
      path: /domain.http.status_is_unauthorized
      required: true
    - as: domain.http.status_is_forbidden
      from: assert.function
      path: /domain.http.status_is_forbidden
      required: true
    - as: domain.http.ok_2xx
      from: assert.function
      path: /domain.http.ok_2xx
      required: true
    - as: domain.http.header_get
      from: assert.function
      path: /domain.http.header_get
      required: true
    - as: domain.http.header_contains
      from: assert.function
      path: /domain.http.header_contains
      required: true
    - as: domain.http.body_text
      from: assert.function
      path: /domain.http.body_text
      required: true
    - as: domain.http.body_json
      from: assert.function
      path: /domain.http.body_json
      required: true
    - as: domain.http.body_json_type_is
      from: assert.function
      path: /domain.http.body_json_type_is
      required: true
    - as: domain.http.body_json_has_key
      from: assert.function
      path: /domain.http.body_json_has_key
      required: true
    - as: domain.http.auth_is_oauth
      from: assert.function
      path: /domain.http.auth_is_oauth
      required: true
    - as: domain.http.has_bearer_header
      from: assert.function
      path: /domain.http.has_bearer_header
      required: true
    - as: domain.http.oauth_scope_requested
      from: assert.function
      path: /domain.http.oauth_scope_requested
      required: true
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-018-DOMAIN-HTTP-CORS-ALLOWS-HEADER
title: 'http projection helper functions: domain.http.cors_allows_header'
type: spec_lang.export
defines:
  public:
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
  private: {}
harness:
  chain:
    exports:
    - as: domain.http.cors_allow_origin
      from: assert.function
      path: /domain.http.cors_allow_origin
      required: true
    - as: domain.http.cors_allows_method
      from: assert.function
      path: /domain.http.cors_allows_method
      required: true
    - as: domain.http.cors_allows_header
      from: assert.function
      path: /domain.http.cors_allows_header
      required: true
    - as: domain.http.cors_credentials_enabled
      from: assert.function
      path: /domain.http.cors_credentials_enabled
      required: true
    - as: domain.http.cors_max_age_gte
      from: assert.function
      path: /domain.http.cors_max_age_gte
      required: true
    - as: domain.http.is_preflight_step
      from: assert.function
      path: /domain.http.is_preflight_step
      required: true
    - as: domain.http.step_by_id
      from: assert.function
      path: /domain.http.step_by_id
      required: true
    - as: domain.http.step_status_is
      from: assert.function
      path: /domain.http.step_status_is
      required: true
    - as: domain.http.step_body_json_get
      from: assert.function
      path: /domain.http.step_body_json_get
      required: true
    - as: domain.http.status
      from: assert.function
      path: /domain.http.status
      required: true
    - as: domain.http.status_in
      from: assert.function
      path: /domain.http.status_in
      required: true
    - as: domain.http.status_is
      from: assert.function
      path: /domain.http.status_is
      required: true
    - as: domain.http.status_is_unauthorized
      from: assert.function
      path: /domain.http.status_is_unauthorized
      required: true
    - as: domain.http.status_is_forbidden
      from: assert.function
      path: /domain.http.status_is_forbidden
      required: true
    - as: domain.http.ok_2xx
      from: assert.function
      path: /domain.http.ok_2xx
      required: true
    - as: domain.http.header_get
      from: assert.function
      path: /domain.http.header_get
      required: true
    - as: domain.http.header_contains
      from: assert.function
      path: /domain.http.header_contains
      required: true
    - as: domain.http.body_text
      from: assert.function
      path: /domain.http.body_text
      required: true
    - as: domain.http.body_json
      from: assert.function
      path: /domain.http.body_json
      required: true
    - as: domain.http.body_json_type_is
      from: assert.function
      path: /domain.http.body_json_type_is
      required: true
    - as: domain.http.body_json_has_key
      from: assert.function
      path: /domain.http.body_json_has_key
      required: true
    - as: domain.http.auth_is_oauth
      from: assert.function
      path: /domain.http.auth_is_oauth
      required: true
    - as: domain.http.has_bearer_header
      from: assert.function
      path: /domain.http.has_bearer_header
      required: true
    - as: domain.http.oauth_scope_requested
      from: assert.function
      path: /domain.http.oauth_scope_requested
      required: true
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-019-DOMAIN-HTTP-CORS-CREDENTIALS-ENABLED
title: 'http projection helper functions: domain.http.cors_credentials_enabled'
type: spec_lang.export
defines:
  public:
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
  private: {}
harness:
  chain:
    exports:
    - as: domain.http.cors_allow_origin
      from: assert.function
      path: /domain.http.cors_allow_origin
      required: true
    - as: domain.http.cors_allows_method
      from: assert.function
      path: /domain.http.cors_allows_method
      required: true
    - as: domain.http.cors_allows_header
      from: assert.function
      path: /domain.http.cors_allows_header
      required: true
    - as: domain.http.cors_credentials_enabled
      from: assert.function
      path: /domain.http.cors_credentials_enabled
      required: true
    - as: domain.http.cors_max_age_gte
      from: assert.function
      path: /domain.http.cors_max_age_gte
      required: true
    - as: domain.http.is_preflight_step
      from: assert.function
      path: /domain.http.is_preflight_step
      required: true
    - as: domain.http.step_by_id
      from: assert.function
      path: /domain.http.step_by_id
      required: true
    - as: domain.http.step_status_is
      from: assert.function
      path: /domain.http.step_status_is
      required: true
    - as: domain.http.step_body_json_get
      from: assert.function
      path: /domain.http.step_body_json_get
      required: true
    - as: domain.http.status
      from: assert.function
      path: /domain.http.status
      required: true
    - as: domain.http.status_in
      from: assert.function
      path: /domain.http.status_in
      required: true
    - as: domain.http.status_is
      from: assert.function
      path: /domain.http.status_is
      required: true
    - as: domain.http.status_is_unauthorized
      from: assert.function
      path: /domain.http.status_is_unauthorized
      required: true
    - as: domain.http.status_is_forbidden
      from: assert.function
      path: /domain.http.status_is_forbidden
      required: true
    - as: domain.http.ok_2xx
      from: assert.function
      path: /domain.http.ok_2xx
      required: true
    - as: domain.http.header_get
      from: assert.function
      path: /domain.http.header_get
      required: true
    - as: domain.http.header_contains
      from: assert.function
      path: /domain.http.header_contains
      required: true
    - as: domain.http.body_text
      from: assert.function
      path: /domain.http.body_text
      required: true
    - as: domain.http.body_json
      from: assert.function
      path: /domain.http.body_json
      required: true
    - as: domain.http.body_json_type_is
      from: assert.function
      path: /domain.http.body_json_type_is
      required: true
    - as: domain.http.body_json_has_key
      from: assert.function
      path: /domain.http.body_json_has_key
      required: true
    - as: domain.http.auth_is_oauth
      from: assert.function
      path: /domain.http.auth_is_oauth
      required: true
    - as: domain.http.has_bearer_header
      from: assert.function
      path: /domain.http.has_bearer_header
      required: true
    - as: domain.http.oauth_scope_requested
      from: assert.function
      path: /domain.http.oauth_scope_requested
      required: true
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-020-DOMAIN-HTTP-CORS-MAX-AGE-GTE
title: 'http projection helper functions: domain.http.cors_max_age_gte'
type: spec_lang.export
defines:
  public:
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
  private: {}
harness:
  chain:
    exports:
    - as: domain.http.cors_allow_origin
      from: assert.function
      path: /domain.http.cors_allow_origin
      required: true
    - as: domain.http.cors_allows_method
      from: assert.function
      path: /domain.http.cors_allows_method
      required: true
    - as: domain.http.cors_allows_header
      from: assert.function
      path: /domain.http.cors_allows_header
      required: true
    - as: domain.http.cors_credentials_enabled
      from: assert.function
      path: /domain.http.cors_credentials_enabled
      required: true
    - as: domain.http.cors_max_age_gte
      from: assert.function
      path: /domain.http.cors_max_age_gte
      required: true
    - as: domain.http.is_preflight_step
      from: assert.function
      path: /domain.http.is_preflight_step
      required: true
    - as: domain.http.step_by_id
      from: assert.function
      path: /domain.http.step_by_id
      required: true
    - as: domain.http.step_status_is
      from: assert.function
      path: /domain.http.step_status_is
      required: true
    - as: domain.http.step_body_json_get
      from: assert.function
      path: /domain.http.step_body_json_get
      required: true
    - as: domain.http.status
      from: assert.function
      path: /domain.http.status
      required: true
    - as: domain.http.status_in
      from: assert.function
      path: /domain.http.status_in
      required: true
    - as: domain.http.status_is
      from: assert.function
      path: /domain.http.status_is
      required: true
    - as: domain.http.status_is_unauthorized
      from: assert.function
      path: /domain.http.status_is_unauthorized
      required: true
    - as: domain.http.status_is_forbidden
      from: assert.function
      path: /domain.http.status_is_forbidden
      required: true
    - as: domain.http.ok_2xx
      from: assert.function
      path: /domain.http.ok_2xx
      required: true
    - as: domain.http.header_get
      from: assert.function
      path: /domain.http.header_get
      required: true
    - as: domain.http.header_contains
      from: assert.function
      path: /domain.http.header_contains
      required: true
    - as: domain.http.body_text
      from: assert.function
      path: /domain.http.body_text
      required: true
    - as: domain.http.body_json
      from: assert.function
      path: /domain.http.body_json
      required: true
    - as: domain.http.body_json_type_is
      from: assert.function
      path: /domain.http.body_json_type_is
      required: true
    - as: domain.http.body_json_has_key
      from: assert.function
      path: /domain.http.body_json_has_key
      required: true
    - as: domain.http.auth_is_oauth
      from: assert.function
      path: /domain.http.auth_is_oauth
      required: true
    - as: domain.http.has_bearer_header
      from: assert.function
      path: /domain.http.has_bearer_header
      required: true
    - as: domain.http.oauth_scope_requested
      from: assert.function
      path: /domain.http.oauth_scope_requested
      required: true
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-021-DOMAIN-HTTP-IS-PREFLIGHT-STEP
title: 'http projection helper functions: domain.http.is_preflight_step'
type: spec_lang.export
defines:
  public:
    domain.http.is_preflight_step:
      fn:
      - [step]
      - std.logic.eq:
        - std.object.get:
          - {var: step}
          - method
        - OPTIONS
  private: {}
harness:
  chain:
    exports:
    - as: domain.http.cors_allow_origin
      from: assert.function
      path: /domain.http.cors_allow_origin
      required: true
    - as: domain.http.cors_allows_method
      from: assert.function
      path: /domain.http.cors_allows_method
      required: true
    - as: domain.http.cors_allows_header
      from: assert.function
      path: /domain.http.cors_allows_header
      required: true
    - as: domain.http.cors_credentials_enabled
      from: assert.function
      path: /domain.http.cors_credentials_enabled
      required: true
    - as: domain.http.cors_max_age_gte
      from: assert.function
      path: /domain.http.cors_max_age_gte
      required: true
    - as: domain.http.is_preflight_step
      from: assert.function
      path: /domain.http.is_preflight_step
      required: true
    - as: domain.http.step_by_id
      from: assert.function
      path: /domain.http.step_by_id
      required: true
    - as: domain.http.step_status_is
      from: assert.function
      path: /domain.http.step_status_is
      required: true
    - as: domain.http.step_body_json_get
      from: assert.function
      path: /domain.http.step_body_json_get
      required: true
    - as: domain.http.status
      from: assert.function
      path: /domain.http.status
      required: true
    - as: domain.http.status_in
      from: assert.function
      path: /domain.http.status_in
      required: true
    - as: domain.http.status_is
      from: assert.function
      path: /domain.http.status_is
      required: true
    - as: domain.http.status_is_unauthorized
      from: assert.function
      path: /domain.http.status_is_unauthorized
      required: true
    - as: domain.http.status_is_forbidden
      from: assert.function
      path: /domain.http.status_is_forbidden
      required: true
    - as: domain.http.ok_2xx
      from: assert.function
      path: /domain.http.ok_2xx
      required: true
    - as: domain.http.header_get
      from: assert.function
      path: /domain.http.header_get
      required: true
    - as: domain.http.header_contains
      from: assert.function
      path: /domain.http.header_contains
      required: true
    - as: domain.http.body_text
      from: assert.function
      path: /domain.http.body_text
      required: true
    - as: domain.http.body_json
      from: assert.function
      path: /domain.http.body_json
      required: true
    - as: domain.http.body_json_type_is
      from: assert.function
      path: /domain.http.body_json_type_is
      required: true
    - as: domain.http.body_json_has_key
      from: assert.function
      path: /domain.http.body_json_has_key
      required: true
    - as: domain.http.auth_is_oauth
      from: assert.function
      path: /domain.http.auth_is_oauth
      required: true
    - as: domain.http.has_bearer_header
      from: assert.function
      path: /domain.http.has_bearer_header
      required: true
    - as: domain.http.oauth_scope_requested
      from: assert.function
      path: /domain.http.oauth_scope_requested
      required: true
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-022-DOMAIN-HTTP-STEP-BY-ID
title: 'http projection helper functions: domain.http.step_by_id'
type: spec_lang.export
defines:
  public:
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
  private: {}
harness:
  chain:
    exports:
    - as: domain.http.cors_allow_origin
      from: assert.function
      path: /domain.http.cors_allow_origin
      required: true
    - as: domain.http.cors_allows_method
      from: assert.function
      path: /domain.http.cors_allows_method
      required: true
    - as: domain.http.cors_allows_header
      from: assert.function
      path: /domain.http.cors_allows_header
      required: true
    - as: domain.http.cors_credentials_enabled
      from: assert.function
      path: /domain.http.cors_credentials_enabled
      required: true
    - as: domain.http.cors_max_age_gte
      from: assert.function
      path: /domain.http.cors_max_age_gte
      required: true
    - as: domain.http.is_preflight_step
      from: assert.function
      path: /domain.http.is_preflight_step
      required: true
    - as: domain.http.step_by_id
      from: assert.function
      path: /domain.http.step_by_id
      required: true
    - as: domain.http.step_status_is
      from: assert.function
      path: /domain.http.step_status_is
      required: true
    - as: domain.http.step_body_json_get
      from: assert.function
      path: /domain.http.step_body_json_get
      required: true
    - as: domain.http.status
      from: assert.function
      path: /domain.http.status
      required: true
    - as: domain.http.status_in
      from: assert.function
      path: /domain.http.status_in
      required: true
    - as: domain.http.status_is
      from: assert.function
      path: /domain.http.status_is
      required: true
    - as: domain.http.status_is_unauthorized
      from: assert.function
      path: /domain.http.status_is_unauthorized
      required: true
    - as: domain.http.status_is_forbidden
      from: assert.function
      path: /domain.http.status_is_forbidden
      required: true
    - as: domain.http.ok_2xx
      from: assert.function
      path: /domain.http.ok_2xx
      required: true
    - as: domain.http.header_get
      from: assert.function
      path: /domain.http.header_get
      required: true
    - as: domain.http.header_contains
      from: assert.function
      path: /domain.http.header_contains
      required: true
    - as: domain.http.body_text
      from: assert.function
      path: /domain.http.body_text
      required: true
    - as: domain.http.body_json
      from: assert.function
      path: /domain.http.body_json
      required: true
    - as: domain.http.body_json_type_is
      from: assert.function
      path: /domain.http.body_json_type_is
      required: true
    - as: domain.http.body_json_has_key
      from: assert.function
      path: /domain.http.body_json_has_key
      required: true
    - as: domain.http.auth_is_oauth
      from: assert.function
      path: /domain.http.auth_is_oauth
      required: true
    - as: domain.http.has_bearer_header
      from: assert.function
      path: /domain.http.has_bearer_header
      required: true
    - as: domain.http.oauth_scope_requested
      from: assert.function
      path: /domain.http.oauth_scope_requested
      required: true
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-023-DOMAIN-HTTP-STEP-STATUS-IS
title: 'http projection helper functions: domain.http.step_status_is'
type: spec_lang.export
defines:
  public:
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
  private: {}
harness:
  chain:
    exports:
    - as: domain.http.cors_allow_origin
      from: assert.function
      path: /domain.http.cors_allow_origin
      required: true
    - as: domain.http.cors_allows_method
      from: assert.function
      path: /domain.http.cors_allows_method
      required: true
    - as: domain.http.cors_allows_header
      from: assert.function
      path: /domain.http.cors_allows_header
      required: true
    - as: domain.http.cors_credentials_enabled
      from: assert.function
      path: /domain.http.cors_credentials_enabled
      required: true
    - as: domain.http.cors_max_age_gte
      from: assert.function
      path: /domain.http.cors_max_age_gte
      required: true
    - as: domain.http.is_preflight_step
      from: assert.function
      path: /domain.http.is_preflight_step
      required: true
    - as: domain.http.step_by_id
      from: assert.function
      path: /domain.http.step_by_id
      required: true
    - as: domain.http.step_status_is
      from: assert.function
      path: /domain.http.step_status_is
      required: true
    - as: domain.http.step_body_json_get
      from: assert.function
      path: /domain.http.step_body_json_get
      required: true
    - as: domain.http.status
      from: assert.function
      path: /domain.http.status
      required: true
    - as: domain.http.status_in
      from: assert.function
      path: /domain.http.status_in
      required: true
    - as: domain.http.status_is
      from: assert.function
      path: /domain.http.status_is
      required: true
    - as: domain.http.status_is_unauthorized
      from: assert.function
      path: /domain.http.status_is_unauthorized
      required: true
    - as: domain.http.status_is_forbidden
      from: assert.function
      path: /domain.http.status_is_forbidden
      required: true
    - as: domain.http.ok_2xx
      from: assert.function
      path: /domain.http.ok_2xx
      required: true
    - as: domain.http.header_get
      from: assert.function
      path: /domain.http.header_get
      required: true
    - as: domain.http.header_contains
      from: assert.function
      path: /domain.http.header_contains
      required: true
    - as: domain.http.body_text
      from: assert.function
      path: /domain.http.body_text
      required: true
    - as: domain.http.body_json
      from: assert.function
      path: /domain.http.body_json
      required: true
    - as: domain.http.body_json_type_is
      from: assert.function
      path: /domain.http.body_json_type_is
      required: true
    - as: domain.http.body_json_has_key
      from: assert.function
      path: /domain.http.body_json_has_key
      required: true
    - as: domain.http.auth_is_oauth
      from: assert.function
      path: /domain.http.auth_is_oauth
      required: true
    - as: domain.http.has_bearer_header
      from: assert.function
      path: /domain.http.has_bearer_header
      required: true
    - as: domain.http.oauth_scope_requested
      from: assert.function
      path: /domain.http.oauth_scope_requested
      required: true
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-024-DOMAIN-HTTP-STEP-BODY-JSON-GET
title: 'http projection helper functions: domain.http.step_body_json_get'
type: spec_lang.export
defines:
  public:
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
  private: {}
harness:
  chain:
    exports:
    - as: domain.http.cors_allow_origin
      from: assert.function
      path: /domain.http.cors_allow_origin
      required: true
    - as: domain.http.cors_allows_method
      from: assert.function
      path: /domain.http.cors_allows_method
      required: true
    - as: domain.http.cors_allows_header
      from: assert.function
      path: /domain.http.cors_allows_header
      required: true
    - as: domain.http.cors_credentials_enabled
      from: assert.function
      path: /domain.http.cors_credentials_enabled
      required: true
    - as: domain.http.cors_max_age_gte
      from: assert.function
      path: /domain.http.cors_max_age_gte
      required: true
    - as: domain.http.is_preflight_step
      from: assert.function
      path: /domain.http.is_preflight_step
      required: true
    - as: domain.http.step_by_id
      from: assert.function
      path: /domain.http.step_by_id
      required: true
    - as: domain.http.step_status_is
      from: assert.function
      path: /domain.http.step_status_is
      required: true
    - as: domain.http.step_body_json_get
      from: assert.function
      path: /domain.http.step_body_json_get
      required: true
    - as: domain.http.status
      from: assert.function
      path: /domain.http.status
      required: true
    - as: domain.http.status_in
      from: assert.function
      path: /domain.http.status_in
      required: true
    - as: domain.http.status_is
      from: assert.function
      path: /domain.http.status_is
      required: true
    - as: domain.http.status_is_unauthorized
      from: assert.function
      path: /domain.http.status_is_unauthorized
      required: true
    - as: domain.http.status_is_forbidden
      from: assert.function
      path: /domain.http.status_is_forbidden
      required: true
    - as: domain.http.ok_2xx
      from: assert.function
      path: /domain.http.ok_2xx
      required: true
    - as: domain.http.header_get
      from: assert.function
      path: /domain.http.header_get
      required: true
    - as: domain.http.header_contains
      from: assert.function
      path: /domain.http.header_contains
      required: true
    - as: domain.http.body_text
      from: assert.function
      path: /domain.http.body_text
      required: true
    - as: domain.http.body_json
      from: assert.function
      path: /domain.http.body_json
      required: true
    - as: domain.http.body_json_type_is
      from: assert.function
      path: /domain.http.body_json_type_is
      required: true
    - as: domain.http.body_json_has_key
      from: assert.function
      path: /domain.http.body_json_has_key
      required: true
    - as: domain.http.auth_is_oauth
      from: assert.function
      path: /domain.http.auth_is_oauth
      required: true
    - as: domain.http.has_bearer_header
      from: assert.function
      path: /domain.http.has_bearer_header
      required: true
    - as: domain.http.oauth_scope_requested
      from: assert.function
      path: /domain.http.oauth_scope_requested
      required: true
```
