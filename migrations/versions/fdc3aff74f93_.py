"""empty message

Revision ID: fdc3aff74f93
Revises: ac204b616dd9
Create Date: 2020-09-02 21:16:07.061855

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fdc3aff74f93'
down_revision = 'ac204b616dd9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Show', sa.Column('end_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Show', 'end_time')
    # ### end Alembic commands ###
