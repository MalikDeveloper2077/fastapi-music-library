import uvicorn
from fastapi import FastAPI

from endpoints import users, songs, bands, members
from db.base import db


app = FastAPI(title='Spotify API')

app.include_router(users.router, prefix='/users', tags=['users'])
app.include_router(songs.router, prefix='/songs', tags=['songs'])
app.include_router(bands.router, prefix='/bands', tags=['bands'])
app.include_router(members.router, prefix='/members', tags=['members'])


@app.on_event('startup')
async def startup():
    await db.connect()


@app.on_event('shutdown')
async def shutdown():
    await db.disconnect()


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
