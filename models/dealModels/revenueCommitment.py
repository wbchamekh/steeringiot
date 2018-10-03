from flask import current_app as app

db = app.db


class RevenueCommitment(db.Model):
    __tablename__ = 'revenueCommitment'

    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(100), unique=False)
    direction = db.Column(db.String(100), unique=False)
    commitment = db.Column(db.String(100), unique=False)
    agreement_fk = db.Column(db.Integer, db.ForeignKey('agreements.id'))

    def __init__(self, service=None, direction=None, commitment=None, agreement_fk=None):
        self.service = service
        self.direction = direction
        self.commitment = commitment
        self.agreement_fk = agreement_fk

    def __repr__(self):
        return "<RevenueCommitment(service='%s', direction='%s', commitment='%s', agreement_fk='%s')>" % (
                   self.service, self.direction, self.commitment, self.agreement_fk)