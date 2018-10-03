from flask import current_app as app

db = app.db


class StandardIot(db.Model):
    __tablename__ = 'siot'

    id = db.Column(db.Integer, primary_key=True)
    alias = db.Column(db.String(255), unique=False)
    service = db.Column(db.String(255), unique=False)
    currency = db.Column(db.String(255), unique=False)
    destination = db.Column(db.String(255), unique=False)
    iotairtimepeak = db.Column(db.String(120), unique=False)
    iotairtimeoffpeak = db.Column(db.String(120), unique=False)
    iotiddpeak = db.Column(db.String(120), unique=False)
    iotiddoffpeak = db.Column(db.String(120), unique=False)
    firstChargingInt = db.Column(db.String(120), unique=False)
    secondChargingInt = db.Column(db.String(120), unique=False)
    taxPercentage = db.Column(db.String(120), unique=False)
    taxFix = db.Column(db.String(120), unique=False)
    network_fk = db.Column(db.Integer, db.ForeignKey('network.id'))

    def __init__(self, alias=None, service=None, currency=None, destination=None,
                 iotairtimepeak=None, iotairtimeoffpeak=None, iotiddpeak=None, iotiddoffpeak=None,
                 firstChargingInt=None, secondChargingInt=None, taxPercentage=None, taxFix=None,
                 network_fk=None):
        self.alias = alias
        self.service = service
        self.currency = currency
        self.destination = destination
        self.iotairtimepeak = iotairtimepeak
        self.iotairtimeoffpeak = iotairtimeoffpeak
        self.iotiddoffpeak = iotiddpeak
        self.iotiddoffpeak = iotiddoffpeak
        self.firstChargingInt = firstChargingInt
        self.secondChargingInt = secondChargingInt
        self.taxPercentage = taxPercentage
        self.taxFix = taxFix
        self.network_fk = network_fk

    def __repr__(self):
        return "<StandardIot(alias='%s', service='%s', currency='%s', destination='%s', iotairtimepeak='%s'" \
               ", iotairtimeoffpeak='%s', iotiddpeak='%s', iotiddoffpeak='%s', firstChargingInt='%s', secondChargingInt='%s'" \
               ", taxPercentage='%s', taxFix='%s', network_fk='%s')>" % (self.alias, self.service, self.currency, self.destination,
                self.iotairtimepeak, self.iotairtimeoffpeak, self.iotiddpeak, self.iotiddoffpeak, self.firstChargingInt, self.secondChargingInt,
                self.taxPercentage, self.taxFix, self.network_fk)
