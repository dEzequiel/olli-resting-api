from mimetypes import init
import pytest
import json
from repository.commands import init_db, insert_db


def test_get_items_by_sell_in(client, app):

    with app.app_context():
        init_db()
        insert_db()

    response = client.get("/item/sellin/5")
    data = json.loads(response.get_data(as_text=True))

    assert data[0]["id"] == 3
    assert data[0]["name"] == "Elixir of the Mongoose"
    assert data[0]["sell_in"] == 5
    assert data[0]["quality"] == 7

    assert data[1]["id"] == 8
    assert data[1]["name"] == "Backstage passes to a TAFKAL80ETC concert"
    assert data[1]["sell_in"] == 5
    assert data[1]["quality"] == 49

    assert response.status_code == 200

def test_no_items_with_sell_in_found(client, app):
    with app.app_context():
        init_db()
        insert_db()

    response = client.get("/item/sellin/500")
    data = json.loads(response.get_data(as_text=True))

    assert {"Sell in 500": "not found"} == data