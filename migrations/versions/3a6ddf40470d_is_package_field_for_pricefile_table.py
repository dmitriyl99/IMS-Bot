"""is_package field for PriceFile table

Revision ID: 3a6ddf40470d
Revises: fd411f89a4c7
Create Date: 2019-05-03 15:49:21.420611

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a6ddf40470d'
down_revision = 'fd411f89a4c7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('price_files', sa.Column('is_package', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('price_files', 'is_package')
    # ### end Alembic commands ###