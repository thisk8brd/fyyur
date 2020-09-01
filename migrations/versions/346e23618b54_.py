"""empty message

Revision ID: 346e23618b54
Revises: 440d678b7b53
Create Date: 2020-08-31 20:42:56.386430

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '346e23618b54'
down_revision = '440d678b7b53'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('Show_venue_id_fkey', 'Show', type_='foreignkey')
    op.drop_constraint('Show_artist_id_fkey', 'Show', type_='foreignkey')
    op.create_foreign_key(None, 'Show', 'Artist', ['artist_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'Show', 'Venue', ['venue_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Show', type_='foreignkey')
    op.drop_constraint(None, 'Show', type_='foreignkey')
    op.create_foreign_key('Show_artist_id_fkey', 'Show', 'Artist', ['artist_id'], ['id'])
    op.create_foreign_key('Show_venue_id_fkey', 'Show', 'Venue', ['venue_id'], ['id'])
    # ### end Alembic commands ###
