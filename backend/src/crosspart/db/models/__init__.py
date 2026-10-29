"""ORM models. Import every model module here so Alembic can detect it."""

from sqlalchemy.orm import Mapped, mapped_column

from crosspart.db.base import Base


class TemporaryDriftProbe(Base):
    """Temporary model with no migration, for acceptance test F0-9."""

    __tablename__ = "temporary_drift_probe"

    id: Mapped[int] = mapped_column(primary_key=True)
