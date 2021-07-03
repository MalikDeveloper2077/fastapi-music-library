from typing import List

from fastapi import APIRouter, Depends

from endpoints.depends import get_user_repository
from schemas.user import User, UserIn
from repositories.users import UserRepository


router = APIRouter()


@router.get('/', response_model=List[User])
async def get_all(
        users: UserRepository = Depends(get_user_repository),
        limit: int = 100,
        skip: int = 0):
    return await users.get_all(limit=limit, skip=skip)


@router.get('/{id}', response_model=List[User])
async def get(id: int, users: UserRepository = Depends(get_user_repository)):
    return await users.get_by_id(id)


@router.post('/', response_model=User)
async def create(user: UserIn, users: UserRepository = Depends(get_user_repository)):
    return await users.create(user)


@router.put('/{id}', response_model=User)
async def update(
    id: int,
    user: UserIn,
    users: UserRepository = Depends(get_user_repository)
):
    return await users.update(id, user)
