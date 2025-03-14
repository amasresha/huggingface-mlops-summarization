# Makefile for MLOps Text Summarization Project

install:
	pip install --upgrade pip && \
	pip install -r requirements.txt

test:
	python -m pytest -vv --cov=app --cov-report=term-missing tests/

debug:
	python -m pytest -vv --pdb

one-test:
	python -m pytest -vv tests/test_greeting.py::test_my_names

run:
	python app.py