"""Rating images table

Revision ID: f06c21aa37e6
Revises: 6fc9e426e339
Create Date: 2020-01-05 23:32:52.618263

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f06c21aa37e6'
down_revision = '6fc9e426e339'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rating_images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_path', sa.String(length=120), nullable=True),
    sa.Column('image_id', sa.String(length=120), nullable=True),
    sa.Column('rating_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['rating_id'], ['rating.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_column('rating', 'image_path')
    op.drop_column('rating', 'image_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rating', sa.Column('image_id', sa.VARCHAR(length=120), nullable=True))
    op.add_column('rating', sa.Column('image_path', sa.VARCHAR(length=120), nullable=True))
    op.drop_table('rating_images')
    # ### end Alembic commands ###
