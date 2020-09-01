"""empty message

Revision ID: 440d678b7b53
Revises: 05aad8b1443c
Create Date: 2020-08-31 19:51:00.245686

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '440d678b7b53'
down_revision = '05aad8b1443c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('Genre', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('Show', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('Venue', sa.Column('created_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'created_at')
    op.drop_column('Show', 'created_at')
    op.drop_column('Genre', 'created_at')
    op.drop_column('Artist', 'created_at')
    # ### end Alembic commands ###
