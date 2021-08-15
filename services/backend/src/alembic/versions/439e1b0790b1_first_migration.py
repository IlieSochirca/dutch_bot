"""First Migration

Revision ID: 439e1b0790b1
Revises: 
Create Date: 2021-08-15 20:40:52.221967

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '439e1b0790b1'
down_revision = None
branch_labels = None
depends_on = None


def create_dictionary_table():
    """method that will create "Dictionary" table """
    op.create_table(
        "dictionary",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("dutch", sa.String(150)),
        sa.Column("english", sa.String(150)),
        sa.Column("part_of_speech", sa.String(150)),

    )


def upgrade():
    create_dictionary_table()


def downgrade():
    op.drop_table("dictionary")
