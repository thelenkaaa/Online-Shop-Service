"""empty message

Revision ID: 37c3308ba315
Revises: 
Create Date: 2022-11-14 00:13:44.715352

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37c3308ba315'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'address',
        sa.Column('idaddress', sa.Integer(), nullable=False),
        sa.Column('street', sa.String(length=255), nullable=False),
        sa.Column('city', sa.String(length=255), nullable=False),
        sa.Column('house_number', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('idaddress')
    )
    op.create_table(
        'item',
        sa.Column('iditem', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('amount', sa.Integer(), nullable=True),
        sa.Column('price', sa.Integer(), nullable=True),
        sa.Column('status', sa.String(length=255), nullable=False),
        sa.Column('category', sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint('iditem')
    )
    op.create_table(
        'user',
        sa.Column('iduser', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(length=255), nullable=False),
        sa.Column('firstname', sa.String(length=255), nullable=False),
        sa.Column('lastname', sa.String(length=255), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False),
        sa.Column('password', sa.String(length=255), nullable=False),
        sa.Column('phone', sa.String(length=255), nullable=False),
        sa.Column('address_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['address_id'], ['address.idaddress'], ),
        sa.PrimaryKeyConstraint('iduser')
    )
    op.create_table(
        'order',
        sa.Column('idorder', sa.Integer(), nullable=False),
        sa.Column('quantity', sa.Integer(), nullable=True),
        sa.Column('orderDate', sa.DateTime(), nullable=False),
        sa.Column('status', sa.String(length=255), nullable=False),
        sa.Column('payment_method', sa.String(length=255), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('item_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['item_id'], ['item.iditem'], ),
        sa.ForeignKeyConstraint(['user_id'], ['user.iduser'], ),
        sa.PrimaryKeyConstraint('idorder')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order')
    op.drop_table('user')
    op.drop_table('item')
    op.drop_table('address')
    # ### end Alembic commands ###