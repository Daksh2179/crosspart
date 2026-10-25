# CrossPart

AI-assisted RFQ processing and quotation for electronics distributors.

Status: foundation (F0). Repository skeleton and CI only. No application features yet.

## Local checks

Run from `backend/`. Requires uv and Docker.

```bash
uv sync --locked
uv run ruff check .
uv run ruff format --check .
uv run mypy
uv run pytest -m "not integration"
uv run --env-file .env pytest -m integration
uv run --env-file .env alembic upgrade head
uv run --env-file .env alembic downgrade base
uv run --env-file .env alembic upgrade head
uv run --env-file .env alembic check
```