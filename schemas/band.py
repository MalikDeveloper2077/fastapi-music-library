from datetime import date
from typing import Optional, List

from pydantic import BaseModel

from .member import MemberOut


class BandIn(BaseModel):
    name: str
    genre: str
    created_at: Optional[date]
    license: Optional[bool] = False


class BandOut(BandIn):
    id: Optional[int] = None
    members: Optional[List[MemberOut]] = []
