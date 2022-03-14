import pytest
from app import app
from repository.get_item_by_quality import get_item_by_quality


def test_get_item_by_quality():
    with app.app_context():
        expected_result = [
            {"id": 2, "name": "Elixir of the Mongoose", "quality": 5, "sell_in": 7}
        ]
        real_result = get_item_by_quality(5)
        assert expected_result == real_result


def test_no_item():
    with app.app_context():
        expected_result = {"Quality 1000": "not found"}
        real_result = get_item_by_quality(1000)
        assert expected_result == real_result
