from flask import current_app as app

db = app.db


class Country(db.Model):
    __tablename__ = 'country'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    networks = db.relationship('Network', backref='country')

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return "<Country(name='%s')>" % self.name
