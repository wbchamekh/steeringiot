from flask import current_app as app

db = app.db


class Coverage(db.Model):
    __tablename__ = 'coverage'

    id = db.Column(db.Integer, primary_key=True)
    alias = db.Column(db.String(5), unique=False)
    cov = db.Column(db.Integer, unique=False)
    network_fk = db.Column(db.Integer, db.ForeignKey('network.id'))
    country_fk = db.Column(db.Integer, db.ForeignKey('country.id'))

    def __init__(self, alias=None, cov=None, network_fk=None, country_fk=None):
        self.alias = alias
        self.cov = cov
        self.network_fk = network_fk
        self.country_fk = country_fk

    def __repr__(self):
        return "<Coverage(alias='%s', cov='%s', network_fk='%s', country_fk='%s')>" % (self.alias, self.cov, self.network_fk, self.country_fk)
