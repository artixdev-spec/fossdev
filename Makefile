PYTHON = .venv/bin/python
PIP = .venv/bin/pip

SRC = testing/princple/src
TESTS = testing/princple/tests

.PHONY: help venv install test typecheck format lint check

help:
	@echo "Available targets: venv, install, test, typecheck, format, lint, check"

venv:
	python3 -m venv .venv

install: venv
	$(PIP) install -r requirements.txt

test:
	.venv/bin/pytest $(TESTS)

typecheck:
	.venv/bin/mypy $(SRC)

format:
	.venv/bin/black $(SRC)

lint:
	.venv/bin/ruff check $(SRC)

check: typecheck lint test
