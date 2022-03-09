from flask_restful import Resource

from services.service import Services


class ItemsBySellin(Resource):
    def get(self, sellin):
        return Services.get_item_by_sell_in(sellin), 200
