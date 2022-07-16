from datetime import datetime
from sqlalchemy import Column, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite+pysqlite:///utils/test.db", echo=False)
session = sessionmaker(bind=engine)


Base = declarative_base()

class TimedBaseModel(Base):
    __abstract__ = True
    created_date = Column(DateTime, default=datetime.utcnow)

class MyMixin():
    def get_data(self) -> dict:
        attr = vars(self)
        dic = {}
        for k,v in attr.items():
            if not k.startswith('_') and k not in ('id', 'created_date'):
                dic[k] = v
        return dic


def create_db():
    Base.metadata.create_all(engine)

