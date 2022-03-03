from domain.stock_item import Stock_Item

inventoryItems = []
inventoryDemandItems = []

def new_item(item):
    inventoryItems.append(item.__dict__)

def get_item(name):
    for item in inventoryItems:
        if item['name'] == name:
            inventoryDemandItems.append(item)
        else:
            return {name:"not found"}

    return inventoryDemandItems

def get_inventory_size():
    return len(inventoryItems)

def clean_inventory_list():
    inventoryItems.clear()