import pytest
import json
from repository.get_item import get_item
from repository.commands import init_db, insert_db


def test_get_one_item(client, app):

    with app.app_context():
        init_db()
        insert_db()

     # [{"id": 1, "name": "Aged Brie", "sell_in": 2, "quality": 0}]

    response = client.get("/item/name/Aged Brie")
    data = json.loads(response.get_data(as_text=True))

    # This way because data returns a list of dicts. Always
    # entire program returns a list of dicts

    assert data[0]['id'] == 1
    assert data[0]['name'] == 'Aged Brie'
    assert data[0]['sell_in'] == 2
    assert data[0]['quality'] == 0

    assert response.status_code == 200


def test_get_multiple_item():
    with app.app_context():
        expected_result = [
            {"id": 2, "name": "Elixir of the Mongoose", "sell_in": 7, "quality": 5},
            {"id": 3, "name": "Elixir of the Mongoose", "sell_in": 1, "quality": 1},
        ]
        assert expected_result == get_item("Elixir of the Mongoose")


def test_no_item():
    with app.app_context():
        expected_result = {"Elixir": "not found"}
        assert expected_result == get_item("Elixir")
