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

## Targets

- `status`
- `headers`
- `body_text`
- `body_json`

## Type Rules

- Transport/setup details MUST live under `harness`.
- Portable behavior assertions MUST use canonical `assert` groups/operators.
- `request.method` SHOULD be uppercase HTTP token form (for example `GET`, `POST`).
- `request.url` MAY be a URL or a spec-relative path; relative paths MUST remain
  inside contract root.
- target semantics:
  - `status`: HTTP status string
  - `headers`: deterministic header text view
  - `body_text`: response body text
  - `body_json`: parsed JSON value from body text

## Conformance Notes

- `api.http` is an extension type and not required for v1 core conformance.
- Implementations that advertise the same `api.http` capability MUST produce
  matching status/category outcomes for shared-capability fixtures.
