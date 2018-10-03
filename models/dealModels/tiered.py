from flask import current_app as app

db = app.db


class Tiered(db.Model):
    __tablename__ = 'tiered'

    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(100), unique=False)
    tiers = db.Column(db.String(100), unique=False)
    tierService = db.Column(db.String(100), unique=False)
    agreement_fk = db.Column(db.Integer, db.ForeignKey('agreements.id'))

    def __init__(self, service=None, tiers=None, tierService=None, agreement_fk=None):
        self.service = service
        self.tierService = tierService
        self.tiers = tiers
        self.agreement_fk = agreement_fk

    def __repr__(self):
        return "<Tiered(service='%s', tiers='%s', tierService='%s', agreement_fk='%s')>" % (
                   self.service, self.tiers, self.tierService, self.agreement_fk)