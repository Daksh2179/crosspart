import pytest
from sqlalchemy import text

from crosspart.db.engine import create_db_engine
from crosspart.settings import get_settings

pytestmark = pytest.mark.integration


def test_database_is_postgres_16() -> None:
    engine = create_db_engine(get_settings())
    try:
        with engine.connect() as connection:
            version = connection.execute(text("SHOW server_version_num")).scalar_one()
    finally:
        engine.dispose()
    assert 150000 <= int(version) < 160000
