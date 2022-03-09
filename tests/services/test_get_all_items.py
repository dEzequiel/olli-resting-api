from services.service import Services
from repository.get_item import get_all_items
from app import app
import pytest

services = Services()


def test_get_all_items():
    with app.app_context():

        # item make reference to the object returned by services layer
        # expected_result make reference to the object returned by data access layer

        item = services.get_items()
        expected_result = get_all_items()
        assert expected_result == item
