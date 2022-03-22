from flask_restful import Resource
from services.service import Services


class ItemManagement(Resource):

    # 204: The server has successfully fulfilled the request and that there is
    # no additional content to send in the response payload body.
    def delete(self, item_id):
        if Services.delete_item(item_id):
            return {f"ID {item_id}": "deleted"}, 200
        else:
            return {f"ID {item_id}": "not found"}, 404
