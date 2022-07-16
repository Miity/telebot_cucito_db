from utils.db_sqlite.schemas.user import User
from utils.db_sqlite.schemas.client import Client
from utils.db_sqlite.schemas.boat import Boat
from utils.db_sqlite.base import create_db


if __name__ == '__main__':
    create_db()