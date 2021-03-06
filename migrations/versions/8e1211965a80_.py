"""empty message

Revision ID: 8e1211965a80
Revises: 378aa64982bd
Create Date: 2020-09-02 17:12:24.784193

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e1211965a80'
down_revision = '378aa64982bd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('week_days_availability', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Artist', 'week_days_availability')
    # ### end Alembic commands ###
