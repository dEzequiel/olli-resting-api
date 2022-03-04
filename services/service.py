from socket import inet_ntoa
from repository.inventory import Inventory

class Services():

    @staticmethod
    def get_object(name):
        item = Inventory.get_item(name)
        return item
