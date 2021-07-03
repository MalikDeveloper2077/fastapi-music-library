from databases import Database
from sqlalchemy import create_engine, MetaData

from core.config import DB_URL


db = Database(DB_URL)
metadata = MetaData()
engine = create_engine(DB_URL)
