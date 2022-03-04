class Inventory:

    inventory_items = [
        {'name': 'Elixir of the Mongoose', 'sell_in': 5, 'quality': 7}
        ]

    @classmethod
    def new_item(cls, item):
        cls.inventory_items.append(item.__dict__)

    @classmethod
    def get_item(cls, name):
        items = []
        for item in cls.inventory_items:
            if item['name'] == name:
                items.append(item)

        if len(items) != 0:
            return items
        else:
            return {name:"not found"}

    @classmethod
    def get_inventory(cls):
        return cls.inventory_items

    @classmethod
    def get_inventory_size(cls):
        return len(cls.inventory_items)

    @classmethod
    def clean_inventory_list(cls):
        cls.inventory_items.clear()