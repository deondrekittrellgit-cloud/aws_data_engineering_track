PYTHON := python3
VENV := .venv
PIP := $(VENV)/bin/pip

.PHONY: help venv install lint format test run-sample

help:
	@echo ""
	@echo "Commands:"
	@echo "  make venv        - create virtual environment"
	@echo "  make install     - install dependencies"
	@echo "  make lint        - run ruff lint"
	@echo "  make format      - run ruff format"
	@echo "  make test        - run pytest"
	@echo "  make run-sample  - run sample CSV -> Postgres load"
	@echo ""

venv:
	$(PYTHON) -m venv $(VENV)

install:
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	$(PIP) install -r requirements-dev.txt

lint:
	$(VENV)/bin/ruff check .

format:
	$(VENV)/bin/ruff format .

test:
	$(VENV)/bin/pytest -q

run-sample:
	$(VENV)/bin/python -m de_track.pipelines.file_to_postgres --csv data/samples/sample_people.csv
