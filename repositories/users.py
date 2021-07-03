from datetime import datetime
from typing import List, Optional, Union

from core.security import hash_password
from db.users import users
from schemas.user import User, UserIn
from .base import BaseRepository


class UserRepository(BaseRepository):

    async def get_all(self, limit: int = 100, skip: int = 0) -> List[User]:
        query = users.select().limit(limit).offset(skip)
        return await self.db.fetch_all(query=query)

    async def get_by_id(self, id: int) -> Union[Optional[User], None]:
        query = users.select().where(users.c.id == id)
        user = await self.db.fetch_one(query)
        if user:
            return User.parse_obj(user)

    async def get_by_email(self, email: str) -> Union[Optional[User], None]:
        query = users.select().where(users.c.email == email)
        user = await self.db.fetch_one(query)
        if user:
            return User.parse_obj(user)

    async def create(self, u: UserIn) -> User:
        user = User(
            **u.dict(exclude={'password'}),
            created_at=datetime.utcnow(),
            password=hash_password(u.password)
        )
        query = users.insert().values(**user.dict(exclude={'id'}))
        user.id = await self.db.execute(query)
        return user

    async def update(self, id: int, u: UserIn) -> User:
        user = User(
            id=id,
            created_at=datetime.utcnow(),
            password=hash_password(u.password),
            **u.dict(exclude={'password'}),
        )
        user_data = user.dict(exclude={'id', 'created_at'})
        query = users.update().where(users.c.id == id).values(**user_data)
        await self.db.execute(query)
        return user
