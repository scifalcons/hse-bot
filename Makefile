format:
	uv run ruff format

lint: format
	uv run ruff check --fix
	uv run mypy .

lint-wps: lint
	uv run flake8 . --select=WPS

# Run fast and free tests
test: lint
	uv run pytest

pre-commit: lint

run:
	uv run python __main__.py

generate-requirements:
	uv export --no-hashes --format requirements-txt > requirements.txt
