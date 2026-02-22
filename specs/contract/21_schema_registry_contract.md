# Schema Registry Contract (v2)

## Purpose

The schema registry under `specs/schema/registry/v2/` is the machine source of truth for executable case-shape constraints.

## Normative Rules

- Runtime schema validation MUST be driven from compiled registry data.
- Canonical field grammar MUST be driven from `/specs/schema/registry/v2/core.yaml` and `/specs/schema/registry/v2/assertions.yaml`.
- Unknown top-level case keys MUST fail with `schema`.
- Suite top-level validation MUST enforce `spec_version`, `schema_ref`, and non-empty `contracts`.
- Contract-item validation MUST enforce per-item `id` and `asserts` shape.
- `specs/schema/schema_v2.md` MUST contain generated registry snapshot content and stay synchronized.
- Suite runtime metadata MUST define root `harness` (`type`, `profile`, optional `config`).
- Suite runtime services are optional at root.
- When `services` is present, it MUST define non-empty `services[]`.
- Root `bindings` is invalid in v2.
- `contracts.defaults` is invalid in v2.
- `contracts.clauses[].asserts.defaults` is invalid in v2.
- `contracts.clauses[].harness` is invalid in v2.
- `contracts.clauses[].asserts.profile` and `contracts.clauses[].asserts.config` are invalid in v2 runtime ownership.
- `services[].type` MUST resolve to an entry in `/specs/schema/service_contract_catalog_v1.yaml`; unknown service types are hard-fail schema errors.
- `services[].operations[].mode` (effective via defaults+entry merge) MUST be valid for the resolved `services[].type`.
- `services[].operations[].direction` (effective via defaults+entry merge) and `artifacts[].direction` MUST use `input|output|bidirectional`.
- `services[].operations[].imports` (effective via defaults+entry merge) MUST support
  canonical list[mapping] rows (`names`, optional `as`) and compact list[string]
  aliases with deterministic normalization.
- Effective declared service import names MUST be unique per service entry and MUST exist in catalog `available_imports_by_profile` for resolved `type/mode`.
- `services[].defaults.config` and `services[].operations[].config` MUST NOT include direct locator keys (`path`, `url`, `token_url`, `template_path`, `output_path`, `ref`).
- Any external locator consumed by service config MUST be declared in `artifacts[]` and referenced by `*_artifact_id` (or `*_artifact_ids[]`) fields that resolve to `artifacts[].id`.
- `contracts.clauses[].bindings` uses mapping form only: `contracts.clauses[].bindings.defaults` + `contracts.clauses[].bindings.rows[]`.
- Direct list-form bindings are invalid in v2.
- Effective binding row = shallow merge(defaults, row), with row values overriding defaults.
- Effective binding rows MUST include `id`, `service`, and `import`.
- Effective `service` MUST resolve to `services[].operations[].id`.
- Binding I/O surfaces (`contracts.clauses[].bindings.rows[].inputs/outputs`) MUST
  support canonical mapping rows and compact list[string] aliases with deterministic
  normalization.
- `contracts.clauses[].bindings.rows[].inputs[].from` MUST resolve to `artifacts[].id` where `direction` is `input` or `bidirectional`.
- `contracts.clauses[].bindings.rows[].outputs[].to` MUST resolve to `artifacts[].id` where `direction` is `output` or `bidirectional`.
- `contracts.clauses[].asserts.imports` and `contracts.clauses[].asserts.checks[].imports`
  MUST support canonical rows (`{from, names, service?, as?}`) and supported compact
  aliases with deterministic normalization.
- `from: artifact` imported names MUST resolve to suite-declared artifact ids and MUST NOT rely on implicit runtime target injection.
- If any `contracts.clauses[].bindings.rows[]` or any `from: service` assertion import is present, `services` MUST be declared and valid.
- Suite artifact references MUST be declared only under `artifacts[]`.
- Root `exports[]` MUST be function-only declarations using `as` + `from: assert.function` + `path`.
- Documentation metadata surfaces MUST use `docs[]` entry arrays with required `summary|audience|status`; singular `doc` is invalid in v2.
- `docs[].id` and `docs[].owners[].id` are optional metadata keys.
- `contracts.clauses[].asserts.checks[].id` is required and must be explicitly authored.
- Requiredness language is standardized as: `explicit-required`, `optional`, `effective-required (required after deterministic merge)`.

## Profile Types

- `core`
- `assertions`
- `harness`
- `path_model`
- `deprecated type overlays` (migration-only; non-normative)

## Runtime Catalogs

Runtime catalog entries define service additions over common suite/contract keys:

- required suite runtime fields (`harness`; `services[]` when services are used)
- optional contract-local binding field (`contracts.clauses[].bindings`)
- service `type/mode/direction` compatibility and available import names
- allowed function operation prefixes per service type

## Determinism

Registry compilation and validation diagnostics must be deterministic and stable for the same repository state.
