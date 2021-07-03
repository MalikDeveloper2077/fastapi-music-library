import datetime

import sqlalchemy

from .base import metadata


songs = sqlalchemy.Table(
    'songs',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column('name', sqlalchemy.String, nullable=False),
    sqlalchemy.Column('band', sqlalchemy.String, nullable=False),
    sqlalchemy.Column('lyrics', sqlalchemy.String),
    sqlalchemy.Column('streams', sqlalchemy.Integer, default=0),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime, default=datetime.datetime.utcnow())
)
