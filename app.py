from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from utils.jsonParser import JsonParser
from config import Config

app = Flask(__name__)

app.config.from_object('config.Development')

db = SQLAlchemy(app)
app.db = db

with app.app_context():
    from models.agreements import AgreementDetails
    from models.customer import Customer
    from models.country import Country
    from models.coverage import Coverage


@app.before_first_request
def setup():
    # Recreate database each time for demo
    db.drop_all()
    db.create_all()

    # define the json file to parse
    jsonurl = '/home/walid/devops/steeringiot/static/data/tiers_VFGroup.json'

    # Start Parsing the agreement details and commit into database steeringiot:
    jsonType = JsonParser().jsonParser(jsonurl)
    basic = jsonType['DiscountAgreement']['Basic']
    db.session.add(AgreementDetails(basic['AgreementId'], basic['AParty'], basic['BParty'], basic['Start'], basic['Stop'],
                                    basic['Autoreconduction'], basic['GroupDeal'], basic['Network'], basic['Customer']))

    db.session.commit()


@app.route('/')
def root():
    agreements = db.session.query(AgreementDetails).all()
    return u"<br>".join([u"{0}: {0}".format(agreement.agreementId) for agreement in agreements])


if __name__ == '__main__':
    app.run('127.0.0.1', 5000, debug=True)
