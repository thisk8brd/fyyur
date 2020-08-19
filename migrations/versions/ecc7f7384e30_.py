"""empty message

Revision ID: ecc7f7384e30
Revises: 37a9cb9f2af8
Create Date: 2020-08-19 12:24:54.815758

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ecc7f7384e30'
down_revision = '37a9cb9f2af8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('genre_artist')
    op.add_column('Artist', sa.Column('genres', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Artist', 'genres')
    op.create_table('genre_artist',
    sa.Column('genre_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('artist_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['artist_id'], ['Artist.id'], name='genre_artist_artist_id_fkey'),
    sa.ForeignKeyConstraint(['genre_id'], ['Genre.id'], name='genre_artist_genre_id_fkey')
    )
    # ### end Alembic commands ###
