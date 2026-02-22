# Runner CLI Interface Contract (v1)

Defines the portable CLI surface shared by runner implementations and consumed
by the control-plane conformance layer.

## Scope

This contract specifies only implementation-agnostic runner CLI behavior.
Runtime-specific or implementation-specific subcommands remain runner-owned.
Runner-owned CLI behavior specs are maintained in external runner spec
repositories, not in canonical schema trees.

## MUST Surface

Runner CLIs MUST provide deterministic behavior for:

- `runner --help`
- `runner conformance`
- `runner governance`
- `runner contract-spec-format --check <paths...>`
- `runner contract-spec-format --write <paths...>`
- unknown command handling with non-zero exit code
- structured status output mode (`--json` or equivalent capability)

## MAY Surface

Runner CLIs MAY provide:

- implementation-specific helper subcommands
- additional diagnostics modes
- additional output formats beyond the structured mode

## Capability Model

Portable required behavior is represented as required commands and output
contract keys in `/specs/01_schema/runner_cli_contract_v1.yaml`.

`contract-spec-format` contract:

- processes Markdown `*.spec.md` files containing fenced `yaml contract-spec`
  blocks
- applies only to `spec_version: 1` blocks
- `--check` is read-only and exits non-zero when canonical order is found
- `--write` rewrites canonical v1 block key order in place
- non-v1 blocks are skipped (no rewrite)

Canonical executable case payload shape for formatting and execution is
`spec_version/schema_ref/harness/contracts.clauses[].asserts.checks[]`.

Implementation-specific additions MUST be capability-gated and MUST NOT weaken
the required portable command semantics.
