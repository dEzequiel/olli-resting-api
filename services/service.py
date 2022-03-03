from repository import inventory

class Services():

    def get_object(self, name):
        return inventory.get_item(name)