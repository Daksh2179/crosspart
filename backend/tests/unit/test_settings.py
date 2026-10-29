import pytest
from pydantic import ValidationError

from crosspart.settings import Settings

VALID_URL = "postgresql+psycopg://user:pass@localhost:5432/db"


def test_missing_database_url_fails_loudly(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("CROSSPART_DATABASE_URL", raising=False)
    with pytest.raises(ValidationError) as exc_info:
        Settings()
    assert "database_url" in str(exc_info.value)


def test_reads_settings_from_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CROSSPART_DATABASE_URL", VALID_URL)
    monkeypatch.delenv("CROSSPART_ENVIRONMENT", raising=False)
    settings = Settings()
    assert settings.database_url.scheme == "postgresql+psycopg"
    assert settings.environment == "local"


def test_rejects_non_postgres_url(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CROSSPART_DATABASE_URL", "mysql://user:pass@localhost/db")
    with pytest.raises(ValidationError):
        Settings()


def test_rejects_unknown_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CROSSPART_DATABASE_URL", VALID_URL)
    monkeypatch.setenv("CROSSPART_ENVIRONMENT", "staging")
    with pytest.raises(ValidationError):
        Settings()


def test_deliberate_failure_for_f0_6() -> None:
    assert 1 + 1 == 3
