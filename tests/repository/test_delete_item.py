import pytest
import json
from repository.inventory_test.database_test import delete_item
from repository.inventory_test.database_test import init_db, insert_db

def test_unit_delete_item(app):
    with app.app_context():
        init_db()
        insert_db()

        assert {"ID 3":"deleted"} == delete_item(3)


def test_unit_delete_item_not_found(app):
    with app.app_context():
        init_db()
        insert_db()
        assert {"ID 100":"not found"} == delete_item(100)


def test_delete_item(client, app):
    with app.app_context():
        init_db()
        insert_db()

    response = client.delete("/item/del/3")
    assert response.status_code == 200

def test_delete_no_found_item(client, app):
    with app.app_context():
        init_db()
        insert_db()

    response = client.delete("/item/del/100")

    assert response.status_code == 404
