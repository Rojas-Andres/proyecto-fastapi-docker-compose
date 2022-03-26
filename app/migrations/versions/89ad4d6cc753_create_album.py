"""create album

Revision ID: 89ad4d6cc753
Revises: 2104fc0a707e
Create Date: 2022-03-25 16:07:01.217860

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89ad4d6cc753'
down_revision = '2104fc0a707e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('album',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_album_id'), 'album', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_album_id'), table_name='album')
    op.drop_table('album')
    # ### end Alembic commands ###
