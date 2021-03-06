"""empty message

Revision ID: 462916c3b455
Revises: da9fab729ba5
Create Date: 2018-05-30 18:43:04.125077

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '462916c3b455'
down_revision = 'da9fab729ba5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('group', sa.Column('name', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('group', 'name')
    # ### end Alembic commands ###
