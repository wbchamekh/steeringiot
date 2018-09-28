from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from models.agreements import Base, Agreements
from models.customer import Base, Customer
from models.country import Base, Country
from models.coverage import Base, Coverage
from database.agreementDetails import AgreementDetails



app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Walid78!@192.168.43.201/steeringiot'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Walid78!@localhost/steeringiot'
db = SQLAlchemy(app)


@app.before_first_request
def setup():
    # Recreate database each time for demo
    Base.metadata.drop_all(bind=db.engine)
    Base.metadata.create_all(bind=db.engine)

    # define the json file to parse
    # jsonurl = '/home/walid/devops/steeringiot/static/data/tiers_VFGroup.json'
    #
    # # Start Parsing the agreement details and commit into database steeringiot:
    # agreementDetails = AgreementDetails()
    # agrs = agreementDetails.getAgreementsDetails(jsonurl)
    # db.session.add(Agreements(agrs[0], agrs[1], agrs[2], agrs[3], agrs[4], agrs[5], agrs[6], agrs[7], agrs[8]))

    db.session.commit()
    db.session.remove()


@app.route('/')
def root():
    agreements = db.session.query(Agreements).all()
    return u"<br>".join([u"{0}: {0}".format(agreement.agreementId) for agreement in agreements])


if __name__ == '__main__':
    app.run('127.0.0.1', 5000, debug=True)
