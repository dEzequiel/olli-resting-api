import pytest
from repository.get_all_items import get_all_items
from app import app

# WARNING: this test can fail if the db is modified with a new record.


def test_get_all_items():
    with app.app_context():
        expected_result = [
            {"id":1, "name": "Sulfuras", "sell_in": 1, "quality": 1},
            {"id":2,"name": "Elixir of the Mongoose", "sell_in": 7, "quality": 5},
        ]

        assert expected_result == get_all_items()
