from services.service import Services
from repository.get_item import get_all_items
import pytest

services = Services()

# This test uses production database.

def test_get_all_items(app):
    with app.app_context():
        assert services.get_all_items() == get_all_items()
