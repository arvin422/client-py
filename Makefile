.DEFAULT_GOAL := help
PYTHON ?= python
ASYNC_SOURCES := fhirclient/async_client.py fhirclient/smart.py fhirclient/_smart_types.py
ASYNC_TESTS := tests/async_client_test.py tests/smart_async_test.py
.PHONY: help lint typecheck test build check fix
help:
	@echo 'lint | typecheck | test | build | check | fix (install .[tests,smart] and the dev dependency group)'
lint:
	$(PYTHON) -m ruff check $(ASYNC_SOURCES) $(ASYNC_TESTS)
	$(PYTHON) -m ruff format --check $(ASYNC_SOURCES) $(ASYNC_TESTS)
typecheck:
	$(PYTHON) -m basedpyright --pythonpath $(PYTHON)
test:
	$(PYTHON) -m pytest
build:
	$(PYTHON) -m build --outdir build/dist
check: lint typecheck test build
fix:
	$(PYTHON) -m ruff check --fix $(ASYNC_SOURCES) $(ASYNC_TESTS)
	$(PYTHON) -m ruff format $(ASYNC_SOURCES) $(ASYNC_TESTS)
