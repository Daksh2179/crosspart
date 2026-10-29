"""Temporary revision with a failing downgrade, for acceptance test F0-8.

Revision ID: 0001
Revises: 0000
Create Date: 2026-10-26
"""

from collections.abc import Sequence

revision: str = "0001"
down_revision: str | None = "0000"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    raise RuntimeError("Deliberate downgrade failure for acceptance test F0-8.")