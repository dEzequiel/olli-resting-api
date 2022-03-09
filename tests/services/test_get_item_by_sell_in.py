import pytest
from app import app
from services.service import Services
from repository.get_item_by_sell_in import get_item_by_sell_in

services = Services()


def test_get_item_by_sell_in():
    with app.app_context():
        assert services.get_item_by_sell_in(1) == get_item_by_sell_in(1)
