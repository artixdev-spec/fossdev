PYTHON = .venv/bin/python
PIP = .venv/bin/pip
PYTEST = .venv/bin/pytest
MYPY = .venv/bin/mypy
RUFF = .venv/bin/ruff
BLACK = .venv/bin/black

PROJECT = testing/princple
SRC = src
TESTS = tests

.PHONY: help venv install test typecheck format lint check clean

help:
	@echo "Available targets: venv, install, test, typecheck, format, lint, check, clean"

venv:
	python3 -m venv .venv

install: venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

test:
	cd $(PROJECT) && PYTHONPATH=$(SRC) ../../$(PYTEST) $(TESTS)

typecheck:
	cd $(PROJECT) && PYTHONPATH=$(SRC) ../../$(MYPY) --explicit-package-bases --ignore-missing-imports $(SRC) $(TESTS)

format:
	cd $(PROJECT) && ../../$(BLACK) $(SRC) $(TESTS)

lint:
	cd $(PROJECT) && PYTHONPATH=$(SRC) ../../$(RUFF) check $(SRC) $(TESTS)

check: typecheck lint test
