import pytest
from services.service import Services
from repository.group_items_by_quality import group_items_by_quality

service = Services()

def test_get_item_by_quality_from_service(app):
    with app.app_context():
        assert service.group_items_by_quality(5) == group_items_by_quality(5)
