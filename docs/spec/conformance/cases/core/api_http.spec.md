# API HTTP Conformance Fixtures

## SRCONF-API-001

```yaml contract-spec
id: SRCONF-API-001
title: api.http GET reads relative fixture and exposes body assertions
purpose: Verifies api.http can resolve a local relative request url and assert deterministic
  status and json body shape.
type: api.http
requires:
  capabilities:
  - api.http
expect:
  portable:
    status: pass
    category: null
request:
  method: GET
  url: /docs/spec/conformance/cases/fixtures/api_http_ok.json
contract:
- id: assert_1
  class: must
  asserts:
  - std.string.contains:
    - var: subject
    - '200'
  target: status
- id: assert_2
  class: must
  asserts:
  - std.type.json_type:
    - var: subject
    - dict
  target: body_json
```

## SRCONF-API-002

```yaml contract-spec
id: SRCONF-API-002
title: api.http requires request.url
purpose: Verifies api.http reports a schema violation when request url is missing
  from portable fixture input.
type: api.http
requires:
  capabilities:
  - api.http
expect:
  portable:
    status: fail
    category: schema
    message_tokens:
    - api.http request.url is required
request:
  method: GET
contract:
- id: assert_1
  class: must
  asserts:
  - std.string.contains:
    - var: subject
    - '200'
  target: status
```

## SRCONF-API-003

```yaml contract-spec
id: SRCONF-API-003
title: api.http skip path honors requires.when_missing
purpose: Verifies extension capability gating can skip fixtures when a required capability
  is absent.
type: api.http
requires:
  capabilities:
  - api.http
  - api.http.missing
  when_missing: skip
expect:
  portable:
    status: skip
    category: null
request:
  method: GET
  url: /docs/spec/conformance/cases/fixtures/api_http_ok.json
contract:
- id: assert_1
  class: must
  asserts:
  - std.string.contains:
    - var: subject
    - '200'
  target: status
```

## SRCONF-API-004

```yaml contract-spec
id: SRCONF-API-004
title: api.http supports POST with body_json
purpose: Verifies practical REST mutating verb support for POST requests in deterministic
  mode.
type: api.http
requires:
  capabilities:
  - api.http
expect:
  portable:
    status: pass
    category: null
request:
  method: POST
  url: /docs/spec/conformance/cases/fixtures/api_http_created.json
  body_json:
    name: sample
contract:
- id: assert_1
  class: must
  asserts:
  - std.object.has_key:
    - var: subject
    - id
  target: body_json
```

## SRCONF-API-005

```yaml contract-spec
id: SRCONF-API-005
title: api.http supports PUT
purpose: Verifies practical REST verb support for PUT in deterministic mode.
type: api.http
requires:
  capabilities:
  - api.http
expect:
  portable:
    status: pass
    category: null
request:
  method: PUT
  url: /docs/spec/conformance/cases/fixtures/api_http_item_abc-123.json
contract:
- id: assert_1
  class: must
  asserts:
  - std.string.contains:
    - var: subject
    - '200'
  target: status
```

## SRCONF-API-006

```yaml contract-spec
id: SRCONF-API-006
title: api.http supports PATCH
purpose: Verifies practical REST verb support for PATCH in deterministic mode.
type: api.http
requires:
  capabilities:
  - api.http
expect:
  portable:
    status: pass
    category: null
request:
  method: PATCH
  url: /docs/spec/conformance/cases/fixtures/api_http_item_abc-123.json
contract:
- id: assert_1
  class: must
  asserts:
  - std.string.contains:
    - var: subject
    - abc-123
  target: body_text
```

## SRCONF-API-007

```yaml contract-spec
id: SRCONF-API-007
title: api.http supports DELETE
purpose: Verifies practical REST verb support for DELETE in deterministic mode.
type: api.http
requires:
  capabilities:
  - api.http
expect:
  portable:
    status: pass
    category: null
request:
  method: DELETE
  url: /docs/spec/conformance/cases/fixtures/api_http_deleted.json
contract:
- id: assert_1
  class: must
  asserts:
  - std.logic.eq:
    - std.object.get:
      - var: subject
      - deleted
    - true
  target: body_json
```

