from typing import List

from fastapi import APIRouter, Depends, BackgroundTasks

from endpoints import tasks
from endpoints.depends import get_band_repository, get_member_repository
from schemas.band import BandOut, BandIn
from repositories.bands import BandRepository
from repositories.members import MemberRepository


router = APIRouter()


@router.get('/', response_model=List[BandOut])
async def get_bands(bands: BandRepository = Depends(get_band_repository)):
    return await bands.get_all()


@router.get('/{id}', response_model=BandOut)
async def get_band(
    id: int,
    bands: BandRepository = Depends(get_band_repository),
    members: MemberRepository = Depends(get_member_repository)
):
    band = await bands.get_by_id(id)
    band.members = await members.get_by_band(band.id)
    return band


@router.post('/', response_model=BandOut)
async def create_band(
    band: BandIn,
    background_tasks: BackgroundTasks,
    bands: BandRepository = Depends(get_band_repository),
):
    band_out = await bands.create(band)
    background_tasks.add_task(tasks.create_band_license, band_out.id)
    return band_out
