"""empty message

Revision ID: 1e17bc4d8ab2
Revises: 
Create Date: 2023-12-17 17:59:49.788783

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e17bc4d8ab2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('gamename', sa.String(length=50), nullable=False),
    sa.Column('starttime', sa.DateTime(), nullable=False),
    sa.Column('isactive', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('game')
    # ### end Alembic commands ###