from flask import current_app as app

db = app.db


class BalancedUnbalanced(db.Model):
    __tablename__ = 'balancedUnbalanced'

    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(100), unique=False)
    balanced = db.Column(db.String(100), unique=False)
    unbalanced = db.Column(db.String(100), unique=False)
    agreement_fk = db.Column(db.Integer, db.ForeignKey('agreements.id'))

    def __init__(self, service=None, balanced=None, unbalanced=None, agreement_fk=None):
        self.service = service
        self.balanced = balanced
        self.unbalanced = unbalanced
        self.agreement_fk = agreement_fk

    def __repr__(self):
        return "<BalancedUnbalanced(service='%s', balanced='%s', unbalanced='%s', agreement_fk='%s')>" % (
                   self.service, self.balanced, self.unbalanced, self.agreement_fk)
