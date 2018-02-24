"""empty message

Revision ID: be11b9c1ee7d
Revises: 
Create Date: 2018-02-24 11:54:12.086641

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be11b9c1ee7d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('feedbacks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('query', sa.String(length=64), nullable=True),
    sa.Column('feature_vector', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('query')
    )
    op.create_table('images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_url', sa.String(length=128), nullable=True),
    sa.Column('feedback_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['feedback_id'], ['feedbacks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('images')
    op.drop_table('feedbacks')
    # ### end Alembic commands ###