import pathlib

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from utils.jsonParser import JsonParser

app = Flask(__name__)

app.config.from_object('config.Development')

db = SQLAlchemy(app)
app.db = db

with app.app_context():
    from models.agreements import AgreementDetails
    from models.network import Network
    from models.country import Country
    from models.coverage import Coverage


@app.before_first_request
def setup():
    # Recreate database each time for demo
    db.drop_all()
    db.create_all()

    # database init with dummy data
    db.session.add(Network('TUNOR'))
    db.session.add(Network('FRAF1'))
    db.session.add(Country('Germany'))
    db.session.add(Country('United Kingdom'))
    db.session.add(Coverage('DEUD1', 1, 1, 1))
    db.session.add(Coverage('DEUD1', 1, 2, 1))
    db.session.add(Coverage('DEUD2', 1, 1, 1))
    db.session.add(Coverage('DEUD2', 1, 2, 1))
    db.session.add(Coverage('DEUE1', 1, 1, 1))
    db.session.add(Coverage('DEUE1', 1, 2, 1))
    db.session.add(Coverage('GBRVF', 1, 1, 2))
    db.session.add(Coverage('GBRVF', 1, 2, 2))
    db.session.add(Coverage('GBROR', 1, 1, 2))
    db.session.add(Coverage('GBROR', 1, 2, 2))


    # config file has STATIC_FOLDER='/home/walid/devops/steeringiot/static/data'
    directory = app.static_url_path = app.config.get('STATIC_FOLDER')

    # define the path
    currentDirectory = pathlib.Path(directory)

    # Walk through the currentDirectory, parse the json files and persist the data
    for currentFile in currentDirectory.iterdir():
        jsonurl = currentFile
        jsonType = JsonParser().jsonParser(jsonurl)
        basic = jsonType['DiscountAgreement']['Basic']
        db.session.add(
            AgreementDetails(basic['AgreementId'], basic['AParty'], basic['BParty'], basic['Start'], basic['Stop'],
                             basic['Autoreconduction'], basic['GroupDeal'], basic['Network']))


        db.session.commit()


@app.route('/')
def root():
    agreements = db.session.query(AgreementDetails).all()
    return u"<br>".join([u"{0}: {0}".format(agreement.agreementId) for agreement in agreements])


db.session.remove()

if __name__ == '__main__':
    app.run('127.0.0.1', 5000, debug=True)
