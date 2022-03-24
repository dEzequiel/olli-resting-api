from repository.get_all_items import get_all_items
from repository.get_item import get_item
from repository.group_items_by_sell_in import group_items_by_sell_in
from repository.group_items_by_quality import group_items_by_quality
from repository.add_item import add_item
from repository.delete_item import delete_item


class Services:
    @staticmethod
    def get_all_items():
        return get_all_items()

    @staticmethod
    def get_item(name):
        return get_item(name)

    @staticmethod
    def group_items_by_sell_in(sellin):
        return group_items_by_sell_in(sellin)

    @staticmethod
    def group_items_by_quality(quality):
        return group_items_by_quality(quality)

    @staticmethod
    def post_item(name, sell_in=10, quality=10):
        return add_item(name, sell_in, quality)

    @staticmethod
    def delete_item(name):
        return delete_item(name)
