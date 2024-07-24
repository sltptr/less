"""Init

Revision ID: a330e0948ae4
Revises: 
Create Date: 2024-07-24 18:13:25.233434

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "eead2be32444"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "item",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("link", sa.String(), nullable=False),
        sa.Column(
            "prediction", sa.Enum("NEGATIVE", "POSITIVE", name="label"), nullable=False
        ),
        sa.Column(
            "label", sa.Enum("NEGATIVE", "POSITIVE", name="label"), nullable=True
        ),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("author", sa.String(), nullable=True),
        sa.Column("category", sa.String(), nullable=True),
        sa.Column("comments", sa.String(), nullable=True),
        sa.Column("enclosure", sa.String(), nullable=True),
        sa.Column("guid", sa.String(), nullable=True),
        sa.Column("pubDate", sa.String(), nullable=True),
        sa.Column("source", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_item")),
        sa.UniqueConstraint("title", "source", name=op.f("uq_item_title")),
    )
    op.create_index(op.f("ix_item_title"), "item", ["title"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_item_title"), table_name="item")
    op.drop_table("item")
    # ### end Alembic commands ###