"""ondelete cascade implementacion

Revision ID: 9b5178fcc1f1
Revises: 4bb526729f0e
Create Date: 2022-03-26 11:03:25.218909

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b5178fcc1f1'
down_revision = '4bb526729f0e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('comment_postId_fkey', 'comment', type_='foreignkey')
    op.create_foreign_key(None, 'comment', 'post', ['postId'], ['id'], ondelete='CASCADE')
    op.drop_constraint('post_userId_fkey', 'post', type_='foreignkey')
    op.create_foreign_key(None, 'post', 'users', ['userId'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.create_foreign_key('post_userId_fkey', 'post', 'users', ['userId'], ['id'])
    op.drop_constraint(None, 'comment', type_='foreignkey')
    op.create_foreign_key('comment_postId_fkey', 'comment', 'post', ['postId'], ['id'])
    # ### end Alembic commands ###
