.PHONY: help docs-doctor ci-gate test

help:
	@echo "Targets:"
	@echo "  make docs-doctor  - Run fast docs quality checks"
	@echo "  make ci-gate      - Run full CI gate locally"
	@echo "  make test         - Run pytest"

docs-doctor:
	@./scripts/docs_doctor.sh

ci-gate:
	@./scripts/ci_gate.sh

test:
	@.venv/bin/python -m pytest
