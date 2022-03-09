from services.service import Services
from repository.get_item import get_item
from app import app
import pytest

services = Services()


def test_get_one_item():
    with app.app_context():

        # item make reference to the object returned by services layer
        # expected_result make reference to the object returned by data access layer

        item = services.get_item("Sulfuras")
        expected_result = get_item("Sulfuras")
        assert expected_result == item
