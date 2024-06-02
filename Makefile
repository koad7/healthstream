# Makefile for Python project

# Variables
PYTHON = python3.8
PIP = $(PYTHON) -m pip
FLAKE8 = flake8
PYTEST = pytest
REQ_FILE = requirements.txt

# Default target
.PHONY: all
all: install check distcheck

# Target to install dependencies
.PHONY: install
install:
	@echo "Installing dependencies..."
	$(PIP) install --upgrade pip
	$(PIP) install -r $(REQ_FILE)

# Target to lint the code
.PHONY: lint
lint:
	@echo "Linting code with flake8..."
	$(FLAKE8) .

# Target to run tests
.PHONY: test
test:
	@echo "Running tests with pytest..."
	$(PYTEST)

# Target to check the code (lint + test)
.PHONY: check
check: lint test

# Target to perform distribution checks
.PHONY: distcheck
distcheck:
	@echo "Performing distribution checks..."
	$(PYTHON) setup.py sdist
	$(PYTHON) setup.py bdist_wheel
	@echo "Distribution checks complete."

# Clean build files
.PHONY: clean
clean:
	@echo "Cleaning up build files..."
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info
