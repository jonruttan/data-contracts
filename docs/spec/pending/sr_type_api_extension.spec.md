# Pending Type-Model Extensions

## SR-TYPE-API-001

```yaml
id: SR-TYPE-API-001
where: docs/spec/schema/schema_v1.md
priority: P1
statement: MUST define a portable type contract for `api.http` before treating it as a supported conformance type.
rationale: >
  Portable endpoint checks require a stable field/target contract so Python, PHP,
  and future runners evaluate equivalent behavior.
verification: >
  Add conformance fixtures using `type: api.http` only after schema and
  docs/spec/contract/types/api_http.md are both normative and governance-enforced.
```

## SR-TYPE-API-002

```yaml
id: SR-TYPE-API-002
where: docs/spec/contract/07_portable_spec_authoring.md
priority: P1
statement: MUST keep transport/setup details under `harness` and keep API behavior assertions in canonical `assert` targets.
rationale: >
  This preserves implementation independence by isolating runner-specific setup from
  portable behavior claims.
verification: >
  Add governance checks that reject runner-specific setup keys outside `harness`
  for portable conformance cases.
```

## SR-TYPE-API-003

```yaml
id: SR-TYPE-API-003
where: docs/spec/contract/06_conformance.md
priority: P1
statement: MUST declare capability parity requirements for domain types so shared-capability cases produce matching status/category across runners.
rationale: >
  A domain type is only portable when runners expose the same capability semantics
  and compare results under one conformance baseline.
verification: >
  Extend parity checks to include domain-type capability declarations and fail
  when shared-capability outcomes diverge.
```
