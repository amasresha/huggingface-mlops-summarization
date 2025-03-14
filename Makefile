# Makefile for MLOps Text Summarization Project

install:
	pip install --upgrade pip && pip install -r requirements.txt

test:
	pytest -vv tests/

run:
	python app.py

format:
	black .

lint:
	flake8 .

clean:
	rm -rf .pytest_cache __pycache__ */__pycache__

help:
	@echo "Available targets:"
	@echo "  install       - Install dependencies"
	@echo "  test          - Run basic tests"
	@echo "  run           - Run the Gradio app"
	@echo "  format        - Format code using black"
	@echo "  lint          - Lint code using flake8"
	@echo "  clean         - Clean up temporary files"
	@echo "  help          - Show this help message"