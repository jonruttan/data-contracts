# HTTP Subject Profile Contract (v1)

HTTP adapter responses MUST be projected to JSON subject envelopes.

Projection rules:

- status -> integer
- headers -> JSON object mapping string to string
- body_text -> string
- body_json -> parsed JSON value
- meta.auth_mode -> `none` | `oauth`
- meta.oauth_token_source -> `none` | `env_ref`
- context.oauth -> metadata-only OAuth details:
  - token_url_host
  - scope_requested
  - token_fetch_ms
  - used_cached_token

Profile id: `api.http/v1`.
