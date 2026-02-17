# Spec-Lang HTTP Domain Library

## LIB-DOMAIN-HTTP-001

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-001-DOMAIN-HTTP-STATUS
type: spec.export
assert:
- id: __export__domain.http.status
  class: must
  checks:
  - std.object.get:
    - std.object.get:
      - var: subject
      - value
    - status
harness:
  chain:
    exports:
    - as: domain.http.status
      from: assert.function
      path: /__export__domain.http.status
      params:
      - subject
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-002-DOMAIN-HTTP-STATUS-IN
type: spec.export
assert:
- id: __export__domain.http.status_in
  class: must
  checks:
  - std.collection.in:
    - std.object.get:
      - std.object.get:
        - var: subject
        - value
      - status
    - var: allowed
harness:
  chain:
    exports:
    - as: domain.http.status_in
      from: assert.function
      path: /__export__domain.http.status_in
      params:
      - subject
      - allowed
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-003-DOMAIN-HTTP-STATUS-IS
type: spec.export
assert:
- id: __export__domain.http.status_is
  class: must
  checks:
  - std.logic.eq:
    - std.object.get:
      - std.object.get:
        - var: subject
        - value
      - status
    - var: expected
harness:
  chain:
    exports:
    - as: domain.http.status_is
      from: assert.function
      path: /__export__domain.http.status_is
      params:
      - subject
      - expected
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-004-DOMAIN-HTTP-STATUS-IS-UNAUTHORIZED
type: spec.export
assert:
- id: __export__domain.http.status_is_unauthorized
  class: must
  checks:
  - call:
    - var: domain.http.status_is
    - var: subject
    - 401
harness:
  chain:
    exports:
    - as: domain.http.status_is_unauthorized
      from: assert.function
      path: /__export__domain.http.status_is_unauthorized
      params:
      - subject
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-005-DOMAIN-HTTP-STATUS-IS-FORBIDDEN
type: spec.export
assert:
- id: __export__domain.http.status_is_forbidden
  class: must
  checks:
  - call:
    - var: domain.http.status_is
    - var: subject
    - 403
harness:
  chain:
    exports:
    - as: domain.http.status_is_forbidden
      from: assert.function
      path: /__export__domain.http.status_is_forbidden
      params:
      - subject
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-006-DOMAIN-HTTP-OK-2XX
type: spec.export
assert:
- id: __export__domain.http.ok_2xx
  class: must
  checks:
  - std.logic.and:
    - std.logic.gte:
      - std.object.get:
        - std.object.get:
          - var: subject
          - value
        - status
      - 200
    - std.logic.lt:
      - std.object.get:
        - std.object.get:
          - var: subject
          - value
        - status
      - 300
harness:
  chain:
    exports:
    - as: domain.http.ok_2xx
      from: assert.function
      path: /__export__domain.http.ok_2xx
      params:
      - subject
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-007-DOMAIN-HTTP-HEADER-GET
type: spec.export
assert:
- id: __export__domain.http.header_get
  class: must
  checks:
  - std.object.get:
    - std.object.get:
      - std.object.get:
        - var: subject
        - value
      - headers
    - var: key
harness:
  chain:
    exports:
    - as: domain.http.header_get
      from: assert.function
      path: /__export__domain.http.header_get
      params:
      - subject
      - key
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-008-DOMAIN-HTTP-HEADER-CONTAINS
type: spec.export
assert:
- id: __export__domain.http.header_contains
  class: must
  checks:
  - std.string.contains:
    - std.object.get:
      - std.object.get:
        - std.object.get:
          - var: subject
          - value
        - headers
      - var: key
    - var: token
harness:
  chain:
    exports:
    - as: domain.http.header_contains
      from: assert.function
      path: /__export__domain.http.header_contains
      params:
      - subject
      - key
      - token
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-009-DOMAIN-HTTP-BODY-TEXT
type: spec.export
assert:
- id: __export__domain.http.body_text
  class: must
  checks:
  - std.object.get:
    - std.object.get:
      - var: subject
      - value
    - body_text
