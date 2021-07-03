import uvicorn
from fastapi import FastAPI

from endpoints import users, songs
from db.base import db


app = FastAPI(title='Spotify API')

app.include_router(users.router, prefix='/users', tags=['users'])
app.include_router(songs.router, prefix='/songs', tags=['songs'])


@app.on_event('startup')
async def startup():
    await db.connect()


@app.on_event('shutdown')
async def shutdown():
    await db.disconnect()


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)




















# @app.get('/')
# def home():
#     return {'song': 'demolisher'}
#
#
# @app.get('/songs', tags=['songs'])
# def get_songs(q: str = Query(None, min_length=2, max_length=10, description='Nice.')):
#     if q:
#         return {'q': q}
#     return {'q': 'unknown'}
#
#
# @app.get('/songs/{pk}', tags=['songs'])
# def get_song(pk: int = Path(..., ge=1)):
#     return {'pk': pk}
#
#
# @app.post('/songs', tags=['songs'], response_model=SongOut)
# def create_song(song: Song, release_now: bool = Body(True, description='Release just now')):
#     return {'song': song, 'release_now': release_now}
#
#
# @app.post('/bands', tags=['bands'], response_model=Band)
# def create_band(band: Band = Body(..., embed=True)):
#     return band
