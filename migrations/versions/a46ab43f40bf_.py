"""empty message

Revision ID: a46ab43f40bf
Revises: 
Create Date: 2023-12-31 15:53:20.931334

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a46ab43f40bf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('gamename', sa.String(length=50), nullable=False),
    sa.Column('gamedescription', sa.String(length=100), nullable=False),
    sa.Column('gamelocation', sa.String(length=50), nullable=False),
    sa.Column('gamestarttime', sa.DateTime(), nullable=False),
    sa.Column('gamemaster', sa.String(length=50), nullable=False),
    sa.Column('gameassistant', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('game')
    # ### end Alembic commands ###