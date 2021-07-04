from db.base import db
from repositories.bands import BandRepository
from repositories.songs import SongRepository
from repositories.users import UserRepository
from repositories.members import MemberRepository


def get_user_repository():
    return UserRepository(db)


def get_song_repository():
    return SongRepository(db)


def get_band_repository():
    return BandRepository(db)


def get_member_repository():
    return MemberRepository(db)
