from flask import current_app as app

db = app.db


class Network(db.Model):
    __tablename__ = 'network'

    id = db.Column(db.Integer, primary_key=True)
    alias = db.Column(db.String(255), unique=True)
    country_fk = db.Column(db.Integer, db.ForeignKey('country.id'))
    coverages = db.relationship('Coverage', backref='network')
    agreements = db.relationship('AgreementDetails', backref='network')
    siots = db.relationship('StandardIot', backref='network')
    diots = db.relationship('DiscountedIot', backref='network')

    def __init__(self, alias=None):
        self.alias = alias

    def __repr__(self):
        return "<Customer(alias='%s')>" % self.alias
