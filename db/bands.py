import sqlalchemy

from .base import metadata


bands = sqlalchemy.Table(
    'bands',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column('name', sqlalchemy.String, nullable=False),
    sqlalchemy.Column('genre', sqlalchemy.String, nullable=False),
    sqlalchemy.Column('license', sqlalchemy.Boolean, default=False),
    sqlalchemy.Column('created_at', sqlalchemy.Date)
)
