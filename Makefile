.PHONY: help governance docs-check ingest ci-gate check prepush

help:
	@echo "Targets: governance docs-check ingest ci-gate check prepush"

governance:
	@dc-runner governance run

docs-check:
	@dc-runner docs generate-check
	@python3 ./scripts/docs_audience_generate.py --check

ingest:
	@dc-runner governance run
	@mkdir -p .artifacts
	@cp -f .artifacts/governance-summary.json .artifacts/runner-status-matrix.json
	@cp -f .artifacts/governance-summary.md .artifacts/runner-status-matrix.md
	@cp -f .artifacts/governance-trace.json .artifacts/runner-status-ingest-log.json

ci-gate:
	@dc-runner governance critical
	@dc-runner ci gate-summary

check:
	@dc-runner governance run
	@dc-runner docs generate-check
	@python3 ./scripts/docs_audience_generate.py --check
	@mkdir -p .artifacts
	@cp -f .artifacts/governance-summary.json .artifacts/runner-status-matrix.json
	@cp -f .artifacts/governance-summary.md .artifacts/runner-status-matrix.md
	@cp -f .artifacts/governance-trace.json .artifacts/runner-status-ingest-log.json

prepush:
	@dc-runner governance critical
	@dc-runner governance broad
	@dc-runner docs generate-check
	@dc-runner docs-lint
	@dc-runner normalize-check
	@dc-runner schema-registry-build
	@dc-runner schema-registry-check
	@dc-runner schema-docs-check
	@dc-runner style-check
	@mkdir -p .artifacts
	@jq -n --arg generated_at "$$(date -u +%Y-%m-%dT%H:%M:%SZ)" '{generated_at:$$generated_at, status:"ok"}' > .artifacts/gate-summary.json
	@echo "[gate] summary: $(PWD)/.artifacts/gate-summary.json"