## SRCONF-API-008

```yaml contract-spec
id: SRCONF-API-008
title: api.http supports HEAD
purpose: Verifies practical REST verb support for HEAD in deterministic mode.
type: api.http
requires:
  capabilities:
  - api.http
expect:
  portable:
    status: pass
    category: null
request:
  method: HEAD
  url: /docs/spec/conformance/cases/fixtures/api_http_ok.json
contract:
- id: assert_1
  class: must
  asserts:
  - std.string.contains:
    - var: subject
    - '200'
  target: status
```

## SRCONF-API-009

```yaml contract-spec
id: SRCONF-API-009
title: api.http supports OPTIONS
purpose: Verifies practical REST verb support for OPTIONS in deterministic mode.
type: api.http
requires:
  capabilities:
  - api.http
expect:
  portable:
    status: pass
    category: null
request:
  method: OPTIONS
  url: /docs/spec/conformance/cases/fixtures/api_http_ok.json
contract:
- id: assert_1
  class: must
  asserts:
  - std.string.contains:
    - var: subject
    - '200'
  target: status
```

## SRCONF-API-010

```yaml contract-spec
id: SRCONF-API-010
title: api.http rejects unsupported request method
purpose: Verifies unsupported HTTP verbs are rejected as schema violations.
type: api.http
requires:
  capabilities:
  - api.http
expect:
  portable:
    status: fail
    category: schema
    message_tokens:
    - request.method must be one of
request:
  method: TRACE
  url: /docs/spec/conformance/cases/fixtures/api_http_ok.json
contract:
- id: assert_1
  class: must
  asserts:
  - std.string.contains:
    - var: subject
    - '200'
  target: status
```

## SRCONF-API-011

```yaml contract-spec
id: SRCONF-API-011
title: api.http preflight requires OPTIONS method
purpose: Verifies cors preflight helper enforces request.method OPTIONS.
type: api.http
requires:
  capabilities:
  - api.http
expect:
  portable:
    status: fail
    category: schema
    message_tokens:
    - request.cors.preflight requires request.method OPTIONS
request:
  method: GET
  url: /docs/spec/conformance/cases/fixtures/api_http_ok.json
  cors:
    preflight: true
    origin: https://client.example
    request_method: POST
contract:
- id: assert_1
  class: must
  asserts:
  - std.string.contains:
    - var: subject
    - '200'
  target: status
```

## SRCONF-API-012

```yaml contract-spec
id: SRCONF-API-012
title: api.http scenario executes round-trip requests in order
purpose: Verifies requests scenario supports step templating and exposes steps_json
  target.
type: api.http
requires:
  capabilities:
  - api.http
expect:
  portable:
    status: pass
    category: null
harness:
  api_http:
    scenario:
      fail_fast: true
requests:
- id: create
  method: POST
  url: /docs/spec/conformance/cases/fixtures/api_http_created.json
- id: get
  method: GET
  url: /docs/spec/conformance/cases/fixtures/api_http_item_{{steps.create.body_json.id}}.json
- id: cleanup
  method: DELETE
  url: /docs/spec/conformance/cases/fixtures/api_http_deleted.json
contract:
- id: assert_1
  class: must
  asserts:
  - std.string.contains:
    - var: subject
    - '200'
  target: status
- id: assert_2
  class: must
  asserts:
  - std.logic.eq:
    - std.collection.len:
      - var: subject
    - 3
  target: steps_json
```

## SRCONF-API-013

```yaml contract-spec
id: SRCONF-API-013
title: api.http oauth deterministic local token exchange
purpose: Verifies oauth auth profile resolves env refs and produces oauth context
  metadata without network access.
type: api.http
requires:
  capabilities:
  - api.http
expect:
  portable:
    status: pass
    category: null
harness:
  api_http:
    mode: deterministic
    auth:
      oauth:
        grant_type: client_credentials
        token_url: /docs/spec/conformance/cases/fixtures/oauth_token_ok.json
        client_id_env: PATH
        client_secret_env: HOME
        scope: read:spec
request:
  method: GET
  url: /docs/spec/conformance/cases/fixtures/api_http_ok.json
contract:
- id: assert_1
  class: must
  asserts:
  - must:
    - std.logic.eq:
      - std.object.get:
        - std.object.get:
          - var: subject
          - meta
        - auth_mode
      - oauth
    - std.logic.eq:
      - std.object.get:
        - std.object.get:
          - var: subject
          - meta
        - oauth_token_source
      - env_ref
  target: context_json
```

