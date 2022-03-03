from domain.normal_item import Normal_Item
from services.service import Services
from repository import inventory
import pytest

def test_get_object_from_db():

    normal_item = Normal_Item("Elixir of the Mongoose", 5, 7)
    inventory.new_item(normal_item)

    services = Services()
    item = services.get_object("Elixir of the Mongoose")

    expected_result = [{'name': 'Elixir of the Mongoose', 'quality': 7, 'sell_in': 5}]

    assert expected_result == item

def test_get_objects_from_db():

    inventory.clean_inventory_list()

    assert 0 == inventory.get_inventory_size()

    normal_item = Normal_Item("Elixir of the Mongoose", 5, 7)
    normal_item2 = Normal_Item("Elixir of the Mongoose", 1, 1)

    inventory.new_item(normal_item)
    inventory.new_item(normal_item2)

    assert 2 == inventory.get_inventory_size()

    services = Services()
    item = services.get_object("Elixir of the Mongoose")

    expected_result = [{'name': 'Elixir of the Mongoose', 'quality': 7, 'sell_in': 5},
                        {'name': 'Elixir of the Mongoose', 'quality': 1, 'sell_in': 1}]

    assert expected_result == item