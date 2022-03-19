import pytest
from repository.database import get_db
from repository.inventory_test.database_test import delete_item
from repository.inventory_test.database_test import init_db, insert_db

def test_unit_delete_item(app):
    with app.app_context():
        init_db()
        insert_db()

        assert "Item with id=3 was deleted" == delete_item(3)


def test_unit_delete_item_not_found(app):
    with app.app_context():
        init_db()
        insert_db()
        assert "Item with id=100 was not found" == delete_item(100)
