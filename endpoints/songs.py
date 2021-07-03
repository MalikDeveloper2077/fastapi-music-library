from typing import List

from fastapi import APIRouter, Depends

from endpoints.depends import get_song_repository
from schemas.song import SongOut, SongIn
from repositories.songs import SongRepository


router = APIRouter()


@router.get('/', response_model=List[SongOut])
async def get_songs(songs: SongRepository = Depends(get_song_repository)):
    return await songs.get_all()


@router.get('/{id}', response_model=SongOut)
async def get_song(id: int, songs: SongRepository = Depends(get_song_repository)):
    return await songs.get_by_id(id)


@router.post('/', response_model=SongOut)
async def create_song(song: SongIn, songs: SongRepository = Depends(get_song_repository)):
    return await songs.create(song)


@router.put('/{id}', response_model=SongOut)
async def create_song(id: int, song: SongIn, songs: SongRepository = Depends(get_song_repository)):
    return await songs.update(id, song)
