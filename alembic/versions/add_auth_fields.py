"""Add email and hashed_password to user table

Revision ID: add_auth_fields
Revises: 4b9d34a1eb2d
Create Date: 2025-12-07

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'add_auth_fields'
down_revision: Union[str, None] = '4b9d34a1eb2d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Добавляем новые колонки
    op.add_column('user', sa.Column('email', sa.String(255), nullable=True))
    op.add_column('user', sa.Column('hashed_password', sa.String(255), nullable=True))
    
    # Мигрируем данные: используем api_key как временный email для существующих пользователей
    op.execute("UPDATE \"user\" SET email = nickname || '@temp.local', hashed_password = 'migrated_user_needs_password_reset'")
    
    # Делаем колонки обязательными и уникальными
    op.alter_column('user', 'email', nullable=False)
    op.alter_column('user', 'hashed_password', nullable=False)
    op.create_unique_constraint('uq_user_email', 'user', ['email'])
    
    # Удаляем старую колонку api_key
    op.drop_constraint('user_api_key_key', 'user', type_='unique')
    op.drop_column('user', 'api_key')


def downgrade() -> None:
    # Восстанавливаем api_key
    op.add_column('user', sa.Column('api_key', sa.String(30), nullable=True))
    op.execute("UPDATE \"user\" SET api_key = 'key_' || id")
    op.alter_column('user', 'api_key', nullable=False)
    op.create_unique_constraint('user_api_key_key', 'user', ['api_key'])
    
    # Удаляем новые колонки
    op.drop_constraint('uq_user_email', 'user', type_='unique')
    op.drop_column('user', 'hashed_password')
    op.drop_column('user', 'email')
