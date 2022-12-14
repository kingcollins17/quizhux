"""first revision

Revision ID: 5262ca14b87b
Revises: 
Create Date: 2022-08-28 20:35:31.905579

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5262ca14b87b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('record',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('score', sa.String(), nullable=False),
    sa.Column('date_added', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('record')
    # ### end Alembic commands ###
