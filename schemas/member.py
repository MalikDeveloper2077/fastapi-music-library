from typing import Optional

from pydantic import BaseModel, Field


class MemberIn(BaseModel):
    name: str = Field(min_length=2)
    surname: str = Field(min_length=2)
    age: int = Field(gt=0)
    band_id: Optional[int] = None


class MemberOut(MemberIn):
    id: Optional[int] = None
