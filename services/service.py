from socket import inet_ntoa
from repository.get_all_items import get_all_items
from repository.get_item import get_item
from repository.get_item_by_sell_in import get_item_by_sell_in
from repository.get_item_by_quality import get_item_by_quality
from repository.add_item import add_item


class Services:
    @staticmethod
    def get_items():
        return get_all_items()

    @staticmethod
    def get_item(name):
        return get_item(name)

    @staticmethod
    def get_item_by_sell_in(sellin):
        return get_item_by_sell_in(sellin)

    @staticmethod
    def get_item_by_quality(quality):
        return get_item_by_quality(quality)

    @staticmethod
    def add_new_item(name):
        add_item(name)
