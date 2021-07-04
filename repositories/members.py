from typing import List

from db.members import members
from repositories.base import BaseRepository
from schemas.member import MemberOut, MemberIn


class MemberRepository(BaseRepository):

    async def get_all(self) -> List[MemberOut]:
        query = members.select()
        return await self.db.fetch_all(query=query)

    async def get_by_band(self, band_id: int) -> List[MemberOut]:
        query = members.select().where(members.c.band_id == band_id)
        return await self.db.fetch_all(query=query)

    # async def get_by_id(self, id: int) -> MemberOut:
    #     query = members.select().where(members.c.id == id)
    #     band = await self.db.fetch_one(query=query)
    #     if band:
    #         return MemberOut.parse_obj(band)

    async def create(self, member: MemberIn) -> MemberOut:
        member_out = MemberOut(**member.dict())
        query = members.insert().values(member_out.dict(exclude={'id'}))
        member_out.id = await self.db.execute(query=query)
        return member_out

    # async def update(self, id: int, band: MemberIn) -> MemberOut:
    #     song_out = MemberOut(**band.dict(), id=id)
    #     query = members.update().where(members.c.id == id).values(song_out.dict(exclude={'id'}))
    #     song_out.id = await self.db.execute(query=query)
    #     return song_out
