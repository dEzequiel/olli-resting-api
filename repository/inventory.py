from domain.stock_item import Stock_Item

class Inventory:

    inventoryItems = []
    inventoryDemandItems = []

    @classmethod
    def new_item(cls, item):
        cls.inventoryItems.append(item.__dict__)

    @classmethod
    def get_item(cls, name):
        for item in cls.inventoryItems:
            if item['name'] == name:
                cls.inventoryDemandItems.append(item)
            else:
                return {name:"not found"}

        return cls.inventoryDemandItems

    @classmethod
    def get_inventory(cls):
        return cls.inventoryItems

    @classmethod
    def get_inventory_size(cls):
        return len(cls.inventoryItems)

    @classmethod
    def clean_inventory_list(cls):
        cls.inventoryItems.clear()
        cls.inventoryDemandItems.clear()