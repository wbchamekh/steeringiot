import pathlib

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

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
    from models.siot import StandardIot
    from models.dealModels.balancedUnbalanced import BalancedUnbalanced
    from models.dealModels.invoiceFlat import InvoiceFlat
    from models.dealModels.revenueCommitment import RevenueCommitment
    from models.dealModels.sendOrPay import SendOrPay
    from models.dealModels.standardFlat import StandardFlat
    from models.dealModels.tiered import Tiered


@app.before_first_request
def setup():
    # Recreate service each time for demo
    db.drop_all()
    db.create_all()

    # service init with dummy data
    file = open('dbinit.sql', 'r')
    connection = db.session
    connection.execute(text(file.read()))
    connection.commit()

    # config file has STATIC_FOLDER:
    # '/home/walid/devops/steeringiot/static/data'
    directory = app.static_url_path = app.config.get('STATIC_FOLDER')

    # define the path
    currentDirectory = pathlib.Path(directory)

    # Walk through the currentDirectory, parse the discount agreements from th json files and persist the data
    for currentFile in currentDirectory.iterdir():
        jsonurl = currentFile
        jsonType = JsonParser().jsonParser(jsonurl)
        basic = jsonType['DiscountAgreement']['Basic']
        nw = basic['Network']
        network = Network.query.filter_by(alias=nw).first()
        db.session.add(
            AgreementDetails(basic['AgreementId'], basic['AParty'], basic['BParty'], basic['Start'], basic['Stop'],
                             basic['Autoreconduction'], basic['GroupDeal'], basic['DealStatus'], network.id))

        db.session.commit()


@app.route('/')
def root():
    agreements = db.session.query(AgreementDetails).all()
    return u"<br>".join([u"{0}: {0}".format(agreement.agreementId) for agreement in agreements])


db.session.remove()

if __name__ == '__main__':
    app.run('127.0.0.1', 5000, debug=True)
