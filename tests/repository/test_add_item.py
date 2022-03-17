from dataclasses import dataclass
import pytest
from app import app
from repository.database import get_db
from repository.add_item import add_item


def test_add_new_item():
    with app.app_context():
        add_item(None, "Elixir of the Mongoose", 12, 12)

        database = get_db()
        item = [
            dict(row)
            for row in database.execute(
                "SELECT * FROM inventory ORDER BY quality DESC LIMIT 1;"
            )
        ]

        expected_result = [
            {"id": 21, "name": "Elixir of the Mongoose", "sell_in": 12, "quality": 12}
        ]
        assert item == expected_result
