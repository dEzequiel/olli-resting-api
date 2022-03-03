from operator import inv
import pytest
from domain.normal_item import Normal_Item
from repository.inventory import Inventory

def test_object_into_dict():

    inventory = Inventory()
    normal_item = Normal_Item("Elixir of the Mongoose", 5, 7)

    inventory.new_item(normal_item)
    assert {"name": "Elixir of the Mongoose", "sell_in": 5, "quality": 7} == inventory.inventoryItems[0]

def test_object_class():
    inventory = Inventory()
    normal_item = Normal_Item("Elixir of the Mongoose", 5, 7)

    inventory.new_item(normal_item)
    assert isinstance (inventory.inventoryItems[0], dict)

def test_get_object_by_name():

    inventory = Inventory()
    normal_item = Normal_Item("Elixir of the Mongoose", 5, 7)
    inventory.new_item(normal_item)
    normal_item2 = Normal_Item("Elixir of the Mongoose", 1, 2)
    inventory.new_item(normal_item2)

    assert 2 == len(inventory.inventoryItems)
    expected_result = [{'name': 'Elixir of the Mongoose', 'quality': 7, 'sell_in': 5}]

    assert expected_result == inventory.get_item('Elixir of the Mongoose')
    assert {"Harry":"not found"} == inventory.get_item("Harry")
