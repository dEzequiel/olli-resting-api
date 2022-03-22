import pytest
import json
from repository.commands import init_db, insert_db


def test_get_one_item(client, app):

    # This test uses production database!

    with app.app_context():
        init_db()
        insert_db()

    # [{"id": 1, "name": "Aged Brie", "sell_in": 2, "quality": 0}]

    response = client.get("/item/identifier/Aged Brie")
    data = json.loads(response.get_data(as_text=True))

    # This way because data returns a list of dicts. Always
    # entire program returns a list of dicts

    assert data[0]["id"] == 1
    assert data[0]["name"] == "Aged Brie"
    assert data[0]["sell_in"] == 2
    assert data[0]["quality"] == 0

    assert response.status_code == 200


def test_get_multiple_item(client, app):

    # This test uses production database!

    with app.app_context():
        init_db()
        insert_db()

    response = client.get("/item/identifier/Sulfuras, Hand of Ragnaros")
    data = json.loads(response.get_data(as_text=True))

    assert data[0]["id"] == 4
    assert data[0]["name"] == "Sulfuras, Hand of Ragnaros"
    assert data[0]["sell_in"] == 0
    assert data[0]["quality"] == 80

    assert data[1]["id"] == 5
    assert data[1]["name"] == "Sulfuras, Hand of Ragnaros"
    assert data[1]["sell_in"] == -1
    assert data[1]["quality"] == 80

    assert response.status_code == 200


def test_no_item(client):
    response = client.get("/item/identifier/Elixir")
    data = json.loads(response.get_data(as_text=True))

    assert {"Elixir": "not found"} == data
