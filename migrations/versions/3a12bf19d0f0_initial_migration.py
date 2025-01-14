"""Initial migration

Revision ID: 3a12bf19d0f0
Revises: 70c1ffcbb2cf
Create Date: 2024-12-17 19:11:19.021239

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a12bf19d0f0'
down_revision = '70c1ffcbb2cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('User',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('role', sa.String(length=200), nullable=False),
    sa.Column('validity', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Operator',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('image', sa.String(length=500), nullable=True),
    sa.Column('validity', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Operator')
    op.drop_table('User')
    # ### end Alembic commands ###
