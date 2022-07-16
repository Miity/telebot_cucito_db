
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from utils.db_sqlite.base import MyMixin, TimedBaseModel


class Client(TimedBaseModel, MyMixin):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True)
    phone = Column(String(15))
    boat = relationship("Boat", uselist=False, back_populates="owner")

    def __repr__(self):
       return f"DbClients(id={self.id!r}, name={self.name!r})"

    def text_info(self) -> str:
        text = '#' + str(self.id) + " owner: " + self.name + '\n'
        text += 'phone: ' + str(self.phone) + '\n'
        return text
    
    def add_data(self, data: dict):
        if data.get('name'):
            self.name = data.get('name')
        if data.get('phone'):
            self.phone = data.get('phone')
        if data.get('boat'):
            self.boat = data.get('boat')