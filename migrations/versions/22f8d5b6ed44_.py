"""empty message

Revision ID: 22f8d5b6ed44
Revises: 
Create Date: 2023-12-14 15:23:49.174298

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22f8d5b6ed44'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('gamename', sa.String(length=50), nullable=False),
    sa.Column('starttime', sa.DateTime(), nullable=True),
    sa.Column('gamestatus', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('game')
    # ### end Alembic commands ###