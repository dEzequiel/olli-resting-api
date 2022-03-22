from flask_restful import Resource
from services.service import Services


class ItemsByQuality(Resource):
    def get(self, quality):
        return Services.group_items_by_quality(quality), 200
