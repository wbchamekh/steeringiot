from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Agreements(Base):
    __tablename__ = 'agreements'

    id = Column(Integer, primary_key=True)
    agreementId = Column(Integer, unique=True)
    aparty = Column(String(255), unique=False)
    bparty = Column(String(255), unique=True)
    start = Column(String(120), unique=False)
    stop = Column(String(120), unique=False)
    autoreconduction = Column(String(5), unique=False)
    groupdeal = Column(Boolean, unique=False)
    network = Column(String(5), unique=False)
    customer = Column(String(255), unique=False)

    def __init__(self, agreementId=None, aparty=None, bparty=None, start=None,
                 stop=None, autoreconduction=None, groupdeal=None, network=None, customer=None):
        self.agreementId = agreementId
        self.aparty = aparty
        self.bparty = bparty
        self.start = start
        self.stop = stop
        self.autoreconduction = autoreconduction
        self.groupdeal = groupdeal
        self.network = network
        self.customer = customer


    def __repr__(self):
        return "<Agreements(agreementId='%s', aparty='%s', bparty='%s', start='%s', stop='%s'" \
               ", autoreconduction='%s', groupdeal='%s', network='%s',customer_fk='%s')>" % (self.agreementId, self.agreementId, self.bparty
                                                                                             , self.start, self.stop, self.autoreconduction,
                                                                                             self.groupdeal, self.network, self.customer)
