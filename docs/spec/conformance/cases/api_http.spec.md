# API HTTP Conformance Fixtures

## SRCONF-API-001

```yaml spec-test
id: SRCONF-API-001
title: api.http reads relative fixture and exposes body assertions
purpose: Verifies api.http can resolve a local relative request url and assert deterministic status and json body shape.
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
  url: fixtures/api_http_ok.json
assert:
- target: status
  must:
  - contain:
    - '200'
- target: body_text
  must:
  - contain:
    - '"ok":true'
- target: body_json
  must:
  - json_type:
    - dict
```

## SRCONF-API-002

```yaml spec-test
id: SRCONF-API-002
title: api.http requires request.url
purpose: Verifies api.http reports a schema violation when request url is missing from portable fixture input.
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
  - contain:
    - '200'
```

## SRCONF-API-003

```yaml spec-test
id: SRCONF-API-003
title: api.http skip path honors requires.when_missing
purpose: Verifies extension type capability gating can skip deterministic fixtures when an additional required capability is absent.
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
  url: fixtures/api_http_ok.json
assert:
- target: status
  must:
  - contain:
    - '200'
```
