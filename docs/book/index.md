# YAML `contract-spec` Book

Practical guide for authoring and running executable spec tests in this repo.

## Who This Is For

- Engineers writing new `yaml contract-spec` cases.
- Reviewers validating schema/assertion correctness.
- Port maintainers comparing behavior across Python and PHP runners.

## Read Paths

Fast start:

1. `docs/book/01_quickstart.md`
2. `docs/book/90_appendix_cheatsheet.md`

Deterministic onboarding:

1. `docs/book/00_first_10_minutes.md`
2. `docs/book/01_quickstart.md`

Full authoring:

1. `docs/book/01_quickstart.md`
2. `docs/book/02_core_model.md`
3. `docs/book/03_assertions.md`
4. `docs/book/04_spec_lang_guide.md`
5. `docs/book/05_howto.md`
6. `docs/book/06_troubleshooting.md`
7. `docs/book/07_spec_lang_reference.md`
8. `docs/spec/schema/schema_v1.md`
9. `docs/spec/contract/`

Portability and conformance:

1. `docs/spec/conformance/index.md`
2. `docs/spec/conformance/cases/*.spec.md`
3. `docs/spec/impl/php.md`

## Canonical Sources

- Stable schema: `docs/spec/schema/schema_v1.md`
- Portable contract: `docs/spec/contract/`
- Conformance fixtures: `docs/spec/conformance/cases/`
- PHP implementation fixtures: `docs/spec/impl/php/cases/`

## Chapter Guide

- `00_first_10_minutes.md`: deterministic first run and safety model
- `01_quickstart.md`: smallest runnable examples
- `02_core_model.md`: case shape, discovery, types, harness rules
- `03_assertions.md`: assertion tree and operators
- `04_spec_lang_guide.md`: practical composition, reuse, and debugging patterns
- `05_howto.md`: task-focused contributor workflows
- `06_troubleshooting.md`: triage and recovery playbooks
- `07_spec_lang_reference.md`: strict operator semantics reference
- `90_appendix_cheatsheet.md`: compact templates
- `91_appendix_runner_api_reference.md` through `99_appendix_reference_index.md`: generated appendices
- `93a_std_core.md` through `93i_std_json_schema_fn_null.md`: generated namespace chapters

## Docs Quality Authoring Guide

Reference docs are machine-checked product surfaces. Canonical chapters listed
in `docs/book/reference_manifest.yaml` must include valid `doc-meta`.

### `doc-meta` Template

Use either front matter or a fenced `yaml doc-meta` block near the top of the
document. Canonical template:

```yaml doc-meta
doc_id: DOC-REF-###
title: Chapter title
status: active
audience: author
owns_tokens:
- token_defined_here
requires_tokens:
- token_defined_elsewhere
commands:
- run: ./scripts/ci_gate.sh
  purpose: One-line reason this command is in the doc.
examples:
- id: EX-CHAPTER-001
  runnable: true
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

### Field Rules

- `doc_id`: `DOC-<AREA>-###`
- `status`: `active` or `draft`
- `audience`: `author`, `reviewer`, or `maintainer`
- `owns_tokens`: tokens this doc is canonical owner of (must be unique across
  canonical chapters)
- `requires_tokens`: tokens this doc depends on (must resolve to owner docs)
- `commands[*]`: each entry requires non-empty `run` and `purpose`
- `examples[*].id`: `EX-...` unique across canonical chapters
- `examples[*].runnable`: boolean
- `examples[*].opt_out_reason`: required when `runnable: false`

### Valid Example

```yaml doc-meta
doc_id: DOC-REF-007
title: Example Chapter
status: active
audience: reviewer
owns_tokens:
- example_token_owner
requires_tokens:
- quickstart_minimal_case
commands:
- run: make docs-check
  purpose: Validate generated docs artifacts and metadata lint checks.
examples:
- id: EX-EXAMPLE-001
  runnable: true
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

### Invalid Examples

Missing `opt_out_reason` when example is non-runnable:

```yaml doc-meta
doc_id: DOC-REF-008
title: Bad Example
status: active
audience: author
owns_tokens:
- bad_owner
requires_tokens:
- quickstart_minimal_case
commands:
- run: make docs-check
  purpose: Check docs.
examples:
- id: EX-BAD-001
  runnable: false
sections_required:
- '## Purpose'
```

Duplicate token ownership across chapters (fails ownership uniqueness):

```yaml doc-meta
doc_id: DOC-REF-009
title: Also Defines Existing Token
status: active
audience: maintainer
owns_tokens:
- quickstart_minimal_case
requires_tokens:
- core_case_model
commands:
- run: ./scripts/docs_doctor.sh
  purpose: Run fast docs checks.
examples:
- id: EX-BAD-002
  runnable: true
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

### Authoring Workflow

1. Edit chapter content + `doc-meta`.
2. Regenerate artifacts:
   - `make docs-build`
3. Verify generated + lint checks:
   - `make docs-check`
4. Run fast docs gate:
   - `./scripts/docs_doctor.sh`
5. Before merge, run full gate:
   - `./scripts/ci_gate.sh`
