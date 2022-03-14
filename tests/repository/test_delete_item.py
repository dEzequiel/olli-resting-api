import pytest
from app import app
from repository.database import get_db
from repository.delete_item import delete_item

def test_delete_item():
    with app.app_context():
        assert "Item with id=3 was deleted" == delete_item(3)

def test_delete_item_not_found():
    with app.app_context():
        assert "Item with id=5 was not found" == delete_item(5)