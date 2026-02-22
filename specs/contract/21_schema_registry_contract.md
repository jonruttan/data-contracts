# Schema Registry Contract (v2)

## Purpose

The schema registry under `specs/schema/registry/v2/` is the machine source of truth for executable case-shape constraints.

## Normative Rules

- Runtime schema validation MUST be driven from compiled registry data.
- Canonical field grammar MUST be driven from `/specs/schema/registry/v2/core.yaml` and `/specs/schema/registry/v2/assertions.yaml`.
- Unknown top-level case keys MUST fail with `schema`.
- Suite top-level validation MUST enforce `spec_version`, `schema_ref`, and non-empty `contracts`.
- Contract-item validation MUST enforce per-item `id` and `clauses` shape.
- `specs/schema/schema_v2.md` MUST contain generated registry snapshot content and stay synchronized.
- Suite runtime metadata MUST define root `harness` (`type`, `profile`, optional `config`).
- Suite runtime services are optional at root.
- When `services` is present, it MUST define non-empty `services[]`.
- Root `bindings` is invalid in v2.
- `contracts[].harness` is invalid in v2.
- `contracts[].clauses.profile` and `contracts[].clauses.config` are invalid in v2 runtime ownership.
- `services[].type` MUST resolve to an entry in `/specs/schema/service_contract_catalog_v1.yaml`; unknown service types are hard-fail schema errors.
- `services[].mode` MUST be valid for the resolved `services[].type`.
- `services[].direction` and `artifacts[].direction` MUST use `input|output|bidirectional`.
- `services[].imports` MUST use canonical list[mapping] rows (`names`, optional `as`).
- Compact/short import aliases are invalid in v2.
- Effective declared service import names MUST be unique per service entry and MUST exist in catalog `available_imports_by_profile` for resolved `type/mode`.
- `services[].config` MUST NOT include direct locator keys (`path`, `url`, `token_url`, `template_path`, `output_path`, `ref`).
- Any external locator consumed by service config MUST be declared in `artifacts[]` and referenced by `*_artifact_id` (or `*_artifact_ids[]`) fields that resolve to `artifacts[].id`.
- `contracts[].bindings` uses mapping form only: `contracts[].bindings.defaults` + `contracts[].bindings.rows[]`.
- Direct list-form bindings are invalid in v2.
- Effective binding row = shallow merge(defaults, row), with row values overriding defaults.
- Effective binding rows MUST include `id`, `service`, and `import`.
- Effective `service` MUST resolve to `services[].id`.
- Binding I/O surfaces (`contracts[].bindings.rows[].inputs/outputs`) MUST use canonical mapping rows only.
- `contracts[].bindings.rows[].inputs[].from` MUST resolve to `artifacts[].id` where `direction` is `input` or `bidirectional`.
- `contracts[].bindings.rows[].outputs[].to` MUST resolve to `artifacts[].id` where `direction` is `output` or `bidirectional`.
- `contracts[].clauses.imports` and `contracts[].clauses.predicates[].imports` MUST use canonical rows (`{from, names, service?, as?}`).
- Bare-string and grouped alias rows are invalid in v2.
- `from: artifact` imported names MUST resolve to suite-declared artifact ids and MUST NOT rely on implicit runtime target injection.
- If any `contracts[].bindings.rows[]` or any `from: service` assertion import is present, `services` MUST be declared and valid.
- Suite artifact references MUST be declared only under `artifacts[]`.
- Root `exports[]` MUST be function-only declarations using `as` + `from: assert.function` + `path`.
- Documentation metadata surfaces MUST use `docs[]` entry arrays with required `summary|audience|status`; singular `doc` is invalid in v2.
- `docs[].id` and `docs[].owners[].id` are optional metadata keys.
- `contracts[].clauses.predicates[].id` is required and must be explicitly authored.
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
- optional contract-local binding field (`contracts[].bindings`)
- service `type/mode/direction` compatibility and available import names
- allowed function operation prefixes per service type

## Determinism

Registry compilation and validation diagnostics must be deterministic and stable for the same repository state.
