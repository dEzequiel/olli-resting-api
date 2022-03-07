import sqlite3
from repository.database import get_db
from repository.get_all_items import get_all_items

def get_item(name):

    items = list(filter(lambda item: item['name'] == name, get_all_items()))

    return items if len(items) != 0 else {name:"not found"}