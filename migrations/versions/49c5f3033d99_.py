"""empty message

Revision ID: 49c5f3033d99
Revises: 711274c7bd6e
Create Date: 2019-03-16 18:28:36.655247

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49c5f3033d99'
down_revision = '711274c7bd6e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('biography', sa.String(length=1000), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profiles', 'biography')
    # ### end Alembic commands ###
