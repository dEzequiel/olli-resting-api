from flask_restful import Resource, reqparse
from services.service import Services


class Item(Resource):
    def get(self, name, sell_in, quality):
        return Services.get_item(name), 200


    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True, location='json')
        parser.add_argument('sell_in', type=int, required=True, location='json')
        parser.add_argument('quality', type=int, required=True, location='json')
        Services.post_item(name), 201
        args = parser.parse_args()
        return args

    # 204: The server has successfully fulfilled the request and that there is
    # no additional content to send in the response payload body.
    def delete(self, name):
        if Services.delete_item(name):
            return {f"{name}": "deleted"}, 200
        else:
            return {f"{name}": "not found"}, 404