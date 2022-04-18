"""create post table

Revision ID: 4c788bf25ce0
Revises: 
Create Date: 2022-04-15 18:32:25.427676

"""
from alembic import op
import sqlalchemy as sa
import time


# revision identifiers, used by Alembic.
revision = '4c788bf25ce0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
            'post',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('imgur_id', sa.String(25), nullable=False, unique=True),
            sa.Column('title', sa.String(512), nullable=False),
            sa.Column('created_at', sa.Integer, default=time.time())
    )


def downgrade():
    op.drop_table('post')
