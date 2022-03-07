from socket import inet_ntoa
from repository.get_all_items import get_all_items
from repository.get_item import get_item
from repository.get_by_sell_in import get_by_sell_in

class Services:
    @staticmethod
    def get_items():
        return get_all_items()

    @staticmethod
    def get_item(name):
        return get_item(name)

    @staticmethod
    def get_item_by_sell_in(sell_in):
        return get_by_sell_in(sell_in)
