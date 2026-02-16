# Type Contract: api.http

## Status

- published extension type contract (not in v1 core set)

## Purpose

Define portable API endpoint behavior checks without coupling specs to one runtime.

## Required Fields

- `id` (string)
- `type` (must equal `api.http`)
- `request.method` (string)
- `request.url` (string)
- `assert` (assertion tree)

## Optional Fields

- `request.headers` (mapping[string, string])
- `request.body_text` (string)
- `request.body_json` (mapping or list)
- `harness` (mapping for setup, if needed)

`harness.api_http` (optional):

- `mode` (`deterministic` | `live`, default `deterministic`)
- `auth.oauth` (mapping):
  - `grant_type` (`client_credentials`)
  - `token_url` (string)
  - `client_id_env` (string env var name)
  - `client_secret_env` (string env var name)
  - `scope` (optional string)
  - `audience` (optional string)
  - `auth_style` (`basic` | `body`, default `basic`)
  - `token_field` (default `access_token`)
  - `expires_field` (default `expires_in`)
  - `refresh_skew_seconds` (default `30`)

## Targets

- `status`
- `headers`
- `body_text`
- `body_json`
- `context_json`

## Type Rules

- Transport/setup details MUST live under `harness`.
- Portable behavior assertions MUST use canonical `assert` groups/operators.
- `request.method` SHOULD be uppercase HTTP token form (for example `GET`, `POST`).
- `request.url` MAY be a URL or a contract path (`/` = contract root);
  root-relative values normalize to canonical `/...` and MUST remain inside
  contract root.
- network URLs (`http://` / `https://`) require `harness.api_http.mode: live`;
  deterministic mode allows contract-root and `file://` paths only.
- OAuth credentials are env-ref only (`*_env`); inline secret literals are
  forbidden.
- target semantics:
  - `status`: HTTP status string
  - `headers`: deterministic header text view
  - `body_text`: response body text
  - `body_json`: parsed JSON value from body text
  - `context_json`: JSON subject profile envelope for `api.http/v1` including
    auth metadata (`meta.auth_mode`, `meta.oauth_token_source`,
    `context.oauth.*`) without raw token/secret values

## Conformance Notes

- `api.http` is an extension type and not required for v1 core conformance.
- Implementations that advertise the same `api.http` capability MUST produce
  matching status/category outcomes for shared-capability fixtures.
