from services.service import Services
from repository.get_item import get_item

services = Services()


def test_get_one_item(app):
    with app.app_context():
        # item make reference to the object returned by services layer
        # expected_result make reference to the object returned by data access layer
        assert  services.get_item('Aged Brie') == get_item('Aged Brie')
