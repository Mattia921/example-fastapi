"""add content column to posts table

Revision ID: 06dad315ffd8
Revises: cb2086ff9a1b
Create Date: 2022-01-17 15:03:53.262188

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06dad315ffd8'
down_revision = 'cb2086ff9a1b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