harness:
  chain:
    exports:
    - as: domain.http.body_text
      from: assert.function
      path: /__export__domain.http.body_text
      params:
      - subject
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-010-DOMAIN-HTTP-BODY-JSON
type: spec.export
assert:
- id: __export__domain.http.body_json
  class: must
  checks:
  - std.object.get:
    - std.object.get:
      - var: subject
      - value
    - body_json
harness:
  chain:
    exports:
    - as: domain.http.body_json
      from: assert.function
      path: /__export__domain.http.body_json
      params:
      - subject
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-011-DOMAIN-HTTP-BODY-JSON-TYPE-IS
type: spec.export
assert:
- id: __export__domain.http.body_json_type_is
  class: must
  checks:
  - std.type.json_type:
    - std.object.get:
      - std.object.get:
        - var: subject
        - value
      - body_json
    - var: expected_type
harness:
  chain:
    exports:
    - as: domain.http.body_json_type_is
      from: assert.function
      path: /__export__domain.http.body_json_type_is
      params:
      - subject
      - expected_type
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-012-DOMAIN-HTTP-BODY-JSON-HAS-KEY
type: spec.export
assert:
- id: __export__domain.http.body_json_has_key
  class: must
  checks:
  - std.object.has_key:
    - std.object.get:
      - std.object.get:
        - var: subject
        - value
      - body_json
    - var: key
harness:
  chain:
    exports:
    - as: domain.http.body_json_has_key
      from: assert.function
      path: /__export__domain.http.body_json_has_key
      params:
      - subject
      - key
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-013-DOMAIN-HTTP-AUTH-IS-OAUTH
type: spec.export
assert:
- id: __export__domain.http.auth_is_oauth
  class: must
  checks:
  - std.logic.eq:
    - std.object.get:
      - std.object.get:
        - var: subject
        - meta
      - auth_mode
    - oauth
harness:
  chain:
    exports:
    - as: domain.http.auth_is_oauth
      from: assert.function
      path: /__export__domain.http.auth_is_oauth
      params:
      - subject
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-014-DOMAIN-HTTP-HAS-BEARER-HEADER
type: spec.export
assert:
- id: __export__domain.http.has_bearer_header
  class: must
  checks:
  - std.string.starts_with:
    - std.object.get:
      - std.object.get:
        - std.object.get:
          - var: subject
          - value
        - headers
      - Authorization
    - 'Bearer '
harness:
  chain:
    exports:
    - as: domain.http.has_bearer_header
      from: assert.function
      path: /__export__domain.http.has_bearer_header
      params:
      - subject
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-015-DOMAIN-HTTP-OAUTH-SCOPE-REQUESTED
type: spec.export
assert:
- id: __export__domain.http.oauth_scope_requested
  class: must
  checks:
  - std.logic.neq:
    - std.object.get:
      - std.object.get:
        - std.object.get:
          - var: subject
          - context
        - oauth
      - scope_requested
    - null
harness:
  chain:
    exports:
    - as: domain.http.oauth_scope_requested
      from: assert.function
      path: /__export__domain.http.oauth_scope_requested
      params:
      - subject
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-016-DOMAIN-HTTP-CORS-ALLOW-ORIGIN
type: spec.export
assert:
- id: __export__domain.http.cors_allow_origin
  class: must
  checks:
  - std.object.get:
    - std.object.get:
      - std.object.get:
        - var: subject
        - value
      - cors
    - allow_origin
harness:
  chain:
    exports:
    - as: domain.http.cors_allow_origin
      from: assert.function
      path: /__export__domain.http.cors_allow_origin
      params:
      - subject
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-017-DOMAIN-HTTP-CORS-ALLOWS-METHOD
type: spec.export
assert:
- id: __export__domain.http.cors_allows_method
  class: must
  checks:
  - std.collection.includes:
    - std.object.get:
      - std.object.get:
        - std.object.get:
          - var: subject
          - value
        - cors
      - allow_methods
    - var: method_name
