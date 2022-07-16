
from sqlalchemy import Column, Integer
from utils.db_sqlite.base import TimedBaseModel


class User(TimedBaseModel):
    __tablename__='users'

    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer)

    def __repr__(self):
        return f"User(id={self.id!r},telegram_id={self.telegram_id!r})"

    def __init__(self, telegram_id: int):
        self.telegram_id = telegram_id
