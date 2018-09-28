from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True)
    name = Column(Integer, unique=True)
    networkList = Column(String(255), unique=False)
    coverages = relationship('Coverage', backref='customer_fk')

    def __init__(self, name=None, networkList=None):
        self.name = name
        self.networkList = networkList

    def __repr__(self):
        return "<Customer(name='%s', networkList='%s')>" % (self.name, self.networkList)
