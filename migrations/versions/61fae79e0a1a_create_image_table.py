"""Create image table

Revision ID: 61fae79e0a1a
Revises: 4c788bf25ce0
Create Date: 2022-04-15 21:07:36.651072

"""
from alembic import op
from sqlalchemy import Integer, Column, ForeignKey, String, Text
from datetime import datetime


# revision identifiers, used by Alembic.
revision = '61fae79e0a1a'
down_revision = '4c788bf25ce0'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
            'image',
            Column('id', Integer, primary_key=True),
            Column('imgur_id', String(25), nullable=False, unique=True),
            Column('description', Text),
            Column('link', String(128), nullable=False),
            Column('post_id', Integer, ForeignKey('post.id')),
            Column('created_at', Integer, default=datetime.utcnow)
    )


def downgrade():
    op.drop_table('image')
