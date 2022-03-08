import pytest
from app import app
from services.service import Services
from repository.get_item_by_quality import get_item_by_quality

service = Services()

def test_get_item_by_quality_from_service():
    with app.app_context():
        assert service.get_item_by_quality(5) == get_item_by_quality(5)