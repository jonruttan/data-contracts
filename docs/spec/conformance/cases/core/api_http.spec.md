# API HTTP Conformance Fixtures

## SRCONF-API-001

```yaml spec-test
id: SRCONF-API-001
title: api.http reads relative fixture and exposes body assertions
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
assert:
- target: status
  must:
  - evaluate:
    - std.string.contains:
      - {var: subject}
      - '200'
- target: body_text
  must:
  - evaluate:
    - std.string.contains:
      - {var: subject}
      - '"ok":true'
- target: body_json
  must:
  - evaluate:
    - std.type.json_type:
      - {var: subject}
      - dict
```

## SRCONF-API-002

```yaml spec-test
id: SRCONF-API-002
title: api.http requires request.url
purpose: Verifies api.http reports a schema violation when request url is missing from portable
  fixture input.
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
assert:
- target: status
  must:
  - evaluate:
    - std.string.contains:
      - {var: subject}
      - '200'
```

## SRCONF-API-003

```yaml spec-test
id: SRCONF-API-003
title: api.http skip path honors requires.when_missing
purpose: Verifies extension type capability gating can skip deterministic fixtures when an
  additional required capability is absent.
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
assert:
- target: status
  must:
  - evaluate:
    - std.string.contains:
      - {var: subject}
      - '200'
```

## SRCONF-API-004

```yaml spec-test
id: SRCONF-API-004
title: api.http oauth deterministic local token exchange
purpose: Verifies oauth auth profile resolves env refs and produces oauth context metadata
  without network access.
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
assert:
- target: status
  must:
  - evaluate:
    - std.string.contains:
      - {var: subject}
      - '200'
- target: context_json
  must:
  - evaluate:
    - std.logic.eq:
      - std.object.get:
        - std.object.get:
          - {var: subject}
          - meta
        - auth_mode
      - oauth
    - std.logic.eq:
      - std.object.get:
        - std.object.get:
          - {var: subject}
          - meta
        - oauth_token_source
      - env_ref
    - std.logic.eq:
      - std.object.get:
        - std.object.get:
          - std.object.get:
            - {var: subject}
            - context
          - oauth
        - scope_requested
      - read:spec
```

## SRCONF-API-005

```yaml spec-test
id: SRCONF-API-005
title: api.http oauth missing env refs is schema failure
purpose: Verifies oauth env-ref credentials are required and missing env vars fail as schema.
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
assert:
- target: status
  must:
  - evaluate:
    - std.string.contains:
      - {var: subject}
      - '200'
```

## SRCONF-API-006

```yaml spec-test
id: SRCONF-API-006
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
assert:
- target: status
  must:
  - evaluate:
    - std.string.contains:
      - {var: subject}
      - '200'
```

## SRCONF-API-007

```yaml spec-test
id: SRCONF-API-007
title: api.http oauth live mode is optional capability
type: api.http
purpose: Verifies optional live oauth/network execution can be capability-gated and skipped
  in portable lanes.
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
assert:
- target: status
  must:
  - evaluate:
    - std.string.contains:
      - {var: subject}
      - '200'
```
