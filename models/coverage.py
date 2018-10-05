from flask import current_app as app

db = app.db


class Coverage(db.Model):
    __tablename__ = 'coverage'

    id = db.Column(db.Integer, primary_key=True)
    alias = db.Column(db.String(5), unique=False)
    cov = db.Column(db.Integer, unique=False)
    country_fk = db.Column(db.Integer, db.ForeignKey('country.id'))
    network_fk = db.Column(db.Integer, db.ForeignKey('network.id'))
    siots = db.relationship('StandardIot', backref='coverage')

    def __init__(self, alias=None, cov=None, country_fk=None, network_fk=None):
        self.alias = alias
        self.cov = cov
        self.country_fk = country_fk
        self.network_fk = network_fk

    def __repr__(self):
        return "<Coverage(alias='%s', cov='%s', country_fk='%s', network_fk='%s')>" % (
        self.alias, self.cov, self.country_fk, self.network_fk)
