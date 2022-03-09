import sqlite3
from repository.database import get_db
from repository.get_all_items import get_all_items


def get_item_by_sell_in(sellin):
    database = get_db()
    item = [dict(row) for row in database.execute(f"SELECT * FROM inventory WHERE sell_in='{sellin}'")]
    database.close()
    return item if len(item) != 0 else {f"Sell in {sellin}":"not found"}
