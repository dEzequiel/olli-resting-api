import pytest
from app import app
from repository.database import get_db
from repository.delete_item import delete_item
import sqlite3

def test_delete_item():
    with app.app_context():

        database = get_db()
        assert [{"id": 3, "name": "Elixir of the Mongoose", "sell_in": 1, "quality": 1}] == delete_item(3)