from flask_restful import Resource
from services.service import Services

class Item(Resource):
    def get(self, name):
        return Services.get_object(name), 200