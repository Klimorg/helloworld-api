.PHONY: api-run
api-run:
	uvicorn app.main:app --reload --host 0.0.0.0

.PHONY: tests
tests:
	python -m pytest -v --cov
