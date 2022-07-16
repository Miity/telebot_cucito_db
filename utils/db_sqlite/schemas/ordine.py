from http import client
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.orm import relationship

from utils.db_sqlite.base import MyMixin, TimedBaseModel


class Order(TimedBaseModel, MyMixin):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    title = Column(String(30), unique=True)
    description = Column(String(250))
    # aiogram simple callendar
    date_limit = Column(Date)
    client = relationship("Client", uselist=False, back_populates="order")
    boat = relationship("Boat", uselist=True, back_populates="order")


    def __repr__(self):
       return f"Ordine(id={self.id!r}, title={self.title!r})"

    def text_info(self) -> str:
        text = '#' + str(self.id) + " Client: " + self.client.name + '\n'
        text += 'title: ' + str(self.title) + '\n'
        text += 'date limit:'
        return text
    
    def add_data(self, data: dict):
        if data.get('title'):
            self.name = data.get('title')
        if data.get('description'):
            self.phone = data.get('description')
        if data.get('boat'):
            self.boat = data.get('boat')