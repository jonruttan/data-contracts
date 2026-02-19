# Guide 01: Onboarding

```yaml doc-meta
doc_id: DOC-GUIDE-201
title: Guide 01 Onboarding
status: active
audience: author
owns_tokens:
- guide_onboarding_flow
requires_tokens:
- usage_guides_entrypoint
commands:
- run: ./scripts/control_plane.sh governance
  purpose: Validate local environment against required governance checks.
examples:
- id: EX-GUIDE-01-001
  runnable: true
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

## Purpose

Bring a new contributor to first successful local validation in the required lane.

## Inputs

- clean checkout
- shell with `bash`, `git`, and Rust toolchain available
- access to `./scripts/runner_bin.sh`

## Outputs

- validated local environment
- first successful governance run
- baseline understanding of where specs, contracts, and docs live

## Failure Modes

- missing runner adapter prerequisites
- running compatibility-lane workflows as primary gate
- editing generated docs sections manually

## Do This Now

```bash
git status --short
./scripts/control_plane.sh governance
./scripts/control_plane.sh docs-generate-check
```

## How To Verify Success

- [ ] `governance` exits 0
- [ ] `docs-generate-check` exits 0
- [ ] no unexpected tracked file changes after checks

## Common Failure Signatures

| Signature | Likely Cause | Action |
| --- | --- | --- |
| `unknown command` from runner binary | stale command path or invocation typo | run exactly from repo root with `./scripts/runner_bin.sh` |
| docs freshness drift | generated references stale | run `./scripts/docs_generate_all.py --build` then re-check |
| governance check id violation | contract/docs mismatch | open referenced contract and align doc content |
