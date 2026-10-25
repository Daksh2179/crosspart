from sqlalchemy import Engine, create_engine

from crosspart.settings import Settings


def create_db_engine(settings: Settings) -> Engine:
    return create_engine(str(settings.database_url), pool_pre_ping=True)
