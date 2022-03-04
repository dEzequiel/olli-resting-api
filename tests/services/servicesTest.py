from services.service import Services
import pytest

services = Services()


def test_get_object_from_inventory():

    item = services.get_object("Sulfuras")
    expected_result = [{'name': 'Sulfuras', 'quality': 1, 'sell_in': 1}]
    assert expected_result == item

def test_get_objects_from_inventory():

    item = services.get_object("Elixir of the Mongoose")
    expected_result = [{'name': 'Elixir of the Mongoose', 'sell_in': 5, 'quality': 7}, {'name': 'Elixir of the Mongoose', 'sell_in': 1, 'quality': 1}]
    assert expected_result == item