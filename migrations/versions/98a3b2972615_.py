"""empty message

Revision ID: 98a3b2972615
Revises: ca6dedf3b472
Create Date: 2023-04-01 09:05:55.726436

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98a3b2972615'
down_revision = 'ca6dedf3b472'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('is_public', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('permissions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('canPost', sa.Boolean(), nullable=False),
    sa.Column('canDelete', sa.Boolean(), nullable=False),
    sa.Column('canView', sa.Boolean(), nullable=False),
    sa.Column('canTimeout', sa.Boolean(), nullable=False),
    sa.Column('canAttachFiles', sa.Boolean(), nullable=False),
    sa.Column('canMute', sa.Boolean(), nullable=False),
    sa.Column('canBan', sa.Boolean(), nullable=False),
    sa.Column('canPromote', sa.Boolean(), nullable=False),
    sa.Column('canModify', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('posts',
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.PrimaryKeyConstraint('post_id', 'category_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    op.drop_table('permissions')
    op.drop_table('category')
    # ### end Alembic commands ###
