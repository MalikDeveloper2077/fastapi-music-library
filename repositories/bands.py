from typing import List

from db.bands import bands
from repositories.base import BaseRepository
from schemas.band import BandOut, BandIn


class BandRepository(BaseRepository):

    async def get_all(self) -> List[BandOut]:
        query = bands.select()
        return await self.db.fetch_all(query=query)

    async def get_by_id(self, id: int) -> BandOut:
        query = bands.select().where(bands.c.id == id)
        band = await self.db.fetch_one(query=query)
        if band:
            return BandOut.parse_obj(band)

    async def create(self, band: BandIn) -> BandOut:
        band_out = BandOut(**band.dict())
        query = bands.insert().values(band_out.dict(exclude={'id', 'members'}))
        band_out.id = await self.db.execute(query=query)
        return band_out

    async def update(self, id: int, band: BandIn) -> BandOut:
        song_out = BandOut(**band.dict(), id=id)
        query = bands.update().where(bands.c.id == id).values(song_out.dict(exclude={'id', 'created_at'}))
        song_out.id = await self.db.execute(query=query)
        return song_out
