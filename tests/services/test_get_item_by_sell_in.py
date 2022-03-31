import pytest
from services.service import Services
from repository.group_items_by_sell_in import group_items_by_sell_in

services = Services()

def test_get_item_by_sell_in(app):
    with app.app_context():
        assert services.group_items_by_sell_in(1) == group_items_by_sell_in(1)
