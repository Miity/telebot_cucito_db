
import json
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from utils.db_sqlite.base import MyMixin, TimedBaseModel


class Boat(TimedBaseModel, MyMixin):
    __tablename__ = "boats"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    media = Column(String)
    owner_id = Column(Integer, ForeignKey("clients.id"), )
    owner = relationship("Client", back_populates="boat", uselist=False)

    def __repr__(self):
        return f"DbBoats(id={self.id!r}, name={self.name!r})"

    def text_info(self) -> str:
        text = '#' + str(self.id) + ' Boat title: ' + self.name + '\n'
        if self.media:
            text += 'Num of photos: ' + str(len(json.loads(self.media)))
        return text

    def add_data(self, data: dict):
        if data.get('name'):
            self.name = data.get('name')
        if data.get('media'):
            self.media = json.dumps(data.get('media'))
        if data.get('owner_id'):
            self.owner_id = data.get('owner_id')

    def list_path_to_photo(self):
        l=[]
        media = json.loads(self.media)
        for photo in media:
            path = photo.get('path')
            name = photo.get('name')
            path = path+name
            l.append(path)
        return l