import pytest
from repository.get_all_items import get_all_items
from app import app

# WARNING: this test can fail if the db is modified with a new record.


def test_get_all_items():
    with app.app_context():
        expected_result = [
            {"name": "Sulfuras", "sell_in": 1, "quality": 1},
            {"name": "Elixir of the Mongoose", "sell_in": 7, "quality": 5},
            {"name": "Elixir of the Mongoose", "sell_in": 1, "quality": 1},
            {"name": "+5 Dextery Vest", "sell_in": 10, "quality": 20},
            {"name": "Aged Brie", "sell_in": 2, "quality": 0},
            {
                "name": "Backstage passes to a TAFKAL80ETC concert",
                "sell_in": 15,
                "quality": 20,
            },
            {
                "name": "Backstage passes to a TAFKAL80ETC concert",
                "sell_in": 10,
                "quality": 40,
            },
            {
                "name": "Backstage passes to a TAFKAL80ETC concert",
                "sell_in": 5,
                "quality": 49,
            },
        ]

        assert expected_result == get_all_items()
