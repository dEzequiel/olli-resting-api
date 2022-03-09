from flask_restful import Resource

from services.service import Services


class Items(Resource):
    def get(self):
        return Services.get_items(), 200
