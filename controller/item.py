from flask_restful import Resource
from services.service import Services


class Item(Resource):
    def get(self, name):
        return Services.get_item(name), 200

    def post(self, name):
        return Services.post_item(name), 201

    # 204: The server has successfully fulfilled the request and that there is
    # no additional content to send in the response payload body.
    def delete(self, name):
        if Services.delete_item(name):
            return {f"{name}": "deleted"}, 200
        else:
            return {f"{name}": "not found"}, 404