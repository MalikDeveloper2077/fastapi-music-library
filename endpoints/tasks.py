import time

from endpoints.depends import get_band_repository
from schemas.band import BandIn


async def create_band_license(band_id: int):
    time.sleep(10)  # making the license...
    band_repository = get_band_repository()

    band = await band_repository.get_by_id(band_id)
    band_in = BandIn.parse_obj(band)
    band_in.license = True

    await band_repository.update(id=band_id, band=band_in)
