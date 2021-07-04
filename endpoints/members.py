from typing import List

from fastapi import APIRouter, Depends

from endpoints.depends import get_member_repository
from schemas.member import MemberIn, MemberOut
from repositories.members import MemberRepository


router = APIRouter()


@router.get('/', response_model=List[MemberOut])
async def get_members(members: MemberRepository = Depends(get_member_repository)):
    return await members.get_all()


@router.post('/', response_model=MemberOut)
async def create_member(member: MemberIn, members: MemberRepository = Depends(get_member_repository)):
    return await members.create(member)
