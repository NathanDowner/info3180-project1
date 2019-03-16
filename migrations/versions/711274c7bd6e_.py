"""empty message

Revision ID: 711274c7bd6e
Revises: f25779f4da66
Create Date: 2019-03-16 18:28:09.956718

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '711274c7bd6e'
down_revision = 'f25779f4da66'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profiles', 'biography')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('biography', sa.VARCHAR(length=256), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
