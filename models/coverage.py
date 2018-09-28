from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Coverage(Base):
    __tablename__ = 'coverage'

    id = Column(Integer, primary_key=True)
    alias = Column(String(5), unique=False)
    cov = Column(Integer, unique=False)
    customer_fk = Column(Integer, ForeignKey('customer.id'))

    def __init__(self, alias=None, cov=None, customer_fk=None):
        self.alias = alias
        self.cov = cov
        self.customer_fk = customer_fk

    def __repr__(self):
        return "<Coverage(alias='%s', cov='%s', customer_fk='%s')>" % (self.alias, self.cov, self.customer_fk)
