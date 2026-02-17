# Spec Runner

`spec_runner` is an executable-spec runner for Markdown-authored cases.
It discovers `yaml spec-test` blocks in `*.spec.md` files, validates case shape
against contract/schema rules, and executes typed harnesses through a stable
runner interface.

The project is contract-first: schema, policy, governance checks, and generated
docs are treated as product surfaces.

## Project Status and Safety

This project is **pre-alpha** and changes quickly.

Trust model:

- `spec_runner` is **not a sandbox**.
- Specs are trusted inputs.
- Running untrusted specs is unsafe and out of scope for v1.

Reference contracts:

- `/Users/jon/Workspace/Development/spec_runner/docs/spec/contract/08_v1_scope.md`
- `/Users/jon/Workspace/Development/spec_runner/docs/spec/contract/04_harness.md`

## Quickstart (Contributors)

Setup:

```sh
make setup
```

Canonical local verification:

```sh
make verify-docs
make core-check
make check
```

Required local pre-push gate:

```sh
make prepush
```

`make prepush` runs the fast CI-critical checks (`normalize-check`, `governance`,
`governance-heavy`, `docs-generate-check`, and strict perf-smoke compare).

Clean-checkout CI parity gate (recommended before push):

```sh
make ci-cleanroom
```

Adoption profiles:

- **Core profile**: `make core-check`
- **Full profile**: `make check`

## Canonical Runner Interface

Single public entrypoint:

```sh
./scripts/runner_adapter.sh
```

Default lane (rust):

```sh
./scripts/runner_adapter.sh governance
```

Explicit Python lane (opt-in):

```sh
./scripts/runner_adapter.sh --impl python governance
# or
SPEC_RUNNER_IMPL=python ./scripts/runner_adapter.sh governance
```

Runner interface contract:

- `/Users/jon/Workspace/Development/spec_runner/docs/spec/contract/12_runner_interface.md`

## Minimal `.spec.md` Example

```yaml spec-test
id: EX-TEXT-001
type: text.file
path: /README.md
assert:
- target: text
  must:
  - evaluate:
    - contains:
      - {var: subject}
      - "Spec Runner"
```

Notes:

- Expression authoring uses mapping-AST form.
- Runner-only setup belongs under `harness`.
- Canonical executable format is `*.spec.md`.

## Where To Go Next

- Development workflows: `/Users/jon/Workspace/Development/spec_runner/docs/development.md`
- Book index: `/Users/jon/Workspace/Development/spec_runner/docs/book/index.md`
- Current snapshot: `/Users/jon/Workspace/Development/spec_runner/docs/spec/current.md`
- Schema: `/Users/jon/Workspace/Development/spec_runner/docs/spec/schema/schema_v1.md`
- Contract index: `/Users/jon/Workspace/Development/spec_runner/docs/spec/contract/index.md`
- Implementation appendices: `/Users/jon/Workspace/Development/spec_runner/docs/impl/index.md`

## Repo Layout

- `spec_runner/`: core runtime and harness code
- `scripts/`: runner adapters, gates, and generators
- `docs/`: book, contract/schema specs, implementation appendices
- `tests/`: executable and unit-level validation
