from flask import json


class JsonParser():

    def jsonParser(self, jsoonUrl):
        json_url = jsoonUrl
        data = json.load(open(json_url))
        return data
