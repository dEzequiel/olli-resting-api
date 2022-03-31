from flask_restful import Resource

from services.service import Services


class ItemsBySellin(Resource):
    def get(self, sellin):
        return Services.group_items_by_sell_in(sellin), 200
