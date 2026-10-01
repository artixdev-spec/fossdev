VENV = ../.venv
PIP = $(VENV)/bin/pip
PYTEST = $(VENV)/bin/pytest
SPHINXBUILD = $(abspath $(VENV)/bin/sphinx-build)

.DEFAULT_GOAL := help
.PHONY: help install test docs clean

help:
	@echo "Targets: install, test, docs, clean"

install:
	$(PIP) install -r requirements.txt

test:
	PYTHONPATH=src $(PYTEST) tests

docs:
	$(MAKE) -C docs html SPHINXBUILD=$(SPHINXBUILD)
	@echo "Open docs/build/html/index.html"

clean:
	rm -rf docs/build
