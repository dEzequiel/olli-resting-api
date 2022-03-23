import pytest
import json
from repository.inventory_test.database_test import add_item, get_item
from repository.inventory_test.database_test import init_db, insert_db

def test_add_item(app):

    # This test uses test database!

    with app.app_context():
        init_db()
        insert_db()

        add_item("Prueba", 1, 1)
        assert [{'id': 10, 'name':'Prueba', 'sell_in':1, 'quality':1}] == get_item("Prueba")