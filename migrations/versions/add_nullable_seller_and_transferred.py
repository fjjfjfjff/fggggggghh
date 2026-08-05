"""make seller_id nullable and add TRANSFERRED status
 
Revision ID: 001_fix_seller_nullable
Revises: 
Create Date: 2026-08-05
"""
from alembic import op
import sqlalchemy as sa
 
revision = '001_fix_seller_nullable'
down_revision = None
branch_labels = None
depends_on = None
 
def upgrade() -> None:
    # Делаем seller_id nullable (для сделок созданных покупателем)
    op.alter_column('deals', 'seller_id',
                    existing_type=sa.BigInteger(),
                    nullable=True)
 
    # Добавляем статус TRANSFERRED в enum
    op.execute("ALTER TYPE dealstatus ADD VALUE IF NOT EXISTS 'transferred'")
 
def downgrade() -> None:
    op.alter_column('deals', 'seller_id',
                    existing_type=sa.BigInteger(),
                    nullable=False)
