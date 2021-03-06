"""like

Revision ID: 26fd16a11708
Revises: 69b3373ee6e1
Create Date: 2018-04-22 09:52:35.651880

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26fd16a11708'
down_revision = '69b3373ee6e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('video_like',
    sa.Column('video_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['video_id'], ['video.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('video_like')
    # ### end Alembic commands ###
