"""Initial migration

Revision ID: e577f09a7fa2
Revises: 
Create Date: 2023-12-13 23:53:59.652602

"""
from typing import Sequence, Union

import geoalchemy2
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'e577f09a7fa2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('polygons',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('damage_class', sa.String(), nullable=True),
                    sa.Column('polygon', geoalchemy2.types.Geometry(geometry_type='POLYGON', srid=4326,
                                                                    from_text='ST_GeomFromEWKT', name='geometry'),
                              nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade() -> None:
    op.drop_table('polygons')
