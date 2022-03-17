from flask_restful import Resource
from services.service import Services


class AddItem(Resource):
    def post(self, name):
        Services.add_new_item(name)
        return {"Item": "added"}, 201
