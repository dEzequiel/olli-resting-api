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
