import pytest
import json
from repository.commands import init_db, insert_db
from repository.get_item_by_quality import get_item_by_quality


def test_get_item_by_quality(client, app):
    with app.app_context():
        init_db()
        insert_db()

    response = client.get("/items/quality/80")
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

def test_no_item(client, app):
    with app.app_context():
        init_db()
        insert_db()

    response = client.get("/items/quality/500")
    data = json.loads(response.get_data(as_text=True))

    assert {"Quality 500": "not found"} == data
