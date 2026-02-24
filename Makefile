SPEC_SOURCE ?= workspace

.PHONY: help governance docs-check ingest ci-gate check prepush

help:
	@echo "Targets: governance docs-check ingest ci-gate check prepush"

governance:
	@dc-runner governance run --spec-source $(SPEC_SOURCE)

docs-check:
	@dc-runner docs generate-check --spec-source $(SPEC_SOURCE)

ingest:
	@dc-runner governance run --spec-source $(SPEC_SOURCE)
	@mkdir -p .artifacts
	@cp -f .artifacts/governance-summary.json .artifacts/runner-status-matrix.json
	@cp -f .artifacts/governance-summary.md .artifacts/runner-status-matrix.md
	@cp -f .artifacts/governance-trace.json .artifacts/runner-status-ingest-log.json

ci-gate:
	@dc-runner governance critical --spec-source $(SPEC_SOURCE)
	@dc-runner ci gate-summary

check:
	@dc-runner governance run --spec-source $(SPEC_SOURCE)
	@dc-runner docs generate-check --spec-source $(SPEC_SOURCE)
	@mkdir -p .artifacts
	@cp -f .artifacts/governance-summary.json .artifacts/runner-status-matrix.json
	@cp -f .artifacts/governance-summary.md .artifacts/runner-status-matrix.md
	@cp -f .artifacts/governance-trace.json .artifacts/runner-status-ingest-log.json

prepush:
	@dc-runner governance critical --spec-source $(SPEC_SOURCE)
	@dc-runner governance broad --spec-source $(SPEC_SOURCE)
	@dc-runner docs generate-check --spec-source $(SPEC_SOURCE)
	@dc-runner docs-lint
	@dc-runner normalize-check --spec-source $(SPEC_SOURCE)
	@if dc-runner schema-registry-build --help >/dev/null 2>&1; then \
	  dc-runner schema-registry-build --spec-source $(SPEC_SOURCE); \
	else \
	  echo "[prepush] skipping schema-registry-build (command unavailable in current dc-runner)"; \
	fi
	@if dc-runner schema-registry-check --help >/dev/null 2>&1; then \
	  dc-runner schema-registry-check --spec-source $(SPEC_SOURCE); \
	else \
	  echo "[prepush] skipping schema-registry-check (command unavailable in current dc-runner)"; \
	fi
	@if dc-runner schema-docs-check --help >/dev/null 2>&1; then \
	  dc-runner schema-docs-check --spec-source $(SPEC_SOURCE); \
	else \
	  echo "[prepush] skipping schema-docs-check (command unavailable in current dc-runner)"; \
	fi
	@dc-runner style-check
	@mkdir -p .artifacts
	@jq -n --arg generated_at "$$(date -u +%Y-%m-%dT%H:%M:%SZ)" '{generated_at:$$generated_at, status:"ok"}' > .artifacts/gate-summary.json
	@echo "[gate] summary: $(PWD)/.artifacts/gate-summary.json"
