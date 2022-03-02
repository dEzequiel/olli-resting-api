import pytest
from domain.normal_item import Normal_Item
from repository.inventory import Inventory

def test_object_into_dict():

    inventory = Inventory()
    normal_item = Normal_Item("Elixir of the Mongoose", 5, 7)

    assert {"name": "Elixir of the Mongoose", "sell_in": 5, "quality": 7} == inventory.format_item(normal_item)