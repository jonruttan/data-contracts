# Chapter 5: How-To Workflows

```yaml doc-meta
doc_id: DOC-REF-008
title: Chapter 5 How-To Workflows
status: active
audience: author
owns_tokens:
- authoring_workflows
- governance_workflow_quickpath
requires_tokens:
- spec_lang_guide_patterns
commands:
- run: ./scripts/runner_adapter.sh governance
  purpose: Validate governance checks after workflow changes.
examples:
- id: EX-HOWTO-001
  runnable: true
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

## Purpose

Provide repeatable recipes for common contributor tasks.

## Inputs

- local checkout
- canonical runner entrypoint
- `.spec.md` authoring surface

## Outputs

- predictable task completion with contract/governance compliance

## Failure Modes

- using stale paths/names in docs or harness config
- adding non-canonical expression syntax
- skipping local gate commands before push

## Add A New Spec Case

1. Create `*.spec.md` in the correct domain tree.
2. Add `yaml spec-test` case with `id`, `type`, `assert`.
3. Prefer `evaluate` for policy logic.
4. Run:
   - `./scripts/runner_adapter.sh normalize-check`
   - `./scripts/runner_adapter.sh governance`

## Add Or Reuse A Library Function

1. Add function in a `type: spec_lang.library` file.
2. Keep mapping-AST canonical form.
3. Export symbol through `definitions.public`.
4. Import via `harness.spec_lang.includes` and call with `call`.

## Add A Governance Check

1. Add scanner/check implementation and check id.
2. Add governance case under `/docs/spec/governance/cases/core/`.
3. Wire policy + traceability entries.
4. Run full governance pass.

## Run Local Gate Subsets

- Docs only: `./scripts/runner_adapter.sh docs-generate-check`
- Governance only: `./scripts/runner_adapter.sh governance`
- Full local gate: `./scripts/runner_adapter.sh ci-cleanroom`

## Escalation Path

If a failure appears implementation-specific, move from book docs to:

- `/docs/impl/index.md`
- `/docs/impl/python.md`
- `/docs/impl/php.md`
