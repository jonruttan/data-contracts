# Troubleshooting

## When to read this

Read this when a gate fails and you need deterministic remediation.

## What you will do

- Identify failure category.
- Apply minimal corrective edits.
- Re-run checks to confirm resolution.

## Step-by-step

1. Read failing check ID and summary artifact first.
2. Map the check ID to source case and contract references.
3. Fix the smallest source-of-truth file possible.
4. Re-run required gates in canonical order.

## Common failure signals

- Fixing generated output without fixing source manifests/contracts.
- Editing compatibility surfaces while required-lane issue remains.
- Broad refactors before reproducing failure locally.

## Normative refs

- `specs/02_contracts/10_docs_quality.md`
- `specs/04_governance/check_sets_v1.yaml`
- `docs/book/90_reference_guide.md`
