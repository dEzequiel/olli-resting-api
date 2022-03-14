import pytest
from repository.get_item import get_item
from app import app


def test_get_one_item():
    with app.app_context():
        expected_result = [{"id": 1, "name": "Sulfuras", "sell_in": 1, "quality": 1}]
        assert expected_result == get_item("Sulfuras")


def test_get_multiple_item():
    with app.app_context():
        expected_result = [
            {"id": 2, "name": "Elixir of the Mongoose", "sell_in": 7, "quality": 5},
            {"id": 3, "name": "Elixir of the Mongoose", "sell_in": 1, "quality": 1},
        ]
        assert expected_result == get_item("Elixir of the Mongoose")


def test_no_item():
    with app.app_context():
        expected_result = {"Elixir": "not found"}
        assert expected_result == get_item("Elixir")
