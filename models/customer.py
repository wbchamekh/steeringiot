from flask import current_app as app

db = app.db


class Customer(db.Model):
    __tablename__ = 'customer'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, unique=True)
    networkList = db.Column(db.String(255), unique=False)
    coverages = db.relationship('Coverage', backref='customer')


    def __init__(self, name=None, networkList=None):
        self.name = name
        self.networkList = networkList


    def __repr__(self):
        return "<Customer(name='%s', networkList='%s')>" % (self.name, self.networkList)