"""empty message

Revision ID: a21ef6cd4c9f
Revises: edb805ea8caa
Create Date: 2021-06-21 22:48:43.174113

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a21ef6cd4c9f'
down_revision = 'edb805ea8caa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Artist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('city', sa.String(length=120), nullable=False),
    sa.Column('state', sa.String(length=120), nullable=False),
    sa.Column('phone', sa.Integer(), nullable=False),
    sa.Column('image_link', sa.String(length=500), nullable=True),
    sa.Column('facebook_link', sa.String(length=120), nullable=True),
    sa.Column('website_link', sa.String(length=150), nullable=True),
    sa.Column('seeking_performance', sa.Boolean(), nullable=False),
    sa.Column('seeking_desc', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('Genre',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Venue',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('city', sa.String(length=120), nullable=False),
    sa.Column('state', sa.String(length=120), nullable=False),
    sa.Column('address', sa.String(length=120), nullable=False),
    sa.Column('phone', sa.Integer(), nullable=False),
    sa.Column('image_link', sa.String(length=500), nullable=True),
    sa.Column('facebook_link', sa.String(length=120), nullable=True),
    sa.Column('website_link', sa.String(length=150), nullable=True),
    sa.Column('seeking_talent', sa.Boolean(), nullable=False),
    sa.Column('seeking_desc', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('Show',
    sa.Column('Venue_id', sa.Integer(), nullable=False),
    sa.Column('Artist_id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['Artist_id'], ['Artist.id'], ondelete="CASCADE"),
    sa.ForeignKeyConstraint(['Venue_id'], ['Venue.id'], ondelete="CASCADE"),
    sa.PrimaryKeyConstraint('Venue_id', 'Artist_id', 'start_time')
    )
    op.create_table('artist_genres',
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['Artist.id'], ondelete="CASCADE"),
    sa.ForeignKeyConstraint(['genre_id'], ['Genre.id'], ondelete="CASCADE"),
    sa.PrimaryKeyConstraint('artist_id', 'genre_id')
    )
    op.create_table('venue_genres',
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['genre_id'], ['Genre.id'], ondelete="CASCADE"),
    sa.ForeignKeyConstraint(['venue_id'], ['Venue.id'], ondelete="CASCADE"),
    sa.PrimaryKeyConstraint('venue_id', 'genre_id'),
    
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('venue_genres')
    op.drop_table('artist_genres')
    op.drop_table('Show')
    op.drop_table('Venue')
    op.drop_table('Genre')
    op.drop_table('Artist')
    # ### end Alembic commands ###
