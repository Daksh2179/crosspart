# Decision log

| Date | Decision |
|---|---|
| 2026-10-25 | Python 3.12, managed with uv; `uv.lock` is committed and used locally and in CI. |
| 2026-10-25 | SQLAlchemy 2, Alembic, psycopg 3, Pydantic v2, pydantic-settings. |
| 2026-10-25 | ruff (lint and format), mypy strict, pytest with unit and integration markers. |
| 2026-10-25 | Postgres 16 for local development, CI and production. |
| 2026-10-25 | Settings come only from environment variables prefixed `CROSSPART_`; the app never reads `.env` files itself. |
| 2026-10-25 | Repository is public; `main` requires pull requests and passing checks. |
| 2026-10-25 | GHCR for images; S3 with state locking for Terraform state. |
| 2026-10-25 | Argon2id via argon2-cffi; roles limited to admin and reviewer. |