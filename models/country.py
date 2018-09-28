from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Country(Base):
    __tablename__ = 'country'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=False)

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return "<Country(name='%s', networkList='%s')>" % self.name
