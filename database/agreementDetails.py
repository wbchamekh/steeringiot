from utils.jsonParser import JsonParser


class AgreementDetails:

    def getAgreementsDetails(self, jsonurl):
        agreements = JsonParser()
        agr= agreements.jsonParser(jsonurl)
        jsonType = agr["DiscountAgreement"]
        agreementdetails = list(jsonType['Basic'].values())
        return agreementdetails
