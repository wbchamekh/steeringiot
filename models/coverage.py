from flask import current_app as app

db = app.db


class Coverage(db.Model):
    __tablename__ = 'coverage'

    id = db.Column(db.Integer, primary_key=True)
    alias = db.Column(db.String(5), unique=False)
    cov = db.Column(db.Integer, unique=False)
    customer_fk = db.Column(db.Integer, db.ForeignKey('customer.id'))

    def __init__(self, alias=None, cov=None, customer_fk=None):
        self.alias = alias
        self.cov = cov
        self.customer_fk = customer_fk

    def __repr__(self):
        return "<Coverage(alias='%s', cov='%s', customer_fk='%s')>" % (self.alias, self.cov, self.customer_fk)
