# Valhalla's Path

.PHONY: help start run test install clean format lint quality

PYTHON = py
PIP = py -m pip

help:
	@echo "Comandos disponíveis:"
	@echo "  make install"
	@echo "  make start"
	@echo "  make test"
	@echo "  make lint"
	@echo "  make format"
	@echo "  make quality"
	@echo "  make clean"

run:
	$(PYTHON) main.py

start: run

test:
	pytest

install:
	$(PIP) install -r requirements.txt

format:
	black .

lint:
	ruff check .

quality: lint test

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete