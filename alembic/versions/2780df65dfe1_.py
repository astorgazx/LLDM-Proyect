"""empty message

Revision ID: 2780df65dfe1
Revises: 7e5e0132a2b3
Create Date: 2024-04-30 12:50:34.665909

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2780df65dfe1'
down_revision: Union[str, None] = '7e5e0132a2b3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
