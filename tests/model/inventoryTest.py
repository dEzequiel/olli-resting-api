import pytest
from domain.normal_item import Normal_Item
from repository.inventory import Inventory

@pytest.fixture(autouse=True)
def reset_items_list():
    Inventory.clean_inventory_list()
    assert 0 == Inventory.get_inventory_size()

def test_object_into_dict():

    normal_item = Normal_Item("Elixir of the Mongoose", 5, 7)
    Inventory.new_item(normal_item)
    assert [{"name": "Elixir of the Mongoose", "sell_in": 5, "quality": 7}] == Inventory.get_item("Elixir of the Mongoose")

def test_object_class():
    normal_item = Normal_Item("Elixir of the Mongoose", 5, 7)
    Inventory.new_item(normal_item)
    assert isinstance (Inventory.inventory_items[0], dict)

def test_get_object_by_name():

    normal_item = Normal_Item("Elixir of the Mongoose", 5, 7)
    Inventory.new_item(normal_item)
    normal_item2 = Normal_Item("Elixir of Narnia", 1, 2)
    Inventory.new_item(normal_item2)

    expected_result = [{'name': 'Elixir of the Mongoose', 'sell_in': 5, 'quality': 7}]
    assert expected_result == Inventory.get_item("Elixir of the Mongoose")

def test_get_objects_with_same_name():
    normal_item = Normal_Item("Elixir of the Mongoose", 5, 7)
    Inventory.new_item(normal_item)
    normal_item2 = Normal_Item("Elixir of the Mongoose", 1, 2)
    Inventory.new_item(normal_item2)

    expected_result = [{'name': 'Elixir of the Mongoose', 'sell_in': 5, 'quality': 7}, {'name': 'Elixir of the Mongoose', 'sell_in': 1, 'quality': 2}]

    assert expected_result == Inventory.get_item('Elixir of the Mongoose')

# Test when the inventory class inventoryList has an implicit items inside
# WARNING: Pytest fixture you clean the implicit value in Inventoy items list. So this text is not working with. FIX!!
def test_get_objects_from_inventory_in_elements():

    expected_result = [{'name': 'Elixir of the Mongoose', 'sell_in': 5, 'quality': 7}]
    assert expected_result == Inventory.get_item("Elixir of the Mongoose")
