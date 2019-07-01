"""prepare for company admin

Revision ID: 6b1fff42214e
Revises: f3c19cddc5a7
Create Date: 2019-06-29 23:37:48.172287

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6b1fff42214e'
down_revision = 'f3c19cddc5a7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('delivery', sa.Column('companyID', sa.Integer(), nullable=True))
    op.add_column('delivery', sa.Column('jobID', sa.Integer(), nullable=True))
    op.add_column('delivery', sa.Column('userID', sa.Integer(), nullable=True))
    op.drop_constraint('delivery_ibfk_2', 'delivery', type_='foreignkey')
    op.drop_constraint('delivery_ibfk_1', 'delivery', type_='foreignkey')
    op.create_foreign_key(None, 'delivery', 'user', ['userID'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'delivery', 'job', ['jobID'], ['id'], ondelete='SET NULL')
    op.drop_column('delivery', 'job_id')
    op.drop_column('delivery', 'company_id')
    op.drop_column('delivery', 'user_id')
    op.add_column('job', sa.Column('companyID', sa.Integer(), nullable=True))
    op.drop_constraint('job_ibfk_1', 'job', type_='foreignkey')
    op.create_foreign_key(None, 'job', 'user', ['companyID'], ['id'], ondelete='CASCADE')
    op.drop_column('job', 'company_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('job', sa.Column('company_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'job', type_='foreignkey')
    op.create_foreign_key('job_ibfk_1', 'job', 'user', ['company_id'], ['id'], ondelete='CASCADE')
    op.drop_column('job', 'companyID')
    op.add_column('delivery', sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('delivery', sa.Column('company_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('delivery', sa.Column('job_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'delivery', type_='foreignkey')
    op.drop_constraint(None, 'delivery', type_='foreignkey')
    op.create_foreign_key('delivery_ibfk_1', 'delivery', 'job', ['job_id'], ['id'], ondelete='SET NULL')
    op.create_foreign_key('delivery_ibfk_2', 'delivery', 'user', ['user_id'], ['id'], ondelete='SET NULL')
    op.drop_column('delivery', 'userID')
    op.drop_column('delivery', 'jobID')
    op.drop_column('delivery', 'companyID')
    # ### end Alembic commands ###
