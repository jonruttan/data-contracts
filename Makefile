.PHONY: help governance docs-check ingest ci-gate check prepush

help:
	@echo "Targets: governance docs-check ingest ci-gate check prepush"

governance:
	@./scripts/control_plane.sh governance

docs-check:
	@./scripts/control_plane.sh docs-generate-check

ingest:
	@./scripts/runner_status_ingest.sh --max-age-hours 72 --enforce-freshness

ci-gate:
	@./scripts/ci_gate.sh

check:
	@./scripts/control_plane.sh governance
	@./scripts/control_plane.sh docs-generate-check
	@./scripts/runner_status_ingest.sh --max-age-hours 72 --enforce-freshness

prepush:
	@./scripts/local_ci_parity.sh
