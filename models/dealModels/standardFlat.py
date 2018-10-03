from flask import current_app as app

db = app.db


class StandardFlat(db.Model):
    __tablename__ = 'standardFlat'

    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(100), unique=False)
    tarif = db.Column(db.String(100), unique=False)
    agreement_fk = db.Column(db.Integer, db.ForeignKey('agreements.id'))

    def __init__(self, service=None, tarif=None, agreement_fk=None):
        self.service = service
        self.tarif = tarif
        self.agreement_fk = agreement_fk

    def __repr__(self):
        return "<StandardFlat(service='%s', tarif='%s', agreement_fk='%s')>" % (
                   self.service, self.tarif, self.agreement_fk)