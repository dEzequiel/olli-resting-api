import pytest
from app import app
from repository.database import get_db
from repository.add_item import add_item


def test_add_new_item():
    with app.app_context():
        add_item(None, "Elixir of the Mongoose", 10, 10)

        database = get_db()
        item = [
            dict(row)
            for row in database.execute(
                "SELECT * FROM inventory ORDER BY quality DESC LIMIT 1;"
            )
        ]

        expected_result = [{"id":16, "name": "Elixir of the Mongoose", "sell_in": 10, "quality": 10}]
        assert item == expected_result
