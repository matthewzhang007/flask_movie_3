"""admin email

Revision ID: d65eac3fc1f5
Revises: 01cf29c512b8
Create Date: 2018-05-02 20:17:02.306214

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd65eac3fc1f5'
down_revision = '01cf29c512b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('admin', sa.Column('confirmed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('admin', 'confirmed')
    # ### end Alembic commands ###
