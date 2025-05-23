"""Added SavedWorkouts table

Revision ID: 696c39868718
Revises: e80847f4fa3a
Create Date: 2025-05-14 21:46:53.703843

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '696c39868718'
down_revision = 'e80847f4fa3a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('saved_workouts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('day_of_week', sa.String(length=10), nullable=False),
    sa.Column('exercise_name', sa.String(length=100), nullable=False),
    sa.Column('calories_per_set', sa.Integer(), nullable=False),
    sa.Column('sets', sa.Integer(), nullable=False),
    sa.Column('reps', sa.Integer(), nullable=False),
    sa.Column('weight', sa.Integer(), nullable=False),
    sa.Column('save_date', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('saved_workouts', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_saved_workouts_day_of_week'), ['day_of_week'], unique=False)
        batch_op.create_index(batch_op.f('ix_saved_workouts_user_id'), ['user_id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('saved_workouts', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_saved_workouts_user_id'))
        batch_op.drop_index(batch_op.f('ix_saved_workouts_day_of_week'))

    op.drop_table('saved_workouts')
    # ### end Alembic commands ###