## SRCONF-API-014

```yaml contract-spec
id: SRCONF-API-014
title: api.http oauth missing env refs is schema failure
purpose: Verifies oauth env-ref credentials are required and missing env vars fail
  as schema.
type: api.http
requires:
  capabilities:
  - api.http
expect:
  portable:
    status: fail
    category: schema
    message_tokens:
    - oauth env var is required
harness:
  api_http:
    auth:
      oauth:
        grant_type: client_credentials
        token_url: /docs/spec/conformance/cases/fixtures/oauth_token_ok.json
        client_id_env: SPEC_RUNNER_OAUTH_MISSING_CLIENT_ID
        client_secret_env: SPEC_RUNNER_OAUTH_MISSING_CLIENT_SECRET
request:
  method: GET
  url: /docs/spec/conformance/cases/fixtures/api_http_ok.json
contract:
- id: assert_1
  class: must
  asserts:
  - std.string.contains:
    - var: subject
    - '200'
  target: status
```

## SRCONF-API-015

```yaml contract-spec
id: SRCONF-API-015
title: api.http oauth invalid auth_style is schema failure
purpose: Verifies oauth auth_style is validated against supported values.
type: api.http
requires:
  capabilities:
  - api.http
expect:
  portable:
    status: fail
    category: schema
    message_tokens:
    - auth_style
harness:
  api_http:
    auth:
      oauth:
        grant_type: client_credentials
        token_url: /docs/spec/conformance/cases/fixtures/oauth_token_ok.json
        client_id_env: PATH
        client_secret_env: HOME
        auth_style: token
request:
  method: GET
  url: /docs/spec/conformance/cases/fixtures/api_http_ok.json
contract:
- id: assert_1
  class: must
  asserts:
  - std.string.contains:
    - var: subject
    - '200'
  target: status
```

## SRCONF-API-016

```yaml contract-spec
id: SRCONF-API-016
title: api.http oauth live mode is optional capability
type: api.http
purpose: Verifies optional live oauth/network execution can be capability-gated and
  skipped in portable lanes.
requires:
  capabilities:
  - api.http
  - api.http.oauth.live
  when_missing: skip
expect:
  portable:
    status: skip
    category: null
harness:
  api_http:
    mode: live
    auth:
      oauth:
        grant_type: client_credentials
        token_url: https://issuer.example.invalid/oauth/token
        client_id_env: OAUTH_CLIENT_ID
        client_secret_env: OAUTH_CLIENT_SECRET
request:
  method: GET
  url: https://api.example.invalid/items
contract:
- id: assert_1
  class: must
  asserts:
  - std.string.contains:
    - var: subject
    - '200'
  target: status
```

## SRCONF-API-017

```yaml contract-spec
id: SRCONF-API-017
title: api.http exposes new domain.http helper exports for CORS and steps
purpose: Maintains reference usage for domain.http CORS and scenario helper symbol
  exports.
type: api.http
requires:
  capabilities:
  - api.http
  - api.http.domain_lib_refs
  when_missing: skip
expect:
  portable:
    status: skip
    category: null
harness:
  chain:
    steps:
    - id: lib_http_core_spec
      class: must
      ref: /docs/spec/libraries/domain/http_core.spec.md
    imports:
    - from: lib_http_core_spec
      names:
      - domain.http.cors_allow_origin
      - domain.http.cors_allows_header
      - domain.http.cors_allows_method
      - domain.http.cors_credentials_enabled
      - domain.http.cors_max_age_gte
      - domain.http.is_preflight_step
      - domain.http.step_body_json_get
      - domain.http.step_by_id
      - domain.http.step_status_is
request:
  method: GET
  url: /docs/spec/conformance/cases/fixtures/api_http_ok.json
contract:
- id: assert_1
  class: must
  asserts:
  - std.string.contains:
    - var: subject
    - '200'
  target: status
```
