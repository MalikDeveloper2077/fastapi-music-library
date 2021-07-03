from starlette.config import Config


config = Config('.env')

DB_URL = config('FAST_DB_URL', cast=str, default='')
JWT_SECRET_KEY = config('JWT_SECRET_KEY', cast=str,
                        default='a6259c09eab226da171aa58387db2956f8c5cdf8fff1381fa1f9cc662c524b41')

