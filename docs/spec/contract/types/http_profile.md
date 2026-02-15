# HTTP Subject Profile Contract (v1)

HTTP adapter responses MUST be projected to JSON subject envelopes.

Projection rules:

- status -> integer
- headers -> JSON object mapping string to string
- body_text -> string
- body_json -> parsed JSON value

Profile id: `api.http/v1`.
