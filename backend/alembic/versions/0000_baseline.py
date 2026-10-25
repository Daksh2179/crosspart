"""Empty baseline revision.

Exercises the migration pipeline before any real tables exist.

Revision ID: 0000
Revises:
Create Date: 2026-10-25
"""

from collections.abc import Sequence

revision: str = "0000"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
