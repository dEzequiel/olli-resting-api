import json
import pytest
from repository.get_all_items import get_all_items
from repository.commands import init_db, insert_db


# WARNING: this test can fail if the db is modified with a new record.



def test_get_all_items(client, app):

    with app.app_context():
        init_db()
        insert_db()

    expected_result = [
            {"id": 1, "name": "Aged Brie", "sell_in": 2, "quality": 0},
            {"id": 2, "name": "+5 Dexterity Vest", "sell_in": 10, "quality": 20},
            {"id": 3, "name": "Elixir of the Mongoose", "sell_in": 5, "quality": 7},
            {
                "id": 4,
                "name": "Sulfuras, Hand of Ragnaros",
                "sell_in": 0,
                "quality": 80,
            },
            {
                "id": 5,
                "name": "Sulfuras, Hand of Ragnaros",
                "sell_in": -1,
                "quality": 80,
            },
            {
                "id": 6,
                "name": "Backstage passes to a TAFKAL80ETC concert",
                "sell_in": 15,
                "quality": 20,
            },
            {
                "id": 7,
                "name": "Backstage passes to a TAFKAL80ETC concert",
                "sell_in": 10,
                "quality": 49,
            },
            {
                "id": 8,
                "name": "Backstage passes to a TAFKAL80ETC concert",
                "sell_in": 5,
                "quality": 49,
            },
            {"id": 9, "name": "Conjured Mana Cake", "sell_in": 3, "quality": 6},
        ]

    # Convert into json response data, returned as text
    response = client.get("/items")
    data = json.loads(response.get_data(as_text=True))

    assert expected_result == data
    assert response.status_code == 200


def test_no_items(client, app):

    with app.app_context():
        init_db()

    response = client.get("/items")
    data = json.loads(response.get_data(as_text=True))
    assert {"Inventory":"is empty"} == data
