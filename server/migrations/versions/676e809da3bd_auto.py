"""auto

Revision ID: 676e809da3bd
Revises: 9f9ffe5f017c
Create Date: 2023-09-06 20:47:22.027866

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '676e809da3bd'
down_revision = '9f9ffe5f017c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('videos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('timestamp', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('thumbnail', sa.String(), nullable=True))
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('videos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DATE(), nullable=True))
        batch_op.drop_column('thumbnail')
        batch_op.drop_column('timestamp')

    # ### end Alembic commands ###