from domain.normal_item import Normal_Item
import pytest


def test_check_item_type_object():

    normal_item = Normal_Item("Elixir of the Mongoose", 5, 7)
    assert isinstance(normal_item, Normal_Item)
    assert 5 == normal_item.sell_in
    assert 7 == normal_item.quality

    normal_item.update_quality()

    assert 4 == normal_item.sell_in
    assert 6 == normal_item.quality
