from flask import current_app as app

db = app.db


class SendOrPay(db.Model):
    __tablename__ = 'sendOrPay'

    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(100), unique=False)
    commitment = db.Column(db.String(100), unique=False)
    commitmentService = db.Column(db.String(100), unique=False)
    agreement_fk = db.Column(db.Integer, db.ForeignKey('agreements.id'))

    def __init__(self, service=None, commitment=None, commitmentService=None, agreement_fk=None):
        self.service = service
        self.commitment = commitment
        self.commitmentService = commitmentService
        self.agreement_fk = agreement_fk

    def __repr__(self):
        return "<SendOrPay(service='%s', commitment='%s', commitmentService='%s', agreement_fk='%s')>" % (
                   self.service, self.commitment, self.commitmentService, self.agreement_fk)