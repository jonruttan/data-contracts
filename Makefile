.PHONY: help setup docs-doctor verify-docs docs-build docs-lint docs-check normalize-check normalize-fix schema-registry-check schema-registry-build schema-docs-check schema-docs-build ci-smoke core-check check ci-gate test
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

normalize-check: ## Verify normalization across specs/contracts/tests
	@./scripts/runner_adapter.sh normalize-check

normalize-fix: ## Apply normalization rewrites across specs/contracts/tests
	@./scripts/runner_adapter.sh normalize-fix

schema-registry-check: ## Verify schema registry artifacts and docs are up-to-date
	@./scripts/runner_adapter.sh schema-registry-check
	@./scripts/runner_adapter.sh schema-docs-check

schema-registry-build: ## Build schema registry artifacts and generated schema docs
	@./scripts/runner_adapter.sh schema-registry-build
	@./scripts/runner_adapter.sh schema-docs-build

schema-docs-check: ## Verify generated schema docs snapshot is up-to-date
	@./scripts/runner_adapter.sh schema-docs-check

schema-docs-build: ## Regenerate schema docs snapshot from registry
	@./scripts/runner_adapter.sh schema-docs-build

ci-smoke: ## Fast CI preflight (governance + docs + style)
	@./scripts/runner_adapter.sh governance
	@./scripts/runner_adapter.sh docs-build-check
	@./scripts/runner_adapter.sh docs-lint
	@./scripts/runner_adapter.sh normalize-check
	@./scripts/runner_adapter.sh schema-registry-check
	@./scripts/runner_adapter.sh schema-docs-check
	@./scripts/runner_adapter.sh style-check

check: ## Alias for ci-gate
	@$(MAKE) ci-gate

core-check: ## Run lightweight core adoption checks
	@./scripts/core_gate.sh

ci-gate: ## Run full CI gate locally
	@./scripts/ci_gate.sh

test: ## Run pytest
	@.venv/bin/python -m pytest
