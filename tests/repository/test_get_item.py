import pytest
from repository.get_item import get_item
from app import app

def test_get_one_item():
    with app.app_context():
        expected_result = [{"name": "Sulfuras", "sell_in": 1, "quality": 1}]
        assert expected_result == get_item("Sulfuras")
