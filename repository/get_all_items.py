import sqlite3
from repository.database import get_db


def get_all_items():
    database = get_db()
    items = [dict(row) for row in database.execute("SELECT * FROM inventory")]
    database.close()
    return items if len(items) != 0 else {"Inventory": "is empty"}
