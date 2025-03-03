"""Create shortener schema

Revision ID: 32da89362c76
Revises:
Create Date: 2025-03-03 14:49:00.071659

"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "32da89362c76"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE SCHEMA link_shortener;")


def downgrade() -> None:
    op.execute("DROP SCHEMA link_shortener;")
