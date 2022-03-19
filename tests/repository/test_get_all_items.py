import json
import pytest
from repository.get_all_items import get_all_items
from repository.inventory_test.database_test import init_db, insert_db


# WARNING: this test can fail if the db is modified with a new record.


def test_get_all_items(client, app):

    # This test uses production database!
    # Why? never gonna fail if one item is posted or deleted from the db via requests,
    # because response should be equal to the existing fields in db.

    with app.app_context():
        expected_result = get_all_items()

    # Convert into json response data, returned as text
    response = client.get("/items")
    data = json.loads(response.get_data(as_text=True))

    assert expected_result == data
    assert response.status_code == 200


def test_no_items(client, app):

    # This test uses testing database. Just for initialization.

    with app.app_context():
        init_db()

    response = client.get("/items")
    data = json.loads(response.get_data(as_text=True))
    assert {"Inventory": "is empty"} == data
