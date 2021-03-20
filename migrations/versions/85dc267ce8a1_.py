"""empty message

Revision ID: 85dc267ce8a1
Revises: d9a66dc15793
Create Date: 2021-03-15 19:39:48.568140

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85dc267ce8a1'
down_revision = 'd9a66dc15793'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('sessTokenTime', sa.Float(), nullable=True))
    op.execute('UPDATE "user" SET sessTokenTime = 0') # apply default
    with op.batch_alter_table('user') as batch_op:
        batch_op.alter_column('sessTokenTime', nullable=False)
        batch_op.drop_column('session_token')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('session_token', sa.VARCHAR(length=128), nullable=False))
    op.drop_column('user', 'sessTokenTime')
    # ### end Alembic commands ###
