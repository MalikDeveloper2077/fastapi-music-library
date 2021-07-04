import sqlalchemy

from .base import metadata


members = sqlalchemy.Table(
    'members',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column('band_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('bands.id')),
    sqlalchemy.Column('name', sqlalchemy.String, nullable=False),
    sqlalchemy.Column('surname', sqlalchemy.String, nullable=False),
    sqlalchemy.Column('age', sqlalchemy.SmallInteger),
)
