from flask_restful import Resource
from services.service import Services

class ItemManagement(Resource):
    def delete(self, item_id):
        return Services.delete_item(item_id), 204