from flask import current_app as app

db = app.db


class InvoiceFlat(db.Model):
    __tablename__ = 'invoiceFlat'

    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(100), unique=False)
    invoicePercentage = db.Column(db.String(100), unique=False)
    agreement_fk = db.Column(db.Integer, db.ForeignKey('agreements.id'))

    def __init__(self, service=None, invoicePercentage=None, agreement_fk=None):
        self.service = service
        self.invoicePercentage = invoicePercentage
        self.agreement_fk = agreement_fk

    def __repr__(self):
        return "<InvoiceFlat(service='%s', invoicePercentage='%s', agreement_fk='%s')>" % (
                   self.service, self.invoicePercentage, self.agreement_fk)