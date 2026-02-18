# Spec Runner

`spec_runner` is a data contract spec format and runner for Markdown-authored cases.
It discovers `yaml contract-spec` blocks in `*.spec.md` files, validates case shape
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

`make prepush` runs the fast CI-critical checks (`normalize-check`, targeted
governance triage, `governance-heavy`, `docs-generate-check`, and strict perf-smoke compare).
`governance-heavy` and `docs-generate-check` are path-scoped to relevant
changes.
It is Rust-only on the runtime path.
Governance in this flow is targeted-first triage (`scripts/governance_triage.sh --mode auto`)
to avoid broad-first latency and to emit deterministic triage artifacts.
Broad governance remains mandatory in CI merge-gate (`ci-gate-summary`).

Fast local mode:

```sh
make prepush-fast
# or
SPEC_PREPUSH_MODE=fast make prepush
```

Managed pre-push hook enforcement:

```sh
make hooks-install
```

Emergency bypass (only when absolutely required):

```sh
SPEC_PREPUSH_BYPASS=1 git push
```

If governance fails/stalls, inspect:

- `/.artifacts/governance-triage-summary.md`

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
./runners/public/runner_adapter.sh
```

Default lane (rust):

```sh
./runners/public/runner_adapter.sh governance
```

Python impl in runtime adapter is forbidden (hard cut):

```sh
./runners/public/runner_adapter.sh --impl python governance
# => exits with migration guidance to --impl rust
```

Runner interface contract:

- `/Users/jon/Workspace/Development/spec_runner/docs/spec/contract/12_runner_interface.md`

## Minimal `.spec.md` Example

```yaml contract-spec
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

## Documentation Health

Use strict docs/spec drift checks before pushing:

```sh
python3 -m spec_runner.spec_lang_commands check-docs-freshness --strict
```

This check is blocking in local parity and CI gate lanes.
