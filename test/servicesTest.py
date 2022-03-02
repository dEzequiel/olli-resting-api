import pytest
from controller.Object import Object
from model.inventory import myjson
from service.service import Service

def test_get_object():

    admin = Object()
    assert "f" == admin.get(myjson["advanced_targeting_enabled"])

# def test_no_object_provided():

#     admin = Object()

#     assert "aa not in database" == admin.get("aa")
