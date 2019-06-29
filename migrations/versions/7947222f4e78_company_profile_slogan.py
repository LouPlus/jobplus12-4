"""Company Profile Slogan

Revision ID: 7947222f4e78
Revises: 6b1fff42214e
Create Date: 2019-06-29 23:50:42.798983

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7947222f4e78'
down_revision = '6b1fff42214e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('company_detail', sa.Column('slogan', sa.String(length=256), nullable=True))
    op.drop_column('company_detail', 'team_introduction')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('company_detail', sa.Column('team_introduction', mysql.VARCHAR(length=256), nullable=True))
    op.drop_column('company_detail', 'slogan')
    # ### end Alembic commands ###