from unittest import result
import pytest
from app import app
from repository.database import get_db
from repository.add_item import add_item
import sqlite3

    # This test is just to let Eze knows the item is added succesfully to the database

def test_add_new_item():
    with app.app_context():
        # add_item('Rocky')
        pass
