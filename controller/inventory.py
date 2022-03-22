from flask_restful import Resource

from services.service import Services


class Inventory(Resource):
    def get(self):
        return Services.get_items(), 200
