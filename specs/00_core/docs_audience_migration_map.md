# Docs Audience Migration Map (v1)

Canonical audience enum:

- operator
- integrator
- implementer
- maintainer
- governance
- reviewer
- auditor

Deterministic migration mapping:

- `spec-authors` -> `implementer`
- `author` -> `implementer`
- `maintainer` -> `maintainer`
- `reviewer` -> `reviewer`

Notes:

- Active v1 executable surfaces use only canonical audience values.
- Non-canonical audience tokens are invalid in active authoring.
