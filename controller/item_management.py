from flask_restful import Resource
from services.service import Services

class ItemManagement(Resource):

    # 204: The server has successfully fulfilled the request and that there is
    # no additional content to send in the response payload body.
    def delete(self, item_id):
        return 200 if Services.delete_item(item_id) else 404