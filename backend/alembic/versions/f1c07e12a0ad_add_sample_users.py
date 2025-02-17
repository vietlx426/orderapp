"""add_sample_users

Revision ID: f1c07e12a0ad
Revises: 6661f6f76cee
Create Date: 2025-02-16 00:30:38.481858

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from datetime import datetime
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# revision identifiers, used by Alembic.
revision: str = 'f1c07e12a0ad'
down_revision: Union[str, None] = '6661f6f76cee'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create a temp table representation
    users = table('users',
        column('id', sa.Integer),
        column('email', sa.String),
        column('full_name', sa.String),
        column('hashed_password', sa.String),
        column('created_at', sa.DateTime),
        column('is_active', sa.Boolean),
        # column('is_superuser', sa.Boolean)
    )

    op.bulk_insert(users,
        [
            {
                'email': 'admin2@example.com',
                'full_name': 'Hieu Dang',
                'hashed_password': pwd_context.hash('123456'),
                'created_at': datetime.now(),
                'is_active': True,
                # 'is_superuser': False
            },
        
        ])


def downgrade() -> None:
    # Optional: Remove the sample users if you want
    op.execute("DELETE FROM users WHERE email IN ('admin@example.com')")
