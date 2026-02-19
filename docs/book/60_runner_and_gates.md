# Chapter 60: Runner Boundaries And Gates

```yaml doc-meta
doc_id: DOC-REF-160
title: Chapter 60 Runner Boundaries And Gates
status: active
audience: maintainer
owns_tokens:
- runner_boundary_and_control_plane_gates
requires_tokens:
- system_topology_view
commands:
- run: ./scripts/ci_gate.sh
  purpose: Execute control-plane gate checks.
examples:
- id: EX-RUNNER-GATES-001
  runnable: true
sections_required:
- '## Purpose'
- '## Inputs'
- '## Outputs'
- '## Failure Modes'
```

## Purpose

Explain boundary separation between control-plane governance in this repo and runtime execution in runner repos.

## Inputs

- runner interface contracts
- CI/gate scripts in this repository

## Outputs

- clear ownership split for execution vs governance
- deterministic understanding of what this repo validates

## Failure Modes

- treating control-plane CI as runtime execution testing
- moving runner implementation concerns back into this repo

## Boundary Model

- This repo validates control-plane integrity (spec/contract/schema/docs/governance).
- Runner repos execute runtime implementation behavior.
- Status exchange artifacts communicate cross-repo execution status back to this control plane.

## Runtime Ownership

- Rust implementation owner: `dc-runner-rust`
- Python implementation owner: `dc-runner-python`
- PHP implementation owner: `dc-runner-php`

## Control-Plane Gate

```sh
./scripts/ci_gate.sh
```
