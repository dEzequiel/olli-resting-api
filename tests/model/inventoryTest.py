import pytest
from domain.normal_item import Normal_Item
from repository.inventory import Inventory

def test_object_into_dict():

    normal_item = Normal_Item("Elixir of the Mongoose", 5, 7)

    Inventory.new_item(normal_item)
    assert {"name": "Elixir of the Mongoose", "sell_in": 5, "quality": 7} == Inventory.inventoryItems[0]

def test_object_class():
    normal_item = Normal_Item("Elixir of the Mongoose", 5, 7)

    Inventory.new_item(normal_item)
    assert isinstance (Inventory.inventoryItems[0], dict)

def test_get_object_by_name():

    Inventory.clean_inventory_list()

    assert 0 == Inventory.get_inventory_size()

    normal_item = Normal_Item("Elixir of the Mongoose", 5, 7)
    Inventory.new_item(normal_item)
    normal_item2 = Normal_Item("Elixir of the Narnia", 1, 2)
    Inventory.new_item(normal_item2)

    assert 2 == Inventory.get_inventory_size()
    print(Inventory.get_inventory())
    expected_result = [{'name': 'Elixir of the Mongoose', 'sell_in': 5, 'quality': 7}]

    assert expected_result == Inventory.get_item('Elixir of the Mongoose')
    # assert {"Harry":"not found"} == Inventory.get_item("Harry")
