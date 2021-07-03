from datetime import datetime
from typing import List

from db.songs import songs
from repositories.base import BaseRepository
from schemas.song import SongOut, SongIn


class SongRepository(BaseRepository):

    async def get_all(self) -> List[SongOut]:
        query = songs.select()
        return await self.db.fetch_all(query=query)

    async def get_by_id(self, id: int) -> SongOut:
        query = songs.select().where(songs.c.id == id)
        song = await self.db.fetch_one(query=query)
        if song:
            return SongOut.parse_obj(song)

    async def create(self, song: SongIn) -> SongOut:
        song_out = SongOut(**song.dict(), created_at=datetime.utcnow())
        query = songs.insert().values(song_out.dict(exclude={'id'}))
        song_out.id = await self.db.execute(query=query)
        return song_out

    async def update(self, id: int, song: SongIn) -> SongOut:
        song_out = SongOut(**song.dict(), id=id, created_at=datetime.utcnow())
        query = songs.update().where(songs.c.id == id).values(song_out.dict(exclude={'id', 'created_at'}))
        song_out.id = await self.db.execute(query=query)
        return song_out
