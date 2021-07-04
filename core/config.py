from starlette.config import Config


config = Config('.env')
DB_URL = config('FAST_DB_URL', cast=str, default='')
