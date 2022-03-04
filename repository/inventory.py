class Inventory:

    inventory_items = [
        {"name": "Elixir of the Mongoose", "sell_in": 5, "quality": 7},
        {"name": "Elixir of the Mongoose", "sell_in": 1, "quality": 1},
        {"name": "Sulfuras", "sell_in": 1, "quality": 1},
        {"name": "+5 Dexterity Vest", "sell_in": 10, "quality": 20},
        {"name": "Aged Brie", "sell_in": 2, "quality": 0},
        {
            "name": "Backstage passes to a TAFKAL80ETC concert",
            "sell_in": 15,
            "quality": 20,
        },
        {
            "name": "Backstage passes to a TAFKAL80ETC concert",
            "sell_in": 10,
            "quality": 49,
        },
        {
            "name": "Backstage passes to a TAFKAL80ETC concert",
            "sell_in": 5,
            "quality": 49,
        },
    ]

    @classmethod
    def new_item(cls, item):
        cls.inventory_items.append(item.__dict__)

    @classmethod
    def get_item(cls, name):
        items = []
        for item in cls.inventory_items:
            if item["name"] == name:
                items.append(item)

        if len(items) != 0:
            return items
        else:
            return {name: "not found"}

    @classmethod
    def get_inventory(cls):
        return cls.inventory_items

    @classmethod
    def get_inventory_size(cls):
        return len(cls.inventory_items)

    @classmethod
    def clean_inventory_list(cls):
        cls.inventory_items.clear()
