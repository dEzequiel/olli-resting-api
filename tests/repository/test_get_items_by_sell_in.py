import pytest
from repository.get_item_by_sell_in import get_item_by_sell_in
from app import app

def test_get_items_by_sell_in():
    with app.app_context():
        expected_result = [{"name": "Sulfuras", "sell_in": 1, "quality": 1},
                            {'name': 'Elixir of the Mongoose', 'quality': 1, 'sell_in': 1}]
        assert expected_result == get_item_by_sell_in(1)
