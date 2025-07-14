build:
	uv build

install:
	uv sync

package-install:
	uv tool install dist/*.whl

package-install-force:
	uv tool install --force dist/*.whl

package-update: build package-install-force

lint:
	uv run ruff check gendiff

lint-fix:
	uv run ruff check gendiff --fix

test:
	uv run pytest

check: lint test

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml
