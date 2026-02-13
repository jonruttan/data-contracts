# Type Contract: api.http

## Status

- draft candidate (not part of v1 core set)

## Purpose

Define portable API endpoint behavior checks without coupling specs to one runtime.

## Proposed Required Fields

- `id` (string)
- `type` (must equal `api.http`)
- `request.method` (string)
- `request.url` (string)
- `assert` (assertion tree)

## Proposed Optional Fields

- `request.headers` (mapping[string, string])
- `request.body_text` (string)
- `request.body_json` (mapping or list)
- `harness` (mapping for setup, if needed)

## Proposed Targets

- `status`
- `headers`
- `body_text`
- `body_json`

## Notes

- This draft is intended for pending-spec maturation.
- Do not treat `api.http` as a supported v1 core type until schema and conformance docs explicitly adopt it.
