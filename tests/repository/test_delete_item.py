import pytest
import json
from repository.inventory_test.database_test import delete_item
from repository.inventory_test.database_test import init_db, insert_db
from repository import commands

def test_unit_delete_item(app):
    with app.app_context():
        init_db()
        insert_db()
        assert True == delete_item(3)


def test_unit_delete_item_not_found(app):
    with app.app_context():
        init_db()
        insert_db()
        assert False == delete_item(100)


# This tests uses production database.
# Why? because we doing integration test by making a request to the app route /item/del/<item_id>

def test_delete_item(client, app):
    with app.app_context():
        commands.init_db()
        commands.insert_db()

    response = client.delete("/item/identifier/Aged Brie")
    data = json.loads(response.get_data(as_text=True))

    assert {"Aged Brie": "deleted"} == data
    assert response.status_code == 200

def test_delete_no_found_item(client, app):
    with app.app_context():
        commands.init_db()
        commands.insert_db()

    response = client.delete("/item/identifier/Conjure")
    data = json.loads(response.get_data(as_text=True))

    assert {"Conjure": "not found"} == data
    assert response.status_code == 404
