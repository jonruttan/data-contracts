```yaml contract-spec
spec_version: 2
schema_ref: "/specs/schema/schema_v2.md"
defaults:
  harness: check
  requires:
    capabilities:
    - api.http
harness:
  type: unit.test
  profile: check
services:
  defaults:
    type: assert.check
    io: input
    profile: api.http
    imports:
    - names:
      - pipe_identity
  entries:
  - id: svc.assert_check.api_http.1
    config:
      request:
        method: GET
        url: "/specs/conformance/cases/fixtures/api_http_ok.json"
  - id: svc.assert_check.api_http.2
    config:
      request:
        method: GET
  - id: svc.assert_check.api_http.3
    config:
      request:
        method: POST
        url: "/specs/conformance/cases/fixtures/api_http_created.json"
        body_json:
          name: sample
  - id: svc.assert_check.api_http.4
    config:
      request:
        method: PUT
        url: "/specs/conformance/cases/fixtures/api_http_item_abc-123.json"
  - id: svc.assert_check.api_http.5
    config:
      request:
        method: PATCH
        url: "/specs/conformance/cases/fixtures/api_http_item_abc-123.json"
  - id: svc.assert_check.api_http.6
    config:
      request:
        method: DELETE
        url: "/specs/conformance/cases/fixtures/api_http_deleted.json"
  - id: svc.assert_check.api_http.7
    config:
      request:
        method: HEAD
        url: "/specs/conformance/cases/fixtures/api_http_ok.json"
  - id: svc.assert_check.api_http.8
    config:
      request:
        method: OPTIONS
        url: "/specs/conformance/cases/fixtures/api_http_ok.json"
  - id: svc.assert_check.api_http.9
    config:
      request:
        method: TRACE
        url: "/specs/conformance/cases/fixtures/api_http_ok.json"
  - id: svc.assert_check.api_http.10
    config:
      request:
        method: GET
        url: "/specs/conformance/cases/fixtures/api_http_ok.json"
        cors:
          preflight: true
          origin: https://client.example
          request_method: POST
  - id: svc.assert_check.api_http.11
    config:
      requests:
      - id: create
        method: POST
        url: "/specs/conformance/cases/fixtures/api_http_created.json"
      - id: get
        method: GET
        url: "/specs/conformance/cases/fixtures/api_http_item_{{steps.create.body_json.id}}.json"
      - id: cleanup
        method: DELETE
        url: "/specs/conformance/cases/fixtures/api_http_deleted.json"
      api_http:
        scenario:
          fail_fast: true
  - id: svc.assert_check.api_http.12
    config:
      request:
        method: GET
        url: "/specs/conformance/cases/fixtures/api_http_ok.json"
      api_http:
        mode: deterministic
        auth:
          oauth:
            grant_type: client_credentials
            token_url: "/specs/conformance/cases/fixtures/oauth_token_ok.json"
            client_id_env: PATH
            client_secret_env: HOME
            scope: read:spec
  - id: svc.assert_check.api_http.13
    config:
      request:
        method: GET
        url: "/specs/conformance/cases/fixtures/api_http_ok.json"
      api_http:
        auth:
          oauth:
            grant_type: client_credentials
            token_url: "/specs/conformance/cases/fixtures/oauth_token_ok.json"
            client_id_env: SPEC_RUNNER_OAUTH_MISSING_CLIENT_ID
            client_secret_env: SPEC_RUNNER_OAUTH_MISSING_CLIENT_SECRET
  - id: svc.assert_check.api_http.14
    config:
      request:
        method: GET
        url: "/specs/conformance/cases/fixtures/api_http_ok.json"
      api_http:
        auth:
          oauth:
            grant_type: client_credentials
            token_url: "/specs/conformance/cases/fixtures/oauth_token_ok.json"
            client_id_env: PATH
            client_secret_env: HOME
            auth_style: token
  - id: svc.assert_check.api_http.15
    config:
      request:
        method: GET
        url: https://api.example.invalid/items
      api_http:
        mode: live
        auth:
          oauth:
            grant_type: client_credentials
            token_url: https://issuer.example.invalid/oauth/token
            client_id_env: OAUTH_CLIENT_ID
            client_secret_env: OAUTH_CLIENT_SECRET
  - id: svc.assert_check.api_http.16
    config:
      request:
        method: GET
        url: "/specs/conformance/cases/fixtures/api_http_ok.json"
      use:
      - ref: "/specs/libraries/domain/http_core.spec.md"
        as: lib_http_core_spec
        symbols:
        - domain.http.cors_allow_origin
        - domain.http.cors_allows_header
        - domain.http.cors_allows_method
        - domain.http.cors_credentials_enabled
        - domain.http.cors_max_age_gte
        - domain.http.is_preflight_step
        - domain.http.step_body_json_get
        - domain.http.step_by_id
        - domain.http.step_status_is
artifact:
  exports:
  - id: body_json
    ref: artifact://api_http/body_json
    type: application/json
  - id: body_text
    ref: artifact://api_http/body_text
    type: application/json
  - id: context_json
    ref: artifact://api_http/context_json
    type: application/json
  - id: status
    ref: artifact://api_http/status
    type: application/json
  - id: steps_json
    ref: artifact://api_http/steps_json
    type: application/json
bindings:
- id: bind.api_http.1
  contract: DCCONF-API-001
  service: svc.assert_check.api_http.1
  import: pipe_identity
  outputs:
  - to: body_json
    as: body_json
  - to: status
    as: status
  mode: merge
- id: bind.api_http.2
  contract: DCCONF-API-002
  service: svc.assert_check.api_http.2
  import: pipe_identity
  outputs:
  - to: status
    as: status
  mode: merge
- id: bind.api_http.3
  contract: DCCONF-API-003
  service: svc.assert_check.api_http.3
  import: pipe_identity
  outputs:
  - to: status
    as: status
  mode: merge
- id: bind.api_http.4
  contract: DCCONF-API-004
  service: svc.assert_check.api_http.4
  import: pipe_identity
  outputs:
  - to: body_json
    as: body_json
  mode: merge
- id: bind.api_http.5
  contract: DCCONF-API-005
  service: svc.assert_check.api_http.5
  import: pipe_identity
  outputs:
  - to: status
    as: status
  mode: merge
- id: bind.api_http.6
  contract: DCCONF-API-006
  service: svc.assert_check.api_http.6
  import: pipe_identity
  outputs:
  - to: body_text
    as: body_text
  mode: merge
- id: bind.api_http.7
  contract: DCCONF-API-007
  service: svc.assert_check.api_http.7
  import: pipe_identity
  outputs:
  - to: body_json
    as: body_json
  mode: merge
- id: bind.api_http.8
  contract: DCCONF-API-008
  service: svc.assert_check.api_http.8
  import: pipe_identity
  outputs:
  - to: status
    as: status
  mode: merge
- id: bind.api_http.9
  contract: DCCONF-API-009
  service: svc.assert_check.api_http.9
  import: pipe_identity
  outputs:
  - to: status
    as: status
  mode: merge
- id: bind.api_http.10
  contract: DCCONF-API-010
  service: svc.assert_check.api_http.10
  import: pipe_identity
  outputs:
  - to: status
    as: status
  mode: merge
- id: bind.api_http.11
  contract: DCCONF-API-011
  service: svc.assert_check.api_http.11
  import: pipe_identity
  outputs:
  - to: status
    as: status
  mode: merge
- id: bind.api_http.12
  contract: DCCONF-API-012
  service: svc.assert_check.api_http.12
  import: pipe_identity
  outputs:
  - to: status
    as: status
  - to: steps_json
    as: steps_json
  mode: merge
- id: bind.api_http.13
  contract: DCCONF-API-013
  service: svc.assert_check.api_http.13
  import: pipe_identity
  outputs:
  - to: context_json
    as: context_json
  mode: merge
- id: bind.api_http.14
  contract: DCCONF-API-014
  service: svc.assert_check.api_http.14
  import: pipe_identity
  outputs:
  - to: status
    as: status
  mode: merge
- id: bind.api_http.15
  contract: DCCONF-API-015
  service: svc.assert_check.api_http.15
  import: pipe_identity
  outputs:
  - to: status
    as: status
  mode: merge
- id: bind.api_http.16
  contract: DCCONF-API-016
  service: svc.assert_check.api_http.16
  import: pipe_identity
  outputs:
  - to: status
    as: status
  mode: merge
- id: bind.api_http.17
  contract: DCCONF-API-017
  service: svc.assert_check.api_http.16
  import: pipe_identity
  outputs:
  - to: status
    as: status
  mode: merge
contracts:
- id: DCCONF-API-001
  title: api.http GET reads relative fixture and exposes body assertions
  purpose: Verifies api.http can resolve a local relative request url and assert deterministic status and json body shape.
  expect:
    portable:
      status: pass
      category:
  clauses:
    imports:
    - from: artifact
      names:
      - status
    predicates:
    - id: assert_1
      assert:
        std.string.contains:
        - var: status
        - '200'
    - id: assert_2
      assert:
        std.type.json_type:
        - var: body_json
        - dict
      imports:
      - from: artifact
        names:
        - body_json
- id: DCCONF-API-002
  title: api.http requires request.url
  purpose: Verifies api.http reports a schema violation when request url is missing from portable fixture input.
  expect:
    portable:
      status: fail
      category: schema
      message_tokens:
      - api.http request.url is required
  clauses:
    imports:
    - from: artifact
      names:
      - status
    predicates:
    - id: assert_1
      assert:
        std.string.contains:
        - var: status
        - '200'
- id: DCCONF-API-003
  title: api.http skip path honors requires.when_missing
  purpose: Verifies extension capability gating can skip fixtures when a required capability is absent.
  expect:
    portable:
      status: skip
      category:
  requires:
    capabilities:
    - api.http
    - api.http.missing
    when_missing: skip
  clauses:
    imports:
    - from: artifact
      names:
      - status
    predicates:
    - id: assert_1
      assert:
        std.string.contains:
        - var: status
        - '200'
- id: DCCONF-API-004
  title: api.http supports POST with body_json
  purpose: Verifies practical REST mutating verb support for POST requests in deterministic mode.
  expect:
    portable:
      status: pass
      category:
  clauses:
    imports:
    - from: artifact
      names:
      - body_json
    predicates:
    - id: assert_1
      assert:
        std.object.has_key:
        - var: body_json
        - id
- id: DCCONF-API-005
  title: api.http supports PUT
  purpose: Verifies practical REST verb support for PUT in deterministic mode.
  expect:
    portable:
      status: pass
      category:
  clauses:
    imports:
    - from: artifact
      names:
      - status
    predicates:
    - id: assert_1
      assert:
        std.string.contains:
        - var: status
        - '200'
- id: DCCONF-API-006
  title: api.http supports PATCH
  purpose: Verifies practical REST verb support for PATCH in deterministic mode.
  expect:
    portable:
      status: pass
      category:
  clauses:
    imports:
    - from: artifact
      names:
      - body_text
    predicates:
    - id: assert_1
      assert:
        std.string.contains:
        - var: body_text
        - abc-123
- id: DCCONF-API-007
  title: api.http supports DELETE
  purpose: Verifies practical REST verb support for DELETE in deterministic mode.
  expect:
    portable:
      status: pass
      category:
  clauses:
    imports:
    - from: artifact
      names:
      - body_json
    predicates:
    - id: assert_1
      assert:
        std.logic.eq:
        - std.object.get:
          - var: body_json
          - deleted
        - true
- id: DCCONF-API-008
  title: api.http supports HEAD
  purpose: Verifies practical REST verb support for HEAD in deterministic mode.
  expect:
    portable:
      status: pass
      category:
  clauses:
    imports:
    - from: artifact
      names:
      - status
    predicates:
    - id: assert_1
      assert:
        std.string.contains:
        - var: status
        - '200'
- id: DCCONF-API-009
  title: api.http supports OPTIONS
  purpose: Verifies practical REST verb support for OPTIONS in deterministic mode.
  expect:
    portable:
      status: pass
      category:
  clauses:
    imports:
    - from: artifact
      names:
      - status
    predicates:
    - id: assert_1
      assert:
        std.string.contains:
        - var: status
        - '200'
- id: DCCONF-API-010
  title: api.http rejects unsupported request method
  purpose: Verifies unsupported HTTP verbs are rejected as schema violations.
  expect:
    portable:
      status: fail
      category: schema
      message_tokens:
      - request.method must be one of
  clauses:
    imports:
    - from: artifact
      names:
      - status
    predicates:
    - id: assert_1
      assert:
        std.string.contains:
        - var: status
        - '200'
- id: DCCONF-API-011
  title: api.http preflight requires OPTIONS method
  purpose: Verifies cors preflight helper enforces request.method OPTIONS.
  expect:
    portable:
      status: fail
      category: schema
      message_tokens:
      - request.cors.preflight requires request.method OPTIONS
  clauses:
    imports:
    - from: artifact
      names:
      - status
    predicates:
    - id: assert_1
      assert:
        std.string.contains:
        - var: status
        - '200'
- id: DCCONF-API-012
  title: api.http scenario executes round-trip requests in order
  purpose: Verifies requests scenario supports step templating and exposes steps_json target.
  expect:
    portable:
      status: pass
      category:
  clauses:
    imports:
    - from: artifact
      names:
      - status
    predicates:
    - id: assert_1
      assert:
        std.string.contains:
        - var: status
        - '200'
    - id: assert_2
      assert:
        std.logic.eq:
        - std.collection.len:
          - var: steps_json
        - 3
      imports:
      - from: artifact
        names:
        - steps_json
- id: DCCONF-API-013
  title: api.http oauth deterministic local token exchange
  purpose: Verifies oauth auth profile resolves env refs and produces oauth context metadata without network access.
  expect:
    portable:
      status: pass
      category:
  clauses:
    imports:
    - from: artifact
      names:
      - context_json
    predicates:
    - id: assert_1
      assert:
      - std.logic.eq:
        - std.object.get:
          - std.object.get:
            - var: context_json
            - meta
          - auth_mode
        - oauth
      - std.logic.eq:
        - std.object.get:
          - std.object.get:
            - var: context_json
            - meta
          - oauth_token_source
        - env_ref
- id: DCCONF-API-014
  title: api.http oauth missing env refs is schema failure
  purpose: Verifies oauth env-ref credentials are required and missing env vars fail as schema.
  expect:
    portable:
      status: fail
      category: schema
      message_tokens:
      - oauth env var is required
  clauses:
    imports:
    - from: artifact
      names:
      - status
    predicates:
    - id: assert_1
      assert:
        std.string.contains:
        - var: status
        - '200'
- id: DCCONF-API-015
  title: api.http oauth invalid auth_style is schema failure
  purpose: Verifies oauth auth_style is validated against supported values.
  expect:
    portable:
      status: fail
      category: schema
      message_tokens:
      - auth_style
  clauses:
    imports:
    - from: artifact
      names:
      - status
    predicates:
    - id: assert_1
      assert:
        std.string.contains:
        - var: status
        - '200'
- id: DCCONF-API-016
  title: api.http oauth live mode is optional capability
  purpose: Verifies optional live oauth/network execution can be capability-gated and skipped in portable lanes.
  expect:
    portable:
      status: skip
      category:
  requires:
    capabilities:
    - api.http
    - api.http.oauth.live
    when_missing: skip
  clauses:
    imports:
    - from: artifact
      names:
      - status
    predicates:
    - id: assert_1
      assert:
        std.string.contains:
        - var: status
        - '200'
- id: DCCONF-API-017
  title: api.http exposes new domain.http helper exports for CORS and steps
  purpose: Maintains reference usage for domain.http CORS and scenario helper symbol exports.
  expect:
    portable:
      status: skip
      category:
  requires:
    capabilities:
    - api.http
    - api.http.domain_lib_refs
    when_missing: skip
  clauses:
    imports:
    - from: artifact
      names:
      - status
    predicates:
    - id: assert_1
      assert:
        std.string.contains:
        - var: status
        - '200'
```
