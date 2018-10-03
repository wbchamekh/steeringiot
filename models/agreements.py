from flask import current_app as app

db = app.db


class AgreementDetails(db.Model):
    __tablename__ = 'agreements'

    id = db.Column(db.Integer, primary_key=True)
    agreementId = db.Column(db.Integer, unique=True)
    aparty = db.Column(db.String(255), unique=False)
    bparty = db.Column(db.String(255), unique=True)
    start = db.Column(db.String(120), unique=False)
    stop = db.Column(db.String(120), unique=False)
    autoreconduction = db.Column(db.String(5), unique=False)
    groupdeal = db.Column(db.Boolean, unique=False)
    network_fk = db.Column(db.Integer, db.ForeignKey('network.id'))

    def __init__(self, agreementId=None, aparty=None, bparty=None, start=None,
                 stop=None, autoreconduction=None, groupdeal=None, network_fk=None):
        self.agreementId = agreementId
        self.aparty = aparty
        self.bparty = bparty
        self.start = start
        self.stop = stop
        self.autoreconduction = autoreconduction
        self.groupdeal = groupdeal
        self.network_fk = network_fk

    def __repr__(self):
        return "<Agreements(agreementId='%s', aparty='%s', bparty='%s', start='%s', stop='%s'" \
               ", autoreconduction='%s', groupdeal='%s', network_fk='%s')>" % (
               self.agreementId, self.agreementId, self.bparty
               , self.start, self.stop, self.autoreconduction,
               self.groupdeal, self.network_fk)
