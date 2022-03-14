import pytest
from repository.get_item_by_sell_in import get_item_by_sell_in
from app import app


def test_get_items_by_sell_in():
    with app.app_context():
        expected_result = [
            {"id":1, "name": "Sulfuras", "sell_in": 1, "quality": 1},
            {"id": 3, "name": "Elixir of the Mongoose", "quality": 1, "sell_in": 1},
        ]
        assert expected_result == get_item_by_sell_in(1)


def test_no_items_with_sell_in_found():
    with app.app_context():
        expected_result = {"Sell in 100": "not found"}
        assert expected_result == get_item_by_sell_in(100)
