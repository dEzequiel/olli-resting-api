import sqlite3
from repository.database import get_db


def group_items_by_sell_in(sellin):
    database = get_db()
    item = [
        dict(row)
        for row in database.execute(f"SELECT * FROM inventory WHERE sell_in='{sellin}'")
    ]
    database.close()
    return item if len(item) != 0 else {f"Sell in {sellin}": "not found"}
