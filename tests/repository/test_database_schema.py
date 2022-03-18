import pytest
import json
from repository.inventory_test.database_test import get_db
from repository.commands import init_db, insert_db


def test_database_schema(client, app):
    with app.app_context():
        init_db()
        insert_db()

    response = client.get("/items")
    data = json.loads(response.get_data(as_text=True))

    expected_keys = ['id', 'name', 'sell_in', 'quality']
    schema_keys = list(data[0].keys())

    assert expected_keys == schema_keys
