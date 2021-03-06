"""Add is_moderated column

Revision ID: 5c1cc7c81f11
Revises: 928586bf69e2
Create Date: 2021-01-23 22:40:16.855017

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c1cc7c81f11'
down_revision = '928586bf69e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('exam_statuses',
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('name', name=op.f('pk_exam_statuses'))
    )
    op.bulk_insert(sa.sql.table('exam_statuses', sa.sql.column('name', sa.String)),
        [
            {'name': 'На рассмотрении'},
            {'name': 'Одобрено'},
            {'name': 'Отклонено'},
        ]
    )
    op.add_column('exam_reviews', sa.Column('is_moderated', sa.String(length=128), nullable=False))
    op.create_foreign_key(op.f('fk_exam_reviews_is_moderated_exam_statuses'), 'exam_reviews', 'exam_statuses', ['is_moderated'], ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_exam_reviews_is_moderated_exam_statuses'), 'exam_reviews', type_='foreignkey')
    op.drop_column('exam_reviews', 'is_moderated')
    op.drop_table('exam_statuses')
    # ### end Alembic commands ###
