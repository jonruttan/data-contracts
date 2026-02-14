.PHONY: help setup docs-doctor verify-docs docs-build docs-lint docs-check core-check check ci-gate test
.DEFAULT_GOAL := help

help: ## Display this help section
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_-]+:.*?## / {printf "\033[32m%-38s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

setup: ## Create .venv and install editable package with dev deps
	@python3 -m venv .venv
	@.venv/bin/python -m pip install -U pip
	@.venv/bin/python -m pip install -e '.[dev]'

docs-doctor: ## Run fast docs quality checks
	@./scripts/docs_doctor.sh

verify-docs: ## Alias for docs-doctor
	@$(MAKE) docs-doctor

docs-build: ## Generate reference docs artifacts (index, coverage, graph)
	@./scripts/runner_adapter.sh docs-build

docs-lint: ## Run docs metadata/schema and quality lint checks
	@./scripts/runner_adapter.sh docs-lint

docs-check: ## Verify generated docs artifacts are up-to-date and lint passes
	@./scripts/runner_adapter.sh docs-build-check
	@./scripts/runner_adapter.sh docs-lint

check: ## Alias for ci-gate
	@$(MAKE) ci-gate

core-check: ## Run lightweight core adoption checks
	@./scripts/core_gate.sh

ci-gate: ## Run full CI gate locally
	@./scripts/ci_gate.sh

test: ## Run pytest
	@.venv/bin/python -m pytest
