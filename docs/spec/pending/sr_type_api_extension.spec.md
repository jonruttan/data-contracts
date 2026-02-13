# Pending Type-Model Extensions

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
