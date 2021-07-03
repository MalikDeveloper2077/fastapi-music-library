from .users import users
from .songs import songs
from .base import metadata, engine


metadata.create_all(bind=engine)
