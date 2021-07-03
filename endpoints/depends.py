from db.base import db
from repositories.songs import SongRepository
from repositories.users import UserRepository


def get_user_repository():
    return UserRepository(db)


def get_song_repository():
    return SongRepository(db)
