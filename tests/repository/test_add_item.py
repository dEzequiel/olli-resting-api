from unittest import result
import pytest
from app import app
from repository.database import get_db
from repository.add_item import add_item
import sqlite3


def test_add_new_item():
    with app.app_context():
        add_item("Rocky", 1, 1)

        database = get_db()
        item = [
            dict(row)
            for row in database.execute(
                "SELECT * FROM inventory ORDER BY quality DESC LIMIT 1;"
            )
        ]

        expected_result = [{"name": "Rocky", "sell_in": 1, "quality": 1}]
        assert item == expected_result
