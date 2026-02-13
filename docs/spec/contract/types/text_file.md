# Type Contract: text.file

## Status

- v1 core type

## Purpose

Assert text content from the containing spec document or an explicit relative path.

## Required Fields

- `id` (string)
- `type` (must equal `text.file`)
- `assert` (assertion tree)

## Optional Fields

- `path` (string, relative, in-root after resolution)
- common optional fields from schema v1 (`title`, `assert_health`, `expect`, `requires`, `harness`)

## Targets

- `text`

## Type Rules

- when `path` is omitted, target subject is the containing spec document
- when `path` is present, it MUST be relative
- resolved `path` MUST remain inside configured contract root

## Failure Category Guidance

- schema violations -> `schema`
- assertion mismatches -> `assertion`
- unexpected runtime faults -> `runtime`