harness:
  chain:
    exports:
    - as: domain.http.cors_allows_method
      from: assert.function
      path: /__export__domain.http.cors_allows_method
      params:
      - subject
      - method_name
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-018-DOMAIN-HTTP-CORS-ALLOWS-HEADER
type: spec.export
assert:
- id: __export__domain.http.cors_allows_header
  class: must
  checks:
  - std.collection.includes:
    - std.object.get:
      - std.object.get:
        - std.object.get:
          - var: subject
          - value
        - cors
      - allow_headers
    - var: header_name
harness:
  chain:
    exports:
    - as: domain.http.cors_allows_header
      from: assert.function
      path: /__export__domain.http.cors_allows_header
      params:
      - subject
      - header_name
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-019-DOMAIN-HTTP-CORS-CREDENTIALS-ENABLED
type: spec.export
assert:
- id: __export__domain.http.cors_credentials_enabled
  class: must
  checks:
  - std.logic.eq:
    - std.object.get:
      - std.object.get:
        - std.object.get:
          - var: subject
          - value
        - cors
      - allow_credentials
    - true
harness:
  chain:
    exports:
    - as: domain.http.cors_credentials_enabled
      from: assert.function
      path: /__export__domain.http.cors_credentials_enabled
      params:
      - subject
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-020-DOMAIN-HTTP-CORS-MAX-AGE-GTE
type: spec.export
assert:
- id: __export__domain.http.cors_max_age_gte
  class: must
  checks:
  - std.logic.gte:
    - std.object.get:
      - std.object.get:
        - std.object.get:
          - var: subject
          - value
        - cors
      - max_age
    - var: min_age
harness:
  chain:
    exports:
    - as: domain.http.cors_max_age_gte
      from: assert.function
      path: /__export__domain.http.cors_max_age_gte
      params:
      - subject
      - min_age
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-021-DOMAIN-HTTP-IS-PREFLIGHT-STEP
type: spec.export
assert:
- id: __export__domain.http.is_preflight_step
  class: must
  checks:
  - std.logic.eq:
    - std.object.get:
      - var: step
      - method
    - OPTIONS
harness:
  chain:
    exports:
    - as: domain.http.is_preflight_step
      from: assert.function
      path: /__export__domain.http.is_preflight_step
      params:
      - step
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-022-DOMAIN-HTTP-STEP-BY-ID
type: spec.export
assert:
- id: __export__domain.http.step_by_id
  class: must
  checks:
  - std.collection.find:
    - fn:
      - - row
      - std.logic.eq:
        - std.object.get:
          - var: row
          - id
        - var: step_id
    - var: steps
harness:
  chain:
    exports:
    - as: domain.http.step_by_id
      from: assert.function
      path: /__export__domain.http.step_by_id
      params:
      - steps
      - step_id
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-023-DOMAIN-HTTP-STEP-STATUS-IS
type: spec.export
assert:
- id: __export__domain.http.step_status_is
  class: must
  checks:
  - std.logic.eq:
    - std.object.get:
      - call:
        - var: domain.http.step_by_id
        - var: steps
        - var: step_id
      - status
    - var: expected
harness:
  chain:
    exports:
    - as: domain.http.step_status_is
      from: assert.function
      path: /__export__domain.http.step_status_is
      params:
      - steps
      - step_id
      - expected
```

```yaml spec-test
id: LIB-DOMAIN-HTTP-001-024-DOMAIN-HTTP-STEP-BODY-JSON-GET
type: spec.export
assert:
- id: __export__domain.http.step_body_json_get
  class: must
  checks:
  - std.object.get:
    - std.object.get:
      - call:
        - var: domain.http.step_by_id
        - var: steps
        - var: step_id
      - body_json
    - var: field
harness:
  chain:
    exports:
    - as: domain.http.step_body_json_get
      from: assert.function
      path: /__export__domain.http.step_body_json_get
      params:
      - steps
      - step_id
      - field
```
