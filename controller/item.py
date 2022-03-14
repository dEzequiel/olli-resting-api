from flask_restful import Resource
from services.service import Services


class Item(Resource):
    def get(self, name):
        return Services.get_item(name), 200

    def post(self, name):
        return Services.post_item(name), 201