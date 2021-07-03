from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class SongIn(BaseModel):
    name: str
    band: str
    lyrics: Optional[str]
    streams: int = 0


class SongOut(SongIn):
    id: Optional[int] = None
    created_at: datetime
